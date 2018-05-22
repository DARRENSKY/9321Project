import xlrd

def save_data_unit(i):
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

    rent_unit_one_dict={}
    rent_unit_two_dict={}
    rent_unit_all_dict={}
    sale_unit_dict={}
    # for i in range(4,15):
    if i>=4 and i<15:
        rent_unit_one_line=rent_unit_one.row_values(i)
        index=0
        for j in rent_unit_one_line:
            if j=="-":
                rent_unit_one_line[index]=rent_unit_one.row_values(3)[index]
            index+=1

        rent_unit_one_dict["rent_unit_one_mar05"]=rent_unit_one_line[121]
        rent_unit_one_dict["rent_unit_one_jun05"]=rent_unit_one_line[121+2]
        rent_unit_one_dict["rent_unit_one_sep05"]=rent_unit_one_line[121+4]
        rent_unit_one_dict["rent_unit_one_dec05"]=rent_unit_one_line[121+6]

        rent_unit_one_dict["rent_unit_one_mar06"] = rent_unit_one_line[121+8]
        rent_unit_one_dict["rent_unit_one_jun06"] = rent_unit_one_line[121+10]
        rent_unit_one_dict["rent_unit_one_sep06"] = rent_unit_one_line[121+12]
        rent_unit_one_dict["rent_unit_one_dec06"] = rent_unit_one_line[121+14]

        rent_unit_one_dict["rent_unit_one_mar07"] = rent_unit_one_line[121+16]
        rent_unit_one_dict["rent_unit_one_jun07"] = rent_unit_one_line[121+18]
        rent_unit_one_dict["rent_unit_one_sep07"] = rent_unit_one_line[121+20]
        rent_unit_one_dict["rent_unit_one_dec07"] = rent_unit_one_line[121+22]

        rent_unit_one_dict["rent_unit_one_mar08"] = rent_unit_one_line[121+24]
        rent_unit_one_dict["rent_unit_one_jun08"] = rent_unit_one_line[121+26]
        rent_unit_one_dict["rent_unit_one_sep08"] = rent_unit_one_line[121+28]
        rent_unit_one_dict["rent_unit_one_dec08"] = rent_unit_one_line[121+30]

        rent_unit_one_dict["rent_unit_one_mar09"] = rent_unit_one_line[121+32]
        rent_unit_one_dict["rent_unit_one_jun09"] = rent_unit_one_line[121+34]
        rent_unit_one_dict["rent_unit_one_sep09"] = rent_unit_one_line[121+36]
        rent_unit_one_dict["rent_unit_one_dec09"] = rent_unit_one_line[121+38]

        rent_unit_one_dict["rent_unit_one_mar10"] = rent_unit_one_line[121+40]
        rent_unit_one_dict["rent_unit_one_jun10"] = rent_unit_one_line[121+42]
        rent_unit_one_dict["rent_unit_one_sep10"] = rent_unit_one_line[121+44]
        rent_unit_one_dict["rent_unit_one_dec10"] = rent_unit_one_line[121+46]

        rent_unit_one_dict["rent_unit_one_mar11"] = rent_unit_one_line[121+48]
        rent_unit_one_dict["rent_unit_one_jun11"] = rent_unit_one_line[121+50]
        rent_unit_one_dict["rent_unit_one_sep11"] = rent_unit_one_line[121+52]
        rent_unit_one_dict["rent_unit_one_dec11"] = rent_unit_one_line[121+54]

        rent_unit_one_dict["rent_unit_one_mar12"] = rent_unit_one_line[121+56]
        rent_unit_one_dict["rent_unit_one_jun12"] = rent_unit_one_line[121+58]
        rent_unit_one_dict["rent_unit_one_sep12"] = rent_unit_one_line[121+60]
        rent_unit_one_dict["rent_unit_one_dec12"] = rent_unit_one_line[121+62]

        rent_unit_one_dict["rent_unit_one_mar13"] = rent_unit_one_line[121+64]
        rent_unit_one_dict["rent_unit_one_jun13"] = rent_unit_one_line[121+66]
        rent_unit_one_dict["rent_unit_one_sep13"] = rent_unit_one_line[121+68]
        rent_unit_one_dict["rent_unit_one_dec13"] = rent_unit_one_line[121+70]

        rent_unit_one_dict["rent_unit_one_mar14"] = rent_unit_one_line[121 + 72]
        rent_unit_one_dict["rent_unit_one_jun14"] = rent_unit_one_line[121 + 74]
        rent_unit_one_dict["rent_unit_one_sep14"] = rent_unit_one_line[121 + 76]
        rent_unit_one_dict["rent_unit_one_dec14"] = rent_unit_one_line[121 + 78]

        rent_unit_one_dict["rent_unit_one_mar15"] = rent_unit_one_line[121 + 80]
        rent_unit_one_dict["rent_unit_one_jun15"] = rent_unit_one_line[121 + 82]
        rent_unit_one_dict["rent_unit_one_sep15"] = rent_unit_one_line[121 + 84]
        rent_unit_one_dict["rent_unit_one_dec15"] = rent_unit_one_line[121 + 86]

        rent_unit_one_dict["rent_unit_one_mar16"] = rent_unit_one_line[121 + 88]
        rent_unit_one_dict["rent_unit_one_jun16"] = rent_unit_one_line[121 + 91]
        rent_unit_one_dict["rent_unit_one_sep16"] = rent_unit_one_line[121 + 93]
        rent_unit_one_dict["rent_unit_one_dec16"] = rent_unit_one_line[121 + 95]

        rent_unit_two_line = rent_unit_two.row_values(i)
        index = 0
        for j in rent_unit_two_line:
            if j=="-":
                rent_unit_two_line[index] = rent_unit_two.row_values(3)[index]
            index += 1

        rent_unit_two_dict["rent_unit_two_mar05"] = rent_unit_two_line[121]
        rent_unit_two_dict["rent_unit_two_jun05"] = rent_unit_two_line[121 + 2]
        rent_unit_two_dict["rent_unit_two_sep05"] = rent_unit_two_line[121 + 4]
        rent_unit_two_dict["rent_unit_two_dec05"] = rent_unit_two_line[121 + 6]

        rent_unit_two_dict["rent_unit_two_mar06"] = rent_unit_two_line[121 + 8]
        rent_unit_two_dict["rent_unit_two_jun06"] = rent_unit_two_line[121 + 10]
        rent_unit_two_dict["rent_unit_two_sep06"] = rent_unit_two_line[121 + 12]
        rent_unit_two_dict["rent_unit_two_dec06"] = rent_unit_two_line[121 + 14]

        rent_unit_two_dict["rent_unit_two_mar07"] = rent_unit_two_line[121 + 16]
        rent_unit_two_dict["rent_unit_two_jun07"] = rent_unit_two_line[121 + 18]
        rent_unit_two_dict["rent_unit_two_sep07"] = rent_unit_two_line[121 + 20]
        rent_unit_two_dict["rent_unit_two_dec07"] = rent_unit_two_line[121 + 22]

        rent_unit_two_dict["rent_unit_two_mar08"] = rent_unit_two_line[121 + 24]
        rent_unit_two_dict["rent_unit_two_jun08"] = rent_unit_two_line[121 + 26]
        rent_unit_two_dict["rent_unit_two_sep08"] = rent_unit_two_line[121 + 28]
        rent_unit_two_dict["rent_unit_two_dec08"] = rent_unit_two_line[121 + 30]

        rent_unit_two_dict["rent_unit_two_mar09"] = rent_unit_two_line[121 + 32]
        rent_unit_two_dict["rent_unit_two_jun09"] = rent_unit_two_line[121 + 34]
        rent_unit_two_dict["rent_unit_two_sep09"] = rent_unit_two_line[121 + 36]
        rent_unit_two_dict["rent_unit_two_dec09"] = rent_unit_two_line[121 + 38]

        rent_unit_two_dict["rent_unit_two_mar10"] = rent_unit_two_line[121 + 40]
        rent_unit_two_dict["rent_unit_two_jun10"] = rent_unit_two_line[121 + 42]
        rent_unit_two_dict["rent_unit_two_sep10"] = rent_unit_two_line[121 + 44]
        rent_unit_two_dict["rent_unit_two_dec10"] = rent_unit_two_line[121 + 46]

        rent_unit_two_dict["rent_unit_two_mar11"] = rent_unit_two_line[121 + 48]
        rent_unit_two_dict["rent_unit_two_jun11"] = rent_unit_two_line[121 + 50]
        rent_unit_two_dict["rent_unit_two_sep11"] = rent_unit_two_line[121 + 52]
        rent_unit_two_dict["rent_unit_two_dec11"] = rent_unit_two_line[121 + 54]

        rent_unit_two_dict["rent_unit_two_mar12"] = rent_unit_two_line[121 + 56]
        rent_unit_two_dict["rent_unit_two_jun12"] = rent_unit_two_line[121 + 58]
        rent_unit_two_dict["rent_unit_two_sep12"] = rent_unit_two_line[121 + 60]
        rent_unit_two_dict["rent_unit_two_dec12"] = rent_unit_two_line[121 + 62]

        rent_unit_two_dict["rent_unit_two_mar13"] = rent_unit_two_line[121 + 64]
        rent_unit_two_dict["rent_unit_two_jun13"] = rent_unit_two_line[121 + 66]
        rent_unit_two_dict["rent_unit_two_sep13"] = rent_unit_two_line[121 + 68]
        rent_unit_two_dict["rent_unit_two_dec13"] = rent_unit_two_line[121 + 70]

        rent_unit_two_dict["rent_unit_two_mar14"] = rent_unit_two_line[121 + 72]
        rent_unit_two_dict["rent_unit_two_jun14"] = rent_unit_two_line[121 + 74]
        rent_unit_two_dict["rent_unit_two_sep14"] = rent_unit_two_line[121 + 76]
        rent_unit_two_dict["rent_unit_two_dec14"] = rent_unit_two_line[121 + 78]

        rent_unit_two_dict["rent_unit_two_mar15"] = rent_unit_two_line[121 + 80]
        rent_unit_two_dict["rent_unit_two_jun15"] = rent_unit_two_line[121 + 82]
        rent_unit_two_dict["rent_unit_two_sep15"] = rent_unit_two_line[121 + 84]
        rent_unit_two_dict["rent_unit_two_dec15"] = rent_unit_two_line[121 + 86]

        rent_unit_two_dict["rent_unit_two_mar16"] = rent_unit_two_line[121 + 88]
        rent_unit_two_dict["rent_unit_two_jun16"] = rent_unit_two_line[121 + 91]
        rent_unit_two_dict["rent_unit_two_sep16"] = rent_unit_two_line[121 + 93]
        rent_unit_two_dict["rent_unit_two_dec16"] = rent_unit_two_line[121 + 95]

        rent_unit_all_line = rent_unit_all.row_values(i)
        index = 0
        for j in rent_unit_all_line:
            if j=="-":
                rent_unit_all_line[index] = rent_unit_all.row_values(3)[index]
            index += 1

        rent_unit_all_dict["rent_unit_all_mar05"] = rent_unit_all_line[121]
        rent_unit_all_dict["rent_unit_all_jun05"] = rent_unit_all_line[121 + 2]
        rent_unit_all_dict["rent_unit_all_sep05"] = rent_unit_all_line[121 + 4]
        rent_unit_all_dict["rent_unit_all_dec05"] = rent_unit_all_line[121 + 6]

        rent_unit_all_dict["rent_unit_all_mar06"] = rent_unit_all_line[121 + 8]
        rent_unit_all_dict["rent_unit_all_jun06"] = rent_unit_all_line[121 + 10]
        rent_unit_all_dict["rent_unit_all_sep06"] = rent_unit_all_line[121 + 12]
        rent_unit_all_dict["rent_unit_all_dec06"] = rent_unit_all_line[121 + 14]

        rent_unit_all_dict["rent_unit_all_mar07"] = rent_unit_all_line[121 + 16]
        rent_unit_all_dict["rent_unit_all_jun07"] = rent_unit_all_line[121 + 18]
        rent_unit_all_dict["rent_unit_all_sep07"] = rent_unit_all_line[121 + 20]
        rent_unit_all_dict["rent_unit_all_dec07"] = rent_unit_all_line[121 + 22]

        rent_unit_all_dict["rent_unit_all_mar08"] = rent_unit_all_line[121 + 24]
        rent_unit_all_dict["rent_unit_all_jun08"] = rent_unit_all_line[121 + 26]
        rent_unit_all_dict["rent_unit_all_sep08"] = rent_unit_all_line[121 + 28]
        rent_unit_all_dict["rent_unit_all_dec08"] = rent_unit_all_line[121 + 30]

        rent_unit_all_dict["rent_unit_all_mar09"] = rent_unit_all_line[121 + 32]
        rent_unit_all_dict["rent_unit_all_jun09"] = rent_unit_all_line[121 + 34]
        rent_unit_all_dict["rent_unit_all_sep09"] = rent_unit_all_line[121 + 36]
        rent_unit_all_dict["rent_unit_all_dec09"] = rent_unit_all_line[121 + 38]

        rent_unit_all_dict["rent_unit_all_mar10"] = rent_unit_all_line[121 + 40]
        rent_unit_all_dict["rent_unit_all_jun10"] = rent_unit_all_line[121 + 42]
        rent_unit_all_dict["rent_unit_all_sep10"] = rent_unit_all_line[121 + 44]
        rent_unit_all_dict["rent_unit_all_dec10"] = rent_unit_all_line[121 + 46]

        rent_unit_all_dict["rent_unit_all_mar11"] = rent_unit_all_line[121 + 48]
        rent_unit_all_dict["rent_unit_all_jun11"] = rent_unit_all_line[121 + 50]
        rent_unit_all_dict["rent_unit_all_sep11"] = rent_unit_all_line[121 + 52]
        rent_unit_all_dict["rent_unit_all_dec11"] = rent_unit_all_line[121 + 54]

        rent_unit_all_dict["rent_unit_all_mar12"] = rent_unit_all_line[121 + 56]
        rent_unit_all_dict["rent_unit_all_jun12"] = rent_unit_all_line[121 + 58]
        rent_unit_all_dict["rent_unit_all_sep12"] = rent_unit_all_line[121 + 60]
        rent_unit_all_dict["rent_unit_all_dec12"] = rent_unit_all_line[121 + 62]

        rent_unit_all_dict["rent_unit_all_mar13"] = rent_unit_all_line[121 + 64]
        rent_unit_all_dict["rent_unit_all_jun13"] = rent_unit_all_line[121 + 66]
        rent_unit_all_dict["rent_unit_all_sep13"] = rent_unit_all_line[121 + 68]
        rent_unit_all_dict["rent_unit_all_dec13"] = rent_unit_all_line[121 + 70]

        rent_unit_all_dict["rent_unit_all_mar14"] = rent_unit_all_line[121 + 72]
        rent_unit_all_dict["rent_unit_all_jun14"] = rent_unit_all_line[121 + 74]
        rent_unit_all_dict["rent_unit_all_sep14"] = rent_unit_all_line[121 + 76]
        rent_unit_all_dict["rent_unit_all_dec14"] = rent_unit_all_line[121 + 78]

        rent_unit_all_dict["rent_unit_all_mar15"] = rent_unit_all_line[121 + 80]
        rent_unit_all_dict["rent_unit_all_jun15"] = rent_unit_all_line[121 + 82]
        rent_unit_all_dict["rent_unit_all_sep15"] = rent_unit_all_line[121 + 84]
        rent_unit_all_dict["rent_unit_all_dec15"] = rent_unit_all_line[121 + 86]

        rent_unit_all_dict["rent_unit_all_mar16"] = rent_unit_all_line[121 + 88]
        rent_unit_all_dict["rent_unit_all_jun16"] = rent_unit_all_line[121 + 91]
        rent_unit_all_dict["rent_unit_all_sep16"] = rent_unit_all_line[121 + 93]
        rent_unit_all_dict["rent_unit_all_dec16"] = rent_unit_all_line[121 + 95]

        sale_unit_line = sale_unit.row_values(i + 2)
        index = 0
        for j in sale_unit_line:
            if j=="-":
                sale_unit_line[index] = sale_unit.row_values(5)[index]
            index += 1
        sale_unit_dict['sale_unit_05'] = sale_unit_line[115 + 0] + sale_unit_line[115 + 2] + sale_unit_line[115 + 4] + sale_unit_line[115 + 6]
        sale_unit_dict['sale_unit_06'] = sale_unit_line[115 + 8] + sale_unit_line[115 + 10] + sale_unit_line[115 + 12] +sale_unit_line[115 + 14]
        sale_unit_dict['sale_unit_07'] = sale_unit_line[115 + 16] + sale_unit_line[115 + 18] + sale_unit_line[115 + 20] + sale_unit_line[115 + 22]
        sale_unit_dict['sale_unit_08'] = sale_unit_line[115 + 24] + sale_unit_line[115 + 26] + sale_unit_line[115 + 28] + sale_unit_line[115 + 30]
        sale_unit_dict['sale_unit_09'] = sale_unit_line[115 + 32] + sale_unit_line[115 + 34] + sale_unit_line[115 + 36] + sale_unit_line[115 + 38]
        sale_unit_dict['sale_unit_10'] = sale_unit_line[115 + 40] + sale_unit_line[115 + 42] + sale_unit_line[115 + 44] + sale_unit_line[115 + 46]
        sale_unit_dict['sale_unit_11'] = sale_unit_line[115 + 48] + sale_unit_line[115 + 50] + sale_unit_line[115 + 52] + sale_unit_line[115 + 54]
        sale_unit_dict['sale_unit_12'] = sale_unit_line[115 + 56] + sale_unit_line[115 + 58] + sale_unit_line[115 + 60] + sale_unit_line[115 + 62]
        sale_unit_dict['sale_unit_13'] = sale_unit_line[115 + 64] + sale_unit_line[115 + 66] + sale_unit_line[115 + 68] + sale_unit_line[115 + 70]
        sale_unit_dict['sale_unit_14'] = sale_unit_line[115 + 72] + sale_unit_line[115 + 74] + sale_unit_line[115 + 76] + sale_unit_line[115 + 78]
        sale_unit_dict['sale_unit_15'] = sale_unit_line[115 + 80] + sale_unit_line[115 + 82] + sale_unit_line[115 + 84] + sale_unit_line[115 + 86]
        sale_unit_dict['sale_unit_16'] = sale_unit_line[115 + 88] + sale_unit_line[115 + 90] + sale_unit_line[115 + 92] + sale_unit_line[115 + 94]

        unit_dict={}
        unit_dict["one_rent"]=rent_unit_one_dict
        unit_dict["two_rent"]=rent_unit_two_dict
        unit_dict["all_rent"]=rent_unit_all_dict
        unit_dict["sales"]=sale_unit_dict
        return unit_dict
        # house_dict={}
        # t1 = Dwellings(lga=rent_unit_one_line[0],unit=unit_dict)
        #
        # connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        # t1.save()

    # for i in range(16,31):
    if i>=16 and i<31:
        rent_unit_one_line=rent_unit_one.row_values(i)
        index=0
        for j in rent_unit_one_line:
            if j=="-":
                rent_unit_one_line[index]=rent_unit_one.row_values(15)[index]
            index+=1

        rent_unit_one_dict["rent_unit_one_mar05"]=rent_unit_one_line[121]
        rent_unit_one_dict["rent_unit_one_jun05"]=rent_unit_one_line[121+2]
        rent_unit_one_dict["rent_unit_one_sep05"]=rent_unit_one_line[121+4]
        rent_unit_one_dict["rent_unit_one_dec05"]=rent_unit_one_line[121+6]

        rent_unit_one_dict["rent_unit_one_mar06"] = rent_unit_one_line[121+8]
        rent_unit_one_dict["rent_unit_one_jun06"] = rent_unit_one_line[121+10]
        rent_unit_one_dict["rent_unit_one_sep06"] = rent_unit_one_line[121+12]
        rent_unit_one_dict["rent_unit_one_dec06"] = rent_unit_one_line[121+14]

        rent_unit_one_dict["rent_unit_one_mar07"] = rent_unit_one_line[121+16]
        rent_unit_one_dict["rent_unit_one_jun07"] = rent_unit_one_line[121+18]
        rent_unit_one_dict["rent_unit_one_sep07"] = rent_unit_one_line[121+20]
        rent_unit_one_dict["rent_unit_one_dec07"] = rent_unit_one_line[121+22]

        rent_unit_one_dict["rent_unit_one_mar08"] = rent_unit_one_line[121+24]
        rent_unit_one_dict["rent_unit_one_jun08"] = rent_unit_one_line[121+26]
        rent_unit_one_dict["rent_unit_one_sep08"] = rent_unit_one_line[121+28]
        rent_unit_one_dict["rent_unit_one_dec08"] = rent_unit_one_line[121+30]

        rent_unit_one_dict["rent_unit_one_mar09"] = rent_unit_one_line[121+32]
        rent_unit_one_dict["rent_unit_one_jun09"] = rent_unit_one_line[121+34]
        rent_unit_one_dict["rent_unit_one_sep09"] = rent_unit_one_line[121+36]
        rent_unit_one_dict["rent_unit_one_dec09"] = rent_unit_one_line[121+38]

        rent_unit_one_dict["rent_unit_one_mar10"] = rent_unit_one_line[121+40]
        rent_unit_one_dict["rent_unit_one_jun10"] = rent_unit_one_line[121+42]
        rent_unit_one_dict["rent_unit_one_sep10"] = rent_unit_one_line[121+44]
        rent_unit_one_dict["rent_unit_one_dec10"] = rent_unit_one_line[121+46]

        rent_unit_one_dict["rent_unit_one_mar11"] = rent_unit_one_line[121+48]
        rent_unit_one_dict["rent_unit_one_jun11"] = rent_unit_one_line[121+50]
        rent_unit_one_dict["rent_unit_one_sep11"] = rent_unit_one_line[121+52]
        rent_unit_one_dict["rent_unit_one_dec11"] = rent_unit_one_line[121+54]

        rent_unit_one_dict["rent_unit_one_mar12"] = rent_unit_one_line[121+56]
        rent_unit_one_dict["rent_unit_one_jun12"] = rent_unit_one_line[121+58]
        rent_unit_one_dict["rent_unit_one_sep12"] = rent_unit_one_line[121+60]
        rent_unit_one_dict["rent_unit_one_dec12"] = rent_unit_one_line[121+62]

        rent_unit_one_dict["rent_unit_one_mar13"] = rent_unit_one_line[121+64]
        rent_unit_one_dict["rent_unit_one_jun13"] = rent_unit_one_line[121+66]
        rent_unit_one_dict["rent_unit_one_sep13"] = rent_unit_one_line[121+68]
        rent_unit_one_dict["rent_unit_one_dec13"] = rent_unit_one_line[121+70]

        rent_unit_one_dict["rent_unit_one_mar14"] = rent_unit_one_line[121 + 72]
        rent_unit_one_dict["rent_unit_one_jun14"] = rent_unit_one_line[121 + 74]
        rent_unit_one_dict["rent_unit_one_sep14"] = rent_unit_one_line[121 + 76]
        rent_unit_one_dict["rent_unit_one_dec14"] = rent_unit_one_line[121 + 78]

        rent_unit_one_dict["rent_unit_one_mar15"] = rent_unit_one_line[121 + 80]
        rent_unit_one_dict["rent_unit_one_jun15"] = rent_unit_one_line[121 + 82]
        rent_unit_one_dict["rent_unit_one_sep15"] = rent_unit_one_line[121 + 84]
        rent_unit_one_dict["rent_unit_one_dec15"] = rent_unit_one_line[121 + 86]

        rent_unit_one_dict["rent_unit_one_mar16"] = rent_unit_one_line[121 + 88]
        rent_unit_one_dict["rent_unit_one_jun16"] = rent_unit_one_line[121 + 91]
        rent_unit_one_dict["rent_unit_one_sep16"] = rent_unit_one_line[121 + 93]
        rent_unit_one_dict["rent_unit_one_dec16"] = rent_unit_one_line[121 + 95]

        rent_unit_two_line = rent_unit_two.row_values(i)
        index = 0
        for j in rent_unit_two_line:
            if j=="-":
                rent_unit_two_line[index] = rent_unit_two.row_values(15)[index]
            index += 1

        rent_unit_two_dict["rent_unit_two_mar05"] = rent_unit_two_line[121]
        rent_unit_two_dict["rent_unit_two_jun05"] = rent_unit_two_line[121 + 2]
        rent_unit_two_dict["rent_unit_two_sep05"] = rent_unit_two_line[121 + 4]
        rent_unit_two_dict["rent_unit_two_dec05"] = rent_unit_two_line[121 + 6]

        rent_unit_two_dict["rent_unit_two_mar06"] = rent_unit_two_line[121 + 8]
        rent_unit_two_dict["rent_unit_two_jun06"] = rent_unit_two_line[121 + 10]
        rent_unit_two_dict["rent_unit_two_sep06"] = rent_unit_two_line[121 + 12]
        rent_unit_two_dict["rent_unit_two_dec06"] = rent_unit_two_line[121 + 14]

        rent_unit_two_dict["rent_unit_two_mar07"] = rent_unit_two_line[121 + 16]
        rent_unit_two_dict["rent_unit_two_jun07"] = rent_unit_two_line[121 + 18]
        rent_unit_two_dict["rent_unit_two_sep07"] = rent_unit_two_line[121 + 20]
        rent_unit_two_dict["rent_unit_two_dec07"] = rent_unit_two_line[121 + 22]

        rent_unit_two_dict["rent_unit_two_mar08"] = rent_unit_two_line[121 + 24]
        rent_unit_two_dict["rent_unit_two_jun08"] = rent_unit_two_line[121 + 26]
        rent_unit_two_dict["rent_unit_two_sep08"] = rent_unit_two_line[121 + 28]
        rent_unit_two_dict["rent_unit_two_dec08"] = rent_unit_two_line[121 + 30]

        rent_unit_two_dict["rent_unit_two_mar09"] = rent_unit_two_line[121 + 32]
        rent_unit_two_dict["rent_unit_two_jun09"] = rent_unit_two_line[121 + 34]
        rent_unit_two_dict["rent_unit_two_sep09"] = rent_unit_two_line[121 + 36]
        rent_unit_two_dict["rent_unit_two_dec09"] = rent_unit_two_line[121 + 38]

        rent_unit_two_dict["rent_unit_two_mar10"] = rent_unit_two_line[121 + 40]
        rent_unit_two_dict["rent_unit_two_jun10"] = rent_unit_two_line[121 + 42]
        rent_unit_two_dict["rent_unit_two_sep10"] = rent_unit_two_line[121 + 44]
        rent_unit_two_dict["rent_unit_two_dec10"] = rent_unit_two_line[121 + 46]

        rent_unit_two_dict["rent_unit_two_mar11"] = rent_unit_two_line[121 + 48]
        rent_unit_two_dict["rent_unit_two_jun11"] = rent_unit_two_line[121 + 50]
        rent_unit_two_dict["rent_unit_two_sep11"] = rent_unit_two_line[121 + 52]
        rent_unit_two_dict["rent_unit_two_dec11"] = rent_unit_two_line[121 + 54]

        rent_unit_two_dict["rent_unit_two_mar12"] = rent_unit_two_line[121 + 56]
        rent_unit_two_dict["rent_unit_two_jun12"] = rent_unit_two_line[121 + 58]
        rent_unit_two_dict["rent_unit_two_sep12"] = rent_unit_two_line[121 + 60]
        rent_unit_two_dict["rent_unit_two_dec12"] = rent_unit_two_line[121 + 62]

        rent_unit_two_dict["rent_unit_two_mar13"] = rent_unit_two_line[121 + 64]
        rent_unit_two_dict["rent_unit_two_jun13"] = rent_unit_two_line[121 + 66]
        rent_unit_two_dict["rent_unit_two_sep13"] = rent_unit_two_line[121 + 68]
        rent_unit_two_dict["rent_unit_two_dec13"] = rent_unit_two_line[121 + 70]

        rent_unit_two_dict["rent_unit_two_mar14"] = rent_unit_two_line[121 + 72]
        rent_unit_two_dict["rent_unit_two_jun14"] = rent_unit_two_line[121 + 74]
        rent_unit_two_dict["rent_unit_two_sep14"] = rent_unit_two_line[121 + 76]
        rent_unit_two_dict["rent_unit_two_dec14"] = rent_unit_two_line[121 + 78]

        rent_unit_two_dict["rent_unit_two_mar15"] = rent_unit_two_line[121 + 80]
        rent_unit_two_dict["rent_unit_two_jun15"] = rent_unit_two_line[121 + 82]
        rent_unit_two_dict["rent_unit_two_sep15"] = rent_unit_two_line[121 + 84]
        rent_unit_two_dict["rent_unit_two_dec15"] = rent_unit_two_line[121 + 86]

        rent_unit_two_dict["rent_unit_two_mar16"] = rent_unit_two_line[121 + 88]
        rent_unit_two_dict["rent_unit_two_jun16"] = rent_unit_two_line[121 + 91]
        rent_unit_two_dict["rent_unit_two_sep16"] = rent_unit_two_line[121 + 93]
        rent_unit_two_dict["rent_unit_two_dec16"] = rent_unit_two_line[121 + 95]

        rent_unit_all_line = rent_unit_all.row_values(i)
        index = 0
        for j in rent_unit_all_line:
            if j=="-":
                rent_unit_all_line[index] = rent_unit_all.row_values(15)[index]
            index += 1

        rent_unit_all_dict["rent_unit_all_mar05"] = rent_unit_all_line[121]
        rent_unit_all_dict["rent_unit_all_jun05"] = rent_unit_all_line[121 + 2]
        rent_unit_all_dict["rent_unit_all_sep05"] = rent_unit_all_line[121 + 4]
        rent_unit_all_dict["rent_unit_all_dec05"] = rent_unit_all_line[121 + 6]

        rent_unit_all_dict["rent_unit_all_mar06"] = rent_unit_all_line[121 + 8]
        rent_unit_all_dict["rent_unit_all_jun06"] = rent_unit_all_line[121 + 10]
        rent_unit_all_dict["rent_unit_all_sep06"] = rent_unit_all_line[121 + 12]
        rent_unit_all_dict["rent_unit_all_dec06"] = rent_unit_all_line[121 + 14]

        rent_unit_all_dict["rent_unit_all_mar07"] = rent_unit_all_line[121 + 16]
        rent_unit_all_dict["rent_unit_all_jun07"] = rent_unit_all_line[121 + 18]
        rent_unit_all_dict["rent_unit_all_sep07"] = rent_unit_all_line[121 + 20]
        rent_unit_all_dict["rent_unit_all_dec07"] = rent_unit_all_line[121 + 22]

        rent_unit_all_dict["rent_unit_all_mar08"] = rent_unit_all_line[121 + 24]
        rent_unit_all_dict["rent_unit_all_jun08"] = rent_unit_all_line[121 + 26]
        rent_unit_all_dict["rent_unit_all_sep08"] = rent_unit_all_line[121 + 28]
        rent_unit_all_dict["rent_unit_all_dec08"] = rent_unit_all_line[121 + 30]

        rent_unit_all_dict["rent_unit_all_mar09"] = rent_unit_all_line[121 + 32]
        rent_unit_all_dict["rent_unit_all_jun09"] = rent_unit_all_line[121 + 34]
        rent_unit_all_dict["rent_unit_all_sep09"] = rent_unit_all_line[121 + 36]
        rent_unit_all_dict["rent_unit_all_dec09"] = rent_unit_all_line[121 + 38]

        rent_unit_all_dict["rent_unit_all_mar10"] = rent_unit_all_line[121 + 40]
        rent_unit_all_dict["rent_unit_all_jun10"] = rent_unit_all_line[121 + 42]
        rent_unit_all_dict["rent_unit_all_sep10"] = rent_unit_all_line[121 + 44]
        rent_unit_all_dict["rent_unit_all_dec10"] = rent_unit_all_line[121 + 46]

        rent_unit_all_dict["rent_unit_all_mar11"] = rent_unit_all_line[121 + 48]
        rent_unit_all_dict["rent_unit_all_jun11"] = rent_unit_all_line[121 + 50]
        rent_unit_all_dict["rent_unit_all_sep11"] = rent_unit_all_line[121 + 52]
        rent_unit_all_dict["rent_unit_all_dec11"] = rent_unit_all_line[121 + 54]

        rent_unit_all_dict["rent_unit_all_mar12"] = rent_unit_all_line[121 + 56]
        rent_unit_all_dict["rent_unit_all_jun12"] = rent_unit_all_line[121 + 58]
        rent_unit_all_dict["rent_unit_all_sep12"] = rent_unit_all_line[121 + 60]
        rent_unit_all_dict["rent_unit_all_dec12"] = rent_unit_all_line[121 + 62]

        rent_unit_all_dict["rent_unit_all_mar13"] = rent_unit_all_line[121 + 64]
        rent_unit_all_dict["rent_unit_all_jun13"] = rent_unit_all_line[121 + 66]
        rent_unit_all_dict["rent_unit_all_sep13"] = rent_unit_all_line[121 + 68]
        rent_unit_all_dict["rent_unit_all_dec13"] = rent_unit_all_line[121 + 70]

        rent_unit_all_dict["rent_unit_all_mar14"] = rent_unit_all_line[121 + 72]
        rent_unit_all_dict["rent_unit_all_jun14"] = rent_unit_all_line[121 + 74]
        rent_unit_all_dict["rent_unit_all_sep14"] = rent_unit_all_line[121 + 76]
        rent_unit_all_dict["rent_unit_all_dec14"] = rent_unit_all_line[121 + 78]

        rent_unit_all_dict["rent_unit_all_mar15"] = rent_unit_all_line[121 + 80]
        rent_unit_all_dict["rent_unit_all_jun15"] = rent_unit_all_line[121 + 82]
        rent_unit_all_dict["rent_unit_all_sep15"] = rent_unit_all_line[121 + 84]
        rent_unit_all_dict["rent_unit_all_dec15"] = rent_unit_all_line[121 + 86]

        rent_unit_all_dict["rent_unit_all_mar16"] = rent_unit_all_line[121 + 88]
        rent_unit_all_dict["rent_unit_all_jun16"] = rent_unit_all_line[121 + 91]
        rent_unit_all_dict["rent_unit_all_sep16"] = rent_unit_all_line[121 + 93]
        rent_unit_all_dict["rent_unit_all_dec16"] = rent_unit_all_line[121 + 95]

        sale_unit_line = sale_unit.row_values(i + 2)
        index = 0
        for j in sale_unit_line:
            if j=="-":
                sale_unit_line[index] = sale_unit.row_values(17)[index]
            index += 1
        sale_unit_dict['sale_unit_05'] = sale_unit_line[115 + 0] + sale_unit_line[115 + 2] + sale_unit_line[115 + 4] + sale_unit_line[115 + 6]
        sale_unit_dict['sale_unit_06'] = sale_unit_line[115 + 8] + sale_unit_line[115 + 10] + sale_unit_line[115 + 12] +sale_unit_line[115 + 14]
        sale_unit_dict['sale_unit_07'] = sale_unit_line[115 + 16] + sale_unit_line[115 + 18] + sale_unit_line[115 + 20] + sale_unit_line[115 + 22]
        sale_unit_dict['sale_unit_08'] = sale_unit_line[115 + 24] + sale_unit_line[115 + 26] + sale_unit_line[115 + 28] + sale_unit_line[115 + 30]
        sale_unit_dict['sale_unit_09'] = sale_unit_line[115 + 32] + sale_unit_line[115 + 34] + sale_unit_line[115 + 36] + sale_unit_line[115 + 38]
        sale_unit_dict['sale_unit_10'] = sale_unit_line[115 + 40] + sale_unit_line[115 + 42] + sale_unit_line[115 + 44] + sale_unit_line[115 + 46]
        sale_unit_dict['sale_unit_11'] = sale_unit_line[115 + 48] + sale_unit_line[115 + 50] + sale_unit_line[115 + 52] + sale_unit_line[115 + 54]
        sale_unit_dict['sale_unit_12'] = sale_unit_line[115 + 56] + sale_unit_line[115 + 58] + sale_unit_line[115 + 60] + sale_unit_line[115 + 62]
        sale_unit_dict['sale_unit_13'] = sale_unit_line[115 + 64] + sale_unit_line[115 + 66] + sale_unit_line[115 + 68] + sale_unit_line[115 + 70]
        sale_unit_dict['sale_unit_14'] = sale_unit_line[115 + 72] + sale_unit_line[115 + 74] + sale_unit_line[115 + 76] + sale_unit_line[115 + 78]
        sale_unit_dict['sale_unit_15'] = sale_unit_line[115 + 80] + sale_unit_line[115 + 82] + sale_unit_line[115 + 84] + sale_unit_line[115 + 86]
        sale_unit_dict['sale_unit_16'] = sale_unit_line[115 + 88] + sale_unit_line[115 + 90] + sale_unit_line[115 + 92] + sale_unit_line[115 + 94]

        unit_dict={}
        unit_dict["one_rent"]=rent_unit_one_dict
        unit_dict["two_rent"]=rent_unit_two_dict
        unit_dict["all_rent"]=rent_unit_all_dict
        unit_dict["sales"]=sale_unit_dict
        return unit_dict
        # t1 = Dwellings(lga=rent_unit_one_line[0],unit=unit_dict)
        #
        # connect(host='mongodb://9321project:9321project@ds229690.mlab.com:29690/9321project')
        # t1.save()

    # for i in range(32, 49):
    if i>=32 and i<49:
        rent_unit_one_line = rent_unit_one.row_values(i)
        index = 0
        for j in rent_unit_one_line:
            if j=="-":
                rent_unit_one_line[index] = rent_unit_one.row_values(31)[index]
            index += 1

        rent_unit_one_dict["rent_unit_one_mar05"] = rent_unit_one_line[121]
        rent_unit_one_dict["rent_unit_one_jun05"] = rent_unit_one_line[121 + 2]
        rent_unit_one_dict["rent_unit_one_sep05"] = rent_unit_one_line[121 + 4]
        rent_unit_one_dict["rent_unit_one_dec05"] = rent_unit_one_line[121 + 6]

        rent_unit_one_dict["rent_unit_one_mar06"] = rent_unit_one_line[121 + 8]
        rent_unit_one_dict["rent_unit_one_jun06"] = rent_unit_one_line[121 + 10]
        rent_unit_one_dict["rent_unit_one_sep06"] = rent_unit_one_line[121 + 12]
        rent_unit_one_dict["rent_unit_one_dec06"] = rent_unit_one_line[121 + 14]

        rent_unit_one_dict["rent_unit_one_mar07"] = rent_unit_one_line[121 + 16]
        rent_unit_one_dict["rent_unit_one_jun07"] = rent_unit_one_line[121 + 18]
        rent_unit_one_dict["rent_unit_one_sep07"] = rent_unit_one_line[121 + 20]
        rent_unit_one_dict["rent_unit_one_dec07"] = rent_unit_one_line[121 + 22]

        rent_unit_one_dict["rent_unit_one_mar08"] = rent_unit_one_line[121 + 24]
        rent_unit_one_dict["rent_unit_one_jun08"] = rent_unit_one_line[121 + 26]
        rent_unit_one_dict["rent_unit_one_sep08"] = rent_unit_one_line[121 + 28]
        rent_unit_one_dict["rent_unit_one_dec08"] = rent_unit_one_line[121 + 30]

        rent_unit_one_dict["rent_unit_one_mar09"] = rent_unit_one_line[121 + 32]
        rent_unit_one_dict["rent_unit_one_jun09"] = rent_unit_one_line[121 + 34]
        rent_unit_one_dict["rent_unit_one_sep09"] = rent_unit_one_line[121 + 36]
        rent_unit_one_dict["rent_unit_one_dec09"] = rent_unit_one_line[121 + 38]

        rent_unit_one_dict["rent_unit_one_mar10"] = rent_unit_one_line[121 + 40]
        rent_unit_one_dict["rent_unit_one_jun10"] = rent_unit_one_line[121 + 42]
        rent_unit_one_dict["rent_unit_one_sep10"] = rent_unit_one_line[121 + 44]
        rent_unit_one_dict["rent_unit_one_dec10"] = rent_unit_one_line[121 + 46]

        rent_unit_one_dict["rent_unit_one_mar11"] = rent_unit_one_line[121 + 48]
        rent_unit_one_dict["rent_unit_one_jun11"] = rent_unit_one_line[121 + 50]
        rent_unit_one_dict["rent_unit_one_sep11"] = rent_unit_one_line[121 + 52]
        rent_unit_one_dict["rent_unit_one_dec11"] = rent_unit_one_line[121 + 54]

        rent_unit_one_dict["rent_unit_one_mar12"] = rent_unit_one_line[121 + 56]
        rent_unit_one_dict["rent_unit_one_jun12"] = rent_unit_one_line[121 + 58]
        rent_unit_one_dict["rent_unit_one_sep12"] = rent_unit_one_line[121 + 60]
        rent_unit_one_dict["rent_unit_one_dec12"] = rent_unit_one_line[121 + 62]

        rent_unit_one_dict["rent_unit_one_mar13"] = rent_unit_one_line[121 + 64]
        rent_unit_one_dict["rent_unit_one_jun13"] = rent_unit_one_line[121 + 66]
        rent_unit_one_dict["rent_unit_one_sep13"] = rent_unit_one_line[121 + 68]
        rent_unit_one_dict["rent_unit_one_dec13"] = rent_unit_one_line[121 + 70]

        rent_unit_one_dict["rent_unit_one_mar14"] = rent_unit_one_line[121 + 72]
        rent_unit_one_dict["rent_unit_one_jun14"] = rent_unit_one_line[121 + 74]
        rent_unit_one_dict["rent_unit_one_sep14"] = rent_unit_one_line[121 + 76]
        rent_unit_one_dict["rent_unit_one_dec14"] = rent_unit_one_line[121 + 78]

        rent_unit_one_dict["rent_unit_one_mar15"] = rent_unit_one_line[121 + 80]
        rent_unit_one_dict["rent_unit_one_jun15"] = rent_unit_one_line[121 + 82]
        rent_unit_one_dict["rent_unit_one_sep15"] = rent_unit_one_line[121 + 84]
        rent_unit_one_dict["rent_unit_one_dec15"] = rent_unit_one_line[121 + 86]

        rent_unit_one_dict["rent_unit_one_mar16"] = rent_unit_one_line[121 + 88]
        rent_unit_one_dict["rent_unit_one_jun16"] = rent_unit_one_line[121 + 91]
        rent_unit_one_dict["rent_unit_one_sep16"] = rent_unit_one_line[121 + 93]
        rent_unit_one_dict["rent_unit_one_dec16"] = rent_unit_one_line[121 + 95]

        rent_unit_two_line = rent_unit_two.row_values(i)
        index = 0
        for j in rent_unit_two_line:
            if j=="-":
                rent_unit_two_line[index] = rent_unit_two.row_values(31)[index]
            index += 1

        rent_unit_two_dict["rent_unit_two_mar05"] = rent_unit_two_line[121]
        rent_unit_two_dict["rent_unit_two_jun05"] = rent_unit_two_line[121 + 2]
        rent_unit_two_dict["rent_unit_two_sep05"] = rent_unit_two_line[121 + 4]
        rent_unit_two_dict["rent_unit_two_dec05"] = rent_unit_two_line[121 + 6]

        rent_unit_two_dict["rent_unit_two_mar06"] = rent_unit_two_line[121 + 8]
        rent_unit_two_dict["rent_unit_two_jun06"] = rent_unit_two_line[121 + 10]
        rent_unit_two_dict["rent_unit_two_sep06"] = rent_unit_two_line[121 + 12]
        rent_unit_two_dict["rent_unit_two_dec06"] = rent_unit_two_line[121 + 14]

        rent_unit_two_dict["rent_unit_two_mar07"] = rent_unit_two_line[121 + 16]
        rent_unit_two_dict["rent_unit_two_jun07"] = rent_unit_two_line[121 + 18]
        rent_unit_two_dict["rent_unit_two_sep07"] = rent_unit_two_line[121 + 20]
        rent_unit_two_dict["rent_unit_two_dec07"] = rent_unit_two_line[121 + 22]

        rent_unit_two_dict["rent_unit_two_mar08"] = rent_unit_two_line[121 + 24]
        rent_unit_two_dict["rent_unit_two_jun08"] = rent_unit_two_line[121 + 26]
        rent_unit_two_dict["rent_unit_two_sep08"] = rent_unit_two_line[121 + 28]
        rent_unit_two_dict["rent_unit_two_dec08"] = rent_unit_two_line[121 + 30]

        rent_unit_two_dict["rent_unit_two_mar09"] = rent_unit_two_line[121 + 32]
        rent_unit_two_dict["rent_unit_two_jun09"] = rent_unit_two_line[121 + 34]
        rent_unit_two_dict["rent_unit_two_sep09"] = rent_unit_two_line[121 + 36]
        rent_unit_two_dict["rent_unit_two_dec09"] = rent_unit_two_line[121 + 38]

        rent_unit_two_dict["rent_unit_two_mar10"] = rent_unit_two_line[121 + 40]
        rent_unit_two_dict["rent_unit_two_jun10"] = rent_unit_two_line[121 + 42]
        rent_unit_two_dict["rent_unit_two_sep10"] = rent_unit_two_line[121 + 44]
        rent_unit_two_dict["rent_unit_two_dec10"] = rent_unit_two_line[121 + 46]

        rent_unit_two_dict["rent_unit_two_mar11"] = rent_unit_two_line[121 + 48]
        rent_unit_two_dict["rent_unit_two_jun11"] = rent_unit_two_line[121 + 50]
        rent_unit_two_dict["rent_unit_two_sep11"] = rent_unit_two_line[121 + 52]
        rent_unit_two_dict["rent_unit_two_dec11"] = rent_unit_two_line[121 + 54]

        rent_unit_two_dict["rent_unit_two_mar12"] = rent_unit_two_line[121 + 56]
        rent_unit_two_dict["rent_unit_two_jun12"] = rent_unit_two_line[121 + 58]
        rent_unit_two_dict["rent_unit_two_sep12"] = rent_unit_two_line[121 + 60]
        rent_unit_two_dict["rent_unit_two_dec12"] = rent_unit_two_line[121 + 62]

        rent_unit_two_dict["rent_unit_two_mar13"] = rent_unit_two_line[121 + 64]
        rent_unit_two_dict["rent_unit_two_jun13"] = rent_unit_two_line[121 + 66]
        rent_unit_two_dict["rent_unit_two_sep13"] = rent_unit_two_line[121 + 68]
        rent_unit_two_dict["rent_unit_two_dec13"] = rent_unit_two_line[121 + 70]

        rent_unit_two_dict["rent_unit_two_mar14"] = rent_unit_two_line[121 + 72]
        rent_unit_two_dict["rent_unit_two_jun14"] = rent_unit_two_line[121 + 74]
        rent_unit_two_dict["rent_unit_two_sep14"] = rent_unit_two_line[121 + 76]
        rent_unit_two_dict["rent_unit_two_dec14"] = rent_unit_two_line[121 + 78]

        rent_unit_two_dict["rent_unit_two_mar15"] = rent_unit_two_line[121 + 80]
        rent_unit_two_dict["rent_unit_two_jun15"] = rent_unit_two_line[121 + 82]
        rent_unit_two_dict["rent_unit_two_sep15"] = rent_unit_two_line[121 + 84]
        rent_unit_two_dict["rent_unit_two_dec15"] = rent_unit_two_line[121 + 86]

        rent_unit_two_dict["rent_unit_two_mar16"] = rent_unit_two_line[121 + 88]
        rent_unit_two_dict["rent_unit_two_jun16"] = rent_unit_two_line[121 + 91]
        rent_unit_two_dict["rent_unit_two_sep16"] = rent_unit_two_line[121 + 93]
        rent_unit_two_dict["rent_unit_two_dec16"] = rent_unit_two_line[121 + 95]

        rent_unit_all_line = rent_unit_all.row_values(i)
        index = 0
        for j in rent_unit_all_line:
            if j=="-":
                rent_unit_all_line[index] = rent_unit_all.row_values(31)[index]
            index += 1

        rent_unit_all_dict["rent_unit_all_mar05"] = rent_unit_all_line[121]
        rent_unit_all_dict["rent_unit_all_jun05"] = rent_unit_all_line[121 + 2]
        rent_unit_all_dict["rent_unit_all_sep05"] = rent_unit_all_line[121 + 4]
        rent_unit_all_dict["rent_unit_all_dec05"] = rent_unit_all_line[121 + 6]

        rent_unit_all_dict["rent_unit_all_mar06"] = rent_unit_all_line[121 + 8]
        rent_unit_all_dict["rent_unit_all_jun06"] = rent_unit_all_line[121 + 10]
        rent_unit_all_dict["rent_unit_all_sep06"] = rent_unit_all_line[121 + 12]
        rent_unit_all_dict["rent_unit_all_dec06"] = rent_unit_all_line[121 + 14]

        rent_unit_all_dict["rent_unit_all_mar07"] = rent_unit_all_line[121 + 16]
        rent_unit_all_dict["rent_unit_all_jun07"] = rent_unit_all_line[121 + 18]
        rent_unit_all_dict["rent_unit_all_sep07"] = rent_unit_all_line[121 + 20]
        rent_unit_all_dict["rent_unit_all_dec07"] = rent_unit_all_line[121 + 22]

        rent_unit_all_dict["rent_unit_all_mar08"] = rent_unit_all_line[121 + 24]
        rent_unit_all_dict["rent_unit_all_jun08"] = rent_unit_all_line[121 + 26]
        rent_unit_all_dict["rent_unit_all_sep08"] = rent_unit_all_line[121 + 28]
        rent_unit_all_dict["rent_unit_all_dec08"] = rent_unit_all_line[121 + 30]

        rent_unit_all_dict["rent_unit_all_mar09"] = rent_unit_all_line[121 + 32]
        rent_unit_all_dict["rent_unit_all_jun09"] = rent_unit_all_line[121 + 34]
        rent_unit_all_dict["rent_unit_all_sep09"] = rent_unit_all_line[121 + 36]
        rent_unit_all_dict["rent_unit_all_dec09"] = rent_unit_all_line[121 + 38]

        rent_unit_all_dict["rent_unit_all_mar10"] = rent_unit_all_line[121 + 40]
        rent_unit_all_dict["rent_unit_all_jun10"] = rent_unit_all_line[121 + 42]
        rent_unit_all_dict["rent_unit_all_sep10"] = rent_unit_all_line[121 + 44]
        rent_unit_all_dict["rent_unit_all_dec10"] = rent_unit_all_line[121 + 46]

        rent_unit_all_dict["rent_unit_all_mar11"] = rent_unit_all_line[121 + 48]
        rent_unit_all_dict["rent_unit_all_jun11"] = rent_unit_all_line[121 + 50]
        rent_unit_all_dict["rent_unit_all_sep11"] = rent_unit_all_line[121 + 52]
        rent_unit_all_dict["rent_unit_all_dec11"] = rent_unit_all_line[121 + 54]

        rent_unit_all_dict["rent_unit_all_mar12"] = rent_unit_all_line[121 + 56]
        rent_unit_all_dict["rent_unit_all_jun12"] = rent_unit_all_line[121 + 58]
        rent_unit_all_dict["rent_unit_all_sep12"] = rent_unit_all_line[121 + 60]
        rent_unit_all_dict["rent_unit_all_dec12"] = rent_unit_all_line[121 + 62]

        rent_unit_all_dict["rent_unit_all_mar13"] = rent_unit_all_line[121 + 64]
        rent_unit_all_dict["rent_unit_all_jun13"] = rent_unit_all_line[121 + 66]
        rent_unit_all_dict["rent_unit_all_sep13"] = rent_unit_all_line[121 + 68]
        rent_unit_all_dict["rent_unit_all_dec13"] = rent_unit_all_line[121 + 70]

        rent_unit_all_dict["rent_unit_all_mar14"] = rent_unit_all_line[121 + 72]
        rent_unit_all_dict["rent_unit_all_jun14"] = rent_unit_all_line[121 + 74]
        rent_unit_all_dict["rent_unit_all_sep14"] = rent_unit_all_line[121 + 76]
        rent_unit_all_dict["rent_unit_all_dec14"] = rent_unit_all_line[121 + 78]

        rent_unit_all_dict["rent_unit_all_mar15"] = rent_unit_all_line[121 + 80]
        rent_unit_all_dict["rent_unit_all_jun15"] = rent_unit_all_line[121 + 82]
        rent_unit_all_dict["rent_unit_all_sep15"] = rent_unit_all_line[121 + 84]
        rent_unit_all_dict["rent_unit_all_dec15"] = rent_unit_all_line[121 + 86]

        rent_unit_all_dict["rent_unit_all_mar16"] = rent_unit_all_line[121 + 88]
        rent_unit_all_dict["rent_unit_all_jun16"] = rent_unit_all_line[121 + 91]
        rent_unit_all_dict["rent_unit_all_sep16"] = rent_unit_all_line[121 + 93]
        rent_unit_all_dict["rent_unit_all_dec16"] = rent_unit_all_line[121 + 95]

        sale_unit_line = sale_unit.row_values(i + 2)
        index = 0
        for j in sale_unit_line:

            if j=="-":
            # if j=="-":
                sale_unit_line[index] = sale_unit.row_values(33)[index]
            index += 1

        # print(sale_unit_line)
        sale_unit_dict['sale_unit_05'] = sale_unit_line[115 + 0] + sale_unit_line[115 + 2] + sale_unit_line[115 + 4] + sale_unit_line[115 + 6]
        sale_unit_dict['sale_unit_06'] = sale_unit_line[115 + 8] + sale_unit_line[115 + 10] + sale_unit_line[115 + 12] + sale_unit_line[115 + 14]
        sale_unit_dict['sale_unit_07'] = sale_unit_line[115 + 16] + sale_unit_line[115 + 18] + sale_unit_line[115 + 20] + sale_unit_line[115 + 22]
        sale_unit_dict['sale_unit_08'] = sale_unit_line[115 + 24] + sale_unit_line[115 + 26] + sale_unit_line[115 + 28] + sale_unit_line[115 + 30]
        sale_unit_dict['sale_unit_09'] = sale_unit_line[115 + 32] + sale_unit_line[115 + 34] + sale_unit_line[115 + 36] + sale_unit_line[115 + 38]
        sale_unit_dict['sale_unit_10'] = sale_unit_line[115 + 40] + sale_unit_line[115 + 42] + sale_unit_line[115 + 44] + sale_unit_line[115 + 46]
        sale_unit_dict['sale_unit_11'] = sale_unit_line[115 + 48] + sale_unit_line[115 + 50] + sale_unit_line[115 + 52] + sale_unit_line[115 + 54]
        sale_unit_dict['sale_unit_12'] = sale_unit_line[115 + 56] + sale_unit_line[115 + 58] + sale_unit_line[115 + 60] + sale_unit_line[115 + 62]
        sale_unit_dict['sale_unit_13'] = sale_unit_line[115 + 64] + sale_unit_line[115 + 66] + sale_unit_line[115 + 68] + sale_unit_line[115 + 70]
        sale_unit_dict['sale_unit_14'] = sale_unit_line[115 + 72] + sale_unit_line[115 + 74] + sale_unit_line[115 + 76] + sale_unit_line[115 + 78]
        sale_unit_dict['sale_unit_15'] = sale_unit_line[115 + 80] + sale_unit_line[115 + 82] + sale_unit_line[115 + 84] + sale_unit_line[115 + 86]
        sale_unit_dict['sale_unit_16'] = sale_unit_line[115 + 88] + sale_unit_line[115 + 90] + sale_unit_line[115 + 92] + sale_unit_line[115 + 94]

        unit_dict = {}
        unit_dict["one_rent"] = rent_unit_one_dict
        unit_dict["two_rent"] = rent_unit_two_dict
        unit_dict["all_rent"] = rent_unit_all_dict
        unit_dict["sales"] = sale_unit_dict
        return unit_dict

    # for i in range(50, 58):
    if i>=50 and i<58:
        rent_unit_one_line = rent_unit_one.row_values(i)
        index = 0
        for j in rent_unit_one_line:
            if j=="-":
                rent_unit_one_line[index] = rent_unit_one.row_values(49)[index]
            index += 1

        rent_unit_one_dict["rent_unit_one_mar05"] = rent_unit_one_line[121]
        rent_unit_one_dict["rent_unit_one_jun05"] = rent_unit_one_line[121 + 2]
        rent_unit_one_dict["rent_unit_one_sep05"] = rent_unit_one_line[121 + 4]
        rent_unit_one_dict["rent_unit_one_dec05"] = rent_unit_one_line[121 + 6]

        rent_unit_one_dict["rent_unit_one_mar06"] = rent_unit_one_line[121 + 8]
        rent_unit_one_dict["rent_unit_one_jun06"] = rent_unit_one_line[121 + 10]
        rent_unit_one_dict["rent_unit_one_sep06"] = rent_unit_one_line[121 + 12]
        rent_unit_one_dict["rent_unit_one_dec06"] = rent_unit_one_line[121 + 14]

        rent_unit_one_dict["rent_unit_one_mar07"] = rent_unit_one_line[121 + 16]
        rent_unit_one_dict["rent_unit_one_jun07"] = rent_unit_one_line[121 + 18]
        rent_unit_one_dict["rent_unit_one_sep07"] = rent_unit_one_line[121 + 20]
        rent_unit_one_dict["rent_unit_one_dec07"] = rent_unit_one_line[121 + 22]

        rent_unit_one_dict["rent_unit_one_mar08"] = rent_unit_one_line[121 + 24]
        rent_unit_one_dict["rent_unit_one_jun08"] = rent_unit_one_line[121 + 26]
        rent_unit_one_dict["rent_unit_one_sep08"] = rent_unit_one_line[121 + 28]
        rent_unit_one_dict["rent_unit_one_dec08"] = rent_unit_one_line[121 + 30]

        rent_unit_one_dict["rent_unit_one_mar09"] = rent_unit_one_line[121 + 32]
        rent_unit_one_dict["rent_unit_one_jun09"] = rent_unit_one_line[121 + 34]
        rent_unit_one_dict["rent_unit_one_sep09"] = rent_unit_one_line[121 + 36]
        rent_unit_one_dict["rent_unit_one_dec09"] = rent_unit_one_line[121 + 38]

        rent_unit_one_dict["rent_unit_one_mar10"] = rent_unit_one_line[121 + 40]
        rent_unit_one_dict["rent_unit_one_jun10"] = rent_unit_one_line[121 + 42]
        rent_unit_one_dict["rent_unit_one_sep10"] = rent_unit_one_line[121 + 44]
        rent_unit_one_dict["rent_unit_one_dec10"] = rent_unit_one_line[121 + 46]

        rent_unit_one_dict["rent_unit_one_mar11"] = rent_unit_one_line[121 + 48]
        rent_unit_one_dict["rent_unit_one_jun11"] = rent_unit_one_line[121 + 50]
        rent_unit_one_dict["rent_unit_one_sep11"] = rent_unit_one_line[121 + 52]
        rent_unit_one_dict["rent_unit_one_dec11"] = rent_unit_one_line[121 + 54]

        rent_unit_one_dict["rent_unit_one_mar12"] = rent_unit_one_line[121 + 56]
        rent_unit_one_dict["rent_unit_one_jun12"] = rent_unit_one_line[121 + 58]
        rent_unit_one_dict["rent_unit_one_sep12"] = rent_unit_one_line[121 + 60]
        rent_unit_one_dict["rent_unit_one_dec12"] = rent_unit_one_line[121 + 62]

        rent_unit_one_dict["rent_unit_one_mar13"] = rent_unit_one_line[121 + 64]
        rent_unit_one_dict["rent_unit_one_jun13"] = rent_unit_one_line[121 + 66]
        rent_unit_one_dict["rent_unit_one_sep13"] = rent_unit_one_line[121 + 68]
        rent_unit_one_dict["rent_unit_one_dec13"] = rent_unit_one_line[121 + 70]

        rent_unit_one_dict["rent_unit_one_mar14"] = rent_unit_one_line[121 + 72]
        rent_unit_one_dict["rent_unit_one_jun14"] = rent_unit_one_line[121 + 74]
        rent_unit_one_dict["rent_unit_one_sep14"] = rent_unit_one_line[121 + 76]
        rent_unit_one_dict["rent_unit_one_dec14"] = rent_unit_one_line[121 + 78]

        rent_unit_one_dict["rent_unit_one_mar15"] = rent_unit_one_line[121 + 80]
        rent_unit_one_dict["rent_unit_one_jun15"] = rent_unit_one_line[121 + 82]
        rent_unit_one_dict["rent_unit_one_sep15"] = rent_unit_one_line[121 + 84]
        rent_unit_one_dict["rent_unit_one_dec15"] = rent_unit_one_line[121 + 86]

        rent_unit_one_dict["rent_unit_one_mar16"] = rent_unit_one_line[121 + 88]
        rent_unit_one_dict["rent_unit_one_jun16"] = rent_unit_one_line[121 + 91]
        rent_unit_one_dict["rent_unit_one_sep16"] = rent_unit_one_line[121 + 93]
        rent_unit_one_dict["rent_unit_one_dec16"] = rent_unit_one_line[121 + 95]

        rent_unit_two_line = rent_unit_two.row_values(i)
        index = 0
        for j in rent_unit_two_line:
            if j=="-":
                rent_unit_two_line[index] = rent_unit_two.row_values(49)[index]
            index += 1

        rent_unit_two_dict["rent_unit_two_mar05"] = rent_unit_two_line[121]
        rent_unit_two_dict["rent_unit_two_jun05"] = rent_unit_two_line[121 + 2]
        rent_unit_two_dict["rent_unit_two_sep05"] = rent_unit_two_line[121 + 4]
        rent_unit_two_dict["rent_unit_two_dec05"] = rent_unit_two_line[121 + 6]

        rent_unit_two_dict["rent_unit_two_mar06"] = rent_unit_two_line[121 + 8]
        rent_unit_two_dict["rent_unit_two_jun06"] = rent_unit_two_line[121 + 10]
        rent_unit_two_dict["rent_unit_two_sep06"] = rent_unit_two_line[121 + 12]
        rent_unit_two_dict["rent_unit_two_dec06"] = rent_unit_two_line[121 + 14]

        rent_unit_two_dict["rent_unit_two_mar07"] = rent_unit_two_line[121 + 16]
        rent_unit_two_dict["rent_unit_two_jun07"] = rent_unit_two_line[121 + 18]
        rent_unit_two_dict["rent_unit_two_sep07"] = rent_unit_two_line[121 + 20]
        rent_unit_two_dict["rent_unit_two_dec07"] = rent_unit_two_line[121 + 22]

        rent_unit_two_dict["rent_unit_two_mar08"] = rent_unit_two_line[121 + 24]
        rent_unit_two_dict["rent_unit_two_jun08"] = rent_unit_two_line[121 + 26]
        rent_unit_two_dict["rent_unit_two_sep08"] = rent_unit_two_line[121 + 28]
        rent_unit_two_dict["rent_unit_two_dec08"] = rent_unit_two_line[121 + 30]

        rent_unit_two_dict["rent_unit_two_mar09"] = rent_unit_two_line[121 + 32]
        rent_unit_two_dict["rent_unit_two_jun09"] = rent_unit_two_line[121 + 34]
        rent_unit_two_dict["rent_unit_two_sep09"] = rent_unit_two_line[121 + 36]
        rent_unit_two_dict["rent_unit_two_dec09"] = rent_unit_two_line[121 + 38]

        rent_unit_two_dict["rent_unit_two_mar10"] = rent_unit_two_line[121 + 40]
        rent_unit_two_dict["rent_unit_two_jun10"] = rent_unit_two_line[121 + 42]
        rent_unit_two_dict["rent_unit_two_sep10"] = rent_unit_two_line[121 + 44]
        rent_unit_two_dict["rent_unit_two_dec10"] = rent_unit_two_line[121 + 46]

        rent_unit_two_dict["rent_unit_two_mar11"] = rent_unit_two_line[121 + 48]
        rent_unit_two_dict["rent_unit_two_jun11"] = rent_unit_two_line[121 + 50]
        rent_unit_two_dict["rent_unit_two_sep11"] = rent_unit_two_line[121 + 52]
        rent_unit_two_dict["rent_unit_two_dec11"] = rent_unit_two_line[121 + 54]

        rent_unit_two_dict["rent_unit_two_mar12"] = rent_unit_two_line[121 + 56]
        rent_unit_two_dict["rent_unit_two_jun12"] = rent_unit_two_line[121 + 58]
        rent_unit_two_dict["rent_unit_two_sep12"] = rent_unit_two_line[121 + 60]
        rent_unit_two_dict["rent_unit_two_dec12"] = rent_unit_two_line[121 + 62]

        rent_unit_two_dict["rent_unit_two_mar13"] = rent_unit_two_line[121 + 64]
        rent_unit_two_dict["rent_unit_two_jun13"] = rent_unit_two_line[121 + 66]
        rent_unit_two_dict["rent_unit_two_sep13"] = rent_unit_two_line[121 + 68]
        rent_unit_two_dict["rent_unit_two_dec13"] = rent_unit_two_line[121 + 70]

        rent_unit_two_dict["rent_unit_two_mar14"] = rent_unit_two_line[121 + 72]
        rent_unit_two_dict["rent_unit_two_jun14"] = rent_unit_two_line[121 + 74]
        rent_unit_two_dict["rent_unit_two_sep14"] = rent_unit_two_line[121 + 76]
        rent_unit_two_dict["rent_unit_two_dec14"] = rent_unit_two_line[121 + 78]

        rent_unit_two_dict["rent_unit_two_mar15"] = rent_unit_two_line[121 + 80]
        rent_unit_two_dict["rent_unit_two_jun15"] = rent_unit_two_line[121 + 82]
        rent_unit_two_dict["rent_unit_two_sep15"] = rent_unit_two_line[121 + 84]
        rent_unit_two_dict["rent_unit_two_dec15"] = rent_unit_two_line[121 + 86]

        rent_unit_two_dict["rent_unit_two_mar16"] = rent_unit_two_line[121 + 88]
        rent_unit_two_dict["rent_unit_two_jun16"] = rent_unit_two_line[121 + 91]
        rent_unit_two_dict["rent_unit_two_sep16"] = rent_unit_two_line[121 + 93]
        rent_unit_two_dict["rent_unit_two_dec16"] = rent_unit_two_line[121 + 95]

        rent_unit_all_line = rent_unit_all.row_values(i)
        index = 0
        for j in rent_unit_all_line:
            if j=="-":
                rent_unit_all_line[index] = rent_unit_all.row_values(49)[index]
            index += 1

        rent_unit_all_dict["rent_unit_all_mar05"] = rent_unit_all_line[121]
        rent_unit_all_dict["rent_unit_all_jun05"] = rent_unit_all_line[121 + 2]
        rent_unit_all_dict["rent_unit_all_sep05"] = rent_unit_all_line[121 + 4]
        rent_unit_all_dict["rent_unit_all_dec05"] = rent_unit_all_line[121 + 6]

        rent_unit_all_dict["rent_unit_all_mar06"] = rent_unit_all_line[121 + 8]
        rent_unit_all_dict["rent_unit_all_jun06"] = rent_unit_all_line[121 + 10]
        rent_unit_all_dict["rent_unit_all_sep06"] = rent_unit_all_line[121 + 12]
        rent_unit_all_dict["rent_unit_all_dec06"] = rent_unit_all_line[121 + 14]

        rent_unit_all_dict["rent_unit_all_mar07"] = rent_unit_all_line[121 + 16]
        rent_unit_all_dict["rent_unit_all_jun07"] = rent_unit_all_line[121 + 18]
        rent_unit_all_dict["rent_unit_all_sep07"] = rent_unit_all_line[121 + 20]
        rent_unit_all_dict["rent_unit_all_dec07"] = rent_unit_all_line[121 + 22]

        rent_unit_all_dict["rent_unit_all_mar08"] = rent_unit_all_line[121 + 24]
        rent_unit_all_dict["rent_unit_all_jun08"] = rent_unit_all_line[121 + 26]
        rent_unit_all_dict["rent_unit_all_sep08"] = rent_unit_all_line[121 + 28]
        rent_unit_all_dict["rent_unit_all_dec08"] = rent_unit_all_line[121 + 30]

        rent_unit_all_dict["rent_unit_all_mar09"] = rent_unit_all_line[121 + 32]
        rent_unit_all_dict["rent_unit_all_jun09"] = rent_unit_all_line[121 + 34]
        rent_unit_all_dict["rent_unit_all_sep09"] = rent_unit_all_line[121 + 36]
        rent_unit_all_dict["rent_unit_all_dec09"] = rent_unit_all_line[121 + 38]

        rent_unit_all_dict["rent_unit_all_mar10"] = rent_unit_all_line[121 + 40]
        rent_unit_all_dict["rent_unit_all_jun10"] = rent_unit_all_line[121 + 42]
        rent_unit_all_dict["rent_unit_all_sep10"] = rent_unit_all_line[121 + 44]
        rent_unit_all_dict["rent_unit_all_dec10"] = rent_unit_all_line[121 + 46]

        rent_unit_all_dict["rent_unit_all_mar11"] = rent_unit_all_line[121 + 48]
        rent_unit_all_dict["rent_unit_all_jun11"] = rent_unit_all_line[121 + 50]
        rent_unit_all_dict["rent_unit_all_sep11"] = rent_unit_all_line[121 + 52]
        rent_unit_all_dict["rent_unit_all_dec11"] = rent_unit_all_line[121 + 54]

        rent_unit_all_dict["rent_unit_all_mar12"] = rent_unit_all_line[121 + 56]
        rent_unit_all_dict["rent_unit_all_jun12"] = rent_unit_all_line[121 + 58]
        rent_unit_all_dict["rent_unit_all_sep12"] = rent_unit_all_line[121 + 60]
        rent_unit_all_dict["rent_unit_all_dec12"] = rent_unit_all_line[121 + 62]

        rent_unit_all_dict["rent_unit_all_mar13"] = rent_unit_all_line[121 + 64]
        rent_unit_all_dict["rent_unit_all_jun13"] = rent_unit_all_line[121 + 66]
        rent_unit_all_dict["rent_unit_all_sep13"] = rent_unit_all_line[121 + 68]
        rent_unit_all_dict["rent_unit_all_dec13"] = rent_unit_all_line[121 + 70]

        rent_unit_all_dict["rent_unit_all_mar14"] = rent_unit_all_line[121 + 72]
        rent_unit_all_dict["rent_unit_all_jun14"] = rent_unit_all_line[121 + 74]
        rent_unit_all_dict["rent_unit_all_sep14"] = rent_unit_all_line[121 + 76]
        rent_unit_all_dict["rent_unit_all_dec14"] = rent_unit_all_line[121 + 78]

        rent_unit_all_dict["rent_unit_all_mar15"] = rent_unit_all_line[121 + 80]
        rent_unit_all_dict["rent_unit_all_jun15"] = rent_unit_all_line[121 + 82]
        rent_unit_all_dict["rent_unit_all_sep15"] = rent_unit_all_line[121 + 84]
        rent_unit_all_dict["rent_unit_all_dec15"] = rent_unit_all_line[121 + 86]

        rent_unit_all_dict["rent_unit_all_mar16"] = rent_unit_all_line[121 + 88]
        rent_unit_all_dict["rent_unit_all_jun16"] = rent_unit_all_line[121 + 91]
        rent_unit_all_dict["rent_unit_all_sep16"] = rent_unit_all_line[121 + 93]
        rent_unit_all_dict["rent_unit_all_dec16"] = rent_unit_all_line[121 + 95]

        sale_unit_line = sale_unit.row_values(i + 2)
        index = 0
        for j in sale_unit_line:
            if j=="-":
                sale_unit_line[index] = sale_unit.row_values(51)[index]
            index += 1
        sale_unit_dict['sale_unit_05'] = sale_unit_line[115 + 0] + sale_unit_line[115 + 2] + sale_unit_line[115 + 4] + sale_unit_line[115 + 6]
        sale_unit_dict['sale_unit_06'] = sale_unit_line[115 + 8] + sale_unit_line[115 + 10] + sale_unit_line[115 + 12] + sale_unit_line[115 + 14]
        sale_unit_dict['sale_unit_07'] = sale_unit_line[115 + 16] + sale_unit_line[115 + 18] + sale_unit_line[115 + 20] + sale_unit_line[115 + 22]
        sale_unit_dict['sale_unit_08'] = sale_unit_line[115 + 24] + sale_unit_line[115 + 26] + sale_unit_line[115 + 28] + sale_unit_line[115 + 30]
        sale_unit_dict['sale_unit_09'] = sale_unit_line[115 + 32] + sale_unit_line[115 + 34] + sale_unit_line[115 + 36] + sale_unit_line[115 + 38]
        sale_unit_dict['sale_unit_10'] = sale_unit_line[115 + 40] + sale_unit_line[115 + 42] + sale_unit_line[115 + 44] + sale_unit_line[115 + 46]
        sale_unit_dict['sale_unit_11'] = sale_unit_line[115 + 48] + sale_unit_line[115 + 50] + sale_unit_line[115 + 52] + sale_unit_line[115 + 54]
        sale_unit_dict['sale_unit_12'] = sale_unit_line[115 + 56] + sale_unit_line[115 + 58] + sale_unit_line[115 + 60] + sale_unit_line[115 + 62]
        sale_unit_dict['sale_unit_13'] = sale_unit_line[115 + 64] + sale_unit_line[115 + 66] + sale_unit_line[115 + 68] + sale_unit_line[115 + 70]
        sale_unit_dict['sale_unit_14'] = sale_unit_line[115 + 72] + sale_unit_line[115 + 74] + sale_unit_line[115 + 76] + sale_unit_line[115 + 78]
        sale_unit_dict['sale_unit_15'] = sale_unit_line[115 + 80] + sale_unit_line[115 + 82] + sale_unit_line[115 + 84] + sale_unit_line[115 + 86]
        sale_unit_dict['sale_unit_16'] = sale_unit_line[115 + 88] + sale_unit_line[115 + 90] + sale_unit_line[115 + 92] + sale_unit_line[115 + 94]

        unit_dict = {}
        unit_dict["one_rent"] = rent_unit_one_dict
        unit_dict["two_rent"] = rent_unit_two_dict
        unit_dict["all_rent"] = rent_unit_all_dict
        unit_dict["sales"] = sale_unit_dict
        return unit_dict