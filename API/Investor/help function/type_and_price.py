from models import Dwellings
from mongoengine import connect
from collections import OrderedDict
from operator import itemgetter
from return_rate import return_rate
#sale need to mul 10

def type_and_price_tenyears(type = 'all', minprice = 0, maxprice = 100000000):
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    minprice = minprice/1000
    maxprice = maxprice/1000
    wanted_lga = list()
    for i in Dwellings.objects:
        type_sale = i[type]['sales']
        type_sale = OrderedDict(type_sale)
        type_sale = list(type_sale.items())

        if maxprice >= (type_sale[-1][1]/4) >= minprice:
            wanted_lga.append(i['lga'])

    final_list = []

    for i in wanted_lga:
        notail_return_rate = return_rate(i, type)
        notail_return_rate = round(sum(notail_return_rate)/10,2)
        final_list.append((i, notail_return_rate))

    final_list = sorted(final_list, key = itemgetter(1), reverse = True)
    return final_list[:5]




print(type_and_price_tenyears())

def type_and_price_threeyears(type = 'all', minprice = 0, maxprice = 100000000):
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    minprice = minprice/1000
    maxprice = maxprice/1000
    wanted_lga = list()
    for i in Dwellings.objects:
        type_sale = i[type]['sales']
        type_sale = OrderedDict(type_sale)
        type_sale = list(type_sale.items())
        if maxprice >= (type_sale[-1][1]/4) >= minprice:
            wanted_lga.append(i['lga'])

    final_list = []

    for i in wanted_lga:
        notail_return_rate = return_rate(i, type)
        notail_return_rate = round((notail_return_rate[-1] + notail_return_rate[-2] + notail_return_rate[-3])/3,2)
        final_list.append((i, notail_return_rate))

    final_list = sorted(final_list, key = itemgetter(1), reverse = True)
    return final_list[:5]


print(type_and_price_threeyears())