
from mongoengine import connect
from flask import Flask, request,Response
from models import Dwellings

from save_data_unit import *
from save_data_house import *
from save_data_all import *
app = Flask(__name__)


def save_data():
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    rentname="rent_data.xls"
    salename="sales_data.xls"
    data_sales = xlrd.open_workbook(salename)
    sale_all=data_sales.sheets()[1]
    sale_house=data_sales.sheets()[2]
    sale_unit=data_sales.sheets()[3]
    data_rent=xlrd.open_workbook(rentname)
    rent_all_all=data_rent.sheets()[1]
    rent_all_one=data_rent.sheets()[2]
    rent_all_two = data_rent.sheets()[3]
    rent_all_three = data_rent.sheets()[4]
    rent_all_four = data_rent.sheets()[5]
    rent_house_all= data_rent.sheets()[6]
    rent_house_two = data_rent.sheets()[7]
    rent_house_three = data_rent.sheets()[8]
    rent_unit_all = data_rent.sheets()[9]
    rent_unit_one = data_rent.sheets()[10]
    rent_unit_two = data_rent.sheets()[11]
    not_lga=["Middle Ring","Outer Ring", "Rest of GMR"]

    for i in range(4,15):
        rent_unit_one_line = rent_unit_one.row_values(i)

        unit_dict=save_data_unit(i)
        house_dict=save_data_house(i)
        all_dict=save_data_all(i)
        t1 = Dwellings(lga=rent_unit_one_line[0], unit=unit_dict,house=house_dict,all=all_dict)
        connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        t1.save()
    for i in range(16,31):
        rent_unit_one_line = rent_unit_one.row_values(i)

        unit_dict=save_data_unit(i)
        house_dict=save_data_house(i)
        all_dict=save_data_all(i)
        t1 = Dwellings(lga=rent_unit_one_line[0], unit=unit_dict,house=house_dict,all=all_dict)
        connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        t1.save()
    for i in range(32,49):
        rent_unit_one_line = rent_unit_one.row_values(i)

        unit_dict=save_data_unit(i)
        house_dict=save_data_house(i)
        all_dict=save_data_all(i)
        t1 = Dwellings(lga=rent_unit_one_line[0], unit=unit_dict,house=house_dict,all=all_dict)
        connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        t1.save()
    for i in range(50,58):
        rent_unit_one_line = rent_unit_one.row_values(i)

        unit_dict=save_data_unit(i)
        house_dict=save_data_house(i)
        all_dict=save_data_all(i)
        t1 = Dwellings(lga=rent_unit_one_line[0], unit=unit_dict,house=house_dict,all=all_dict)
        connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        t1.save()

    for i in range(59,60):
        unit_dict = save_data_unit(i)
        house_dict = save_data_house(i)
        all_dict = save_data_all(i)
        t1 = Dwellings(lga="NSW", unit=unit_dict, house=house_dict, all=all_dict)
        connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        t1.save()


save_data()

