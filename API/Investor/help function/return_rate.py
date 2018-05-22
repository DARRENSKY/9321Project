from mongoengine import connect

from models import Dwellings
def return_rate(area,property_type):
    # area="Ashfield"
    # property_type="unit"
    area=area
    property_type=property_type
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    
    for dw in Dwellings.objects:
        
        if dw.lga==area and property_type=="unit":
            rent_dict=dw[property_type]["all_rent"]
            rent_year_06 = (rent_dict["rent_unit_all_mar06"] + rent_dict["rent_unit_all_jun06"] + rent_dict["rent_unit_all_sep06"] + rent_dict["rent_unit_all_dec06"]) / 4
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

            sale_dict=dw[property_type]["sales"]

            sale_year_06 = sale_dict["sale_unit_06"]/4
            sale_year_07 = sale_dict["sale_unit_07"]/4
            sale_year_08 = sale_dict["sale_unit_08"]/4
            sale_year_09 = sale_dict["sale_unit_09"]/4
            sale_year_10 = sale_dict["sale_unit_10"]/4
            sale_year_11 = sale_dict["sale_unit_11"]/4
            sale_year_12 = sale_dict["sale_unit_12"]/4
            sale_year_13 = sale_dict["sale_unit_13"]/4
            sale_year_14 = sale_dict["sale_unit_14"]/4
            sale_year_15 = sale_dict["sale_unit_15"]/4
            sale_year_16 = sale_dict["sale_unit_16"]/4

            return_rate_07 = (rent_year_06 * 50 + (sale_year_07 - sale_year_06) * 1000) / (sale_year_06*1000)*100
            return_rate_08 = (rent_year_07 * 50 + (sale_year_08 - sale_year_07) * 1000) / (sale_year_07*1000)*100
            return_rate_09 = (rent_year_08 * 50 + (sale_year_09 - sale_year_08) * 1000) / (sale_year_08*1000)*100
            return_rate_10 = (rent_year_09 * 50 + (sale_year_10 - sale_year_09) * 1000) / (sale_year_09*1000)*100
            return_rate_11 = (rent_year_10 * 50 + (sale_year_11 - sale_year_10) * 1000) / (sale_year_10*1000)*100
            return_rate_12 = (rent_year_11 * 50 + (sale_year_12 - sale_year_11) * 1000) / (sale_year_11*1000)*100
            return_rate_13 = (rent_year_12 * 50 + (sale_year_13 - sale_year_12) * 1000) / (sale_year_12*1000)*100
            return_rate_14 = (rent_year_13 * 50 + (sale_year_14 - sale_year_13) * 1000) / (sale_year_13*1000)*100
            return_rate_15 = (rent_year_14 * 50 + (sale_year_15 - sale_year_14) * 1000) / (sale_year_14*1000)*100
            return_rate_16 = (rent_year_15 * 50 + (sale_year_16 - sale_year_15) * 1000) / (sale_year_15*1000)*100

            rate_list=[]
            rate_list.append(return_rate_07)
            rate_list.append(return_rate_08)
            rate_list.append(return_rate_09)
            rate_list.append(return_rate_10)
            rate_list.append(return_rate_11)
            rate_list.append(return_rate_12)
            rate_list.append(return_rate_13)
            rate_list.append(return_rate_14)
            rate_list.append(return_rate_15)
            rate_list.append(return_rate_16)
            rate_list_after=[]
            for rate in rate_list:
                rate=round(rate,2)
                rate_list_after.append(rate)
            area_rate={}
            area_rate[area]=rate_list_after
            return rate_list_after

        if dw.lga == area and property_type == "house":
            rent_dict = dw[property_type]["all_rent"]
            rent_year_06 = (rent_dict["rent_house_all_mar06"] + rent_dict["rent_house_all_jun06"] + rent_dict[
                "rent_house_all_sep06"] + rent_dict["rent_house_all_dec06"]) / 4
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

            sale_dict = dw[property_type]["sales"]

            sale_year_06 = sale_dict["sale_house_06"]/4
            sale_year_07 = sale_dict["sale_house_07"]/4
            sale_year_08 = sale_dict["sale_house_08"]/4
            sale_year_09 = sale_dict["sale_house_09"]/4
            sale_year_10 = sale_dict["sale_house_10"]/4
            sale_year_11 = sale_dict["sale_house_11"]/4
            sale_year_12 = sale_dict["sale_house_12"]/4
            sale_year_13 = sale_dict["sale_house_13"]/4
            sale_year_14 = sale_dict["sale_house_14"]/4
            sale_year_15 = sale_dict["sale_house_15"]/4
            sale_year_16 = sale_dict["sale_house_16"]/4

            return_rate_07 = (rent_year_06 * 50 + (sale_year_07 - sale_year_06) * 1000) / (sale_year_06*1000)*100
            return_rate_08 = (rent_year_07 * 50 + (sale_year_08 - sale_year_07) * 1000) / (sale_year_07*1000)*100
            return_rate_09 = (rent_year_08 * 50 + (sale_year_09 - sale_year_08) * 1000) / (sale_year_08*1000)*100
            return_rate_10 = (rent_year_09 * 50 + (sale_year_10 - sale_year_09) * 1000) / (sale_year_09*1000)*100
            return_rate_11 = (rent_year_10 * 50 + (sale_year_11 - sale_year_10) * 1000) / (sale_year_10*1000)*100
            return_rate_12 = (rent_year_11 * 50 + (sale_year_12 - sale_year_11) * 1000) / (sale_year_11*1000)*100
            return_rate_13 = (rent_year_12 * 50 + (sale_year_13 - sale_year_12) * 1000) / (sale_year_12*1000)*100
            return_rate_14 = (rent_year_13 * 50 + (sale_year_14 - sale_year_13) * 1000) / (sale_year_13*1000)*100
            return_rate_15 = (rent_year_14 * 50 + (sale_year_15 - sale_year_14) * 1000) / (sale_year_14*1000)*100
            return_rate_16 = (rent_year_15 * 50 + (sale_year_16 - sale_year_15) * 1000) / (sale_year_15*1000)*100

            rate_list = []
            rate_list.append(return_rate_07)
            rate_list.append(return_rate_08)
            rate_list.append(return_rate_09)
            rate_list.append(return_rate_10)
            rate_list.append(return_rate_11)
            rate_list.append(return_rate_12)
            rate_list.append(return_rate_13)
            rate_list.append(return_rate_14)
            rate_list.append(return_rate_15)
            rate_list.append(return_rate_16)
            rate_list_after = []
            for rate in rate_list:
                rate = round(rate, 2)
                rate_list_after.append(rate)
            # area_rate = {}
            # area_rate[area] = rate_list_after
            return rate_list_after

        if dw.lga == area and property_type == "all":
            rent_dict = dw[property_type]["all_rent"]
            rent_year_06 = (rent_dict["rent_all_all_mar06"] + rent_dict["rent_all_all_jun06"] + rent_dict[
                "rent_all_all_sep06"] + rent_dict["rent_all_all_dec06"]) / 4
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

            sale_dict = dw[property_type]["sales"]

            sale_year_06 = sale_dict["sale_all_06"]/4
            sale_year_07 = sale_dict["sale_all_07"]/4
            sale_year_08 = sale_dict["sale_all_08"]/4
            sale_year_09 = sale_dict["sale_all_09"]/4
            sale_year_10 = sale_dict["sale_all_10"]/4
            sale_year_11 = sale_dict["sale_all_11"]/4
            sale_year_12 = sale_dict["sale_all_12"]/4
            sale_year_13 = sale_dict["sale_all_13"]/4
            sale_year_14 = sale_dict["sale_all_14"]/4
            sale_year_15 = sale_dict["sale_all_15"]/4
            sale_year_16 = sale_dict["sale_all_16"]/4

            return_rate_07 = (rent_year_06 * 50 + (sale_year_07 - sale_year_06) * 1000) / (sale_year_06*1000)*100
            return_rate_08 = (rent_year_07 * 50 + (sale_year_08 - sale_year_07) * 1000) / (sale_year_07*1000)*100
            return_rate_09 = (rent_year_08 * 50 + (sale_year_09 - sale_year_08) * 1000) / (sale_year_08*1000)*100
            return_rate_10 = (rent_year_09 * 50 + (sale_year_10 - sale_year_09) * 1000) / (sale_year_09*1000)*100
            return_rate_11 = (rent_year_10 * 50 + (sale_year_11 - sale_year_10) * 1000) / (sale_year_10*1000)*100
            return_rate_12 = (rent_year_11 * 50 + (sale_year_12 - sale_year_11) * 1000) / (sale_year_11*1000)*100
            return_rate_13 = (rent_year_12 * 50 + (sale_year_13 - sale_year_12) * 1000) / (sale_year_12*1000)*100
            return_rate_14 = (rent_year_13 * 50 + (sale_year_14 - sale_year_13) * 1000) / (sale_year_13*1000)*100
            return_rate_15 = (rent_year_14 * 50 + (sale_year_15 - sale_year_14) * 1000) / (sale_year_14*1000)*100
            return_rate_16 = (rent_year_15 * 50 + (sale_year_16 - sale_year_15) * 1000) / (sale_year_15*1000)*100

            rate_list = []
            rate_list.append(return_rate_07)
            rate_list.append(return_rate_08)
            rate_list.append(return_rate_09)
            rate_list.append(return_rate_10)
            rate_list.append(return_rate_11)
            rate_list.append(return_rate_12)
            rate_list.append(return_rate_13)
            rate_list.append(return_rate_14)
            rate_list.append(return_rate_15)
            rate_list.append(return_rate_16)
            rate_list_after = []
            for rate in rate_list:
                rate = round(rate, 2)
                rate_list_after.append(rate)
            area_rate = {}
            area_rate[area] = rate_list_after
            return rate_list_after


# area="Ashfield"
# property_type="unit"
# lga="Mosman"
# property_type="house"
# rate_list=return_rate(lga,property_type)
# print(rate_list)