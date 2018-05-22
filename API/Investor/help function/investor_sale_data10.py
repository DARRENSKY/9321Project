from mongoengine import connect

from models import Dwellings
def sale_data10(area,property_type):
    # area="Ashfield"
    # property_type="unit"
    area=area
    property_type=property_type
    connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
    
    for dw in Dwellings.objects:
        
        if dw.lga==area and property_type=="unit":

            sale_dict=dw[property_type]["sales"]

            # sale_year_06 = sale_dict["sale_unit_06"]
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

            sale_list=[]

            sale_list.append(sale_year_07)
            sale_list.append(sale_year_08)
            sale_list.append(sale_year_09)
            sale_list.append(sale_year_10)
            sale_list.append(sale_year_11)
            sale_list.append(sale_year_12)
            sale_list.append(sale_year_13)
            sale_list.append(sale_year_14)
            sale_list.append(sale_year_15)
            sale_list.append(sale_year_16)

            return sale_list

        if dw.lga == area and property_type == "house":
            sale_dict = dw[property_type]["sales"]

            # sale_year_06 = sale_dict["sale_unit_06"]
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

            sale_list = []

            sale_list.append(sale_year_07)
            sale_list.append(sale_year_08)
            sale_list.append(sale_year_09)
            sale_list.append(sale_year_10)
            sale_list.append(sale_year_11)
            sale_list.append(sale_year_12)
            sale_list.append(sale_year_13)
            sale_list.append(sale_year_14)
            sale_list.append(sale_year_15)
            sale_list.append(sale_year_16)

            return sale_list

        if dw.lga == area and property_type == "all":
            sale_dict = dw[property_type]["sales"]

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

            sale_list = []

            sale_list.append(sale_year_07)
            sale_list.append(sale_year_08)
            sale_list.append(sale_year_09)
            sale_list.append(sale_year_10)
            sale_list.append(sale_year_11)
            sale_list.append(sale_year_12)
            sale_list.append(sale_year_13)
            sale_list.append(sale_year_14)
            sale_list.append(sale_year_15)
            sale_list.append(sale_year_16)

            return sale_list


# area="Ashfield"
# property_type="unit"
# lga="Mosman"
# property_type="unit"
# sale_list=sale_data10(lga,property_type)
# print(sale_list)