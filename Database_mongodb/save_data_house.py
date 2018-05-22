import xlrd

def save_data_house(i):
    rentname = "rent_data.xls"
    salename = "sales_data.xls"
    data_sales = xlrd.open_workbook(salename)

    sale_house = data_sales.sheets()[2]

    data_rent = xlrd.open_workbook(rentname)

    rent_house_all = data_rent.sheets()[6]
    rent_house_two = data_rent.sheets()[7]
    rent_house_three = data_rent.sheets()[8]


    rent_house_two_dict = {}
    rent_house_three_dict = {}
    rent_house_all_dict = {}
    sale_house_dict = {}

    if i >= 4 and i < 15:
        rent_house_two_line = rent_house_two.row_values(i)
        index = 0
        for j in rent_house_two_line:
            if j=="-":
                rent_house_two_line[index] = rent_house_two.row_values(3)[index]
            index += 1

        rent_house_two_dict["rent_house_two_mar05"] = rent_house_two_line[121]
        rent_house_two_dict["rent_house_two_jun05"] = rent_house_two_line[121 + 2]
        rent_house_two_dict["rent_house_two_sep05"] = rent_house_two_line[121 + 4]
        rent_house_two_dict["rent_house_two_dec05"] = rent_house_two_line[121 + 6]

        rent_house_two_dict["rent_house_two_mar06"] = rent_house_two_line[121 + 8]
        rent_house_two_dict["rent_house_two_jun06"] = rent_house_two_line[121 + 10]
        rent_house_two_dict["rent_house_two_sep06"] = rent_house_two_line[121 + 12]
        rent_house_two_dict["rent_house_two_dec06"] = rent_house_two_line[121 + 14]

        rent_house_two_dict["rent_house_two_mar07"] = rent_house_two_line[121 + 16]
        rent_house_two_dict["rent_house_two_jun07"] = rent_house_two_line[121 + 18]
        rent_house_two_dict["rent_house_two_sep07"] = rent_house_two_line[121 + 20]
        rent_house_two_dict["rent_house_two_dec07"] = rent_house_two_line[121 + 22]

        rent_house_two_dict["rent_house_two_mar08"] = rent_house_two_line[121 + 24]
        rent_house_two_dict["rent_house_two_jun08"] = rent_house_two_line[121 + 26]
        rent_house_two_dict["rent_house_two_sep08"] = rent_house_two_line[121 + 28]
        rent_house_two_dict["rent_house_two_dec08"] = rent_house_two_line[121 + 30]

        rent_house_two_dict["rent_house_two_mar09"] = rent_house_two_line[121 + 32]
        rent_house_two_dict["rent_house_two_jun09"] = rent_house_two_line[121 + 34]
        rent_house_two_dict["rent_house_two_sep09"] = rent_house_two_line[121 + 36]
        rent_house_two_dict["rent_house_two_dec09"] = rent_house_two_line[121 + 38]

        rent_house_two_dict["rent_house_two_mar10"] = rent_house_two_line[121 + 40]
        rent_house_two_dict["rent_house_two_jun10"] = rent_house_two_line[121 + 42]
        rent_house_two_dict["rent_house_two_sep10"] = rent_house_two_line[121 + 44]
        rent_house_two_dict["rent_house_two_dec10"] = rent_house_two_line[121 + 46]

        rent_house_two_dict["rent_house_two_mar11"] = rent_house_two_line[121 + 48]
        rent_house_two_dict["rent_house_two_jun11"] = rent_house_two_line[121 + 50]
        rent_house_two_dict["rent_house_two_sep11"] = rent_house_two_line[121 + 52]
        rent_house_two_dict["rent_house_two_dec11"] = rent_house_two_line[121 + 54]

        rent_house_two_dict["rent_house_two_mar12"] = rent_house_two_line[121 + 56]
        rent_house_two_dict["rent_house_two_jun12"] = rent_house_two_line[121 + 58]
        rent_house_two_dict["rent_house_two_sep12"] = rent_house_two_line[121 + 60]
        rent_house_two_dict["rent_house_two_dec12"] = rent_house_two_line[121 + 62]

        rent_house_two_dict["rent_house_two_mar13"] = rent_house_two_line[121 + 64]
        rent_house_two_dict["rent_house_two_jun13"] = rent_house_two_line[121 + 66]
        rent_house_two_dict["rent_house_two_sep13"] = rent_house_two_line[121 + 68]
        rent_house_two_dict["rent_house_two_dec13"] = rent_house_two_line[121 + 70]

        rent_house_two_dict["rent_house_two_mar14"] = rent_house_two_line[121 + 72]
        rent_house_two_dict["rent_house_two_jun14"] = rent_house_two_line[121 + 74]
        rent_house_two_dict["rent_house_two_sep14"] = rent_house_two_line[121 + 76]
        rent_house_two_dict["rent_house_two_dec14"] = rent_house_two_line[121 + 78]

        rent_house_two_dict["rent_house_two_mar15"] = rent_house_two_line[121 + 80]
        rent_house_two_dict["rent_house_two_jun15"] = rent_house_two_line[121 + 82]
        rent_house_two_dict["rent_house_two_sep15"] = rent_house_two_line[121 + 84]
        rent_house_two_dict["rent_house_two_dec15"] = rent_house_two_line[121 + 86]

        rent_house_two_dict["rent_house_two_mar16"] = rent_house_two_line[121 + 88]
        rent_house_two_dict["rent_house_two_jun16"] = rent_house_two_line[121 + 91]
        rent_house_two_dict["rent_house_two_sep16"] = rent_house_two_line[121 + 93]
        rent_house_two_dict["rent_house_two_dec16"] = rent_house_two_line[121 + 95]

        rent_house_three_line = rent_house_three.row_values(i)
        index = 0
        for j in rent_house_three_line:
            if j=="-":
                rent_house_three_line[index] = rent_house_three.row_values(3)[index]
            index += 1

        rent_house_three_dict["rent_house_three_mar05"] = rent_house_three_line[121]
        rent_house_three_dict["rent_house_three_jun05"] = rent_house_three_line[121 + 2]
        rent_house_three_dict["rent_house_three_sep05"] = rent_house_three_line[121 + 4]
        rent_house_three_dict["rent_house_three_dec05"] = rent_house_three_line[121 + 6]

        rent_house_three_dict["rent_house_three_mar06"] = rent_house_three_line[121 + 8]
        rent_house_three_dict["rent_house_three_jun06"] = rent_house_three_line[121 + 10]
        rent_house_three_dict["rent_house_three_sep06"] = rent_house_three_line[121 + 12]
        rent_house_three_dict["rent_house_three_dec06"] = rent_house_three_line[121 + 14]

        rent_house_three_dict["rent_house_three_mar07"] = rent_house_three_line[121 + 16]
        rent_house_three_dict["rent_house_three_jun07"] = rent_house_three_line[121 + 18]
        rent_house_three_dict["rent_house_three_sep07"] = rent_house_three_line[121 + 20]
        rent_house_three_dict["rent_house_three_dec07"] = rent_house_three_line[121 + 22]

        rent_house_three_dict["rent_house_three_mar08"] = rent_house_three_line[121 + 24]
        rent_house_three_dict["rent_house_three_jun08"] = rent_house_three_line[121 + 26]
        rent_house_three_dict["rent_house_three_sep08"] = rent_house_three_line[121 + 28]
        rent_house_three_dict["rent_house_three_dec08"] = rent_house_three_line[121 + 30]

        rent_house_three_dict["rent_house_three_mar09"] = rent_house_three_line[121 + 32]
        rent_house_three_dict["rent_house_three_jun09"] = rent_house_three_line[121 + 34]
        rent_house_three_dict["rent_house_three_sep09"] = rent_house_three_line[121 + 36]
        rent_house_three_dict["rent_house_three_dec09"] = rent_house_three_line[121 + 38]

        rent_house_three_dict["rent_house_three_mar10"] = rent_house_three_line[121 + 40]
        rent_house_three_dict["rent_house_three_jun10"] = rent_house_three_line[121 + 42]
        rent_house_three_dict["rent_house_three_sep10"] = rent_house_three_line[121 + 44]
        rent_house_three_dict["rent_house_three_dec10"] = rent_house_three_line[121 + 46]

        rent_house_three_dict["rent_house_three_mar11"] = rent_house_three_line[121 + 48]
        rent_house_three_dict["rent_house_three_jun11"] = rent_house_three_line[121 + 50]
        rent_house_three_dict["rent_house_three_sep11"] = rent_house_three_line[121 + 52]
        rent_house_three_dict["rent_house_three_dec11"] = rent_house_three_line[121 + 54]

        rent_house_three_dict["rent_house_three_mar12"] = rent_house_three_line[121 + 56]
        rent_house_three_dict["rent_house_three_jun12"] = rent_house_three_line[121 + 58]
        rent_house_three_dict["rent_house_three_sep12"] = rent_house_three_line[121 + 60]
        rent_house_three_dict["rent_house_three_dec12"] = rent_house_three_line[121 + 62]

        rent_house_three_dict["rent_house_three_mar13"] = rent_house_three_line[121 + 64]
        rent_house_three_dict["rent_house_three_jun13"] = rent_house_three_line[121 + 66]
        rent_house_three_dict["rent_house_three_sep13"] = rent_house_three_line[121 + 68]
        rent_house_three_dict["rent_house_three_dec13"] = rent_house_three_line[121 + 70]

        rent_house_three_dict["rent_house_three_mar14"] = rent_house_three_line[121 + 72]
        rent_house_three_dict["rent_house_three_jun14"] = rent_house_three_line[121 + 74]
        rent_house_three_dict["rent_house_three_sep14"] = rent_house_three_line[121 + 76]
        rent_house_three_dict["rent_house_three_dec14"] = rent_house_three_line[121 + 78]

        rent_house_three_dict["rent_house_three_mar15"] = rent_house_three_line[121 + 80]
        rent_house_three_dict["rent_house_three_jun15"] = rent_house_three_line[121 + 82]
        rent_house_three_dict["rent_house_three_sep15"] = rent_house_three_line[121 + 84]
        rent_house_three_dict["rent_house_three_dec15"] = rent_house_three_line[121 + 86]

        rent_house_three_dict["rent_house_three_mar16"] = rent_house_three_line[121 + 88]
        rent_house_three_dict["rent_house_three_jun16"] = rent_house_three_line[121 + 91]
        rent_house_three_dict["rent_house_three_sep16"] = rent_house_three_line[121 + 93]
        rent_house_three_dict["rent_house_three_dec16"] = rent_house_three_line[121 + 95]

        rent_house_all_line = rent_house_all.row_values(i)
        index = 0
        for j in rent_house_all_line:
            if j=="-":
                rent_house_all_line[index] = rent_house_all.row_values(3)[index]
            index += 1

        rent_house_all_dict["rent_house_all_mar05"] = rent_house_all_line[121]
        rent_house_all_dict["rent_house_all_jun05"] = rent_house_all_line[121 + 2]
        rent_house_all_dict["rent_house_all_sep05"] = rent_house_all_line[121 + 4]
        rent_house_all_dict["rent_house_all_dec05"] = rent_house_all_line[121 + 6]

        rent_house_all_dict["rent_house_all_mar06"] = rent_house_all_line[121 + 8]
        rent_house_all_dict["rent_house_all_jun06"] = rent_house_all_line[121 + 10]
        rent_house_all_dict["rent_house_all_sep06"] = rent_house_all_line[121 + 12]
        rent_house_all_dict["rent_house_all_dec06"] = rent_house_all_line[121 + 14]

        rent_house_all_dict["rent_house_all_mar07"] = rent_house_all_line[121 + 16]
        rent_house_all_dict["rent_house_all_jun07"] = rent_house_all_line[121 + 18]
        rent_house_all_dict["rent_house_all_sep07"] = rent_house_all_line[121 + 20]
        rent_house_all_dict["rent_house_all_dec07"] = rent_house_all_line[121 + 22]

        rent_house_all_dict["rent_house_all_mar08"] = rent_house_all_line[121 + 24]
        rent_house_all_dict["rent_house_all_jun08"] = rent_house_all_line[121 + 26]
        rent_house_all_dict["rent_house_all_sep08"] = rent_house_all_line[121 + 28]
        rent_house_all_dict["rent_house_all_dec08"] = rent_house_all_line[121 + 30]

        rent_house_all_dict["rent_house_all_mar09"] = rent_house_all_line[121 + 32]
        rent_house_all_dict["rent_house_all_jun09"] = rent_house_all_line[121 + 34]
        rent_house_all_dict["rent_house_all_sep09"] = rent_house_all_line[121 + 36]
        rent_house_all_dict["rent_house_all_dec09"] = rent_house_all_line[121 + 38]

        rent_house_all_dict["rent_house_all_mar10"] = rent_house_all_line[121 + 40]
        rent_house_all_dict["rent_house_all_jun10"] = rent_house_all_line[121 + 42]
        rent_house_all_dict["rent_house_all_sep10"] = rent_house_all_line[121 + 44]
        rent_house_all_dict["rent_house_all_dec10"] = rent_house_all_line[121 + 46]

        rent_house_all_dict["rent_house_all_mar11"] = rent_house_all_line[121 + 48]
        rent_house_all_dict["rent_house_all_jun11"] = rent_house_all_line[121 + 50]
        rent_house_all_dict["rent_house_all_sep11"] = rent_house_all_line[121 + 52]
        rent_house_all_dict["rent_house_all_dec11"] = rent_house_all_line[121 + 54]

        rent_house_all_dict["rent_house_all_mar12"] = rent_house_all_line[121 + 56]
        rent_house_all_dict["rent_house_all_jun12"] = rent_house_all_line[121 + 58]
        rent_house_all_dict["rent_house_all_sep12"] = rent_house_all_line[121 + 60]
        rent_house_all_dict["rent_house_all_dec12"] = rent_house_all_line[121 + 62]

        rent_house_all_dict["rent_house_all_mar13"] = rent_house_all_line[121 + 64]
        rent_house_all_dict["rent_house_all_jun13"] = rent_house_all_line[121 + 66]
        rent_house_all_dict["rent_house_all_sep13"] = rent_house_all_line[121 + 68]
        rent_house_all_dict["rent_house_all_dec13"] = rent_house_all_line[121 + 70]

        rent_house_all_dict["rent_house_all_mar14"] = rent_house_all_line[121 + 72]
        rent_house_all_dict["rent_house_all_jun14"] = rent_house_all_line[121 + 74]
        rent_house_all_dict["rent_house_all_sep14"] = rent_house_all_line[121 + 76]
        rent_house_all_dict["rent_house_all_dec14"] = rent_house_all_line[121 + 78]

        rent_house_all_dict["rent_house_all_mar15"] = rent_house_all_line[121 + 80]
        rent_house_all_dict["rent_house_all_jun15"] = rent_house_all_line[121 + 82]
        rent_house_all_dict["rent_house_all_sep15"] = rent_house_all_line[121 + 84]
        rent_house_all_dict["rent_house_all_dec15"] = rent_house_all_line[121 + 86]

        rent_house_all_dict["rent_house_all_mar16"] = rent_house_all_line[121 + 88]
        rent_house_all_dict["rent_house_all_jun16"] = rent_house_all_line[121 + 91]
        rent_house_all_dict["rent_house_all_sep16"] = rent_house_all_line[121 + 93]
        rent_house_all_dict["rent_house_all_dec16"] = rent_house_all_line[121 + 95]

        sale_house_line = sale_house.row_values(i + 2)
        index = 0
        for j in sale_house_line:
            if j=="-":
                sale_house_line[index] = sale_house.row_values(5)[index]
            index += 1
        sale_house_dict['sale_house_05'] = sale_house_line[115 + 0] + sale_house_line[115 + 2] + sale_house_line[
            115 + 4] + sale_house_line[115 + 6]
        sale_house_dict['sale_house_06'] = sale_house_line[115 + 8] + sale_house_line[115 + 10] + sale_house_line[
            115 + 12] + sale_house_line[115 + 14]
        sale_house_dict['sale_house_07'] = sale_house_line[115 + 16] + sale_house_line[115 + 18] + sale_house_line[
            115 + 20] + sale_house_line[115 + 22]
        sale_house_dict['sale_house_08'] = sale_house_line[115 + 24] + sale_house_line[115 + 26] + sale_house_line[
            115 + 28] + sale_house_line[115 + 30]
        sale_house_dict['sale_house_09'] = sale_house_line[115 + 32] + sale_house_line[115 + 34] + sale_house_line[
            115 + 36] + sale_house_line[115 + 38]
        sale_house_dict['sale_house_10'] = sale_house_line[115 + 40] + sale_house_line[115 + 42] + sale_house_line[
            115 + 44] + sale_house_line[115 + 46]
        sale_house_dict['sale_house_11'] = sale_house_line[115 + 48] + sale_house_line[115 + 50] + sale_house_line[
            115 + 52] + sale_house_line[115 + 54]
        sale_house_dict['sale_house_12'] = sale_house_line[115 + 56] + sale_house_line[115 + 58] + sale_house_line[
            115 + 60] + sale_house_line[115 + 62]
        sale_house_dict['sale_house_13'] = sale_house_line[115 + 64] + sale_house_line[115 + 66] + sale_house_line[
            115 + 68] + sale_house_line[115 + 70]
        sale_house_dict['sale_house_14'] = sale_house_line[115 + 72] + sale_house_line[115 + 74] + sale_house_line[
            115 + 76] + sale_house_line[115 + 78]
        sale_house_dict['sale_house_15'] = sale_house_line[115 + 80] + sale_house_line[115 + 82] + sale_house_line[
            115 + 84] + sale_house_line[115 + 86]
        sale_house_dict['sale_house_16'] = sale_house_line[115 + 88] + sale_house_line[115 + 90] + sale_house_line[
            115 + 92] + sale_house_line[115 + 94]

    if i >= 16 and i < 31:
        rent_house_two_line = rent_house_two.row_values(i)
        index = 0
        for j in rent_house_two_line:
            if j=="-":
                rent_house_two_line[index] = rent_house_two.row_values(3)[index]
            index += 1

        rent_house_two_dict["rent_house_two_mar05"] = rent_house_two_line[121]
        rent_house_two_dict["rent_house_two_jun05"] = rent_house_two_line[121 + 2]
        rent_house_two_dict["rent_house_two_sep05"] = rent_house_two_line[121 + 4]
        rent_house_two_dict["rent_house_two_dec05"] = rent_house_two_line[121 + 6]

        rent_house_two_dict["rent_house_two_mar06"] = rent_house_two_line[121 + 8]
        rent_house_two_dict["rent_house_two_jun06"] = rent_house_two_line[121 + 10]
        rent_house_two_dict["rent_house_two_sep06"] = rent_house_two_line[121 + 12]
        rent_house_two_dict["rent_house_two_dec06"] = rent_house_two_line[121 + 14]

        rent_house_two_dict["rent_house_two_mar07"] = rent_house_two_line[121 + 16]
        rent_house_two_dict["rent_house_two_jun07"] = rent_house_two_line[121 + 18]
        rent_house_two_dict["rent_house_two_sep07"] = rent_house_two_line[121 + 20]
        rent_house_two_dict["rent_house_two_dec07"] = rent_house_two_line[121 + 22]

        rent_house_two_dict["rent_house_two_mar08"] = rent_house_two_line[121 + 24]
        rent_house_two_dict["rent_house_two_jun08"] = rent_house_two_line[121 + 26]
        rent_house_two_dict["rent_house_two_sep08"] = rent_house_two_line[121 + 28]
        rent_house_two_dict["rent_house_two_dec08"] = rent_house_two_line[121 + 30]

        rent_house_two_dict["rent_house_two_mar09"] = rent_house_two_line[121 + 32]
        rent_house_two_dict["rent_house_two_jun09"] = rent_house_two_line[121 + 34]
        rent_house_two_dict["rent_house_two_sep09"] = rent_house_two_line[121 + 36]
        rent_house_two_dict["rent_house_two_dec09"] = rent_house_two_line[121 + 38]

        rent_house_two_dict["rent_house_two_mar10"] = rent_house_two_line[121 + 40]
        rent_house_two_dict["rent_house_two_jun10"] = rent_house_two_line[121 + 42]
        rent_house_two_dict["rent_house_two_sep10"] = rent_house_two_line[121 + 44]
        rent_house_two_dict["rent_house_two_dec10"] = rent_house_two_line[121 + 46]

        rent_house_two_dict["rent_house_two_mar11"] = rent_house_two_line[121 + 48]
        rent_house_two_dict["rent_house_two_jun11"] = rent_house_two_line[121 + 50]
        rent_house_two_dict["rent_house_two_sep11"] = rent_house_two_line[121 + 52]
        rent_house_two_dict["rent_house_two_dec11"] = rent_house_two_line[121 + 54]

        rent_house_two_dict["rent_house_two_mar12"] = rent_house_two_line[121 + 56]
        rent_house_two_dict["rent_house_two_jun12"] = rent_house_two_line[121 + 58]
        rent_house_two_dict["rent_house_two_sep12"] = rent_house_two_line[121 + 60]
        rent_house_two_dict["rent_house_two_dec12"] = rent_house_two_line[121 + 62]

        rent_house_two_dict["rent_house_two_mar13"] = rent_house_two_line[121 + 64]
        rent_house_two_dict["rent_house_two_jun13"] = rent_house_two_line[121 + 66]
        rent_house_two_dict["rent_house_two_sep13"] = rent_house_two_line[121 + 68]
        rent_house_two_dict["rent_house_two_dec13"] = rent_house_two_line[121 + 70]

        rent_house_two_dict["rent_house_two_mar14"] = rent_house_two_line[121 + 72]
        rent_house_two_dict["rent_house_two_jun14"] = rent_house_two_line[121 + 74]
        rent_house_two_dict["rent_house_two_sep14"] = rent_house_two_line[121 + 76]
        rent_house_two_dict["rent_house_two_dec14"] = rent_house_two_line[121 + 78]

        rent_house_two_dict["rent_house_two_mar15"] = rent_house_two_line[121 + 80]
        rent_house_two_dict["rent_house_two_jun15"] = rent_house_two_line[121 + 82]
        rent_house_two_dict["rent_house_two_sep15"] = rent_house_two_line[121 + 84]
        rent_house_two_dict["rent_house_two_dec15"] = rent_house_two_line[121 + 86]

        rent_house_two_dict["rent_house_two_mar16"] = rent_house_two_line[121 + 88]
        rent_house_two_dict["rent_house_two_jun16"] = rent_house_two_line[121 + 91]
        rent_house_two_dict["rent_house_two_sep16"] = rent_house_two_line[121 + 93]
        rent_house_two_dict["rent_house_two_dec16"] = rent_house_two_line[121 + 95]

        rent_house_three_line = rent_house_three.row_values(i)
        index = 0
        for j in rent_house_three_line:
            if j=="-":
                rent_house_three_line[index] = rent_house_three.row_values(3)[index]
            index += 1

        rent_house_three_dict["rent_house_three_mar05"] = rent_house_three_line[121]
        rent_house_three_dict["rent_house_three_jun05"] = rent_house_three_line[121 + 2]
        rent_house_three_dict["rent_house_three_sep05"] = rent_house_three_line[121 + 4]
        rent_house_three_dict["rent_house_three_dec05"] = rent_house_three_line[121 + 6]

        rent_house_three_dict["rent_house_three_mar06"] = rent_house_three_line[121 + 8]
        rent_house_three_dict["rent_house_three_jun06"] = rent_house_three_line[121 + 10]
        rent_house_three_dict["rent_house_three_sep06"] = rent_house_three_line[121 + 12]
        rent_house_three_dict["rent_house_three_dec06"] = rent_house_three_line[121 + 14]

        rent_house_three_dict["rent_house_three_mar07"] = rent_house_three_line[121 + 16]
        rent_house_three_dict["rent_house_three_jun07"] = rent_house_three_line[121 + 18]
        rent_house_three_dict["rent_house_three_sep07"] = rent_house_three_line[121 + 20]
        rent_house_three_dict["rent_house_three_dec07"] = rent_house_three_line[121 + 22]

        rent_house_three_dict["rent_house_three_mar08"] = rent_house_three_line[121 + 24]
        rent_house_three_dict["rent_house_three_jun08"] = rent_house_three_line[121 + 26]
        rent_house_three_dict["rent_house_three_sep08"] = rent_house_three_line[121 + 28]
        rent_house_three_dict["rent_house_three_dec08"] = rent_house_three_line[121 + 30]

        rent_house_three_dict["rent_house_three_mar09"] = rent_house_three_line[121 + 32]
        rent_house_three_dict["rent_house_three_jun09"] = rent_house_three_line[121 + 34]
        rent_house_three_dict["rent_house_three_sep09"] = rent_house_three_line[121 + 36]
        rent_house_three_dict["rent_house_three_dec09"] = rent_house_three_line[121 + 38]

        rent_house_three_dict["rent_house_three_mar10"] = rent_house_three_line[121 + 40]
        rent_house_three_dict["rent_house_three_jun10"] = rent_house_three_line[121 + 42]
        rent_house_three_dict["rent_house_three_sep10"] = rent_house_three_line[121 + 44]
        rent_house_three_dict["rent_house_three_dec10"] = rent_house_three_line[121 + 46]

        rent_house_three_dict["rent_house_three_mar11"] = rent_house_three_line[121 + 48]
        rent_house_three_dict["rent_house_three_jun11"] = rent_house_three_line[121 + 50]
        rent_house_three_dict["rent_house_three_sep11"] = rent_house_three_line[121 + 52]
        rent_house_three_dict["rent_house_three_dec11"] = rent_house_three_line[121 + 54]

        rent_house_three_dict["rent_house_three_mar12"] = rent_house_three_line[121 + 56]
        rent_house_three_dict["rent_house_three_jun12"] = rent_house_three_line[121 + 58]
        rent_house_three_dict["rent_house_three_sep12"] = rent_house_three_line[121 + 60]
        rent_house_three_dict["rent_house_three_dec12"] = rent_house_three_line[121 + 62]

        rent_house_three_dict["rent_house_three_mar13"] = rent_house_three_line[121 + 64]
        rent_house_three_dict["rent_house_three_jun13"] = rent_house_three_line[121 + 66]
        rent_house_three_dict["rent_house_three_sep13"] = rent_house_three_line[121 + 68]
        rent_house_three_dict["rent_house_three_dec13"] = rent_house_three_line[121 + 70]

        rent_house_three_dict["rent_house_three_mar14"] = rent_house_three_line[121 + 72]
        rent_house_three_dict["rent_house_three_jun14"] = rent_house_three_line[121 + 74]
        rent_house_three_dict["rent_house_three_sep14"] = rent_house_three_line[121 + 76]
        rent_house_three_dict["rent_house_three_dec14"] = rent_house_three_line[121 + 78]

        rent_house_three_dict["rent_house_three_mar15"] = rent_house_three_line[121 + 80]
        rent_house_three_dict["rent_house_three_jun15"] = rent_house_three_line[121 + 82]
        rent_house_three_dict["rent_house_three_sep15"] = rent_house_three_line[121 + 84]
        rent_house_three_dict["rent_house_three_dec15"] = rent_house_three_line[121 + 86]

        rent_house_three_dict["rent_house_three_mar16"] = rent_house_three_line[121 + 88]
        rent_house_three_dict["rent_house_three_jun16"] = rent_house_three_line[121 + 91]
        rent_house_three_dict["rent_house_three_sep16"] = rent_house_three_line[121 + 93]
        rent_house_three_dict["rent_house_three_dec16"] = rent_house_three_line[121 + 95]

        rent_house_all_line = rent_house_all.row_values(i)
        index = 0
        for j in rent_house_all_line:
            if j=="-":
                rent_house_all_line[index] = rent_house_all.row_values(3)[index]
            index += 1

        rent_house_all_dict["rent_house_all_mar05"] = rent_house_all_line[121]
        rent_house_all_dict["rent_house_all_jun05"] = rent_house_all_line[121 + 2]
        rent_house_all_dict["rent_house_all_sep05"] = rent_house_all_line[121 + 4]
        rent_house_all_dict["rent_house_all_dec05"] = rent_house_all_line[121 + 6]

        rent_house_all_dict["rent_house_all_mar06"] = rent_house_all_line[121 + 8]
        rent_house_all_dict["rent_house_all_jun06"] = rent_house_all_line[121 + 10]
        rent_house_all_dict["rent_house_all_sep06"] = rent_house_all_line[121 + 12]
        rent_house_all_dict["rent_house_all_dec06"] = rent_house_all_line[121 + 14]

        rent_house_all_dict["rent_house_all_mar07"] = rent_house_all_line[121 + 16]
        rent_house_all_dict["rent_house_all_jun07"] = rent_house_all_line[121 + 18]
        rent_house_all_dict["rent_house_all_sep07"] = rent_house_all_line[121 + 20]
        rent_house_all_dict["rent_house_all_dec07"] = rent_house_all_line[121 + 22]

        rent_house_all_dict["rent_house_all_mar08"] = rent_house_all_line[121 + 24]
        rent_house_all_dict["rent_house_all_jun08"] = rent_house_all_line[121 + 26]
        rent_house_all_dict["rent_house_all_sep08"] = rent_house_all_line[121 + 28]
        rent_house_all_dict["rent_house_all_dec08"] = rent_house_all_line[121 + 30]

        rent_house_all_dict["rent_house_all_mar09"] = rent_house_all_line[121 + 32]
        rent_house_all_dict["rent_house_all_jun09"] = rent_house_all_line[121 + 34]
        rent_house_all_dict["rent_house_all_sep09"] = rent_house_all_line[121 + 36]
        rent_house_all_dict["rent_house_all_dec09"] = rent_house_all_line[121 + 38]

        rent_house_all_dict["rent_house_all_mar10"] = rent_house_all_line[121 + 40]
        rent_house_all_dict["rent_house_all_jun10"] = rent_house_all_line[121 + 42]
        rent_house_all_dict["rent_house_all_sep10"] = rent_house_all_line[121 + 44]
        rent_house_all_dict["rent_house_all_dec10"] = rent_house_all_line[121 + 46]

        rent_house_all_dict["rent_house_all_mar11"] = rent_house_all_line[121 + 48]
        rent_house_all_dict["rent_house_all_jun11"] = rent_house_all_line[121 + 50]
        rent_house_all_dict["rent_house_all_sep11"] = rent_house_all_line[121 + 52]
        rent_house_all_dict["rent_house_all_dec11"] = rent_house_all_line[121 + 54]

        rent_house_all_dict["rent_house_all_mar12"] = rent_house_all_line[121 + 56]
        rent_house_all_dict["rent_house_all_jun12"] = rent_house_all_line[121 + 58]
        rent_house_all_dict["rent_house_all_sep12"] = rent_house_all_line[121 + 60]
        rent_house_all_dict["rent_house_all_dec12"] = rent_house_all_line[121 + 62]

        rent_house_all_dict["rent_house_all_mar13"] = rent_house_all_line[121 + 64]
        rent_house_all_dict["rent_house_all_jun13"] = rent_house_all_line[121 + 66]
        rent_house_all_dict["rent_house_all_sep13"] = rent_house_all_line[121 + 68]
        rent_house_all_dict["rent_house_all_dec13"] = rent_house_all_line[121 + 70]

        rent_house_all_dict["rent_house_all_mar14"] = rent_house_all_line[121 + 72]
        rent_house_all_dict["rent_house_all_jun14"] = rent_house_all_line[121 + 74]
        rent_house_all_dict["rent_house_all_sep14"] = rent_house_all_line[121 + 76]
        rent_house_all_dict["rent_house_all_dec14"] = rent_house_all_line[121 + 78]

        rent_house_all_dict["rent_house_all_mar15"] = rent_house_all_line[121 + 80]
        rent_house_all_dict["rent_house_all_jun15"] = rent_house_all_line[121 + 82]
        rent_house_all_dict["rent_house_all_sep15"] = rent_house_all_line[121 + 84]
        rent_house_all_dict["rent_house_all_dec15"] = rent_house_all_line[121 + 86]

        rent_house_all_dict["rent_house_all_mar16"] = rent_house_all_line[121 + 88]
        rent_house_all_dict["rent_house_all_jun16"] = rent_house_all_line[121 + 91]
        rent_house_all_dict["rent_house_all_sep16"] = rent_house_all_line[121 + 93]
        rent_house_all_dict["rent_house_all_dec16"] = rent_house_all_line[121 + 95]

        sale_house_line = sale_house.row_values(i + 2)
        index = 0
        for j in sale_house_line:
            if j=="-":
                sale_house_line[index] = sale_house.row_values(5)[index]
            index += 1
        sale_house_dict['sale_house_05'] = sale_house_line[115 + 0] + sale_house_line[115 + 2] + sale_house_line[
            115 + 4] + sale_house_line[115 + 6]
        sale_house_dict['sale_house_06'] = sale_house_line[115 + 8] + sale_house_line[115 + 10] + sale_house_line[
            115 + 12] + sale_house_line[115 + 14]
        sale_house_dict['sale_house_07'] = sale_house_line[115 + 16] + sale_house_line[115 + 18] + sale_house_line[
            115 + 20] + sale_house_line[115 + 22]
        sale_house_dict['sale_house_08'] = sale_house_line[115 + 24] + sale_house_line[115 + 26] + sale_house_line[
            115 + 28] + sale_house_line[115 + 30]
        sale_house_dict['sale_house_09'] = sale_house_line[115 + 32] + sale_house_line[115 + 34] + sale_house_line[
            115 + 36] + sale_house_line[115 + 38]
        sale_house_dict['sale_house_10'] = sale_house_line[115 + 40] + sale_house_line[115 + 42] + sale_house_line[
            115 + 44] + sale_house_line[115 + 46]
        sale_house_dict['sale_house_11'] = sale_house_line[115 + 48] + sale_house_line[115 + 50] + sale_house_line[
            115 + 52] + sale_house_line[115 + 54]
        sale_house_dict['sale_house_12'] = sale_house_line[115 + 56] + sale_house_line[115 + 58] + sale_house_line[
            115 + 60] + sale_house_line[115 + 62]
        sale_house_dict['sale_house_13'] = sale_house_line[115 + 64] + sale_house_line[115 + 66] + sale_house_line[
            115 + 68] + sale_house_line[115 + 70]
        sale_house_dict['sale_house_14'] = sale_house_line[115 + 72] + sale_house_line[115 + 74] + sale_house_line[
            115 + 76] + sale_house_line[115 + 78]
        sale_house_dict['sale_house_15'] = sale_house_line[115 + 80] + sale_house_line[115 + 82] + sale_house_line[
            115 + 84] + sale_house_line[115 + 86]
        sale_house_dict['sale_house_16'] = sale_house_line[115 + 88] + sale_house_line[115 + 90] + sale_house_line[
            115 + 92] + sale_house_line[115 + 94]

    if i >= 32 and i < 49:
        rent_house_two_line = rent_house_two.row_values(i)
        index = 0
        for j in rent_house_two_line:
            if j=="-":
                rent_house_two_line[index] = rent_house_two.row_values(3)[index]
            index += 1

        rent_house_two_dict["rent_house_two_mar05"] = rent_house_two_line[121]
        rent_house_two_dict["rent_house_two_jun05"] = rent_house_two_line[121 + 2]
        rent_house_two_dict["rent_house_two_sep05"] = rent_house_two_line[121 + 4]
        rent_house_two_dict["rent_house_two_dec05"] = rent_house_two_line[121 + 6]

        rent_house_two_dict["rent_house_two_mar06"] = rent_house_two_line[121 + 8]
        rent_house_two_dict["rent_house_two_jun06"] = rent_house_two_line[121 + 10]
        rent_house_two_dict["rent_house_two_sep06"] = rent_house_two_line[121 + 12]
        rent_house_two_dict["rent_house_two_dec06"] = rent_house_two_line[121 + 14]

        rent_house_two_dict["rent_house_two_mar07"] = rent_house_two_line[121 + 16]
        rent_house_two_dict["rent_house_two_jun07"] = rent_house_two_line[121 + 18]
        rent_house_two_dict["rent_house_two_sep07"] = rent_house_two_line[121 + 20]
        rent_house_two_dict["rent_house_two_dec07"] = rent_house_two_line[121 + 22]

        rent_house_two_dict["rent_house_two_mar08"] = rent_house_two_line[121 + 24]
        rent_house_two_dict["rent_house_two_jun08"] = rent_house_two_line[121 + 26]
        rent_house_two_dict["rent_house_two_sep08"] = rent_house_two_line[121 + 28]
        rent_house_two_dict["rent_house_two_dec08"] = rent_house_two_line[121 + 30]

        rent_house_two_dict["rent_house_two_mar09"] = rent_house_two_line[121 + 32]
        rent_house_two_dict["rent_house_two_jun09"] = rent_house_two_line[121 + 34]
        rent_house_two_dict["rent_house_two_sep09"] = rent_house_two_line[121 + 36]
        rent_house_two_dict["rent_house_two_dec09"] = rent_house_two_line[121 + 38]

        rent_house_two_dict["rent_house_two_mar10"] = rent_house_two_line[121 + 40]
        rent_house_two_dict["rent_house_two_jun10"] = rent_house_two_line[121 + 42]
        rent_house_two_dict["rent_house_two_sep10"] = rent_house_two_line[121 + 44]
        rent_house_two_dict["rent_house_two_dec10"] = rent_house_two_line[121 + 46]

        rent_house_two_dict["rent_house_two_mar11"] = rent_house_two_line[121 + 48]
        rent_house_two_dict["rent_house_two_jun11"] = rent_house_two_line[121 + 50]
        rent_house_two_dict["rent_house_two_sep11"] = rent_house_two_line[121 + 52]
        rent_house_two_dict["rent_house_two_dec11"] = rent_house_two_line[121 + 54]

        rent_house_two_dict["rent_house_two_mar12"] = rent_house_two_line[121 + 56]
        rent_house_two_dict["rent_house_two_jun12"] = rent_house_two_line[121 + 58]
        rent_house_two_dict["rent_house_two_sep12"] = rent_house_two_line[121 + 60]
        rent_house_two_dict["rent_house_two_dec12"] = rent_house_two_line[121 + 62]

        rent_house_two_dict["rent_house_two_mar13"] = rent_house_two_line[121 + 64]
        rent_house_two_dict["rent_house_two_jun13"] = rent_house_two_line[121 + 66]
        rent_house_two_dict["rent_house_two_sep13"] = rent_house_two_line[121 + 68]
        rent_house_two_dict["rent_house_two_dec13"] = rent_house_two_line[121 + 70]

        rent_house_two_dict["rent_house_two_mar14"] = rent_house_two_line[121 + 72]
        rent_house_two_dict["rent_house_two_jun14"] = rent_house_two_line[121 + 74]
        rent_house_two_dict["rent_house_two_sep14"] = rent_house_two_line[121 + 76]
        rent_house_two_dict["rent_house_two_dec14"] = rent_house_two_line[121 + 78]

        rent_house_two_dict["rent_house_two_mar15"] = rent_house_two_line[121 + 80]
        rent_house_two_dict["rent_house_two_jun15"] = rent_house_two_line[121 + 82]
        rent_house_two_dict["rent_house_two_sep15"] = rent_house_two_line[121 + 84]
        rent_house_two_dict["rent_house_two_dec15"] = rent_house_two_line[121 + 86]

        rent_house_two_dict["rent_house_two_mar16"] = rent_house_two_line[121 + 88]
        rent_house_two_dict["rent_house_two_jun16"] = rent_house_two_line[121 + 91]
        rent_house_two_dict["rent_house_two_sep16"] = rent_house_two_line[121 + 93]
        rent_house_two_dict["rent_house_two_dec16"] = rent_house_two_line[121 + 95]

        rent_house_three_line = rent_house_three.row_values(i)
        index = 0
        for j in rent_house_three_line:
            if j=="-":
                rent_house_three_line[index] = rent_house_three.row_values(3)[index]
            index += 1

        rent_house_three_dict["rent_house_three_mar05"] = rent_house_three_line[121]
        rent_house_three_dict["rent_house_three_jun05"] = rent_house_three_line[121 + 2]
        rent_house_three_dict["rent_house_three_sep05"] = rent_house_three_line[121 + 4]
        rent_house_three_dict["rent_house_three_dec05"] = rent_house_three_line[121 + 6]

        rent_house_three_dict["rent_house_three_mar06"] = rent_house_three_line[121 + 8]
        rent_house_three_dict["rent_house_three_jun06"] = rent_house_three_line[121 + 10]
        rent_house_three_dict["rent_house_three_sep06"] = rent_house_three_line[121 + 12]
        rent_house_three_dict["rent_house_three_dec06"] = rent_house_three_line[121 + 14]

        rent_house_three_dict["rent_house_three_mar07"] = rent_house_three_line[121 + 16]
        rent_house_three_dict["rent_house_three_jun07"] = rent_house_three_line[121 + 18]
        rent_house_three_dict["rent_house_three_sep07"] = rent_house_three_line[121 + 20]
        rent_house_three_dict["rent_house_three_dec07"] = rent_house_three_line[121 + 22]

        rent_house_three_dict["rent_house_three_mar08"] = rent_house_three_line[121 + 24]
        rent_house_three_dict["rent_house_three_jun08"] = rent_house_three_line[121 + 26]
        rent_house_three_dict["rent_house_three_sep08"] = rent_house_three_line[121 + 28]
        rent_house_three_dict["rent_house_three_dec08"] = rent_house_three_line[121 + 30]

        rent_house_three_dict["rent_house_three_mar09"] = rent_house_three_line[121 + 32]
        rent_house_three_dict["rent_house_three_jun09"] = rent_house_three_line[121 + 34]
        rent_house_three_dict["rent_house_three_sep09"] = rent_house_three_line[121 + 36]
        rent_house_three_dict["rent_house_three_dec09"] = rent_house_three_line[121 + 38]

        rent_house_three_dict["rent_house_three_mar10"] = rent_house_three_line[121 + 40]
        rent_house_three_dict["rent_house_three_jun10"] = rent_house_three_line[121 + 42]
        rent_house_three_dict["rent_house_three_sep10"] = rent_house_three_line[121 + 44]
        rent_house_three_dict["rent_house_three_dec10"] = rent_house_three_line[121 + 46]

        rent_house_three_dict["rent_house_three_mar11"] = rent_house_three_line[121 + 48]
        rent_house_three_dict["rent_house_three_jun11"] = rent_house_three_line[121 + 50]
        rent_house_three_dict["rent_house_three_sep11"] = rent_house_three_line[121 + 52]
        rent_house_three_dict["rent_house_three_dec11"] = rent_house_three_line[121 + 54]

        rent_house_three_dict["rent_house_three_mar12"] = rent_house_three_line[121 + 56]
        rent_house_three_dict["rent_house_three_jun12"] = rent_house_three_line[121 + 58]
        rent_house_three_dict["rent_house_three_sep12"] = rent_house_three_line[121 + 60]
        rent_house_three_dict["rent_house_three_dec12"] = rent_house_three_line[121 + 62]

        rent_house_three_dict["rent_house_three_mar13"] = rent_house_three_line[121 + 64]
        rent_house_three_dict["rent_house_three_jun13"] = rent_house_three_line[121 + 66]
        rent_house_three_dict["rent_house_three_sep13"] = rent_house_three_line[121 + 68]
        rent_house_three_dict["rent_house_three_dec13"] = rent_house_three_line[121 + 70]

        rent_house_three_dict["rent_house_three_mar14"] = rent_house_three_line[121 + 72]
        rent_house_three_dict["rent_house_three_jun14"] = rent_house_three_line[121 + 74]
        rent_house_three_dict["rent_house_three_sep14"] = rent_house_three_line[121 + 76]
        rent_house_three_dict["rent_house_three_dec14"] = rent_house_three_line[121 + 78]

        rent_house_three_dict["rent_house_three_mar15"] = rent_house_three_line[121 + 80]
        rent_house_three_dict["rent_house_three_jun15"] = rent_house_three_line[121 + 82]
        rent_house_three_dict["rent_house_three_sep15"] = rent_house_three_line[121 + 84]
        rent_house_three_dict["rent_house_three_dec15"] = rent_house_three_line[121 + 86]

        rent_house_three_dict["rent_house_three_mar16"] = rent_house_three_line[121 + 88]
        rent_house_three_dict["rent_house_three_jun16"] = rent_house_three_line[121 + 91]
        rent_house_three_dict["rent_house_three_sep16"] = rent_house_three_line[121 + 93]
        rent_house_three_dict["rent_house_three_dec16"] = rent_house_three_line[121 + 95]

        rent_house_all_line = rent_house_all.row_values(i)
        index = 0
        for j in rent_house_all_line:
            if j=="-":
                rent_house_all_line[index] = rent_house_all.row_values(3)[index]
            index += 1

        rent_house_all_dict["rent_house_all_mar05"] = rent_house_all_line[121]
        rent_house_all_dict["rent_house_all_jun05"] = rent_house_all_line[121 + 2]
        rent_house_all_dict["rent_house_all_sep05"] = rent_house_all_line[121 + 4]
        rent_house_all_dict["rent_house_all_dec05"] = rent_house_all_line[121 + 6]

        rent_house_all_dict["rent_house_all_mar06"] = rent_house_all_line[121 + 8]
        rent_house_all_dict["rent_house_all_jun06"] = rent_house_all_line[121 + 10]
        rent_house_all_dict["rent_house_all_sep06"] = rent_house_all_line[121 + 12]
        rent_house_all_dict["rent_house_all_dec06"] = rent_house_all_line[121 + 14]

        rent_house_all_dict["rent_house_all_mar07"] = rent_house_all_line[121 + 16]
        rent_house_all_dict["rent_house_all_jun07"] = rent_house_all_line[121 + 18]
        rent_house_all_dict["rent_house_all_sep07"] = rent_house_all_line[121 + 20]
        rent_house_all_dict["rent_house_all_dec07"] = rent_house_all_line[121 + 22]

        rent_house_all_dict["rent_house_all_mar08"] = rent_house_all_line[121 + 24]
        rent_house_all_dict["rent_house_all_jun08"] = rent_house_all_line[121 + 26]
        rent_house_all_dict["rent_house_all_sep08"] = rent_house_all_line[121 + 28]
        rent_house_all_dict["rent_house_all_dec08"] = rent_house_all_line[121 + 30]

        rent_house_all_dict["rent_house_all_mar09"] = rent_house_all_line[121 + 32]
        rent_house_all_dict["rent_house_all_jun09"] = rent_house_all_line[121 + 34]
        rent_house_all_dict["rent_house_all_sep09"] = rent_house_all_line[121 + 36]
        rent_house_all_dict["rent_house_all_dec09"] = rent_house_all_line[121 + 38]

        rent_house_all_dict["rent_house_all_mar10"] = rent_house_all_line[121 + 40]
        rent_house_all_dict["rent_house_all_jun10"] = rent_house_all_line[121 + 42]
        rent_house_all_dict["rent_house_all_sep10"] = rent_house_all_line[121 + 44]
        rent_house_all_dict["rent_house_all_dec10"] = rent_house_all_line[121 + 46]

        rent_house_all_dict["rent_house_all_mar11"] = rent_house_all_line[121 + 48]
        rent_house_all_dict["rent_house_all_jun11"] = rent_house_all_line[121 + 50]
        rent_house_all_dict["rent_house_all_sep11"] = rent_house_all_line[121 + 52]
        rent_house_all_dict["rent_house_all_dec11"] = rent_house_all_line[121 + 54]

        rent_house_all_dict["rent_house_all_mar12"] = rent_house_all_line[121 + 56]
        rent_house_all_dict["rent_house_all_jun12"] = rent_house_all_line[121 + 58]
        rent_house_all_dict["rent_house_all_sep12"] = rent_house_all_line[121 + 60]
        rent_house_all_dict["rent_house_all_dec12"] = rent_house_all_line[121 + 62]

        rent_house_all_dict["rent_house_all_mar13"] = rent_house_all_line[121 + 64]
        rent_house_all_dict["rent_house_all_jun13"] = rent_house_all_line[121 + 66]
        rent_house_all_dict["rent_house_all_sep13"] = rent_house_all_line[121 + 68]
        rent_house_all_dict["rent_house_all_dec13"] = rent_house_all_line[121 + 70]

        rent_house_all_dict["rent_house_all_mar14"] = rent_house_all_line[121 + 72]
        rent_house_all_dict["rent_house_all_jun14"] = rent_house_all_line[121 + 74]
        rent_house_all_dict["rent_house_all_sep14"] = rent_house_all_line[121 + 76]
        rent_house_all_dict["rent_house_all_dec14"] = rent_house_all_line[121 + 78]

        rent_house_all_dict["rent_house_all_mar15"] = rent_house_all_line[121 + 80]
        rent_house_all_dict["rent_house_all_jun15"] = rent_house_all_line[121 + 82]
        rent_house_all_dict["rent_house_all_sep15"] = rent_house_all_line[121 + 84]
        rent_house_all_dict["rent_house_all_dec15"] = rent_house_all_line[121 + 86]

        rent_house_all_dict["rent_house_all_mar16"] = rent_house_all_line[121 + 88]
        rent_house_all_dict["rent_house_all_jun16"] = rent_house_all_line[121 + 91]
        rent_house_all_dict["rent_house_all_sep16"] = rent_house_all_line[121 + 93]
        rent_house_all_dict["rent_house_all_dec16"] = rent_house_all_line[121 + 95]

        sale_house_line = sale_house.row_values(i + 2)
        index = 0
        for j in sale_house_line:
            if j=="-":
                sale_house_line[index] = sale_house.row_values(5)[index]
            index += 1
        sale_house_dict['sale_house_05'] = sale_house_line[115 + 0] + sale_house_line[115 + 2] + sale_house_line[
            115 + 4] + sale_house_line[115 + 6]
        sale_house_dict['sale_house_06'] = sale_house_line[115 + 8] + sale_house_line[115 + 10] + sale_house_line[
            115 + 12] + sale_house_line[115 + 14]
        sale_house_dict['sale_house_07'] = sale_house_line[115 + 16] + sale_house_line[115 + 18] + sale_house_line[
            115 + 20] + sale_house_line[115 + 22]
        sale_house_dict['sale_house_08'] = sale_house_line[115 + 24] + sale_house_line[115 + 26] + sale_house_line[
            115 + 28] + sale_house_line[115 + 30]
        sale_house_dict['sale_house_09'] = sale_house_line[115 + 32] + sale_house_line[115 + 34] + sale_house_line[
            115 + 36] + sale_house_line[115 + 38]
        sale_house_dict['sale_house_10'] = sale_house_line[115 + 40] + sale_house_line[115 + 42] + sale_house_line[
            115 + 44] + sale_house_line[115 + 46]
        sale_house_dict['sale_house_11'] = sale_house_line[115 + 48] + sale_house_line[115 + 50] + sale_house_line[
            115 + 52] + sale_house_line[115 + 54]
        sale_house_dict['sale_house_12'] = sale_house_line[115 + 56] + sale_house_line[115 + 58] + sale_house_line[
            115 + 60] + sale_house_line[115 + 62]
        sale_house_dict['sale_house_13'] = sale_house_line[115 + 64] + sale_house_line[115 + 66] + sale_house_line[
            115 + 68] + sale_house_line[115 + 70]
        sale_house_dict['sale_house_14'] = sale_house_line[115 + 72] + sale_house_line[115 + 74] + sale_house_line[
            115 + 76] + sale_house_line[115 + 78]
        sale_house_dict['sale_house_15'] = sale_house_line[115 + 80] + sale_house_line[115 + 82] + sale_house_line[
            115 + 84] + sale_house_line[115 + 86]
        sale_house_dict['sale_house_16'] = sale_house_line[115 + 88] + sale_house_line[115 + 90] + sale_house_line[
            115 + 92] + sale_house_line[115 + 94]

    if i >= 50 and i < 58:
        rent_house_two_line = rent_house_two.row_values(i)
        index = 0
        for j in rent_house_two_line:
            if j=="-":
                rent_house_two_line[index] = rent_house_two.row_values(3)[index]
            index += 1

        rent_house_two_dict["rent_house_two_mar05"] = rent_house_two_line[121]
        rent_house_two_dict["rent_house_two_jun05"] = rent_house_two_line[121 + 2]
        rent_house_two_dict["rent_house_two_sep05"] = rent_house_two_line[121 + 4]
        rent_house_two_dict["rent_house_two_dec05"] = rent_house_two_line[121 + 6]

        rent_house_two_dict["rent_house_two_mar06"] = rent_house_two_line[121 + 8]
        rent_house_two_dict["rent_house_two_jun06"] = rent_house_two_line[121 + 10]
        rent_house_two_dict["rent_house_two_sep06"] = rent_house_two_line[121 + 12]
        rent_house_two_dict["rent_house_two_dec06"] = rent_house_two_line[121 + 14]

        rent_house_two_dict["rent_house_two_mar07"] = rent_house_two_line[121 + 16]
        rent_house_two_dict["rent_house_two_jun07"] = rent_house_two_line[121 + 18]
        rent_house_two_dict["rent_house_two_sep07"] = rent_house_two_line[121 + 20]
        rent_house_two_dict["rent_house_two_dec07"] = rent_house_two_line[121 + 22]

        rent_house_two_dict["rent_house_two_mar08"] = rent_house_two_line[121 + 24]
        rent_house_two_dict["rent_house_two_jun08"] = rent_house_two_line[121 + 26]
        rent_house_two_dict["rent_house_two_sep08"] = rent_house_two_line[121 + 28]
        rent_house_two_dict["rent_house_two_dec08"] = rent_house_two_line[121 + 30]

        rent_house_two_dict["rent_house_two_mar09"] = rent_house_two_line[121 + 32]
        rent_house_two_dict["rent_house_two_jun09"] = rent_house_two_line[121 + 34]
        rent_house_two_dict["rent_house_two_sep09"] = rent_house_two_line[121 + 36]
        rent_house_two_dict["rent_house_two_dec09"] = rent_house_two_line[121 + 38]

        rent_house_two_dict["rent_house_two_mar10"] = rent_house_two_line[121 + 40]
        rent_house_two_dict["rent_house_two_jun10"] = rent_house_two_line[121 + 42]
        rent_house_two_dict["rent_house_two_sep10"] = rent_house_two_line[121 + 44]
        rent_house_two_dict["rent_house_two_dec10"] = rent_house_two_line[121 + 46]

        rent_house_two_dict["rent_house_two_mar11"] = rent_house_two_line[121 + 48]
        rent_house_two_dict["rent_house_two_jun11"] = rent_house_two_line[121 + 50]
        rent_house_two_dict["rent_house_two_sep11"] = rent_house_two_line[121 + 52]
        rent_house_two_dict["rent_house_two_dec11"] = rent_house_two_line[121 + 54]

        rent_house_two_dict["rent_house_two_mar12"] = rent_house_two_line[121 + 56]
        rent_house_two_dict["rent_house_two_jun12"] = rent_house_two_line[121 + 58]
        rent_house_two_dict["rent_house_two_sep12"] = rent_house_two_line[121 + 60]
        rent_house_two_dict["rent_house_two_dec12"] = rent_house_two_line[121 + 62]

        rent_house_two_dict["rent_house_two_mar13"] = rent_house_two_line[121 + 64]
        rent_house_two_dict["rent_house_two_jun13"] = rent_house_two_line[121 + 66]
        rent_house_two_dict["rent_house_two_sep13"] = rent_house_two_line[121 + 68]
        rent_house_two_dict["rent_house_two_dec13"] = rent_house_two_line[121 + 70]

        rent_house_two_dict["rent_house_two_mar14"] = rent_house_two_line[121 + 72]
        rent_house_two_dict["rent_house_two_jun14"] = rent_house_two_line[121 + 74]
        rent_house_two_dict["rent_house_two_sep14"] = rent_house_two_line[121 + 76]
        rent_house_two_dict["rent_house_two_dec14"] = rent_house_two_line[121 + 78]

        rent_house_two_dict["rent_house_two_mar15"] = rent_house_two_line[121 + 80]
        rent_house_two_dict["rent_house_two_jun15"] = rent_house_two_line[121 + 82]
        rent_house_two_dict["rent_house_two_sep15"] = rent_house_two_line[121 + 84]
        rent_house_two_dict["rent_house_two_dec15"] = rent_house_two_line[121 + 86]

        rent_house_two_dict["rent_house_two_mar16"] = rent_house_two_line[121 + 88]
        rent_house_two_dict["rent_house_two_jun16"] = rent_house_two_line[121 + 91]
        rent_house_two_dict["rent_house_two_sep16"] = rent_house_two_line[121 + 93]
        rent_house_two_dict["rent_house_two_dec16"] = rent_house_two_line[121 + 95]

        rent_house_three_line = rent_house_three.row_values(i)
        index = 0
        for j in rent_house_three_line:
            if j=="-":
                rent_house_three_line[index] = rent_house_three.row_values(3)[index]
            index += 1

        rent_house_three_dict["rent_house_three_mar05"] = rent_house_three_line[121]
        rent_house_three_dict["rent_house_three_jun05"] = rent_house_three_line[121 + 2]
        rent_house_three_dict["rent_house_three_sep05"] = rent_house_three_line[121 + 4]
        rent_house_three_dict["rent_house_three_dec05"] = rent_house_three_line[121 + 6]

        rent_house_three_dict["rent_house_three_mar06"] = rent_house_three_line[121 + 8]
        rent_house_three_dict["rent_house_three_jun06"] = rent_house_three_line[121 + 10]
        rent_house_three_dict["rent_house_three_sep06"] = rent_house_three_line[121 + 12]
        rent_house_three_dict["rent_house_three_dec06"] = rent_house_three_line[121 + 14]

        rent_house_three_dict["rent_house_three_mar07"] = rent_house_three_line[121 + 16]
        rent_house_three_dict["rent_house_three_jun07"] = rent_house_three_line[121 + 18]
        rent_house_three_dict["rent_house_three_sep07"] = rent_house_three_line[121 + 20]
        rent_house_three_dict["rent_house_three_dec07"] = rent_house_three_line[121 + 22]

        rent_house_three_dict["rent_house_three_mar08"] = rent_house_three_line[121 + 24]
        rent_house_three_dict["rent_house_three_jun08"] = rent_house_three_line[121 + 26]
        rent_house_three_dict["rent_house_three_sep08"] = rent_house_three_line[121 + 28]
        rent_house_three_dict["rent_house_three_dec08"] = rent_house_three_line[121 + 30]

        rent_house_three_dict["rent_house_three_mar09"] = rent_house_three_line[121 + 32]
        rent_house_three_dict["rent_house_three_jun09"] = rent_house_three_line[121 + 34]
        rent_house_three_dict["rent_house_three_sep09"] = rent_house_three_line[121 + 36]
        rent_house_three_dict["rent_house_three_dec09"] = rent_house_three_line[121 + 38]

        rent_house_three_dict["rent_house_three_mar10"] = rent_house_three_line[121 + 40]
        rent_house_three_dict["rent_house_three_jun10"] = rent_house_three_line[121 + 42]
        rent_house_three_dict["rent_house_three_sep10"] = rent_house_three_line[121 + 44]
        rent_house_three_dict["rent_house_three_dec10"] = rent_house_three_line[121 + 46]

        rent_house_three_dict["rent_house_three_mar11"] = rent_house_three_line[121 + 48]
        rent_house_three_dict["rent_house_three_jun11"] = rent_house_three_line[121 + 50]
        rent_house_three_dict["rent_house_three_sep11"] = rent_house_three_line[121 + 52]
        rent_house_three_dict["rent_house_three_dec11"] = rent_house_three_line[121 + 54]

        rent_house_three_dict["rent_house_three_mar12"] = rent_house_three_line[121 + 56]
        rent_house_three_dict["rent_house_three_jun12"] = rent_house_three_line[121 + 58]
        rent_house_three_dict["rent_house_three_sep12"] = rent_house_three_line[121 + 60]
        rent_house_three_dict["rent_house_three_dec12"] = rent_house_three_line[121 + 62]

        rent_house_three_dict["rent_house_three_mar13"] = rent_house_three_line[121 + 64]
        rent_house_three_dict["rent_house_three_jun13"] = rent_house_three_line[121 + 66]
        rent_house_three_dict["rent_house_three_sep13"] = rent_house_three_line[121 + 68]
        rent_house_three_dict["rent_house_three_dec13"] = rent_house_three_line[121 + 70]

        rent_house_three_dict["rent_house_three_mar14"] = rent_house_three_line[121 + 72]
        rent_house_three_dict["rent_house_three_jun14"] = rent_house_three_line[121 + 74]
        rent_house_three_dict["rent_house_three_sep14"] = rent_house_three_line[121 + 76]
        rent_house_three_dict["rent_house_three_dec14"] = rent_house_three_line[121 + 78]

        rent_house_three_dict["rent_house_three_mar15"] = rent_house_three_line[121 + 80]
        rent_house_three_dict["rent_house_three_jun15"] = rent_house_three_line[121 + 82]
        rent_house_three_dict["rent_house_three_sep15"] = rent_house_three_line[121 + 84]
        rent_house_three_dict["rent_house_three_dec15"] = rent_house_three_line[121 + 86]

        rent_house_three_dict["rent_house_three_mar16"] = rent_house_three_line[121 + 88]
        rent_house_three_dict["rent_house_three_jun16"] = rent_house_three_line[121 + 91]
        rent_house_three_dict["rent_house_three_sep16"] = rent_house_three_line[121 + 93]
        rent_house_three_dict["rent_house_three_dec16"] = rent_house_three_line[121 + 95]

        rent_house_all_line = rent_house_all.row_values(i)
        index = 0
        for j in rent_house_all_line:
            if j=="-":
                rent_house_all_line[index] = rent_house_all.row_values(3)[index]
            index += 1

        rent_house_all_dict["rent_house_all_mar05"] = rent_house_all_line[121]
        rent_house_all_dict["rent_house_all_jun05"] = rent_house_all_line[121 + 2]
        rent_house_all_dict["rent_house_all_sep05"] = rent_house_all_line[121 + 4]
        rent_house_all_dict["rent_house_all_dec05"] = rent_house_all_line[121 + 6]

        rent_house_all_dict["rent_house_all_mar06"] = rent_house_all_line[121 + 8]
        rent_house_all_dict["rent_house_all_jun06"] = rent_house_all_line[121 + 10]
        rent_house_all_dict["rent_house_all_sep06"] = rent_house_all_line[121 + 12]
        rent_house_all_dict["rent_house_all_dec06"] = rent_house_all_line[121 + 14]

        rent_house_all_dict["rent_house_all_mar07"] = rent_house_all_line[121 + 16]
        rent_house_all_dict["rent_house_all_jun07"] = rent_house_all_line[121 + 18]
        rent_house_all_dict["rent_house_all_sep07"] = rent_house_all_line[121 + 20]
        rent_house_all_dict["rent_house_all_dec07"] = rent_house_all_line[121 + 22]

        rent_house_all_dict["rent_house_all_mar08"] = rent_house_all_line[121 + 24]
        rent_house_all_dict["rent_house_all_jun08"] = rent_house_all_line[121 + 26]
        rent_house_all_dict["rent_house_all_sep08"] = rent_house_all_line[121 + 28]
        rent_house_all_dict["rent_house_all_dec08"] = rent_house_all_line[121 + 30]

        rent_house_all_dict["rent_house_all_mar09"] = rent_house_all_line[121 + 32]
        rent_house_all_dict["rent_house_all_jun09"] = rent_house_all_line[121 + 34]
        rent_house_all_dict["rent_house_all_sep09"] = rent_house_all_line[121 + 36]
        rent_house_all_dict["rent_house_all_dec09"] = rent_house_all_line[121 + 38]

        rent_house_all_dict["rent_house_all_mar10"] = rent_house_all_line[121 + 40]
        rent_house_all_dict["rent_house_all_jun10"] = rent_house_all_line[121 + 42]
        rent_house_all_dict["rent_house_all_sep10"] = rent_house_all_line[121 + 44]
        rent_house_all_dict["rent_house_all_dec10"] = rent_house_all_line[121 + 46]

        rent_house_all_dict["rent_house_all_mar11"] = rent_house_all_line[121 + 48]
        rent_house_all_dict["rent_house_all_jun11"] = rent_house_all_line[121 + 50]
        rent_house_all_dict["rent_house_all_sep11"] = rent_house_all_line[121 + 52]
        rent_house_all_dict["rent_house_all_dec11"] = rent_house_all_line[121 + 54]

        rent_house_all_dict["rent_house_all_mar12"] = rent_house_all_line[121 + 56]
        rent_house_all_dict["rent_house_all_jun12"] = rent_house_all_line[121 + 58]
        rent_house_all_dict["rent_house_all_sep12"] = rent_house_all_line[121 + 60]
        rent_house_all_dict["rent_house_all_dec12"] = rent_house_all_line[121 + 62]

        rent_house_all_dict["rent_house_all_mar13"] = rent_house_all_line[121 + 64]
        rent_house_all_dict["rent_house_all_jun13"] = rent_house_all_line[121 + 66]
        rent_house_all_dict["rent_house_all_sep13"] = rent_house_all_line[121 + 68]
        rent_house_all_dict["rent_house_all_dec13"] = rent_house_all_line[121 + 70]

        rent_house_all_dict["rent_house_all_mar14"] = rent_house_all_line[121 + 72]
        rent_house_all_dict["rent_house_all_jun14"] = rent_house_all_line[121 + 74]
        rent_house_all_dict["rent_house_all_sep14"] = rent_house_all_line[121 + 76]
        rent_house_all_dict["rent_house_all_dec14"] = rent_house_all_line[121 + 78]

        rent_house_all_dict["rent_house_all_mar15"] = rent_house_all_line[121 + 80]
        rent_house_all_dict["rent_house_all_jun15"] = rent_house_all_line[121 + 82]
        rent_house_all_dict["rent_house_all_sep15"] = rent_house_all_line[121 + 84]
        rent_house_all_dict["rent_house_all_dec15"] = rent_house_all_line[121 + 86]

        rent_house_all_dict["rent_house_all_mar16"] = rent_house_all_line[121 + 88]
        rent_house_all_dict["rent_house_all_jun16"] = rent_house_all_line[121 + 91]
        rent_house_all_dict["rent_house_all_sep16"] = rent_house_all_line[121 + 93]
        rent_house_all_dict["rent_house_all_dec16"] = rent_house_all_line[121 + 95]

        sale_house_line = sale_house.row_values(i + 2)
        index = 0
        for j in sale_house_line:
            if j=="-":
                sale_house_line[index] = sale_house.row_values(5)[index]
            index += 1
        sale_house_dict['sale_house_05'] = sale_house_line[115 + 0] + sale_house_line[115 + 2] + sale_house_line[
            115 + 4] + sale_house_line[115 + 6]
        sale_house_dict['sale_house_06'] = sale_house_line[115 + 8] + sale_house_line[115 + 10] + sale_house_line[
            115 + 12] + sale_house_line[115 + 14]
        sale_house_dict['sale_house_07'] = sale_house_line[115 + 16] + sale_house_line[115 + 18] + sale_house_line[
            115 + 20] + sale_house_line[115 + 22]
        sale_house_dict['sale_house_08'] = sale_house_line[115 + 24] + sale_house_line[115 + 26] + sale_house_line[
            115 + 28] + sale_house_line[115 + 30]
        sale_house_dict['sale_house_09'] = sale_house_line[115 + 32] + sale_house_line[115 + 34] + sale_house_line[
            115 + 36] + sale_house_line[115 + 38]
        sale_house_dict['sale_house_10'] = sale_house_line[115 + 40] + sale_house_line[115 + 42] + sale_house_line[
            115 + 44] + sale_house_line[115 + 46]
        sale_house_dict['sale_house_11'] = sale_house_line[115 + 48] + sale_house_line[115 + 50] + sale_house_line[
            115 + 52] + sale_house_line[115 + 54]
        sale_house_dict['sale_house_12'] = sale_house_line[115 + 56] + sale_house_line[115 + 58] + sale_house_line[
            115 + 60] + sale_house_line[115 + 62]
        sale_house_dict['sale_house_13'] = sale_house_line[115 + 64] + sale_house_line[115 + 66] + sale_house_line[
            115 + 68] + sale_house_line[115 + 70]
        sale_house_dict['sale_house_14'] = sale_house_line[115 + 72] + sale_house_line[115 + 74] + sale_house_line[
            115 + 76] + sale_house_line[115 + 78]
        sale_house_dict['sale_house_15'] = sale_house_line[115 + 80] + sale_house_line[115 + 82] + sale_house_line[
            115 + 84] + sale_house_line[115 + 86]
        sale_house_dict['sale_house_16'] = sale_house_line[115 + 88] + sale_house_line[115 + 90] + sale_house_line[
            115 + 92] + sale_house_line[115 + 94]

    house_dict = {}
    house_dict["two_rent"] = rent_house_two_dict
    house_dict["three_rent"] = rent_house_three_dict
    house_dict["all_rent"] = rent_house_all_dict
    house_dict["sales"] = sale_house_dict

    return house_dict

