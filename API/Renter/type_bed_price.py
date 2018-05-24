from models import Dwellings
from mongoengine import connect
from collections import OrderedDict
from operator import itemgetter
#sale need to mul 10

def type_bed_price(type = 'all', bed = 'all', minprice = 0, maxprice = 10000000):
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    wanted_lga = list()
    for i in Dwellings.objects:
        data = i[type][bed+'_rent']
        data = OrderedDict(data)
        data = list(data.items())
        data = (data[-1][1] + data[-2][1] + data[-3][1] + data[-4][1])/4 #the average
        if maxprice >= data >= minprice:
            wanted_lga.append((i['lga'], data))

    wanted_lga = sorted(wanted_lga, key = itemgetter(1), reverse= True)

    result_bed_10 = []
    for i in wanted_lga:
        for j in i:
            result_bed_10.append(j)
    return result_bed_10[:20]




# print(type_bed_price(type="unit",bed="one",minprice=400,maxprice=800))