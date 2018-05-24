from lga_postcode import *
import xlrd

def supermarkets():
    lga_woolworths_dict={}
    for i in lga_list:
        lga_woolworths_dict[i]=0

    lga_coles_dict={}
    for i in lga_list:
        lga_coles_dict[i]=0

    lga_supermarkets_dict={}
    for i in lga_list:
        lga_supermarkets_dict[i]=0

    woolwoth_name="woolworths.xlsx"
    woolwoth=xlrd.open_workbook(woolwoth_name)
    woolwoth_data=woolwoth.sheets()[0]

    coles_name="coles.xlsx"
    coles=xlrd.open_workbook(coles_name)
    coles_data=coles.sheets()[0]

    for wwth in range(1011):
        wwthline=woolwoth_data.row_values(wwth)
        state_name=wwthline[10]
        if state_name=="NSW":
            post_code=wwthline[11]
            if post_code !="":
                post_code=int(post_code)
                if post_code in postdic:
                    onecode_lga_lists=postdic[post_code]
                    for lga_name in onecode_lga_lists:
                        if lga_name in lga_list:
                            lga_woolworths_dict[lga_name]+=1

    for one_coles in range(245):
        colesline=coles_data.row_values(one_coles)
        postcode_str=colesline[3]
        for one_code in postdic:
            if str(one_code) in postcode_str:
                onecode_lga_lists = postdic[one_code]
                for lga_name in onecode_lga_lists:
                    if lga_name in lga_list:
                        lga_coles_dict[lga_name] += 1

    for lga_name in lga_list:
        lga_supermarkets_dict[lga_name]+=lga_woolworths_dict[lga_name]+lga_coles_dict[lga_name]
    nsw_supermarkets_number=0
    for i in lga_supermarkets_dict:
        nsw_supermarkets_number+=lga_supermarkets_dict[i]
    lga_supermarkets_dict["NSW"]=nsw_supermarkets_number

    return lga_supermarkets_dict


