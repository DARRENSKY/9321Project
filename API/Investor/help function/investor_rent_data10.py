from mongoengine import connect

from models import Dwellings
def rent_data10(area,property_type):
    # area="Ashfield"
    # property_type="unit"
    area=area
    property_type=property_type
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    
    for dw in Dwellings.objects:
        
        if dw.lga==area and property_type=="unit":
            rent_dict=dw[property_type]["all_rent"]
            #rent_year_06 = (rent_dict["rent_unit_all_mar06"] + rent_dict["rent_unit_all_jun06"] + rent_dict["rent_unit_all_sep06"] + rent_dict["rent_unit_all_dec06"]) / 4
            rent_year_07 = (rent_dict["rent_unit_all_mar07"] + rent_dict["rent_unit_all_jun07"] + rent_dict["rent_unit_all_sep07"] + rent_dict["rent_unit_all_dec07"]) / 4
            rent_year_08 = (rent_dict["rent_unit_all_mar08"] + rent_dict["rent_unit_all_jun08"] + rent_dict["rent_unit_all_sep08"] + rent_dict["rent_unit_all_dec08"]) / 4
            rent_year_09 = (rent_dict["rent_unit_all_mar09"] + rent_dict["rent_unit_all_jun09"] + rent_dict["rent_unit_all_sep09"] + rent_dict["rent_unit_all_dec07"]) / 4
            rent_year_10 = (rent_dict["rent_unit_all_mar10"] + rent_dict["rent_unit_all_jun10"] + rent_dict["rent_unit_all_sep10"] + rent_dict["rent_unit_all_dec10"]) / 4
            rent_year_11 = (rent_dict["rent_unit_all_mar11"] + rent_dict["rent_unit_all_jun11"] + rent_dict["rent_unit_all_sep11"] + rent_dict["rent_unit_all_dec11"]) / 4
            rent_year_12 = (rent_dict["rent_unit_all_mar12"] + rent_dict["rent_unit_all_jun12"] + rent_dict["rent_unit_all_sep12"] + rent_dict["rent_unit_all_dec12"]) / 4
            rent_year_13 = (rent_dict["rent_unit_all_mar13"] + rent_dict["rent_unit_all_jun13"] + rent_dict["rent_unit_all_sep13"] + rent_dict["rent_unit_all_dec13"]) / 4
            rent_year_14 = (rent_dict["rent_unit_all_mar14"] + rent_dict["rent_unit_all_jun14"] + rent_dict["rent_unit_all_sep14"] + rent_dict["rent_unit_all_dec14"]) / 4
            rent_year_15 = (rent_dict["rent_unit_all_mar15"] + rent_dict["rent_unit_all_jun15"] + rent_dict["rent_unit_all_sep15"] + rent_dict["rent_unit_all_dec15"]) / 4
            rent_year_16 = (rent_dict["rent_unit_all_mar16"] + rent_dict["rent_unit_all_jun16"] + rent_dict["rent_unit_all_sep16"] + rent_dict["rent_unit_all_dec16"]) / 4


            rent_list=[]
            rent_list.append(rent_year_07)
            rent_list.append(rent_year_08)
            rent_list.append(rent_year_09)
            rent_list.append(rent_year_10)
            rent_list.append(rent_year_11)
            rent_list.append(rent_year_12)
            rent_list.append(rent_year_13)
            rent_list.append(rent_year_14)
            rent_list.append(rent_year_15)
            rent_list.append(rent_year_16)

            return rent_list

        if dw.lga == area and property_type == "house":
            rent_dict = dw[property_type]["all_rent"]

            rent_year_07 = (rent_dict["rent_house_all_mar07"] + rent_dict["rent_house_all_jun07"] + rent_dict[
                "rent_house_all_sep07"] + rent_dict["rent_house_all_dec07"]) / 4
            rent_year_08 = (rent_dict["rent_house_all_mar08"] + rent_dict["rent_house_all_jun08"] + rent_dict[
                "rent_house_all_sep08"] + rent_dict["rent_house_all_dec08"]) / 4
            rent_year_09 = (rent_dict["rent_house_all_mar09"] + rent_dict["rent_house_all_jun09"] + rent_dict[
                "rent_house_all_sep09"] + rent_dict["rent_house_all_dec07"]) / 4
            rent_year_10 = (rent_dict["rent_house_all_mar10"] + rent_dict["rent_house_all_jun10"] + rent_dict[
                "rent_house_all_sep10"] + rent_dict["rent_house_all_dec10"]) / 4
            rent_year_11 = (rent_dict["rent_house_all_mar11"] + rent_dict["rent_house_all_jun11"] + rent_dict[
                "rent_house_all_sep11"] + rent_dict["rent_house_all_dec11"]) / 4
            rent_year_12 = (rent_dict["rent_house_all_mar12"] + rent_dict["rent_house_all_jun12"] + rent_dict[
                "rent_house_all_sep12"] + rent_dict["rent_house_all_dec12"]) / 4
            rent_year_13 = (rent_dict["rent_house_all_mar13"] + rent_dict["rent_house_all_jun13"] + rent_dict[
                "rent_house_all_sep13"] + rent_dict["rent_house_all_dec13"]) / 4
            rent_year_14 = (rent_dict["rent_house_all_mar14"] + rent_dict["rent_house_all_jun14"] + rent_dict[
                "rent_house_all_sep14"] + rent_dict["rent_house_all_dec14"]) / 4
            rent_year_15 = (rent_dict["rent_house_all_mar15"] + rent_dict["rent_house_all_jun15"] + rent_dict[
                "rent_house_all_sep15"] + rent_dict["rent_house_all_dec15"]) / 4
            rent_year_16 = (rent_dict["rent_house_all_mar16"] + rent_dict["rent_house_all_jun16"] + rent_dict[
                "rent_house_all_sep16"] + rent_dict["rent_house_all_dec16"]) / 4

            rent_list = []
            rent_list.append(rent_year_07)
            rent_list.append(rent_year_08)
            rent_list.append(rent_year_09)
            rent_list.append(rent_year_10)
            rent_list.append(rent_year_11)
            rent_list.append(rent_year_12)
            rent_list.append(rent_year_13)
            rent_list.append(rent_year_14)
            rent_list.append(rent_year_15)
            rent_list.append(rent_year_16)
            return rent_list

        if dw.lga == area and property_type == "all":
            rent_dict = dw[property_type]["all_rent"]

            rent_year_07 = (rent_dict["rent_all_all_mar07"] + rent_dict["rent_all_all_jun07"] + rent_dict[
                "rent_all_all_sep07"] + rent_dict["rent_all_all_dec07"]) / 4
            rent_year_08 = (rent_dict["rent_all_all_mar08"] + rent_dict["rent_all_all_jun08"] + rent_dict[
                "rent_all_all_sep08"] + rent_dict["rent_all_all_dec08"]) / 4
            rent_year_09 = (rent_dict["rent_all_all_mar09"] + rent_dict["rent_all_all_jun09"] + rent_dict[
                "rent_all_all_sep09"] + rent_dict["rent_all_all_dec07"]) / 4
            rent_year_10 = (rent_dict["rent_all_all_mar10"] + rent_dict["rent_all_all_jun10"] + rent_dict[
                "rent_all_all_sep10"] + rent_dict["rent_all_all_dec10"]) / 4
            rent_year_11 = (rent_dict["rent_all_all_mar11"] + rent_dict["rent_all_all_jun11"] + rent_dict[
                "rent_all_all_sep11"] + rent_dict["rent_all_all_dec11"]) / 4
            rent_year_12 = (rent_dict["rent_all_all_mar12"] + rent_dict["rent_all_all_jun12"] + rent_dict[
                "rent_all_all_sep12"] + rent_dict["rent_all_all_dec12"]) / 4
            rent_year_13 = (rent_dict["rent_all_all_mar13"] + rent_dict["rent_all_all_jun13"] + rent_dict[
                "rent_all_all_sep13"] + rent_dict["rent_all_all_dec13"]) / 4
            rent_year_14 = (rent_dict["rent_all_all_mar14"] + rent_dict["rent_all_all_jun14"] + rent_dict[
                "rent_all_all_sep14"] + rent_dict["rent_all_all_dec14"]) / 4
            rent_year_15 = (rent_dict["rent_all_all_mar15"] + rent_dict["rent_all_all_jun15"] + rent_dict[
                "rent_all_all_sep15"] + rent_dict["rent_all_all_dec15"]) / 4
            rent_year_16 = (rent_dict["rent_all_all_mar16"] + rent_dict["rent_all_all_jun16"] + rent_dict[
                "rent_all_all_sep16"] + rent_dict["rent_all_all_dec16"]) / 4

            rent_list = []
            rent_list.append(rent_year_07)
            rent_list.append(rent_year_08)
            rent_list.append(rent_year_09)
            rent_list.append(rent_year_10)
            rent_list.append(rent_year_11)
            rent_list.append(rent_year_12)
            rent_list.append(rent_year_13)
            rent_list.append(rent_year_14)
            rent_list.append(rent_year_15)
            rent_list.append(rent_year_16)
            return rent_list


# area="Ashfield"
# property_type="unit"
# lga="NSW"
# property_type="all"
# rent_list=rent_data10(lga,property_type)
# print(rent_list)