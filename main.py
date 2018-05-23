from flask import *
from flask_restful import reqparse
from statistics import *
from plotly.offline import plot
from plotly.graph_objs import *
from investor_rent_10yrs import *
from investor_sale_10yrs import *
from return_rate import *
import top_5

app = Flask(__name__)


def make_table(data, row_length, title):
    result = '<table>'
    if title == 'yes':
        result = result + '<tr><td>LGA</td><td>Price</td><td>Return rate (%)</td></tr>'

    counter = 0
    for element in data:
        if counter % row_length == 0:
            result = result + '<tr>'
        result = result + '<td>{:}</td>'.format(element)
        counter += 1
        if counter % row_length == 0:
            result = result + '</tr>'
    if counter % row_length != 0:
        for i in range(0, row_length - counter % row_length):
            result = result + '<td>&nbsp;</td>'
        result = result + '</tr>'
    result = result + '</table>'
    return result


@app.route("/investment/search_method_1", methods=['GET'])
def investment_search_method_1():
    parser = reqparse.RequestParser()
    parser.add_argument('building_type', type=str)
    parser.add_argument('min_price', type=int)
    parser.add_argument('max_price', type=int)
    args = parser.parse_args()
    building_type = args.get('building_type')
    min_price = args.get('min_price')
    max_price = args.get('max_price')

    t1_and_t2_data = top_5.type_and_price(building_type, min_price, max_price)
    t1_data = t1_and_t2_data[0]
    t2_data = t1_and_t2_data[1]
    t1 = make_table(t1_data, 3, 'yes')
    t2 = make_table(t2_data, 3, 'yes')

    return render_template('investment_method_1.html', table_10yrs=Markup(t1), table_3yrs=Markup(t2))


@app.route("/investment/search_method_2", methods=['GET'])
def investment_search_method_2():
    summary_table_data = []
    parser = reqparse.RequestParser()
    parser.add_argument('building_type', type=str)
    parser.add_argument('area', type=str)
    args = parser.parse_args()
    building_type = args.get('building_type')
    area = args.get('area')
    if len(area) == 0:
        area = 'NSW'

    if building_type == 'all':
        display_type = '(Houses and Units)'
    elif building_type == 'house':
        display_type = '(Houses)'
    else:
        display_type = '(Units)'

    configuration = dict(showLink=False, displayModeBar=False)
    x = [i for i in range(2007, 2017)]

    y1 = sale_data10(area, building_type)
    summary_table_data.append('Sales (max)')
    summary_table_data.append('$ ' + str('{:,}'.format(int(max(y1)*1000))))
    summary_table_data.append('Sales (min)')
    summary_table_data.append('$ ' + str('{:,}'.format(int(min(y1)*1000))))
    summary_table_data.append('Sales (median)')
    summary_table_data.append('$ ' + str('{:,}'.format(int(median(y1)*1000))))

    data = [Scatter(x=x, y=y1)]
    layout_1 = Layout(xaxis=dict(title='Year'), yaxis=dict(title="Price ($'000)"), title='Sales (2006 - 2016)', height=400)
    fig = Figure(data=data, layout=layout_1)
    plot_div_1 = plot(fig, output_type='div', config=configuration)

    y2 = rent_data10(area, building_type)
    summary_table_data.append('Rent (max)')
    summary_table_data.append('$ ' + str(int(max(y2))) + ' /week')
    summary_table_data.append('Rent (min)')
    summary_table_data.append('$ ' + str(int(min(y2))) + ' /week')
    summary_table_data.append('Rent (median)')
    summary_table_data.append('$ ' + str(int(median(y2))) + ' /week')

    data = [Scatter(x=x, y=y2)]
    layout_2 = Layout(xaxis=dict(title='Year'), yaxis=dict(title='Price ($ / Week)'), title='Rent (2006 - 2016)', height=400)
    fig = Figure(data=data, layout=layout_2)
    plot_div_2 = plot(fig, output_type='div', config=configuration)

    y3 = return_rate(area, building_type)
    summary_table_data.append('Return rate (max)')
    summary_table_data.append(str(round(max(y3), 1)) + '%')
    summary_table_data.append('Return rate (min)')
    summary_table_data.append(str(round(min(y3), 1)) + '%')
    summary_table_data.append('Return rate (median)')
    summary_table_data.append(str(round(median(y3), 1)) + '%')

    data = [Scatter(x=x, y=y3)]
    layout_3 = Layout(xaxis=dict(title='Year'), yaxis=dict(title='Percentage (%)'), title='Return Rate (2006 - 2016)', height=400)
    fig = Figure(data=data, layout=layout_3)
    plot_div_3 = plot(fig, output_type='div', config=configuration)

    t = make_table(summary_table_data, 2, 'no')

    return render_template('investment_method_2.html', lga=area, display_type=display_type, plot_1=Markup(plot_div_1), plot_2=Markup(plot_div_2), plot_3=Markup(plot_div_3), summary_table=Markup(t))


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/investment/homepage", methods=['GET'])
def investment_home():
    return render_template("investment.html")


@app.route("/rental/homepage", methods=['GET'])
def rental_home():
    return render_template("rental.html")


if __name__ == '__main__':
    app.run()
