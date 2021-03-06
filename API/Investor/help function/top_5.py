from models import Dwellings
from mongoengine import connect
from collections import OrderedDict
from operator import itemgetter
from return_rate import return_rate
#sale need to mul 10

def type_and_price(type = 'all', minprice = 0, maxprice = 100000000):
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    minprice = minprice/1000
    maxprice = maxprice/1000
    # wanted_lga = list()
    wanted_lga = {}
    for i in Dwellings.objects:
        type_sale = i[type]['sales']
        type_sale = OrderedDict(type_sale)
        type_sale = list(type_sale.items())
        current_price = type_sale[-1][1]/4
        if maxprice >= (current_price) >= minprice:
            # wanted_lga.append(i['lga'])
            wanted_lga[i['lga']]=current_price

    final_list_10 = []
    final_list_3 = []
    for i in wanted_lga:
        notail_return_rate = return_rate(i, type)

        notail_return_rate_10 = round(sum(notail_return_rate) / 10, 2)
        final_list_10.append((i,'$ '+str('{:,}'.format(int(wanted_lga[i]*1000))), notail_return_rate_10))

        notail_return_rate_3 = round((notail_return_rate[-1] + notail_return_rate[-2] + notail_return_rate[-3]) / 3, 2)
        final_list_3.append((i,'$ '+str('{:,}'.format(int(wanted_lga[i]*1000))),notail_return_rate_3))


    final_list_10 = sorted(final_list_10, key = itemgetter(2), reverse = True)
    final_list_3= sorted(final_list_3, key=itemgetter(2), reverse=True)
    result_10 = []
    result_3 = []

    for i in final_list_10:
        for j in i:
            result_10.append(j)

    for i in final_list_3:
        for j in i:
            result_3.append(j)
    result = []
    result.append(result_10[:15])
    result.append(result_3[:15])
    return result
