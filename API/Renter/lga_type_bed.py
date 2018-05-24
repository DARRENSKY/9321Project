from models import Dwellings
from mongoengine import connect
from collections import OrderedDict
from operator import itemgetter


def lga_type_bed(lga='NSW', type='all', bed='all'):
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    wanted_lga = list()
    for i in Dwellings.objects:
        if i['lga'] == lga:
            data = i[type][bed + '_rent']
            data = OrderedDict(data)
            data = list(data.items())
            wanted_lga.append(data[-8][1])
            wanted_lga.append(data[-7][1])
            wanted_lga.append(data[-6][1])
            wanted_lga.append(data[-5][1])
            wanted_lga.append(data[-4][1])
            wanted_lga.append(data[-3][1])
            wanted_lga.append(data[-2][1])
            wanted_lga.append(data[-1][1])
    return wanted_lga

