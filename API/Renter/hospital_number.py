from lga_postcode import *
import xlrd

def hospitals():
    lga_hospital_dict={}
    for i in lga_list:
        lga_hospital_dict[i]=0

    hospital_name="hospital.xlsx"
    hospital=xlrd.open_workbook(hospital_name)
    hospital_data=hospital.sheets()[0]

    for one_hos in range(3,1013):
        hos_line=hospital_data.row_values(one_hos)
        state_name = hos_line[5]
        if state_name == "NSW":
            postcode_hos=hos_line[4]
            postcode_hos=int(postcode_hos)
            for one_code in postdic:
                if one_code==postcode_hos:
                    onecode_lga_lists = postdic[one_code]
                    for lga_name in onecode_lga_lists:
                        if lga_name in lga_list:
                            lga_hospital_dict[lga_name] += 1


    nsw_hospital_number=0
    for i in lga_hospital_dict:
        nsw_hospital_number+=lga_hospital_dict[i]
    lga_hospital_dict["NSW"]=nsw_hospital_number

    return lga_hospital_dict

