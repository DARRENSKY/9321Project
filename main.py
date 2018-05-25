from flask import *
from flask_restful import reqparse
from statistics import *
from plotly.offline import plot
from plotly.graph_objs import *
from investor_rent_10yrs import *
from investor_sale_10yrs import *
from return_rate import *
import top_5
from type_bed_price import *
from lga_type_bed import *
from supermarkets import *

app = Flask(__name__)


def make_table(data, row_length, title):
    result = '<table>'
    if title == 'top_5_return':
        result = result + '<tr><td>LGA</td><td>Price</td><td>Return rate (%)</td></tr>'

    if title == 'top_10_rental':
        result = result + '<tr><td>LGA</td><td>Rent /week</td></tr>'

    if title == 'summary':
        result = result + '<tr><th colspan="2">Summary</th></tr>'

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
    t1 = make_table(t1_data, 3, 'top_5_return')
    t2 = make_table(t2_data, 3, 'top_5_return')

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
    summary_table_data.append('$ ' + str('{:,}'.format(int(max(y1) * 1000))))
    summary_table_data.append('Sales (min)')
    summary_table_data.append('$ ' + str('{:,}'.format(int(min(y1) * 1000))))
    summary_table_data.append('Sales (median)')
    summary_table_data.append('$ ' + str('{:,}'.format(int(median(y1) * 1000))))

    y2 = rent_data10(area, building_type)
    summary_table_data.append('Rent (max)')
    summary_table_data.append('$ ' + str(int(max(y2))) + ' /week')
    summary_table_data.append('Rent (min)')
    summary_table_data.append('$ ' + str(int(min(y2))) + ' /week')
    summary_table_data.append('Rent (median)')
    summary_table_data.append('$ ' + str(int(median(y2))) + ' /week')

    y3 = return_rate(area, building_type)
    summary_table_data.append('Return rate (max)')
    summary_table_data.append(str(round(max(y3), 1)) + '%')
    summary_table_data.append('Return rate (min)')
    summary_table_data.append(str(round(min(y3), 1)) + '%')
    summary_table_data.append('Return rate (median)')
    summary_table_data.append(str(round(median(y3), 1)) + '%')

    t = make_table(summary_table_data, 2, 'summary')

    if building_type == 'all':
        y1_1 = sale_data10(area, 'house')
        y1_2 = sale_data10(area, 'unit')
        data_1 = [Scatter(x=x, y=y1_1, name='Houses'), Scatter(x=x, y=y1_2, name='Units')]
        y2_1 = rent_data10(area, 'house')
        y2_2 = rent_data10(area, 'unit')
        data_2 = [Scatter(x=x, y=y2_1, name='Houses'), Scatter(x=x, y=y2_2, name='Units')]
        y3_1 = return_rate(area, 'house')
        y3_2 = return_rate(area, 'unit')
        data_3 = [Scatter(x=x, y=y3_1, name='Houses'), Scatter(x=x, y=y3_2, name='Units')]
    else:
        data_1 = [Scatter(x=x, y=y1)]
        data_2 = [Scatter(x=x, y=y2)]
        data_3 = [Scatter(x=x, y=y3)]

    layout_1 = Layout(xaxis=dict(title='Year'), yaxis=dict(title="Price ($'000)"), title='Sales (2006 - 2016)', height=400)
    fig = Figure(data=data_1, layout=layout_1)
    plot_div_1 = plot(fig, output_type='div', config=configuration)

    layout_2 = Layout(xaxis=dict(title='Year'), yaxis=dict(title='Price ($ / Week)'), title='Rent (2006 - 2016)', height=400)
    fig = Figure(data=data_2, layout=layout_2)
    plot_div_2 = plot(fig, output_type='div', config=configuration)

    layout_3 = Layout(xaxis=dict(title='Year'), yaxis=dict(title='Percentage (%)'), title='Return Rate (2006 - 2016)', height=400)
    fig = Figure(data=data_3, layout=layout_3)
    plot_div_3 = plot(fig, output_type='div', config=configuration)

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


@app.route("/rental/search_method_1", methods=['GET'])
def rental_search_method_1():
    parser = reqparse.RequestParser()
    parser.add_argument('building_type', type=str)
    parser.add_argument('bedroom', type=str)
    parser.add_argument('min_price', type=int)
    parser.add_argument('max_price', type=int)
    args = parser.parse_args()
    building_type = args.get('building_type')
    bedroom = args.get('bedroom')
    min_price = args.get('min_price')
    max_price = args.get('max_price')

    if building_type == 'unit':
        if bedroom == 'three':
            error_message = 'No data of 3-bedroom units can be found.'
            return render_template('error.html', error_message=error_message)

    if building_type == 'house':
        if bedroom == 'one':
            error_message = 'No data of 1-bedroom houses can be found.'
            return render_template('error.html', error_message=error_message)

    data = type_bed_price(building_type, bedroom, min_price, max_price)
    t = make_table(data, 2, 'top_10_rental')

    return render_template('rental_method_1.html', table_top_10=Markup(t))


@app.route("/rental/search_method_2", methods=['GET'])
def rental_search_method_2():
    summary_table_data = []
    parser = reqparse.RequestParser()
    parser.add_argument('building_type', type=str)
    parser.add_argument('bedroom', type=str)
    parser.add_argument('area', type=str)
    args = parser.parse_args()
    building_type = args.get('building_type')
    bedroom = args.get('bedroom')
    area = args.get('area')

    if building_type == 'all':
        display_type = '(Houses + Units, '
    elif building_type == 'house':
        display_type = '(Houses, '
    else:
        display_type = '(Units, '

    if bedroom == 'all':
        display_type = display_type + 'any bedroom)'
    elif bedroom == 'one':
        display_type = display_type + 'one bedroom)'
    elif bedroom == 'two':
        display_type = display_type + 'two bedrooms)'
    else:
        display_type = display_type + 'three bedrooms)'

    if building_type == 'unit':
        if bedroom == 'three':
            error_message = 'No data of 3-bedroom units can be found.'
            return render_template('error.html', error_message=error_message)

    if building_type == 'house':
        if bedroom == 'one':
            error_message = 'No data of 1-bedroom houses can be found.'
            return render_template('error.html', error_message=error_message)

    y = lga_type_bed(area, building_type, bedroom)
    x = ['15 Q1', '15 Q2', '15 Q3', '15 Q4', '16 Q1', '16 Q2', '16 Q3', '16 Q4']

    data = [Scatter(x=x, y=y)]
    configuration = dict(showLink=False, displayModeBar=False)
    layout = Layout(xaxis=dict(title='Quarter'), yaxis=dict(title="Price ($ /week)"), title='Rent (2015 - 2016)', height=400)
    fig = Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', config=configuration)

    summary_table_data.append('Rent (max)')
    summary_table_data.append('$ ' + str(int(max(y))) + ' /week')
    summary_table_data.append('Rent (min)')
    summary_table_data.append('$ ' + str(int(min(y))) + ' /week')
    summary_table_data.append('Rent (median)')
    summary_table_data.append('$ ' + str(int(median(y))) + ' /week')
    summary_table_data.append('No. of supermarkets')
    summary_table_data.append(nb_supermarket(area))
    summary_table_data.append('No. of hospitals')
    summary_table_data.append(0)

    t = make_table(summary_table_data, 2, 'summary')

    return render_template('rental_method_2.html', lga=area, display_type=display_type, plot=Markup(plot_div), sum_table=Markup(t))


if __name__ == '__main__':
    app.run()
