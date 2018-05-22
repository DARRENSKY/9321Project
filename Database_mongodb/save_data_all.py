import xlrd


def save_data_all(i):
    rentname = "rent_data.xls"
    salename = "sales_data.xls"
    data_sales = xlrd.open_workbook(salename)

    sale_all = data_sales.sheets()[1]

    data_rent = xlrd.open_workbook(rentname)

    rent_all_all = data_rent.sheets()[1]
    rent_all_one = data_rent.sheets()[2]
    rent_all_two = data_rent.sheets()[3]
    rent_all_three = data_rent.sheets()[4]
    rent_all_four = data_rent.sheets()[5]

    rent_all_all_dict = {}
    rent_all_one_dict = {}
    rent_all_two_dict = {}
    rent_all_three_dict = {}
    rent_all_four_dict = {}

    sale_all_dict = {}

    if i >= 4 and i < 15:
        rent_all_all_line = rent_all_all.row_values(i)
        index = 0
        for j in rent_all_all_line:
            if j == "-":
                rent_all_all_line[index] = rent_all_all.row_values(3)[index]
            index += 1

        rent_all_all_dict["rent_all_all_mar05"] = rent_all_all_line[121]
        rent_all_all_dict["rent_all_all_jun05"] = rent_all_all_line[121 + 2]
        rent_all_all_dict["rent_all_all_sep05"] = rent_all_all_line[121 + 4]
        rent_all_all_dict["rent_all_all_dec05"] = rent_all_all_line[121 + 6]

        rent_all_all_dict["rent_all_all_mar06"] = rent_all_all_line[121 + 8]
        rent_all_all_dict["rent_all_all_jun06"] = rent_all_all_line[121 + 10]
        rent_all_all_dict["rent_all_all_sep06"] = rent_all_all_line[121 + 12]
        rent_all_all_dict["rent_all_all_dec06"] = rent_all_all_line[121 + 14]

        rent_all_all_dict["rent_all_all_mar07"] = rent_all_all_line[121 + 16]
        rent_all_all_dict["rent_all_all_jun07"] = rent_all_all_line[121 + 18]
        rent_all_all_dict["rent_all_all_sep07"] = rent_all_all_line[121 + 20]
        rent_all_all_dict["rent_all_all_dec07"] = rent_all_all_line[121 + 22]

        rent_all_all_dict["rent_all_all_mar08"] = rent_all_all_line[121 + 24]
        rent_all_all_dict["rent_all_all_jun08"] = rent_all_all_line[121 + 26]
        rent_all_all_dict["rent_all_all_sep08"] = rent_all_all_line[121 + 28]
        rent_all_all_dict["rent_all_all_dec08"] = rent_all_all_line[121 + 30]

        rent_all_all_dict["rent_all_all_mar09"] = rent_all_all_line[121 + 32]
        rent_all_all_dict["rent_all_all_jun09"] = rent_all_all_line[121 + 34]
        rent_all_all_dict["rent_all_all_sep09"] = rent_all_all_line[121 + 36]
        rent_all_all_dict["rent_all_all_dec09"] = rent_all_all_line[121 + 38]

        rent_all_all_dict["rent_all_all_mar10"] = rent_all_all_line[121 + 40]
        rent_all_all_dict["rent_all_all_jun10"] = rent_all_all_line[121 + 42]
        rent_all_all_dict["rent_all_all_sep10"] = rent_all_all_line[121 + 44]
        rent_all_all_dict["rent_all_all_dec10"] = rent_all_all_line[121 + 46]

        rent_all_all_dict["rent_all_all_mar11"] = rent_all_all_line[121 + 48]
        rent_all_all_dict["rent_all_all_jun11"] = rent_all_all_line[121 + 50]
        rent_all_all_dict["rent_all_all_sep11"] = rent_all_all_line[121 + 52]
        rent_all_all_dict["rent_all_all_dec11"] = rent_all_all_line[121 + 54]

        rent_all_all_dict["rent_all_all_mar12"] = rent_all_all_line[121 + 56]
        rent_all_all_dict["rent_all_all_jun12"] = rent_all_all_line[121 + 58]
        rent_all_all_dict["rent_all_all_sep12"] = rent_all_all_line[121 + 60]
        rent_all_all_dict["rent_all_all_dec12"] = rent_all_all_line[121 + 62]

        rent_all_all_dict["rent_all_all_mar13"] = rent_all_all_line[121 + 64]
        rent_all_all_dict["rent_all_all_jun13"] = rent_all_all_line[121 + 66]
        rent_all_all_dict["rent_all_all_sep13"] = rent_all_all_line[121 + 68]
        rent_all_all_dict["rent_all_all_dec13"] = rent_all_all_line[121 + 70]

        rent_all_all_dict["rent_all_all_mar14"] = rent_all_all_line[121 + 72]
        rent_all_all_dict["rent_all_all_jun14"] = rent_all_all_line[121 + 74]
        rent_all_all_dict["rent_all_all_sep14"] = rent_all_all_line[121 + 76]
        rent_all_all_dict["rent_all_all_dec14"] = rent_all_all_line[121 + 78]

        rent_all_all_dict["rent_all_all_mar15"] = rent_all_all_line[121 + 80]
        rent_all_all_dict["rent_all_all_jun15"] = rent_all_all_line[121 + 82]
        rent_all_all_dict["rent_all_all_sep15"] = rent_all_all_line[121 + 84]
        rent_all_all_dict["rent_all_all_dec15"] = rent_all_all_line[121 + 86]

        rent_all_all_dict["rent_all_all_mar16"] = rent_all_all_line[121 + 88]
        rent_all_all_dict["rent_all_all_jun16"] = rent_all_all_line[121 + 91]
        rent_all_all_dict["rent_all_all_sep16"] = rent_all_all_line[121 + 93]
        rent_all_all_dict["rent_all_all_dec16"] = rent_all_all_line[121 + 95]

        rent_all_one_line = rent_all_one.row_values(i)
        index = 0
        for j in rent_all_one_line:
            if j == "-":
                rent_all_one_line[index] = rent_all_one.row_values(3)[index]
            index += 1

        rent_all_one_dict["rent_all_one_mar05"] = rent_all_one_line[121]
        rent_all_one_dict["rent_all_one_jun05"] = rent_all_one_line[121 + 2]
        rent_all_one_dict["rent_all_one_sep05"] = rent_all_one_line[121 + 4]
        rent_all_one_dict["rent_all_one_dec05"] = rent_all_one_line[121 + 6]

        rent_all_one_dict["rent_all_one_mar06"] = rent_all_one_line[121 + 8]
        rent_all_one_dict["rent_all_one_jun06"] = rent_all_one_line[121 + 10]
        rent_all_one_dict["rent_all_one_sep06"] = rent_all_one_line[121 + 12]
        rent_all_one_dict["rent_all_one_dec06"] = rent_all_one_line[121 + 14]

        rent_all_one_dict["rent_all_one_mar07"] = rent_all_one_line[121 + 16]
        rent_all_one_dict["rent_all_one_jun07"] = rent_all_one_line[121 + 18]
        rent_all_one_dict["rent_all_one_sep07"] = rent_all_one_line[121 + 20]
        rent_all_one_dict["rent_all_one_dec07"] = rent_all_one_line[121 + 22]

        rent_all_one_dict["rent_all_one_mar08"] = rent_all_one_line[121 + 24]
        rent_all_one_dict["rent_all_one_jun08"] = rent_all_one_line[121 + 26]
        rent_all_one_dict["rent_all_one_sep08"] = rent_all_one_line[121 + 28]
        rent_all_one_dict["rent_all_one_dec08"] = rent_all_one_line[121 + 30]

        rent_all_one_dict["rent_all_one_mar09"] = rent_all_one_line[121 + 32]
        rent_all_one_dict["rent_all_one_jun09"] = rent_all_one_line[121 + 34]
        rent_all_one_dict["rent_all_one_sep09"] = rent_all_one_line[121 + 36]
        rent_all_one_dict["rent_all_one_dec09"] = rent_all_one_line[121 + 38]

        rent_all_one_dict["rent_all_one_mar10"] = rent_all_one_line[121 + 40]
        rent_all_one_dict["rent_all_one_jun10"] = rent_all_one_line[121 + 42]
        rent_all_one_dict["rent_all_one_sep10"] = rent_all_one_line[121 + 44]
        rent_all_one_dict["rent_all_one_dec10"] = rent_all_one_line[121 + 46]

        rent_all_one_dict["rent_all_one_mar11"] = rent_all_one_line[121 + 48]
        rent_all_one_dict["rent_all_one_jun11"] = rent_all_one_line[121 + 50]
        rent_all_one_dict["rent_all_one_sep11"] = rent_all_one_line[121 + 52]
        rent_all_one_dict["rent_all_one_dec11"] = rent_all_one_line[121 + 54]

        rent_all_one_dict["rent_all_one_mar12"] = rent_all_one_line[121 + 56]
        rent_all_one_dict["rent_all_one_jun12"] = rent_all_one_line[121 + 58]
        rent_all_one_dict["rent_all_one_sep12"] = rent_all_one_line[121 + 60]
        rent_all_one_dict["rent_all_one_dec12"] = rent_all_one_line[121 + 62]

        rent_all_one_dict["rent_all_one_mar13"] = rent_all_one_line[121 + 64]
        rent_all_one_dict["rent_all_one_jun13"] = rent_all_one_line[121 + 66]
        rent_all_one_dict["rent_all_one_sep13"] = rent_all_one_line[121 + 68]
        rent_all_one_dict["rent_all_one_dec13"] = rent_all_one_line[121 + 70]

        rent_all_one_dict["rent_all_one_mar14"] = rent_all_one_line[121 + 72]
        rent_all_one_dict["rent_all_one_jun14"] = rent_all_one_line[121 + 74]
        rent_all_one_dict["rent_all_one_sep14"] = rent_all_one_line[121 + 76]
        rent_all_one_dict["rent_all_one_dec14"] = rent_all_one_line[121 + 78]

        rent_all_one_dict["rent_all_one_mar15"] = rent_all_one_line[121 + 80]
        rent_all_one_dict["rent_all_one_jun15"] = rent_all_one_line[121 + 82]
        rent_all_one_dict["rent_all_one_sep15"] = rent_all_one_line[121 + 84]
        rent_all_one_dict["rent_all_one_dec15"] = rent_all_one_line[121 + 86]

        rent_all_one_dict["rent_all_one_mar16"] = rent_all_one_line[121 + 88]
        rent_all_one_dict["rent_all_one_jun16"] = rent_all_one_line[121 + 91]
        rent_all_one_dict["rent_all_one_sep16"] = rent_all_one_line[121 + 93]
        rent_all_one_dict["rent_all_one_dec16"] = rent_all_one_line[121 + 95]

        rent_all_two_line = rent_all_two.row_values(i)
        index = 0
        for j in rent_all_two_line:
            if j == "-":
                rent_all_two_line[index] = rent_all_two.row_values(3)[index]
            index += 1

        rent_all_two_dict["rent_all_two_mar05"] = rent_all_two_line[121]
        rent_all_two_dict["rent_all_two_jun05"] = rent_all_two_line[121 + 2]
        rent_all_two_dict["rent_all_two_sep05"] = rent_all_two_line[121 + 4]
        rent_all_two_dict["rent_all_two_dec05"] = rent_all_two_line[121 + 6]

        rent_all_two_dict["rent_all_two_mar06"] = rent_all_two_line[121 + 8]
        rent_all_two_dict["rent_all_two_jun06"] = rent_all_two_line[121 + 10]
        rent_all_two_dict["rent_all_two_sep06"] = rent_all_two_line[121 + 12]
        rent_all_two_dict["rent_all_two_dec06"] = rent_all_two_line[121 + 14]

        rent_all_two_dict["rent_all_two_mar07"] = rent_all_two_line[121 + 16]
        rent_all_two_dict["rent_all_two_jun07"] = rent_all_two_line[121 + 18]
        rent_all_two_dict["rent_all_two_sep07"] = rent_all_two_line[121 + 20]
        rent_all_two_dict["rent_all_two_dec07"] = rent_all_two_line[121 + 22]

        rent_all_two_dict["rent_all_two_mar08"] = rent_all_two_line[121 + 24]
        rent_all_two_dict["rent_all_two_jun08"] = rent_all_two_line[121 + 26]
        rent_all_two_dict["rent_all_two_sep08"] = rent_all_two_line[121 + 28]
        rent_all_two_dict["rent_all_two_dec08"] = rent_all_two_line[121 + 30]

        rent_all_two_dict["rent_all_two_mar09"] = rent_all_two_line[121 + 32]
        rent_all_two_dict["rent_all_two_jun09"] = rent_all_two_line[121 + 34]
        rent_all_two_dict["rent_all_two_sep09"] = rent_all_two_line[121 + 36]
        rent_all_two_dict["rent_all_two_dec09"] = rent_all_two_line[121 + 38]

        rent_all_two_dict["rent_all_two_mar10"] = rent_all_two_line[121 + 40]
        rent_all_two_dict["rent_all_two_jun10"] = rent_all_two_line[121 + 42]
        rent_all_two_dict["rent_all_two_sep10"] = rent_all_two_line[121 + 44]
        rent_all_two_dict["rent_all_two_dec10"] = rent_all_two_line[121 + 46]

        rent_all_two_dict["rent_all_two_mar11"] = rent_all_two_line[121 + 48]
        rent_all_two_dict["rent_all_two_jun11"] = rent_all_two_line[121 + 50]
        rent_all_two_dict["rent_all_two_sep11"] = rent_all_two_line[121 + 52]
        rent_all_two_dict["rent_all_two_dec11"] = rent_all_two_line[121 + 54]

        rent_all_two_dict["rent_all_two_mar12"] = rent_all_two_line[121 + 56]
        rent_all_two_dict["rent_all_two_jun12"] = rent_all_two_line[121 + 58]
        rent_all_two_dict["rent_all_two_sep12"] = rent_all_two_line[121 + 60]
        rent_all_two_dict["rent_all_two_dec12"] = rent_all_two_line[121 + 62]

        rent_all_two_dict["rent_all_two_mar13"] = rent_all_two_line[121 + 64]
        rent_all_two_dict["rent_all_two_jun13"] = rent_all_two_line[121 + 66]
        rent_all_two_dict["rent_all_two_sep13"] = rent_all_two_line[121 + 68]
        rent_all_two_dict["rent_all_two_dec13"] = rent_all_two_line[121 + 70]

        rent_all_two_dict["rent_all_two_mar14"] = rent_all_two_line[121 + 72]
        rent_all_two_dict["rent_all_two_jun14"] = rent_all_two_line[121 + 74]
        rent_all_two_dict["rent_all_two_sep14"] = rent_all_two_line[121 + 76]
        rent_all_two_dict["rent_all_two_dec14"] = rent_all_two_line[121 + 78]

        rent_all_two_dict["rent_all_two_mar15"] = rent_all_two_line[121 + 80]
        rent_all_two_dict["rent_all_two_jun15"] = rent_all_two_line[121 + 82]
        rent_all_two_dict["rent_all_two_sep15"] = rent_all_two_line[121 + 84]
        rent_all_two_dict["rent_all_two_dec15"] = rent_all_two_line[121 + 86]

        rent_all_two_dict["rent_all_two_mar16"] = rent_all_two_line[121 + 88]
        rent_all_two_dict["rent_all_two_jun16"] = rent_all_two_line[121 + 91]
        rent_all_two_dict["rent_all_two_sep16"] = rent_all_two_line[121 + 93]
        rent_all_two_dict["rent_all_two_dec16"] = rent_all_two_line[121 + 95]

        rent_all_three_line = rent_all_three.row_values(i)
        index = 0
        for j in rent_all_three_line:
            if j == "-":
                rent_all_three_line[index] = rent_all_three.row_values(3)[index]
            index += 1

        rent_all_three_dict["rent_all_three_mar05"] = rent_all_three_line[121]
        rent_all_three_dict["rent_all_three_jun05"] = rent_all_three_line[121 + 2]
        rent_all_three_dict["rent_all_three_sep05"] = rent_all_three_line[121 + 4]
        rent_all_three_dict["rent_all_three_dec05"] = rent_all_three_line[121 + 6]

        rent_all_three_dict["rent_all_three_mar06"] = rent_all_three_line[121 + 8]
        rent_all_three_dict["rent_all_three_jun06"] = rent_all_three_line[121 + 10]
        rent_all_three_dict["rent_all_three_sep06"] = rent_all_three_line[121 + 12]
        rent_all_three_dict["rent_all_three_dec06"] = rent_all_three_line[121 + 14]

        rent_all_three_dict["rent_all_three_mar07"] = rent_all_three_line[121 + 16]
        rent_all_three_dict["rent_all_three_jun07"] = rent_all_three_line[121 + 18]
        rent_all_three_dict["rent_all_three_sep07"] = rent_all_three_line[121 + 20]
        rent_all_three_dict["rent_all_three_dec07"] = rent_all_three_line[121 + 22]

        rent_all_three_dict["rent_all_three_mar08"] = rent_all_three_line[121 + 24]
        rent_all_three_dict["rent_all_three_jun08"] = rent_all_three_line[121 + 26]
        rent_all_three_dict["rent_all_three_sep08"] = rent_all_three_line[121 + 28]
        rent_all_three_dict["rent_all_three_dec08"] = rent_all_three_line[121 + 30]

        rent_all_three_dict["rent_all_three_mar09"] = rent_all_three_line[121 + 32]
        rent_all_three_dict["rent_all_three_jun09"] = rent_all_three_line[121 + 34]
        rent_all_three_dict["rent_all_three_sep09"] = rent_all_three_line[121 + 36]
        rent_all_three_dict["rent_all_three_dec09"] = rent_all_three_line[121 + 38]

        rent_all_three_dict["rent_all_three_mar10"] = rent_all_three_line[121 + 40]
        rent_all_three_dict["rent_all_three_jun10"] = rent_all_three_line[121 + 42]
        rent_all_three_dict["rent_all_three_sep10"] = rent_all_three_line[121 + 44]
        rent_all_three_dict["rent_all_three_dec10"] = rent_all_three_line[121 + 46]

        rent_all_three_dict["rent_all_three_mar11"] = rent_all_three_line[121 + 48]
        rent_all_three_dict["rent_all_three_jun11"] = rent_all_three_line[121 + 50]
        rent_all_three_dict["rent_all_three_sep11"] = rent_all_three_line[121 + 52]
        rent_all_three_dict["rent_all_three_dec11"] = rent_all_three_line[121 + 54]

        rent_all_three_dict["rent_all_three_mar12"] = rent_all_three_line[121 + 56]
        rent_all_three_dict["rent_all_three_jun12"] = rent_all_three_line[121 + 58]
        rent_all_three_dict["rent_all_three_sep12"] = rent_all_three_line[121 + 60]
        rent_all_three_dict["rent_all_three_dec12"] = rent_all_three_line[121 + 62]

        rent_all_three_dict["rent_all_three_mar13"] = rent_all_three_line[121 + 64]
        rent_all_three_dict["rent_all_three_jun13"] = rent_all_three_line[121 + 66]
        rent_all_three_dict["rent_all_three_sep13"] = rent_all_three_line[121 + 68]
        rent_all_three_dict["rent_all_three_dec13"] = rent_all_three_line[121 + 70]

        rent_all_three_dict["rent_all_three_mar14"] = rent_all_three_line[121 + 72]
        rent_all_three_dict["rent_all_three_jun14"] = rent_all_three_line[121 + 74]
        rent_all_three_dict["rent_all_three_sep14"] = rent_all_three_line[121 + 76]
        rent_all_three_dict["rent_all_three_dec14"] = rent_all_three_line[121 + 78]

        rent_all_three_dict["rent_all_three_mar15"] = rent_all_three_line[121 + 80]
        rent_all_three_dict["rent_all_three_jun15"] = rent_all_three_line[121 + 82]
        rent_all_three_dict["rent_all_three_sep15"] = rent_all_three_line[121 + 84]
        rent_all_three_dict["rent_all_three_dec15"] = rent_all_three_line[121 + 86]

        rent_all_three_dict["rent_all_three_mar16"] = rent_all_three_line[121 + 88]
        rent_all_three_dict["rent_all_three_jun16"] = rent_all_three_line[121 + 91]
        rent_all_three_dict["rent_all_three_sep16"] = rent_all_three_line[121 + 93]
        rent_all_three_dict["rent_all_three_dec16"] = rent_all_three_line[121 + 95]

        rent_all_four_line = rent_all_four.row_values(i)
        index = 0
        for j in rent_all_four_line:
            if j == "-":
                rent_all_four_line[index] = rent_all_four.row_values(3)[index]
            index += 1

        rent_all_four_dict["rent_all_four_mar05"] = rent_all_four_line[121]
        rent_all_four_dict["rent_all_four_jun05"] = rent_all_four_line[121 + 2]
        rent_all_four_dict["rent_all_four_sep05"] = rent_all_four_line[121 + 4]
        rent_all_four_dict["rent_all_four_dec05"] = rent_all_four_line[121 + 6]

        rent_all_four_dict["rent_all_four_mar06"] = rent_all_four_line[121 + 8]
        rent_all_four_dict["rent_all_four_jun06"] = rent_all_four_line[121 + 10]
        rent_all_four_dict["rent_all_four_sep06"] = rent_all_four_line[121 + 12]
        rent_all_four_dict["rent_all_four_dec06"] = rent_all_four_line[121 + 14]

        rent_all_four_dict["rent_all_four_mar07"] = rent_all_four_line[121 + 16]
        rent_all_four_dict["rent_all_four_jun07"] = rent_all_four_line[121 + 18]
        rent_all_four_dict["rent_all_four_sep07"] = rent_all_four_line[121 + 20]
        rent_all_four_dict["rent_all_four_dec07"] = rent_all_four_line[121 + 22]

        rent_all_four_dict["rent_all_four_mar08"] = rent_all_four_line[121 + 24]
        rent_all_four_dict["rent_all_four_jun08"] = rent_all_four_line[121 + 26]
        rent_all_four_dict["rent_all_four_sep08"] = rent_all_four_line[121 + 28]
        rent_all_four_dict["rent_all_four_dec08"] = rent_all_four_line[121 + 30]

        rent_all_four_dict["rent_all_four_mar09"] = rent_all_four_line[121 + 32]
        rent_all_four_dict["rent_all_four_jun09"] = rent_all_four_line[121 + 34]
        rent_all_four_dict["rent_all_four_sep09"] = rent_all_four_line[121 + 36]
        rent_all_four_dict["rent_all_four_dec09"] = rent_all_four_line[121 + 38]

        rent_all_four_dict["rent_all_four_mar10"] = rent_all_four_line[121 + 40]
        rent_all_four_dict["rent_all_four_jun10"] = rent_all_four_line[121 + 42]
        rent_all_four_dict["rent_all_four_sep10"] = rent_all_four_line[121 + 44]
        rent_all_four_dict["rent_all_four_dec10"] = rent_all_four_line[121 + 46]

        rent_all_four_dict["rent_all_four_mar11"] = rent_all_four_line[121 + 48]
        rent_all_four_dict["rent_all_four_jun11"] = rent_all_four_line[121 + 50]
        rent_all_four_dict["rent_all_four_sep11"] = rent_all_four_line[121 + 52]
        rent_all_four_dict["rent_all_four_dec11"] = rent_all_four_line[121 + 54]

        rent_all_four_dict["rent_all_four_mar12"] = rent_all_four_line[121 + 56]
        rent_all_four_dict["rent_all_four_jun12"] = rent_all_four_line[121 + 58]
        rent_all_four_dict["rent_all_four_sep12"] = rent_all_four_line[121 + 60]
        rent_all_four_dict["rent_all_four_dec12"] = rent_all_four_line[121 + 62]

        rent_all_four_dict["rent_all_four_mar13"] = rent_all_four_line[121 + 64]
        rent_all_four_dict["rent_all_four_jun13"] = rent_all_four_line[121 + 66]
        rent_all_four_dict["rent_all_four_sep13"] = rent_all_four_line[121 + 68]
        rent_all_four_dict["rent_all_four_dec13"] = rent_all_four_line[121 + 70]

        rent_all_four_dict["rent_all_four_mar14"] = rent_all_four_line[121 + 72]
        rent_all_four_dict["rent_all_four_jun14"] = rent_all_four_line[121 + 74]
        rent_all_four_dict["rent_all_four_sep14"] = rent_all_four_line[121 + 76]
        rent_all_four_dict["rent_all_four_dec14"] = rent_all_four_line[121 + 78]

        rent_all_four_dict["rent_all_four_mar15"] = rent_all_four_line[121 + 80]
        rent_all_four_dict["rent_all_four_jun15"] = rent_all_four_line[121 + 82]
        rent_all_four_dict["rent_all_four_sep15"] = rent_all_four_line[121 + 84]
        rent_all_four_dict["rent_all_four_dec15"] = rent_all_four_line[121 + 86]

        rent_all_four_dict["rent_all_four_mar16"] = rent_all_four_line[121 + 88]
        rent_all_four_dict["rent_all_four_jun16"] = rent_all_four_line[121 + 91]
        rent_all_four_dict["rent_all_four_sep16"] = rent_all_four_line[121 + 93]
        rent_all_four_dict["rent_all_four_dec16"] = rent_all_four_line[121 + 95]

        sale_all_line = sale_all.row_values(i + 2)
        index = 0
        for j in sale_all_line:
            if j == "-":
                sale_all_line[index] = sale_all.row_values(5)[index]
            index += 1
        sale_all_dict['sale_all_05'] = sale_all_line[115 + 0] + sale_all_line[115 + 2] + sale_all_line[
            115 + 4] + sale_all_line[115 + 6]
        sale_all_dict['sale_all_06'] = sale_all_line[115 + 8] + sale_all_line[115 + 10] + sale_all_line[
            115 + 12] + sale_all_line[115 + 14]
        sale_all_dict['sale_all_07'] = sale_all_line[115 + 16] + sale_all_line[115 + 18] + sale_all_line[
            115 + 20] + sale_all_line[115 + 22]
        sale_all_dict['sale_all_08'] = sale_all_line[115 + 24] + sale_all_line[115 + 26] + sale_all_line[
            115 + 28] + sale_all_line[115 + 30]
        sale_all_dict['sale_all_09'] = sale_all_line[115 + 32] + sale_all_line[115 + 34] + sale_all_line[
            115 + 36] + sale_all_line[115 + 38]
        sale_all_dict['sale_all_10'] = sale_all_line[115 + 40] + sale_all_line[115 + 42] + sale_all_line[
            115 + 44] + sale_all_line[115 + 46]
        sale_all_dict['sale_all_11'] = sale_all_line[115 + 48] + sale_all_line[115 + 50] + sale_all_line[
            115 + 52] + sale_all_line[115 + 54]
        sale_all_dict['sale_all_12'] = sale_all_line[115 + 56] + sale_all_line[115 + 58] + sale_all_line[
            115 + 60] + sale_all_line[115 + 62]
        sale_all_dict['sale_all_13'] = sale_all_line[115 + 64] + sale_all_line[115 + 66] + sale_all_line[
            115 + 68] + sale_all_line[115 + 70]
        sale_all_dict['sale_all_14'] = sale_all_line[115 + 72] + sale_all_line[115 + 74] + sale_all_line[
            115 + 76] + sale_all_line[115 + 78]
        sale_all_dict['sale_all_15'] = sale_all_line[115 + 80] + sale_all_line[115 + 82] + sale_all_line[
            115 + 84] + sale_all_line[115 + 86]
        sale_all_dict['sale_all_16'] = sale_all_line[115 + 88] + sale_all_line[115 + 90] + sale_all_line[
            115 + 92] + sale_all_line[115 + 94]

    if i >= 16 and i < 31:
        rent_all_all_line = rent_all_all.row_values(i)
        index = 0
        for j in rent_all_all_line:
            if j == "-":
                rent_all_all_line[index] = rent_all_all.row_values(3)[index]
            index += 1

        rent_all_all_dict["rent_all_all_mar05"] = rent_all_all_line[121]
        rent_all_all_dict["rent_all_all_jun05"] = rent_all_all_line[121 + 2]
        rent_all_all_dict["rent_all_all_sep05"] = rent_all_all_line[121 + 4]
        rent_all_all_dict["rent_all_all_dec05"] = rent_all_all_line[121 + 6]

        rent_all_all_dict["rent_all_all_mar06"] = rent_all_all_line[121 + 8]
        rent_all_all_dict["rent_all_all_jun06"] = rent_all_all_line[121 + 10]
        rent_all_all_dict["rent_all_all_sep06"] = rent_all_all_line[121 + 12]
        rent_all_all_dict["rent_all_all_dec06"] = rent_all_all_line[121 + 14]

        rent_all_all_dict["rent_all_all_mar07"] = rent_all_all_line[121 + 16]
        rent_all_all_dict["rent_all_all_jun07"] = rent_all_all_line[121 + 18]
        rent_all_all_dict["rent_all_all_sep07"] = rent_all_all_line[121 + 20]
        rent_all_all_dict["rent_all_all_dec07"] = rent_all_all_line[121 + 22]

        rent_all_all_dict["rent_all_all_mar08"] = rent_all_all_line[121 + 24]
        rent_all_all_dict["rent_all_all_jun08"] = rent_all_all_line[121 + 26]
        rent_all_all_dict["rent_all_all_sep08"] = rent_all_all_line[121 + 28]
        rent_all_all_dict["rent_all_all_dec08"] = rent_all_all_line[121 + 30]

        rent_all_all_dict["rent_all_all_mar09"] = rent_all_all_line[121 + 32]
        rent_all_all_dict["rent_all_all_jun09"] = rent_all_all_line[121 + 34]
        rent_all_all_dict["rent_all_all_sep09"] = rent_all_all_line[121 + 36]
        rent_all_all_dict["rent_all_all_dec09"] = rent_all_all_line[121 + 38]

        rent_all_all_dict["rent_all_all_mar10"] = rent_all_all_line[121 + 40]
        rent_all_all_dict["rent_all_all_jun10"] = rent_all_all_line[121 + 42]
        rent_all_all_dict["rent_all_all_sep10"] = rent_all_all_line[121 + 44]
        rent_all_all_dict["rent_all_all_dec10"] = rent_all_all_line[121 + 46]

        rent_all_all_dict["rent_all_all_mar11"] = rent_all_all_line[121 + 48]
        rent_all_all_dict["rent_all_all_jun11"] = rent_all_all_line[121 + 50]
        rent_all_all_dict["rent_all_all_sep11"] = rent_all_all_line[121 + 52]
        rent_all_all_dict["rent_all_all_dec11"] = rent_all_all_line[121 + 54]

        rent_all_all_dict["rent_all_all_mar12"] = rent_all_all_line[121 + 56]
        rent_all_all_dict["rent_all_all_jun12"] = rent_all_all_line[121 + 58]
        rent_all_all_dict["rent_all_all_sep12"] = rent_all_all_line[121 + 60]
        rent_all_all_dict["rent_all_all_dec12"] = rent_all_all_line[121 + 62]

        rent_all_all_dict["rent_all_all_mar13"] = rent_all_all_line[121 + 64]
        rent_all_all_dict["rent_all_all_jun13"] = rent_all_all_line[121 + 66]
        rent_all_all_dict["rent_all_all_sep13"] = rent_all_all_line[121 + 68]
        rent_all_all_dict["rent_all_all_dec13"] = rent_all_all_line[121 + 70]

        rent_all_all_dict["rent_all_all_mar14"] = rent_all_all_line[121 + 72]
        rent_all_all_dict["rent_all_all_jun14"] = rent_all_all_line[121 + 74]
        rent_all_all_dict["rent_all_all_sep14"] = rent_all_all_line[121 + 76]
        rent_all_all_dict["rent_all_all_dec14"] = rent_all_all_line[121 + 78]

        rent_all_all_dict["rent_all_all_mar15"] = rent_all_all_line[121 + 80]
        rent_all_all_dict["rent_all_all_jun15"] = rent_all_all_line[121 + 82]
        rent_all_all_dict["rent_all_all_sep15"] = rent_all_all_line[121 + 84]
        rent_all_all_dict["rent_all_all_dec15"] = rent_all_all_line[121 + 86]

        rent_all_all_dict["rent_all_all_mar16"] = rent_all_all_line[121 + 88]
        rent_all_all_dict["rent_all_all_jun16"] = rent_all_all_line[121 + 91]
        rent_all_all_dict["rent_all_all_sep16"] = rent_all_all_line[121 + 93]
        rent_all_all_dict["rent_all_all_dec16"] = rent_all_all_line[121 + 95]

        rent_all_one_line = rent_all_one.row_values(i)
        index = 0
        for j in rent_all_one_line:
            if j == "-":
                rent_all_one_line[index] = rent_all_one.row_values(3)[index]
            index += 1

        rent_all_one_dict["rent_all_one_mar05"] = rent_all_one_line[121]
        rent_all_one_dict["rent_all_one_jun05"] = rent_all_one_line[121 + 2]
        rent_all_one_dict["rent_all_one_sep05"] = rent_all_one_line[121 + 4]
        rent_all_one_dict["rent_all_one_dec05"] = rent_all_one_line[121 + 6]

        rent_all_one_dict["rent_all_one_mar06"] = rent_all_one_line[121 + 8]
        rent_all_one_dict["rent_all_one_jun06"] = rent_all_one_line[121 + 10]
        rent_all_one_dict["rent_all_one_sep06"] = rent_all_one_line[121 + 12]
        rent_all_one_dict["rent_all_one_dec06"] = rent_all_one_line[121 + 14]

        rent_all_one_dict["rent_all_one_mar07"] = rent_all_one_line[121 + 16]
        rent_all_one_dict["rent_all_one_jun07"] = rent_all_one_line[121 + 18]
        rent_all_one_dict["rent_all_one_sep07"] = rent_all_one_line[121 + 20]
        rent_all_one_dict["rent_all_one_dec07"] = rent_all_one_line[121 + 22]

        rent_all_one_dict["rent_all_one_mar08"] = rent_all_one_line[121 + 24]
        rent_all_one_dict["rent_all_one_jun08"] = rent_all_one_line[121 + 26]
        rent_all_one_dict["rent_all_one_sep08"] = rent_all_one_line[121 + 28]
        rent_all_one_dict["rent_all_one_dec08"] = rent_all_one_line[121 + 30]

        rent_all_one_dict["rent_all_one_mar09"] = rent_all_one_line[121 + 32]
        rent_all_one_dict["rent_all_one_jun09"] = rent_all_one_line[121 + 34]
        rent_all_one_dict["rent_all_one_sep09"] = rent_all_one_line[121 + 36]
        rent_all_one_dict["rent_all_one_dec09"] = rent_all_one_line[121 + 38]

        rent_all_one_dict["rent_all_one_mar10"] = rent_all_one_line[121 + 40]
        rent_all_one_dict["rent_all_one_jun10"] = rent_all_one_line[121 + 42]
        rent_all_one_dict["rent_all_one_sep10"] = rent_all_one_line[121 + 44]
        rent_all_one_dict["rent_all_one_dec10"] = rent_all_one_line[121 + 46]

        rent_all_one_dict["rent_all_one_mar11"] = rent_all_one_line[121 + 48]
        rent_all_one_dict["rent_all_one_jun11"] = rent_all_one_line[121 + 50]
        rent_all_one_dict["rent_all_one_sep11"] = rent_all_one_line[121 + 52]
        rent_all_one_dict["rent_all_one_dec11"] = rent_all_one_line[121 + 54]

        rent_all_one_dict["rent_all_one_mar12"] = rent_all_one_line[121 + 56]
        rent_all_one_dict["rent_all_one_jun12"] = rent_all_one_line[121 + 58]
        rent_all_one_dict["rent_all_one_sep12"] = rent_all_one_line[121 + 60]
        rent_all_one_dict["rent_all_one_dec12"] = rent_all_one_line[121 + 62]

        rent_all_one_dict["rent_all_one_mar13"] = rent_all_one_line[121 + 64]
        rent_all_one_dict["rent_all_one_jun13"] = rent_all_one_line[121 + 66]
        rent_all_one_dict["rent_all_one_sep13"] = rent_all_one_line[121 + 68]
        rent_all_one_dict["rent_all_one_dec13"] = rent_all_one_line[121 + 70]

        rent_all_one_dict["rent_all_one_mar14"] = rent_all_one_line[121 + 72]
        rent_all_one_dict["rent_all_one_jun14"] = rent_all_one_line[121 + 74]
        rent_all_one_dict["rent_all_one_sep14"] = rent_all_one_line[121 + 76]
        rent_all_one_dict["rent_all_one_dec14"] = rent_all_one_line[121 + 78]

        rent_all_one_dict["rent_all_one_mar15"] = rent_all_one_line[121 + 80]
        rent_all_one_dict["rent_all_one_jun15"] = rent_all_one_line[121 + 82]
        rent_all_one_dict["rent_all_one_sep15"] = rent_all_one_line[121 + 84]
        rent_all_one_dict["rent_all_one_dec15"] = rent_all_one_line[121 + 86]

        rent_all_one_dict["rent_all_one_mar16"] = rent_all_one_line[121 + 88]
        rent_all_one_dict["rent_all_one_jun16"] = rent_all_one_line[121 + 91]
        rent_all_one_dict["rent_all_one_sep16"] = rent_all_one_line[121 + 93]
        rent_all_one_dict["rent_all_one_dec16"] = rent_all_one_line[121 + 95]

        rent_all_two_line = rent_all_two.row_values(i)
        index = 0
        for j in rent_all_two_line:
            if j == "-":
                rent_all_two_line[index] = rent_all_two.row_values(3)[index]
            index += 1

        rent_all_two_dict["rent_all_two_mar05"] = rent_all_two_line[121]
        rent_all_two_dict["rent_all_two_jun05"] = rent_all_two_line[121 + 2]
        rent_all_two_dict["rent_all_two_sep05"] = rent_all_two_line[121 + 4]
        rent_all_two_dict["rent_all_two_dec05"] = rent_all_two_line[121 + 6]

        rent_all_two_dict["rent_all_two_mar06"] = rent_all_two_line[121 + 8]
        rent_all_two_dict["rent_all_two_jun06"] = rent_all_two_line[121 + 10]
        rent_all_two_dict["rent_all_two_sep06"] = rent_all_two_line[121 + 12]
        rent_all_two_dict["rent_all_two_dec06"] = rent_all_two_line[121 + 14]

        rent_all_two_dict["rent_all_two_mar07"] = rent_all_two_line[121 + 16]
        rent_all_two_dict["rent_all_two_jun07"] = rent_all_two_line[121 + 18]
        rent_all_two_dict["rent_all_two_sep07"] = rent_all_two_line[121 + 20]
        rent_all_two_dict["rent_all_two_dec07"] = rent_all_two_line[121 + 22]

        rent_all_two_dict["rent_all_two_mar08"] = rent_all_two_line[121 + 24]
        rent_all_two_dict["rent_all_two_jun08"] = rent_all_two_line[121 + 26]
        rent_all_two_dict["rent_all_two_sep08"] = rent_all_two_line[121 + 28]
        rent_all_two_dict["rent_all_two_dec08"] = rent_all_two_line[121 + 30]

        rent_all_two_dict["rent_all_two_mar09"] = rent_all_two_line[121 + 32]
        rent_all_two_dict["rent_all_two_jun09"] = rent_all_two_line[121 + 34]
        rent_all_two_dict["rent_all_two_sep09"] = rent_all_two_line[121 + 36]
        rent_all_two_dict["rent_all_two_dec09"] = rent_all_two_line[121 + 38]

        rent_all_two_dict["rent_all_two_mar10"] = rent_all_two_line[121 + 40]
        rent_all_two_dict["rent_all_two_jun10"] = rent_all_two_line[121 + 42]
        rent_all_two_dict["rent_all_two_sep10"] = rent_all_two_line[121 + 44]
        rent_all_two_dict["rent_all_two_dec10"] = rent_all_two_line[121 + 46]

        rent_all_two_dict["rent_all_two_mar11"] = rent_all_two_line[121 + 48]
        rent_all_two_dict["rent_all_two_jun11"] = rent_all_two_line[121 + 50]
        rent_all_two_dict["rent_all_two_sep11"] = rent_all_two_line[121 + 52]
        rent_all_two_dict["rent_all_two_dec11"] = rent_all_two_line[121 + 54]

        rent_all_two_dict["rent_all_two_mar12"] = rent_all_two_line[121 + 56]
        rent_all_two_dict["rent_all_two_jun12"] = rent_all_two_line[121 + 58]
        rent_all_two_dict["rent_all_two_sep12"] = rent_all_two_line[121 + 60]
        rent_all_two_dict["rent_all_two_dec12"] = rent_all_two_line[121 + 62]

        rent_all_two_dict["rent_all_two_mar13"] = rent_all_two_line[121 + 64]
        rent_all_two_dict["rent_all_two_jun13"] = rent_all_two_line[121 + 66]
        rent_all_two_dict["rent_all_two_sep13"] = rent_all_two_line[121 + 68]
        rent_all_two_dict["rent_all_two_dec13"] = rent_all_two_line[121 + 70]

        rent_all_two_dict["rent_all_two_mar14"] = rent_all_two_line[121 + 72]
        rent_all_two_dict["rent_all_two_jun14"] = rent_all_two_line[121 + 74]
        rent_all_two_dict["rent_all_two_sep14"] = rent_all_two_line[121 + 76]
        rent_all_two_dict["rent_all_two_dec14"] = rent_all_two_line[121 + 78]

        rent_all_two_dict["rent_all_two_mar15"] = rent_all_two_line[121 + 80]
        rent_all_two_dict["rent_all_two_jun15"] = rent_all_two_line[121 + 82]
        rent_all_two_dict["rent_all_two_sep15"] = rent_all_two_line[121 + 84]
        rent_all_two_dict["rent_all_two_dec15"] = rent_all_two_line[121 + 86]

        rent_all_two_dict["rent_all_two_mar16"] = rent_all_two_line[121 + 88]
        rent_all_two_dict["rent_all_two_jun16"] = rent_all_two_line[121 + 91]
        rent_all_two_dict["rent_all_two_sep16"] = rent_all_two_line[121 + 93]
        rent_all_two_dict["rent_all_two_dec16"] = rent_all_two_line[121 + 95]

        rent_all_three_line = rent_all_three.row_values(i)
        index = 0
        for j in rent_all_three_line:
            if j == "-":
                rent_all_three_line[index] = rent_all_three.row_values(3)[index]
            index += 1

        rent_all_three_dict["rent_all_three_mar05"] = rent_all_three_line[121]
        rent_all_three_dict["rent_all_three_jun05"] = rent_all_three_line[121 + 2]
        rent_all_three_dict["rent_all_three_sep05"] = rent_all_three_line[121 + 4]
        rent_all_three_dict["rent_all_three_dec05"] = rent_all_three_line[121 + 6]

        rent_all_three_dict["rent_all_three_mar06"] = rent_all_three_line[121 + 8]
        rent_all_three_dict["rent_all_three_jun06"] = rent_all_three_line[121 + 10]
        rent_all_three_dict["rent_all_three_sep06"] = rent_all_three_line[121 + 12]
        rent_all_three_dict["rent_all_three_dec06"] = rent_all_three_line[121 + 14]

        rent_all_three_dict["rent_all_three_mar07"] = rent_all_three_line[121 + 16]
        rent_all_three_dict["rent_all_three_jun07"] = rent_all_three_line[121 + 18]
        rent_all_three_dict["rent_all_three_sep07"] = rent_all_three_line[121 + 20]
        rent_all_three_dict["rent_all_three_dec07"] = rent_all_three_line[121 + 22]

        rent_all_three_dict["rent_all_three_mar08"] = rent_all_three_line[121 + 24]
        rent_all_three_dict["rent_all_three_jun08"] = rent_all_three_line[121 + 26]
        rent_all_three_dict["rent_all_three_sep08"] = rent_all_three_line[121 + 28]
        rent_all_three_dict["rent_all_three_dec08"] = rent_all_three_line[121 + 30]

        rent_all_three_dict["rent_all_three_mar09"] = rent_all_three_line[121 + 32]
        rent_all_three_dict["rent_all_three_jun09"] = rent_all_three_line[121 + 34]
        rent_all_three_dict["rent_all_three_sep09"] = rent_all_three_line[121 + 36]
        rent_all_three_dict["rent_all_three_dec09"] = rent_all_three_line[121 + 38]

        rent_all_three_dict["rent_all_three_mar10"] = rent_all_three_line[121 + 40]
        rent_all_three_dict["rent_all_three_jun10"] = rent_all_three_line[121 + 42]
        rent_all_three_dict["rent_all_three_sep10"] = rent_all_three_line[121 + 44]
        rent_all_three_dict["rent_all_three_dec10"] = rent_all_three_line[121 + 46]

        rent_all_three_dict["rent_all_three_mar11"] = rent_all_three_line[121 + 48]
        rent_all_three_dict["rent_all_three_jun11"] = rent_all_three_line[121 + 50]
        rent_all_three_dict["rent_all_three_sep11"] = rent_all_three_line[121 + 52]
        rent_all_three_dict["rent_all_three_dec11"] = rent_all_three_line[121 + 54]

        rent_all_three_dict["rent_all_three_mar12"] = rent_all_three_line[121 + 56]
        rent_all_three_dict["rent_all_three_jun12"] = rent_all_three_line[121 + 58]
        rent_all_three_dict["rent_all_three_sep12"] = rent_all_three_line[121 + 60]
        rent_all_three_dict["rent_all_three_dec12"] = rent_all_three_line[121 + 62]

        rent_all_three_dict["rent_all_three_mar13"] = rent_all_three_line[121 + 64]
        rent_all_three_dict["rent_all_three_jun13"] = rent_all_three_line[121 + 66]
        rent_all_three_dict["rent_all_three_sep13"] = rent_all_three_line[121 + 68]
        rent_all_three_dict["rent_all_three_dec13"] = rent_all_three_line[121 + 70]

        rent_all_three_dict["rent_all_three_mar14"] = rent_all_three_line[121 + 72]
        rent_all_three_dict["rent_all_three_jun14"] = rent_all_three_line[121 + 74]
        rent_all_three_dict["rent_all_three_sep14"] = rent_all_three_line[121 + 76]
        rent_all_three_dict["rent_all_three_dec14"] = rent_all_three_line[121 + 78]

        rent_all_three_dict["rent_all_three_mar15"] = rent_all_three_line[121 + 80]
        rent_all_three_dict["rent_all_three_jun15"] = rent_all_three_line[121 + 82]
        rent_all_three_dict["rent_all_three_sep15"] = rent_all_three_line[121 + 84]
        rent_all_three_dict["rent_all_three_dec15"] = rent_all_three_line[121 + 86]

        rent_all_three_dict["rent_all_three_mar16"] = rent_all_three_line[121 + 88]
        rent_all_three_dict["rent_all_three_jun16"] = rent_all_three_line[121 + 91]
        rent_all_three_dict["rent_all_three_sep16"] = rent_all_three_line[121 + 93]
        rent_all_three_dict["rent_all_three_dec16"] = rent_all_three_line[121 + 95]

        rent_all_four_line = rent_all_four.row_values(i)
        index = 0
        for j in rent_all_four_line:
            if j == "-":
                rent_all_four_line[index] = rent_all_four.row_values(3)[index]
            index += 1

        rent_all_four_dict["rent_all_four_mar05"] = rent_all_four_line[121]
        rent_all_four_dict["rent_all_four_jun05"] = rent_all_four_line[121 + 2]
        rent_all_four_dict["rent_all_four_sep05"] = rent_all_four_line[121 + 4]
        rent_all_four_dict["rent_all_four_dec05"] = rent_all_four_line[121 + 6]

        rent_all_four_dict["rent_all_four_mar06"] = rent_all_four_line[121 + 8]
        rent_all_four_dict["rent_all_four_jun06"] = rent_all_four_line[121 + 10]
        rent_all_four_dict["rent_all_four_sep06"] = rent_all_four_line[121 + 12]
        rent_all_four_dict["rent_all_four_dec06"] = rent_all_four_line[121 + 14]

        rent_all_four_dict["rent_all_four_mar07"] = rent_all_four_line[121 + 16]
        rent_all_four_dict["rent_all_four_jun07"] = rent_all_four_line[121 + 18]
        rent_all_four_dict["rent_all_four_sep07"] = rent_all_four_line[121 + 20]
        rent_all_four_dict["rent_all_four_dec07"] = rent_all_four_line[121 + 22]

        rent_all_four_dict["rent_all_four_mar08"] = rent_all_four_line[121 + 24]
        rent_all_four_dict["rent_all_four_jun08"] = rent_all_four_line[121 + 26]
        rent_all_four_dict["rent_all_four_sep08"] = rent_all_four_line[121 + 28]
        rent_all_four_dict["rent_all_four_dec08"] = rent_all_four_line[121 + 30]

        rent_all_four_dict["rent_all_four_mar09"] = rent_all_four_line[121 + 32]
        rent_all_four_dict["rent_all_four_jun09"] = rent_all_four_line[121 + 34]
        rent_all_four_dict["rent_all_four_sep09"] = rent_all_four_line[121 + 36]
        rent_all_four_dict["rent_all_four_dec09"] = rent_all_four_line[121 + 38]

        rent_all_four_dict["rent_all_four_mar10"] = rent_all_four_line[121 + 40]
        rent_all_four_dict["rent_all_four_jun10"] = rent_all_four_line[121 + 42]
        rent_all_four_dict["rent_all_four_sep10"] = rent_all_four_line[121 + 44]
        rent_all_four_dict["rent_all_four_dec10"] = rent_all_four_line[121 + 46]

        rent_all_four_dict["rent_all_four_mar11"] = rent_all_four_line[121 + 48]
        rent_all_four_dict["rent_all_four_jun11"] = rent_all_four_line[121 + 50]
        rent_all_four_dict["rent_all_four_sep11"] = rent_all_four_line[121 + 52]
        rent_all_four_dict["rent_all_four_dec11"] = rent_all_four_line[121 + 54]

        rent_all_four_dict["rent_all_four_mar12"] = rent_all_four_line[121 + 56]
        rent_all_four_dict["rent_all_four_jun12"] = rent_all_four_line[121 + 58]
        rent_all_four_dict["rent_all_four_sep12"] = rent_all_four_line[121 + 60]
        rent_all_four_dict["rent_all_four_dec12"] = rent_all_four_line[121 + 62]

        rent_all_four_dict["rent_all_four_mar13"] = rent_all_four_line[121 + 64]
        rent_all_four_dict["rent_all_four_jun13"] = rent_all_four_line[121 + 66]
        rent_all_four_dict["rent_all_four_sep13"] = rent_all_four_line[121 + 68]
        rent_all_four_dict["rent_all_four_dec13"] = rent_all_four_line[121 + 70]

        rent_all_four_dict["rent_all_four_mar14"] = rent_all_four_line[121 + 72]
        rent_all_four_dict["rent_all_four_jun14"] = rent_all_four_line[121 + 74]
        rent_all_four_dict["rent_all_four_sep14"] = rent_all_four_line[121 + 76]
        rent_all_four_dict["rent_all_four_dec14"] = rent_all_four_line[121 + 78]

        rent_all_four_dict["rent_all_four_mar15"] = rent_all_four_line[121 + 80]
        rent_all_four_dict["rent_all_four_jun15"] = rent_all_four_line[121 + 82]
        rent_all_four_dict["rent_all_four_sep15"] = rent_all_four_line[121 + 84]
        rent_all_four_dict["rent_all_four_dec15"] = rent_all_four_line[121 + 86]

        rent_all_four_dict["rent_all_four_mar16"] = rent_all_four_line[121 + 88]
        rent_all_four_dict["rent_all_four_jun16"] = rent_all_four_line[121 + 91]
        rent_all_four_dict["rent_all_four_sep16"] = rent_all_four_line[121 + 93]
        rent_all_four_dict["rent_all_four_dec16"] = rent_all_four_line[121 + 95]

        sale_all_line = sale_all.row_values(i + 2)
        index = 0
        for j in sale_all_line:
            if j == "-":
                sale_all_line[index] = sale_all.row_values(5)[index]
            index += 1
        sale_all_dict['sale_all_05'] = sale_all_line[115 + 0] + sale_all_line[115 + 2] + sale_all_line[
            115 + 4] + sale_all_line[115 + 6]
        sale_all_dict['sale_all_06'] = sale_all_line[115 + 8] + sale_all_line[115 + 10] + sale_all_line[
            115 + 12] + sale_all_line[115 + 14]
        sale_all_dict['sale_all_07'] = sale_all_line[115 + 16] + sale_all_line[115 + 18] + sale_all_line[
            115 + 20] + sale_all_line[115 + 22]
        sale_all_dict['sale_all_08'] = sale_all_line[115 + 24] + sale_all_line[115 + 26] + sale_all_line[
            115 + 28] + sale_all_line[115 + 30]
        sale_all_dict['sale_all_09'] = sale_all_line[115 + 32] + sale_all_line[115 + 34] + sale_all_line[
            115 + 36] + sale_all_line[115 + 38]
        sale_all_dict['sale_all_10'] = sale_all_line[115 + 40] + sale_all_line[115 + 42] + sale_all_line[
            115 + 44] + sale_all_line[115 + 46]
        sale_all_dict['sale_all_11'] = sale_all_line[115 + 48] + sale_all_line[115 + 50] + sale_all_line[
            115 + 52] + sale_all_line[115 + 54]
        sale_all_dict['sale_all_12'] = sale_all_line[115 + 56] + sale_all_line[115 + 58] + sale_all_line[
            115 + 60] + sale_all_line[115 + 62]
        sale_all_dict['sale_all_13'] = sale_all_line[115 + 64] + sale_all_line[115 + 66] + sale_all_line[
            115 + 68] + sale_all_line[115 + 70]
        sale_all_dict['sale_all_14'] = sale_all_line[115 + 72] + sale_all_line[115 + 74] + sale_all_line[
            115 + 76] + sale_all_line[115 + 78]
        sale_all_dict['sale_all_15'] = sale_all_line[115 + 80] + sale_all_line[115 + 82] + sale_all_line[
            115 + 84] + sale_all_line[115 + 86]
        sale_all_dict['sale_all_16'] = sale_all_line[115 + 88] + sale_all_line[115 + 90] + sale_all_line[
            115 + 92] + sale_all_line[115 + 94]

    if i >= 32 and i < 49:
        rent_all_all_line = rent_all_all.row_values(i)
        index = 0
        for j in rent_all_all_line:
            if j == "-":
                rent_all_all_line[index] = rent_all_all.row_values(3)[index]
            index += 1

        rent_all_all_dict["rent_all_all_mar05"] = rent_all_all_line[121]
        rent_all_all_dict["rent_all_all_jun05"] = rent_all_all_line[121 + 2]
        rent_all_all_dict["rent_all_all_sep05"] = rent_all_all_line[121 + 4]
        rent_all_all_dict["rent_all_all_dec05"] = rent_all_all_line[121 + 6]

        rent_all_all_dict["rent_all_all_mar06"] = rent_all_all_line[121 + 8]
        rent_all_all_dict["rent_all_all_jun06"] = rent_all_all_line[121 + 10]
        rent_all_all_dict["rent_all_all_sep06"] = rent_all_all_line[121 + 12]
        rent_all_all_dict["rent_all_all_dec06"] = rent_all_all_line[121 + 14]

        rent_all_all_dict["rent_all_all_mar07"] = rent_all_all_line[121 + 16]
        rent_all_all_dict["rent_all_all_jun07"] = rent_all_all_line[121 + 18]
        rent_all_all_dict["rent_all_all_sep07"] = rent_all_all_line[121 + 20]
        rent_all_all_dict["rent_all_all_dec07"] = rent_all_all_line[121 + 22]

        rent_all_all_dict["rent_all_all_mar08"] = rent_all_all_line[121 + 24]
        rent_all_all_dict["rent_all_all_jun08"] = rent_all_all_line[121 + 26]
        rent_all_all_dict["rent_all_all_sep08"] = rent_all_all_line[121 + 28]
        rent_all_all_dict["rent_all_all_dec08"] = rent_all_all_line[121 + 30]

        rent_all_all_dict["rent_all_all_mar09"] = rent_all_all_line[121 + 32]
        rent_all_all_dict["rent_all_all_jun09"] = rent_all_all_line[121 + 34]
        rent_all_all_dict["rent_all_all_sep09"] = rent_all_all_line[121 + 36]
        rent_all_all_dict["rent_all_all_dec09"] = rent_all_all_line[121 + 38]

        rent_all_all_dict["rent_all_all_mar10"] = rent_all_all_line[121 + 40]
        rent_all_all_dict["rent_all_all_jun10"] = rent_all_all_line[121 + 42]
        rent_all_all_dict["rent_all_all_sep10"] = rent_all_all_line[121 + 44]
        rent_all_all_dict["rent_all_all_dec10"] = rent_all_all_line[121 + 46]

        rent_all_all_dict["rent_all_all_mar11"] = rent_all_all_line[121 + 48]
        rent_all_all_dict["rent_all_all_jun11"] = rent_all_all_line[121 + 50]
        rent_all_all_dict["rent_all_all_sep11"] = rent_all_all_line[121 + 52]
        rent_all_all_dict["rent_all_all_dec11"] = rent_all_all_line[121 + 54]

        rent_all_all_dict["rent_all_all_mar12"] = rent_all_all_line[121 + 56]
        rent_all_all_dict["rent_all_all_jun12"] = rent_all_all_line[121 + 58]
        rent_all_all_dict["rent_all_all_sep12"] = rent_all_all_line[121 + 60]
        rent_all_all_dict["rent_all_all_dec12"] = rent_all_all_line[121 + 62]

        rent_all_all_dict["rent_all_all_mar13"] = rent_all_all_line[121 + 64]
        rent_all_all_dict["rent_all_all_jun13"] = rent_all_all_line[121 + 66]
        rent_all_all_dict["rent_all_all_sep13"] = rent_all_all_line[121 + 68]
        rent_all_all_dict["rent_all_all_dec13"] = rent_all_all_line[121 + 70]

        rent_all_all_dict["rent_all_all_mar14"] = rent_all_all_line[121 + 72]
        rent_all_all_dict["rent_all_all_jun14"] = rent_all_all_line[121 + 74]
        rent_all_all_dict["rent_all_all_sep14"] = rent_all_all_line[121 + 76]
        rent_all_all_dict["rent_all_all_dec14"] = rent_all_all_line[121 + 78]

        rent_all_all_dict["rent_all_all_mar15"] = rent_all_all_line[121 + 80]
        rent_all_all_dict["rent_all_all_jun15"] = rent_all_all_line[121 + 82]
        rent_all_all_dict["rent_all_all_sep15"] = rent_all_all_line[121 + 84]
        rent_all_all_dict["rent_all_all_dec15"] = rent_all_all_line[121 + 86]

        rent_all_all_dict["rent_all_all_mar16"] = rent_all_all_line[121 + 88]
        rent_all_all_dict["rent_all_all_jun16"] = rent_all_all_line[121 + 91]
        rent_all_all_dict["rent_all_all_sep16"] = rent_all_all_line[121 + 93]
        rent_all_all_dict["rent_all_all_dec16"] = rent_all_all_line[121 + 95]

        rent_all_one_line = rent_all_one.row_values(i)
        index = 0
        for j in rent_all_one_line:
            if j == "-":
                rent_all_one_line[index] = rent_all_one.row_values(3)[index]
            index += 1

        rent_all_one_dict["rent_all_one_mar05"] = rent_all_one_line[121]
        rent_all_one_dict["rent_all_one_jun05"] = rent_all_one_line[121 + 2]
        rent_all_one_dict["rent_all_one_sep05"] = rent_all_one_line[121 + 4]
        rent_all_one_dict["rent_all_one_dec05"] = rent_all_one_line[121 + 6]

        rent_all_one_dict["rent_all_one_mar06"] = rent_all_one_line[121 + 8]
        rent_all_one_dict["rent_all_one_jun06"] = rent_all_one_line[121 + 10]
        rent_all_one_dict["rent_all_one_sep06"] = rent_all_one_line[121 + 12]
        rent_all_one_dict["rent_all_one_dec06"] = rent_all_one_line[121 + 14]

        rent_all_one_dict["rent_all_one_mar07"] = rent_all_one_line[121 + 16]
        rent_all_one_dict["rent_all_one_jun07"] = rent_all_one_line[121 + 18]
        rent_all_one_dict["rent_all_one_sep07"] = rent_all_one_line[121 + 20]
        rent_all_one_dict["rent_all_one_dec07"] = rent_all_one_line[121 + 22]

        rent_all_one_dict["rent_all_one_mar08"] = rent_all_one_line[121 + 24]
        rent_all_one_dict["rent_all_one_jun08"] = rent_all_one_line[121 + 26]
        rent_all_one_dict["rent_all_one_sep08"] = rent_all_one_line[121 + 28]
        rent_all_one_dict["rent_all_one_dec08"] = rent_all_one_line[121 + 30]

        rent_all_one_dict["rent_all_one_mar09"] = rent_all_one_line[121 + 32]
        rent_all_one_dict["rent_all_one_jun09"] = rent_all_one_line[121 + 34]
        rent_all_one_dict["rent_all_one_sep09"] = rent_all_one_line[121 + 36]
        rent_all_one_dict["rent_all_one_dec09"] = rent_all_one_line[121 + 38]

        rent_all_one_dict["rent_all_one_mar10"] = rent_all_one_line[121 + 40]
        rent_all_one_dict["rent_all_one_jun10"] = rent_all_one_line[121 + 42]
        rent_all_one_dict["rent_all_one_sep10"] = rent_all_one_line[121 + 44]
        rent_all_one_dict["rent_all_one_dec10"] = rent_all_one_line[121 + 46]

        rent_all_one_dict["rent_all_one_mar11"] = rent_all_one_line[121 + 48]
        rent_all_one_dict["rent_all_one_jun11"] = rent_all_one_line[121 + 50]
        rent_all_one_dict["rent_all_one_sep11"] = rent_all_one_line[121 + 52]
        rent_all_one_dict["rent_all_one_dec11"] = rent_all_one_line[121 + 54]

        rent_all_one_dict["rent_all_one_mar12"] = rent_all_one_line[121 + 56]
        rent_all_one_dict["rent_all_one_jun12"] = rent_all_one_line[121 + 58]
        rent_all_one_dict["rent_all_one_sep12"] = rent_all_one_line[121 + 60]
        rent_all_one_dict["rent_all_one_dec12"] = rent_all_one_line[121 + 62]

        rent_all_one_dict["rent_all_one_mar13"] = rent_all_one_line[121 + 64]
        rent_all_one_dict["rent_all_one_jun13"] = rent_all_one_line[121 + 66]
        rent_all_one_dict["rent_all_one_sep13"] = rent_all_one_line[121 + 68]
        rent_all_one_dict["rent_all_one_dec13"] = rent_all_one_line[121 + 70]

        rent_all_one_dict["rent_all_one_mar14"] = rent_all_one_line[121 + 72]
        rent_all_one_dict["rent_all_one_jun14"] = rent_all_one_line[121 + 74]
        rent_all_one_dict["rent_all_one_sep14"] = rent_all_one_line[121 + 76]
        rent_all_one_dict["rent_all_one_dec14"] = rent_all_one_line[121 + 78]

        rent_all_one_dict["rent_all_one_mar15"] = rent_all_one_line[121 + 80]
        rent_all_one_dict["rent_all_one_jun15"] = rent_all_one_line[121 + 82]
        rent_all_one_dict["rent_all_one_sep15"] = rent_all_one_line[121 + 84]
        rent_all_one_dict["rent_all_one_dec15"] = rent_all_one_line[121 + 86]

        rent_all_one_dict["rent_all_one_mar16"] = rent_all_one_line[121 + 88]
        rent_all_one_dict["rent_all_one_jun16"] = rent_all_one_line[121 + 91]
        rent_all_one_dict["rent_all_one_sep16"] = rent_all_one_line[121 + 93]
        rent_all_one_dict["rent_all_one_dec16"] = rent_all_one_line[121 + 95]

        rent_all_two_line = rent_all_two.row_values(i)
        index = 0
        for j in rent_all_two_line:
            if j == "-":
                rent_all_two_line[index] = rent_all_two.row_values(3)[index]
            index += 1

        rent_all_two_dict["rent_all_two_mar05"] = rent_all_two_line[121]
        rent_all_two_dict["rent_all_two_jun05"] = rent_all_two_line[121 + 2]
        rent_all_two_dict["rent_all_two_sep05"] = rent_all_two_line[121 + 4]
        rent_all_two_dict["rent_all_two_dec05"] = rent_all_two_line[121 + 6]

        rent_all_two_dict["rent_all_two_mar06"] = rent_all_two_line[121 + 8]
        rent_all_two_dict["rent_all_two_jun06"] = rent_all_two_line[121 + 10]
        rent_all_two_dict["rent_all_two_sep06"] = rent_all_two_line[121 + 12]
        rent_all_two_dict["rent_all_two_dec06"] = rent_all_two_line[121 + 14]

        rent_all_two_dict["rent_all_two_mar07"] = rent_all_two_line[121 + 16]
        rent_all_two_dict["rent_all_two_jun07"] = rent_all_two_line[121 + 18]
        rent_all_two_dict["rent_all_two_sep07"] = rent_all_two_line[121 + 20]
        rent_all_two_dict["rent_all_two_dec07"] = rent_all_two_line[121 + 22]

        rent_all_two_dict["rent_all_two_mar08"] = rent_all_two_line[121 + 24]
        rent_all_two_dict["rent_all_two_jun08"] = rent_all_two_line[121 + 26]
        rent_all_two_dict["rent_all_two_sep08"] = rent_all_two_line[121 + 28]
        rent_all_two_dict["rent_all_two_dec08"] = rent_all_two_line[121 + 30]

        rent_all_two_dict["rent_all_two_mar09"] = rent_all_two_line[121 + 32]
        rent_all_two_dict["rent_all_two_jun09"] = rent_all_two_line[121 + 34]
        rent_all_two_dict["rent_all_two_sep09"] = rent_all_two_line[121 + 36]
        rent_all_two_dict["rent_all_two_dec09"] = rent_all_two_line[121 + 38]

        rent_all_two_dict["rent_all_two_mar10"] = rent_all_two_line[121 + 40]
        rent_all_two_dict["rent_all_two_jun10"] = rent_all_two_line[121 + 42]
        rent_all_two_dict["rent_all_two_sep10"] = rent_all_two_line[121 + 44]
        rent_all_two_dict["rent_all_two_dec10"] = rent_all_two_line[121 + 46]

        rent_all_two_dict["rent_all_two_mar11"] = rent_all_two_line[121 + 48]
        rent_all_two_dict["rent_all_two_jun11"] = rent_all_two_line[121 + 50]
        rent_all_two_dict["rent_all_two_sep11"] = rent_all_two_line[121 + 52]
        rent_all_two_dict["rent_all_two_dec11"] = rent_all_two_line[121 + 54]

        rent_all_two_dict["rent_all_two_mar12"] = rent_all_two_line[121 + 56]
        rent_all_two_dict["rent_all_two_jun12"] = rent_all_two_line[121 + 58]
        rent_all_two_dict["rent_all_two_sep12"] = rent_all_two_line[121 + 60]
        rent_all_two_dict["rent_all_two_dec12"] = rent_all_two_line[121 + 62]

        rent_all_two_dict["rent_all_two_mar13"] = rent_all_two_line[121 + 64]
        rent_all_two_dict["rent_all_two_jun13"] = rent_all_two_line[121 + 66]
        rent_all_two_dict["rent_all_two_sep13"] = rent_all_two_line[121 + 68]
        rent_all_two_dict["rent_all_two_dec13"] = rent_all_two_line[121 + 70]

        rent_all_two_dict["rent_all_two_mar14"] = rent_all_two_line[121 + 72]
        rent_all_two_dict["rent_all_two_jun14"] = rent_all_two_line[121 + 74]
        rent_all_two_dict["rent_all_two_sep14"] = rent_all_two_line[121 + 76]
        rent_all_two_dict["rent_all_two_dec14"] = rent_all_two_line[121 + 78]

        rent_all_two_dict["rent_all_two_mar15"] = rent_all_two_line[121 + 80]
        rent_all_two_dict["rent_all_two_jun15"] = rent_all_two_line[121 + 82]
        rent_all_two_dict["rent_all_two_sep15"] = rent_all_two_line[121 + 84]
        rent_all_two_dict["rent_all_two_dec15"] = rent_all_two_line[121 + 86]

        rent_all_two_dict["rent_all_two_mar16"] = rent_all_two_line[121 + 88]
        rent_all_two_dict["rent_all_two_jun16"] = rent_all_two_line[121 + 91]
        rent_all_two_dict["rent_all_two_sep16"] = rent_all_two_line[121 + 93]
        rent_all_two_dict["rent_all_two_dec16"] = rent_all_two_line[121 + 95]

        rent_all_three_line = rent_all_three.row_values(i)
        index = 0
        for j in rent_all_three_line:
            if j == "-":
                rent_all_three_line[index] = rent_all_three.row_values(3)[index]
            index += 1

        rent_all_three_dict["rent_all_three_mar05"] = rent_all_three_line[121]
        rent_all_three_dict["rent_all_three_jun05"] = rent_all_three_line[121 + 2]
        rent_all_three_dict["rent_all_three_sep05"] = rent_all_three_line[121 + 4]
        rent_all_three_dict["rent_all_three_dec05"] = rent_all_three_line[121 + 6]

        rent_all_three_dict["rent_all_three_mar06"] = rent_all_three_line[121 + 8]
        rent_all_three_dict["rent_all_three_jun06"] = rent_all_three_line[121 + 10]
        rent_all_three_dict["rent_all_three_sep06"] = rent_all_three_line[121 + 12]
        rent_all_three_dict["rent_all_three_dec06"] = rent_all_three_line[121 + 14]

        rent_all_three_dict["rent_all_three_mar07"] = rent_all_three_line[121 + 16]
        rent_all_three_dict["rent_all_three_jun07"] = rent_all_three_line[121 + 18]
        rent_all_three_dict["rent_all_three_sep07"] = rent_all_three_line[121 + 20]
        rent_all_three_dict["rent_all_three_dec07"] = rent_all_three_line[121 + 22]

        rent_all_three_dict["rent_all_three_mar08"] = rent_all_three_line[121 + 24]
        rent_all_three_dict["rent_all_three_jun08"] = rent_all_three_line[121 + 26]
        rent_all_three_dict["rent_all_three_sep08"] = rent_all_three_line[121 + 28]
        rent_all_three_dict["rent_all_three_dec08"] = rent_all_three_line[121 + 30]

        rent_all_three_dict["rent_all_three_mar09"] = rent_all_three_line[121 + 32]
        rent_all_three_dict["rent_all_three_jun09"] = rent_all_three_line[121 + 34]
        rent_all_three_dict["rent_all_three_sep09"] = rent_all_three_line[121 + 36]
        rent_all_three_dict["rent_all_three_dec09"] = rent_all_three_line[121 + 38]

        rent_all_three_dict["rent_all_three_mar10"] = rent_all_three_line[121 + 40]
        rent_all_three_dict["rent_all_three_jun10"] = rent_all_three_line[121 + 42]
        rent_all_three_dict["rent_all_three_sep10"] = rent_all_three_line[121 + 44]
        rent_all_three_dict["rent_all_three_dec10"] = rent_all_three_line[121 + 46]

        rent_all_three_dict["rent_all_three_mar11"] = rent_all_three_line[121 + 48]
        rent_all_three_dict["rent_all_three_jun11"] = rent_all_three_line[121 + 50]
        rent_all_three_dict["rent_all_three_sep11"] = rent_all_three_line[121 + 52]
        rent_all_three_dict["rent_all_three_dec11"] = rent_all_three_line[121 + 54]

        rent_all_three_dict["rent_all_three_mar12"] = rent_all_three_line[121 + 56]
        rent_all_three_dict["rent_all_three_jun12"] = rent_all_three_line[121 + 58]
        rent_all_three_dict["rent_all_three_sep12"] = rent_all_three_line[121 + 60]
        rent_all_three_dict["rent_all_three_dec12"] = rent_all_three_line[121 + 62]

        rent_all_three_dict["rent_all_three_mar13"] = rent_all_three_line[121 + 64]
        rent_all_three_dict["rent_all_three_jun13"] = rent_all_three_line[121 + 66]
        rent_all_three_dict["rent_all_three_sep13"] = rent_all_three_line[121 + 68]
        rent_all_three_dict["rent_all_three_dec13"] = rent_all_three_line[121 + 70]

        rent_all_three_dict["rent_all_three_mar14"] = rent_all_three_line[121 + 72]
        rent_all_three_dict["rent_all_three_jun14"] = rent_all_three_line[121 + 74]
        rent_all_three_dict["rent_all_three_sep14"] = rent_all_three_line[121 + 76]
        rent_all_three_dict["rent_all_three_dec14"] = rent_all_three_line[121 + 78]

        rent_all_three_dict["rent_all_three_mar15"] = rent_all_three_line[121 + 80]
        rent_all_three_dict["rent_all_three_jun15"] = rent_all_three_line[121 + 82]
        rent_all_three_dict["rent_all_three_sep15"] = rent_all_three_line[121 + 84]
        rent_all_three_dict["rent_all_three_dec15"] = rent_all_three_line[121 + 86]

        rent_all_three_dict["rent_all_three_mar16"] = rent_all_three_line[121 + 88]
        rent_all_three_dict["rent_all_three_jun16"] = rent_all_three_line[121 + 91]
        rent_all_three_dict["rent_all_three_sep16"] = rent_all_three_line[121 + 93]
        rent_all_three_dict["rent_all_three_dec16"] = rent_all_three_line[121 + 95]

        rent_all_four_line = rent_all_four.row_values(i)
        index = 0
        for j in rent_all_four_line:
            if j == "-":
                rent_all_four_line[index] = rent_all_four.row_values(3)[index]
            index += 1

        rent_all_four_dict["rent_all_four_mar05"] = rent_all_four_line[121]
        rent_all_four_dict["rent_all_four_jun05"] = rent_all_four_line[121 + 2]
        rent_all_four_dict["rent_all_four_sep05"] = rent_all_four_line[121 + 4]
        rent_all_four_dict["rent_all_four_dec05"] = rent_all_four_line[121 + 6]

        rent_all_four_dict["rent_all_four_mar06"] = rent_all_four_line[121 + 8]
        rent_all_four_dict["rent_all_four_jun06"] = rent_all_four_line[121 + 10]
        rent_all_four_dict["rent_all_four_sep06"] = rent_all_four_line[121 + 12]
        rent_all_four_dict["rent_all_four_dec06"] = rent_all_four_line[121 + 14]

        rent_all_four_dict["rent_all_four_mar07"] = rent_all_four_line[121 + 16]
        rent_all_four_dict["rent_all_four_jun07"] = rent_all_four_line[121 + 18]
        rent_all_four_dict["rent_all_four_sep07"] = rent_all_four_line[121 + 20]
        rent_all_four_dict["rent_all_four_dec07"] = rent_all_four_line[121 + 22]

        rent_all_four_dict["rent_all_four_mar08"] = rent_all_four_line[121 + 24]
        rent_all_four_dict["rent_all_four_jun08"] = rent_all_four_line[121 + 26]
        rent_all_four_dict["rent_all_four_sep08"] = rent_all_four_line[121 + 28]
        rent_all_four_dict["rent_all_four_dec08"] = rent_all_four_line[121 + 30]

        rent_all_four_dict["rent_all_four_mar09"] = rent_all_four_line[121 + 32]
        rent_all_four_dict["rent_all_four_jun09"] = rent_all_four_line[121 + 34]
        rent_all_four_dict["rent_all_four_sep09"] = rent_all_four_line[121 + 36]
        rent_all_four_dict["rent_all_four_dec09"] = rent_all_four_line[121 + 38]

        rent_all_four_dict["rent_all_four_mar10"] = rent_all_four_line[121 + 40]
        rent_all_four_dict["rent_all_four_jun10"] = rent_all_four_line[121 + 42]
        rent_all_four_dict["rent_all_four_sep10"] = rent_all_four_line[121 + 44]
        rent_all_four_dict["rent_all_four_dec10"] = rent_all_four_line[121 + 46]

        rent_all_four_dict["rent_all_four_mar11"] = rent_all_four_line[121 + 48]
        rent_all_four_dict["rent_all_four_jun11"] = rent_all_four_line[121 + 50]
        rent_all_four_dict["rent_all_four_sep11"] = rent_all_four_line[121 + 52]
        rent_all_four_dict["rent_all_four_dec11"] = rent_all_four_line[121 + 54]

        rent_all_four_dict["rent_all_four_mar12"] = rent_all_four_line[121 + 56]
        rent_all_four_dict["rent_all_four_jun12"] = rent_all_four_line[121 + 58]
        rent_all_four_dict["rent_all_four_sep12"] = rent_all_four_line[121 + 60]
        rent_all_four_dict["rent_all_four_dec12"] = rent_all_four_line[121 + 62]

        rent_all_four_dict["rent_all_four_mar13"] = rent_all_four_line[121 + 64]
        rent_all_four_dict["rent_all_four_jun13"] = rent_all_four_line[121 + 66]
        rent_all_four_dict["rent_all_four_sep13"] = rent_all_four_line[121 + 68]
        rent_all_four_dict["rent_all_four_dec13"] = rent_all_four_line[121 + 70]

        rent_all_four_dict["rent_all_four_mar14"] = rent_all_four_line[121 + 72]
        rent_all_four_dict["rent_all_four_jun14"] = rent_all_four_line[121 + 74]
        rent_all_four_dict["rent_all_four_sep14"] = rent_all_four_line[121 + 76]
        rent_all_four_dict["rent_all_four_dec14"] = rent_all_four_line[121 + 78]

        rent_all_four_dict["rent_all_four_mar15"] = rent_all_four_line[121 + 80]
        rent_all_four_dict["rent_all_four_jun15"] = rent_all_four_line[121 + 82]
        rent_all_four_dict["rent_all_four_sep15"] = rent_all_four_line[121 + 84]
        rent_all_four_dict["rent_all_four_dec15"] = rent_all_four_line[121 + 86]

        rent_all_four_dict["rent_all_four_mar16"] = rent_all_four_line[121 + 88]
        rent_all_four_dict["rent_all_four_jun16"] = rent_all_four_line[121 + 91]
        rent_all_four_dict["rent_all_four_sep16"] = rent_all_four_line[121 + 93]
        rent_all_four_dict["rent_all_four_dec16"] = rent_all_four_line[121 + 95]

        sale_all_line = sale_all.row_values(i + 2)
        index = 0
        for j in sale_all_line:
            if j == "-":
                sale_all_line[index] = sale_all.row_values(5)[index]
            index += 1
        sale_all_dict['sale_all_05'] = sale_all_line[115 + 0] + sale_all_line[115 + 2] + sale_all_line[
            115 + 4] + sale_all_line[115 + 6]
        sale_all_dict['sale_all_06'] = sale_all_line[115 + 8] + sale_all_line[115 + 10] + sale_all_line[
            115 + 12] + sale_all_line[115 + 14]
        sale_all_dict['sale_all_07'] = sale_all_line[115 + 16] + sale_all_line[115 + 18] + sale_all_line[
            115 + 20] + sale_all_line[115 + 22]
        sale_all_dict['sale_all_08'] = sale_all_line[115 + 24] + sale_all_line[115 + 26] + sale_all_line[
            115 + 28] + sale_all_line[115 + 30]
        sale_all_dict['sale_all_09'] = sale_all_line[115 + 32] + sale_all_line[115 + 34] + sale_all_line[
            115 + 36] + sale_all_line[115 + 38]
        sale_all_dict['sale_all_10'] = sale_all_line[115 + 40] + sale_all_line[115 + 42] + sale_all_line[
            115 + 44] + sale_all_line[115 + 46]
        sale_all_dict['sale_all_11'] = sale_all_line[115 + 48] + sale_all_line[115 + 50] + sale_all_line[
            115 + 52] + sale_all_line[115 + 54]
        sale_all_dict['sale_all_12'] = sale_all_line[115 + 56] + sale_all_line[115 + 58] + sale_all_line[
            115 + 60] + sale_all_line[115 + 62]
        sale_all_dict['sale_all_13'] = sale_all_line[115 + 64] + sale_all_line[115 + 66] + sale_all_line[
            115 + 68] + sale_all_line[115 + 70]
        sale_all_dict['sale_all_14'] = sale_all_line[115 + 72] + sale_all_line[115 + 74] + sale_all_line[
            115 + 76] + sale_all_line[115 + 78]
        sale_all_dict['sale_all_15'] = sale_all_line[115 + 80] + sale_all_line[115 + 82] + sale_all_line[
            115 + 84] + sale_all_line[115 + 86]
        sale_all_dict['sale_all_16'] = sale_all_line[115 + 88] + sale_all_line[115 + 90] + sale_all_line[
            115 + 92] + sale_all_line[115 + 94]

    if i >= 50 and i < 58:
        rent_all_all_line = rent_all_all.row_values(i)
        index = 0
        for j in rent_all_all_line:
            if j == "-":
                rent_all_all_line[index] = rent_all_all.row_values(3)[index]
            index += 1

        rent_all_all_dict["rent_all_all_mar05"] = rent_all_all_line[121]
        rent_all_all_dict["rent_all_all_jun05"] = rent_all_all_line[121 + 2]
        rent_all_all_dict["rent_all_all_sep05"] = rent_all_all_line[121 + 4]
        rent_all_all_dict["rent_all_all_dec05"] = rent_all_all_line[121 + 6]

        rent_all_all_dict["rent_all_all_mar06"] = rent_all_all_line[121 + 8]
        rent_all_all_dict["rent_all_all_jun06"] = rent_all_all_line[121 + 10]
        rent_all_all_dict["rent_all_all_sep06"] = rent_all_all_line[121 + 12]
        rent_all_all_dict["rent_all_all_dec06"] = rent_all_all_line[121 + 14]

        rent_all_all_dict["rent_all_all_mar07"] = rent_all_all_line[121 + 16]
        rent_all_all_dict["rent_all_all_jun07"] = rent_all_all_line[121 + 18]
        rent_all_all_dict["rent_all_all_sep07"] = rent_all_all_line[121 + 20]
        rent_all_all_dict["rent_all_all_dec07"] = rent_all_all_line[121 + 22]

        rent_all_all_dict["rent_all_all_mar08"] = rent_all_all_line[121 + 24]
        rent_all_all_dict["rent_all_all_jun08"] = rent_all_all_line[121 + 26]
        rent_all_all_dict["rent_all_all_sep08"] = rent_all_all_line[121 + 28]
        rent_all_all_dict["rent_all_all_dec08"] = rent_all_all_line[121 + 30]

        rent_all_all_dict["rent_all_all_mar09"] = rent_all_all_line[121 + 32]
        rent_all_all_dict["rent_all_all_jun09"] = rent_all_all_line[121 + 34]
        rent_all_all_dict["rent_all_all_sep09"] = rent_all_all_line[121 + 36]
        rent_all_all_dict["rent_all_all_dec09"] = rent_all_all_line[121 + 38]

        rent_all_all_dict["rent_all_all_mar10"] = rent_all_all_line[121 + 40]
        rent_all_all_dict["rent_all_all_jun10"] = rent_all_all_line[121 + 42]
        rent_all_all_dict["rent_all_all_sep10"] = rent_all_all_line[121 + 44]
        rent_all_all_dict["rent_all_all_dec10"] = rent_all_all_line[121 + 46]

        rent_all_all_dict["rent_all_all_mar11"] = rent_all_all_line[121 + 48]
        rent_all_all_dict["rent_all_all_jun11"] = rent_all_all_line[121 + 50]
        rent_all_all_dict["rent_all_all_sep11"] = rent_all_all_line[121 + 52]
        rent_all_all_dict["rent_all_all_dec11"] = rent_all_all_line[121 + 54]

        rent_all_all_dict["rent_all_all_mar12"] = rent_all_all_line[121 + 56]
        rent_all_all_dict["rent_all_all_jun12"] = rent_all_all_line[121 + 58]
        rent_all_all_dict["rent_all_all_sep12"] = rent_all_all_line[121 + 60]
        rent_all_all_dict["rent_all_all_dec12"] = rent_all_all_line[121 + 62]

        rent_all_all_dict["rent_all_all_mar13"] = rent_all_all_line[121 + 64]
        rent_all_all_dict["rent_all_all_jun13"] = rent_all_all_line[121 + 66]
        rent_all_all_dict["rent_all_all_sep13"] = rent_all_all_line[121 + 68]
        rent_all_all_dict["rent_all_all_dec13"] = rent_all_all_line[121 + 70]

        rent_all_all_dict["rent_all_all_mar14"] = rent_all_all_line[121 + 72]
        rent_all_all_dict["rent_all_all_jun14"] = rent_all_all_line[121 + 74]
        rent_all_all_dict["rent_all_all_sep14"] = rent_all_all_line[121 + 76]
        rent_all_all_dict["rent_all_all_dec14"] = rent_all_all_line[121 + 78]

        rent_all_all_dict["rent_all_all_mar15"] = rent_all_all_line[121 + 80]
        rent_all_all_dict["rent_all_all_jun15"] = rent_all_all_line[121 + 82]
        rent_all_all_dict["rent_all_all_sep15"] = rent_all_all_line[121 + 84]
        rent_all_all_dict["rent_all_all_dec15"] = rent_all_all_line[121 + 86]

        rent_all_all_dict["rent_all_all_mar16"] = rent_all_all_line[121 + 88]
        rent_all_all_dict["rent_all_all_jun16"] = rent_all_all_line[121 + 91]
        rent_all_all_dict["rent_all_all_sep16"] = rent_all_all_line[121 + 93]
        rent_all_all_dict["rent_all_all_dec16"] = rent_all_all_line[121 + 95]

        rent_all_one_line = rent_all_one.row_values(i)
        index = 0
        for j in rent_all_one_line:
            if j == "-":
                rent_all_one_line[index] = rent_all_one.row_values(3)[index]
            index += 1

        rent_all_one_dict["rent_all_one_mar05"] = rent_all_one_line[121]
        rent_all_one_dict["rent_all_one_jun05"] = rent_all_one_line[121 + 2]
        rent_all_one_dict["rent_all_one_sep05"] = rent_all_one_line[121 + 4]
        rent_all_one_dict["rent_all_one_dec05"] = rent_all_one_line[121 + 6]

        rent_all_one_dict["rent_all_one_mar06"] = rent_all_one_line[121 + 8]
        rent_all_one_dict["rent_all_one_jun06"] = rent_all_one_line[121 + 10]
        rent_all_one_dict["rent_all_one_sep06"] = rent_all_one_line[121 + 12]
        rent_all_one_dict["rent_all_one_dec06"] = rent_all_one_line[121 + 14]

        rent_all_one_dict["rent_all_one_mar07"] = rent_all_one_line[121 + 16]
        rent_all_one_dict["rent_all_one_jun07"] = rent_all_one_line[121 + 18]
        rent_all_one_dict["rent_all_one_sep07"] = rent_all_one_line[121 + 20]
        rent_all_one_dict["rent_all_one_dec07"] = rent_all_one_line[121 + 22]

        rent_all_one_dict["rent_all_one_mar08"] = rent_all_one_line[121 + 24]
        rent_all_one_dict["rent_all_one_jun08"] = rent_all_one_line[121 + 26]
        rent_all_one_dict["rent_all_one_sep08"] = rent_all_one_line[121 + 28]
        rent_all_one_dict["rent_all_one_dec08"] = rent_all_one_line[121 + 30]

        rent_all_one_dict["rent_all_one_mar09"] = rent_all_one_line[121 + 32]
        rent_all_one_dict["rent_all_one_jun09"] = rent_all_one_line[121 + 34]
        rent_all_one_dict["rent_all_one_sep09"] = rent_all_one_line[121 + 36]
        rent_all_one_dict["rent_all_one_dec09"] = rent_all_one_line[121 + 38]

        rent_all_one_dict["rent_all_one_mar10"] = rent_all_one_line[121 + 40]
        rent_all_one_dict["rent_all_one_jun10"] = rent_all_one_line[121 + 42]
        rent_all_one_dict["rent_all_one_sep10"] = rent_all_one_line[121 + 44]
        rent_all_one_dict["rent_all_one_dec10"] = rent_all_one_line[121 + 46]

        rent_all_one_dict["rent_all_one_mar11"] = rent_all_one_line[121 + 48]
        rent_all_one_dict["rent_all_one_jun11"] = rent_all_one_line[121 + 50]
        rent_all_one_dict["rent_all_one_sep11"] = rent_all_one_line[121 + 52]
        rent_all_one_dict["rent_all_one_dec11"] = rent_all_one_line[121 + 54]

        rent_all_one_dict["rent_all_one_mar12"] = rent_all_one_line[121 + 56]
        rent_all_one_dict["rent_all_one_jun12"] = rent_all_one_line[121 + 58]
        rent_all_one_dict["rent_all_one_sep12"] = rent_all_one_line[121 + 60]
        rent_all_one_dict["rent_all_one_dec12"] = rent_all_one_line[121 + 62]

        rent_all_one_dict["rent_all_one_mar13"] = rent_all_one_line[121 + 64]
        rent_all_one_dict["rent_all_one_jun13"] = rent_all_one_line[121 + 66]
        rent_all_one_dict["rent_all_one_sep13"] = rent_all_one_line[121 + 68]
        rent_all_one_dict["rent_all_one_dec13"] = rent_all_one_line[121 + 70]

        rent_all_one_dict["rent_all_one_mar14"] = rent_all_one_line[121 + 72]
        rent_all_one_dict["rent_all_one_jun14"] = rent_all_one_line[121 + 74]
        rent_all_one_dict["rent_all_one_sep14"] = rent_all_one_line[121 + 76]
        rent_all_one_dict["rent_all_one_dec14"] = rent_all_one_line[121 + 78]

        rent_all_one_dict["rent_all_one_mar15"] = rent_all_one_line[121 + 80]
        rent_all_one_dict["rent_all_one_jun15"] = rent_all_one_line[121 + 82]
        rent_all_one_dict["rent_all_one_sep15"] = rent_all_one_line[121 + 84]
        rent_all_one_dict["rent_all_one_dec15"] = rent_all_one_line[121 + 86]

        rent_all_one_dict["rent_all_one_mar16"] = rent_all_one_line[121 + 88]
        rent_all_one_dict["rent_all_one_jun16"] = rent_all_one_line[121 + 91]
        rent_all_one_dict["rent_all_one_sep16"] = rent_all_one_line[121 + 93]
        rent_all_one_dict["rent_all_one_dec16"] = rent_all_one_line[121 + 95]

        rent_all_two_line = rent_all_two.row_values(i)
        index = 0
        for j in rent_all_two_line:
            if j == "-":
                rent_all_two_line[index] = rent_all_two.row_values(3)[index]
            index += 1

        rent_all_two_dict["rent_all_two_mar05"] = rent_all_two_line[121]
        rent_all_two_dict["rent_all_two_jun05"] = rent_all_two_line[121 + 2]
        rent_all_two_dict["rent_all_two_sep05"] = rent_all_two_line[121 + 4]
        rent_all_two_dict["rent_all_two_dec05"] = rent_all_two_line[121 + 6]

        rent_all_two_dict["rent_all_two_mar06"] = rent_all_two_line[121 + 8]
        rent_all_two_dict["rent_all_two_jun06"] = rent_all_two_line[121 + 10]
        rent_all_two_dict["rent_all_two_sep06"] = rent_all_two_line[121 + 12]
        rent_all_two_dict["rent_all_two_dec06"] = rent_all_two_line[121 + 14]

        rent_all_two_dict["rent_all_two_mar07"] = rent_all_two_line[121 + 16]
        rent_all_two_dict["rent_all_two_jun07"] = rent_all_two_line[121 + 18]
        rent_all_two_dict["rent_all_two_sep07"] = rent_all_two_line[121 + 20]
        rent_all_two_dict["rent_all_two_dec07"] = rent_all_two_line[121 + 22]

        rent_all_two_dict["rent_all_two_mar08"] = rent_all_two_line[121 + 24]
        rent_all_two_dict["rent_all_two_jun08"] = rent_all_two_line[121 + 26]
        rent_all_two_dict["rent_all_two_sep08"] = rent_all_two_line[121 + 28]
        rent_all_two_dict["rent_all_two_dec08"] = rent_all_two_line[121 + 30]

        rent_all_two_dict["rent_all_two_mar09"] = rent_all_two_line[121 + 32]
        rent_all_two_dict["rent_all_two_jun09"] = rent_all_two_line[121 + 34]
        rent_all_two_dict["rent_all_two_sep09"] = rent_all_two_line[121 + 36]
        rent_all_two_dict["rent_all_two_dec09"] = rent_all_two_line[121 + 38]

        rent_all_two_dict["rent_all_two_mar10"] = rent_all_two_line[121 + 40]
        rent_all_two_dict["rent_all_two_jun10"] = rent_all_two_line[121 + 42]
        rent_all_two_dict["rent_all_two_sep10"] = rent_all_two_line[121 + 44]
        rent_all_two_dict["rent_all_two_dec10"] = rent_all_two_line[121 + 46]

        rent_all_two_dict["rent_all_two_mar11"] = rent_all_two_line[121 + 48]
        rent_all_two_dict["rent_all_two_jun11"] = rent_all_two_line[121 + 50]
        rent_all_two_dict["rent_all_two_sep11"] = rent_all_two_line[121 + 52]
        rent_all_two_dict["rent_all_two_dec11"] = rent_all_two_line[121 + 54]

        rent_all_two_dict["rent_all_two_mar12"] = rent_all_two_line[121 + 56]
        rent_all_two_dict["rent_all_two_jun12"] = rent_all_two_line[121 + 58]
        rent_all_two_dict["rent_all_two_sep12"] = rent_all_two_line[121 + 60]
        rent_all_two_dict["rent_all_two_dec12"] = rent_all_two_line[121 + 62]

        rent_all_two_dict["rent_all_two_mar13"] = rent_all_two_line[121 + 64]
        rent_all_two_dict["rent_all_two_jun13"] = rent_all_two_line[121 + 66]
        rent_all_two_dict["rent_all_two_sep13"] = rent_all_two_line[121 + 68]
        rent_all_two_dict["rent_all_two_dec13"] = rent_all_two_line[121 + 70]

        rent_all_two_dict["rent_all_two_mar14"] = rent_all_two_line[121 + 72]
        rent_all_two_dict["rent_all_two_jun14"] = rent_all_two_line[121 + 74]
        rent_all_two_dict["rent_all_two_sep14"] = rent_all_two_line[121 + 76]
        rent_all_two_dict["rent_all_two_dec14"] = rent_all_two_line[121 + 78]

        rent_all_two_dict["rent_all_two_mar15"] = rent_all_two_line[121 + 80]
        rent_all_two_dict["rent_all_two_jun15"] = rent_all_two_line[121 + 82]
        rent_all_two_dict["rent_all_two_sep15"] = rent_all_two_line[121 + 84]
        rent_all_two_dict["rent_all_two_dec15"] = rent_all_two_line[121 + 86]

        rent_all_two_dict["rent_all_two_mar16"] = rent_all_two_line[121 + 88]
        rent_all_two_dict["rent_all_two_jun16"] = rent_all_two_line[121 + 91]
        rent_all_two_dict["rent_all_two_sep16"] = rent_all_two_line[121 + 93]
        rent_all_two_dict["rent_all_two_dec16"] = rent_all_two_line[121 + 95]

        rent_all_three_line = rent_all_three.row_values(i)
        index = 0
        for j in rent_all_three_line:
            if j == "-":
                rent_all_three_line[index] = rent_all_three.row_values(3)[index]
            index += 1

        rent_all_three_dict["rent_all_three_mar05"] = rent_all_three_line[121]
        rent_all_three_dict["rent_all_three_jun05"] = rent_all_three_line[121 + 2]
        rent_all_three_dict["rent_all_three_sep05"] = rent_all_three_line[121 + 4]
        rent_all_three_dict["rent_all_three_dec05"] = rent_all_three_line[121 + 6]

        rent_all_three_dict["rent_all_three_mar06"] = rent_all_three_line[121 + 8]
        rent_all_three_dict["rent_all_three_jun06"] = rent_all_three_line[121 + 10]
        rent_all_three_dict["rent_all_three_sep06"] = rent_all_three_line[121 + 12]
        rent_all_three_dict["rent_all_three_dec06"] = rent_all_three_line[121 + 14]

        rent_all_three_dict["rent_all_three_mar07"] = rent_all_three_line[121 + 16]
        rent_all_three_dict["rent_all_three_jun07"] = rent_all_three_line[121 + 18]
        rent_all_three_dict["rent_all_three_sep07"] = rent_all_three_line[121 + 20]
        rent_all_three_dict["rent_all_three_dec07"] = rent_all_three_line[121 + 22]

        rent_all_three_dict["rent_all_three_mar08"] = rent_all_three_line[121 + 24]
        rent_all_three_dict["rent_all_three_jun08"] = rent_all_three_line[121 + 26]
        rent_all_three_dict["rent_all_three_sep08"] = rent_all_three_line[121 + 28]
        rent_all_three_dict["rent_all_three_dec08"] = rent_all_three_line[121 + 30]

        rent_all_three_dict["rent_all_three_mar09"] = rent_all_three_line[121 + 32]
        rent_all_three_dict["rent_all_three_jun09"] = rent_all_three_line[121 + 34]
        rent_all_three_dict["rent_all_three_sep09"] = rent_all_three_line[121 + 36]
        rent_all_three_dict["rent_all_three_dec09"] = rent_all_three_line[121 + 38]

        rent_all_three_dict["rent_all_three_mar10"] = rent_all_three_line[121 + 40]
        rent_all_three_dict["rent_all_three_jun10"] = rent_all_three_line[121 + 42]
        rent_all_three_dict["rent_all_three_sep10"] = rent_all_three_line[121 + 44]
        rent_all_three_dict["rent_all_three_dec10"] = rent_all_three_line[121 + 46]

        rent_all_three_dict["rent_all_three_mar11"] = rent_all_three_line[121 + 48]
        rent_all_three_dict["rent_all_three_jun11"] = rent_all_three_line[121 + 50]
        rent_all_three_dict["rent_all_three_sep11"] = rent_all_three_line[121 + 52]
        rent_all_three_dict["rent_all_three_dec11"] = rent_all_three_line[121 + 54]

        rent_all_three_dict["rent_all_three_mar12"] = rent_all_three_line[121 + 56]
        rent_all_three_dict["rent_all_three_jun12"] = rent_all_three_line[121 + 58]
        rent_all_three_dict["rent_all_three_sep12"] = rent_all_three_line[121 + 60]
        rent_all_three_dict["rent_all_three_dec12"] = rent_all_three_line[121 + 62]

        rent_all_three_dict["rent_all_three_mar13"] = rent_all_three_line[121 + 64]
        rent_all_three_dict["rent_all_three_jun13"] = rent_all_three_line[121 + 66]
        rent_all_three_dict["rent_all_three_sep13"] = rent_all_three_line[121 + 68]
        rent_all_three_dict["rent_all_three_dec13"] = rent_all_three_line[121 + 70]

        rent_all_three_dict["rent_all_three_mar14"] = rent_all_three_line[121 + 72]
        rent_all_three_dict["rent_all_three_jun14"] = rent_all_three_line[121 + 74]
        rent_all_three_dict["rent_all_three_sep14"] = rent_all_three_line[121 + 76]
        rent_all_three_dict["rent_all_three_dec14"] = rent_all_three_line[121 + 78]

        rent_all_three_dict["rent_all_three_mar15"] = rent_all_three_line[121 + 80]
        rent_all_three_dict["rent_all_three_jun15"] = rent_all_three_line[121 + 82]
        rent_all_three_dict["rent_all_three_sep15"] = rent_all_three_line[121 + 84]
        rent_all_three_dict["rent_all_three_dec15"] = rent_all_three_line[121 + 86]

        rent_all_three_dict["rent_all_three_mar16"] = rent_all_three_line[121 + 88]
        rent_all_three_dict["rent_all_three_jun16"] = rent_all_three_line[121 + 91]
        rent_all_three_dict["rent_all_three_sep16"] = rent_all_three_line[121 + 93]
        rent_all_three_dict["rent_all_three_dec16"] = rent_all_three_line[121 + 95]

        rent_all_four_line = rent_all_four.row_values(i)
        index = 0
        for j in rent_all_four_line:
            if j == "-":
                rent_all_four_line[index] = rent_all_four.row_values(3)[index]
            index += 1

        rent_all_four_dict["rent_all_four_mar05"] = rent_all_four_line[121]
        rent_all_four_dict["rent_all_four_jun05"] = rent_all_four_line[121 + 2]
        rent_all_four_dict["rent_all_four_sep05"] = rent_all_four_line[121 + 4]
        rent_all_four_dict["rent_all_four_dec05"] = rent_all_four_line[121 + 6]

        rent_all_four_dict["rent_all_four_mar06"] = rent_all_four_line[121 + 8]
        rent_all_four_dict["rent_all_four_jun06"] = rent_all_four_line[121 + 10]
        rent_all_four_dict["rent_all_four_sep06"] = rent_all_four_line[121 + 12]
        rent_all_four_dict["rent_all_four_dec06"] = rent_all_four_line[121 + 14]

        rent_all_four_dict["rent_all_four_mar07"] = rent_all_four_line[121 + 16]
        rent_all_four_dict["rent_all_four_jun07"] = rent_all_four_line[121 + 18]
        rent_all_four_dict["rent_all_four_sep07"] = rent_all_four_line[121 + 20]
        rent_all_four_dict["rent_all_four_dec07"] = rent_all_four_line[121 + 22]

        rent_all_four_dict["rent_all_four_mar08"] = rent_all_four_line[121 + 24]
        rent_all_four_dict["rent_all_four_jun08"] = rent_all_four_line[121 + 26]
        rent_all_four_dict["rent_all_four_sep08"] = rent_all_four_line[121 + 28]
        rent_all_four_dict["rent_all_four_dec08"] = rent_all_four_line[121 + 30]

        rent_all_four_dict["rent_all_four_mar09"] = rent_all_four_line[121 + 32]
        rent_all_four_dict["rent_all_four_jun09"] = rent_all_four_line[121 + 34]
        rent_all_four_dict["rent_all_four_sep09"] = rent_all_four_line[121 + 36]
        rent_all_four_dict["rent_all_four_dec09"] = rent_all_four_line[121 + 38]

        rent_all_four_dict["rent_all_four_mar10"] = rent_all_four_line[121 + 40]
        rent_all_four_dict["rent_all_four_jun10"] = rent_all_four_line[121 + 42]
        rent_all_four_dict["rent_all_four_sep10"] = rent_all_four_line[121 + 44]
        rent_all_four_dict["rent_all_four_dec10"] = rent_all_four_line[121 + 46]

        rent_all_four_dict["rent_all_four_mar11"] = rent_all_four_line[121 + 48]
        rent_all_four_dict["rent_all_four_jun11"] = rent_all_four_line[121 + 50]
        rent_all_four_dict["rent_all_four_sep11"] = rent_all_four_line[121 + 52]
        rent_all_four_dict["rent_all_four_dec11"] = rent_all_four_line[121 + 54]

        rent_all_four_dict["rent_all_four_mar12"] = rent_all_four_line[121 + 56]
        rent_all_four_dict["rent_all_four_jun12"] = rent_all_four_line[121 + 58]
        rent_all_four_dict["rent_all_four_sep12"] = rent_all_four_line[121 + 60]
        rent_all_four_dict["rent_all_four_dec12"] = rent_all_four_line[121 + 62]

        rent_all_four_dict["rent_all_four_mar13"] = rent_all_four_line[121 + 64]
        rent_all_four_dict["rent_all_four_jun13"] = rent_all_four_line[121 + 66]
        rent_all_four_dict["rent_all_four_sep13"] = rent_all_four_line[121 + 68]
        rent_all_four_dict["rent_all_four_dec13"] = rent_all_four_line[121 + 70]

        rent_all_four_dict["rent_all_four_mar14"] = rent_all_four_line[121 + 72]
        rent_all_four_dict["rent_all_four_jun14"] = rent_all_four_line[121 + 74]
        rent_all_four_dict["rent_all_four_sep14"] = rent_all_four_line[121 + 76]
        rent_all_four_dict["rent_all_four_dec14"] = rent_all_four_line[121 + 78]

        rent_all_four_dict["rent_all_four_mar15"] = rent_all_four_line[121 + 80]
        rent_all_four_dict["rent_all_four_jun15"] = rent_all_four_line[121 + 82]
        rent_all_four_dict["rent_all_four_sep15"] = rent_all_four_line[121 + 84]
        rent_all_four_dict["rent_all_four_dec15"] = rent_all_four_line[121 + 86]

        rent_all_four_dict["rent_all_four_mar16"] = rent_all_four_line[121 + 88]
        rent_all_four_dict["rent_all_four_jun16"] = rent_all_four_line[121 + 91]
        rent_all_four_dict["rent_all_four_sep16"] = rent_all_four_line[121 + 93]
        rent_all_four_dict["rent_all_four_dec16"] = rent_all_four_line[121 + 95]

        sale_all_line = sale_all.row_values(i + 2)
        index = 0
        for j in sale_all_line:
            if j == "-":
                sale_all_line[index] = sale_all.row_values(5)[index]
            index += 1
        sale_all_dict['sale_all_05'] = sale_all_line[115 + 0] + sale_all_line[115 + 2] + sale_all_line[
            115 + 4] + sale_all_line[115 + 6]
        sale_all_dict['sale_all_06'] = sale_all_line[115 + 8] + sale_all_line[115 + 10] + sale_all_line[
            115 + 12] + sale_all_line[115 + 14]
        sale_all_dict['sale_all_07'] = sale_all_line[115 + 16] + sale_all_line[115 + 18] + sale_all_line[
            115 + 20] + sale_all_line[115 + 22]
        sale_all_dict['sale_all_08'] = sale_all_line[115 + 24] + sale_all_line[115 + 26] + sale_all_line[
            115 + 28] + sale_all_line[115 + 30]
        sale_all_dict['sale_all_09'] = sale_all_line[115 + 32] + sale_all_line[115 + 34] + sale_all_line[
            115 + 36] + sale_all_line[115 + 38]
        sale_all_dict['sale_all_10'] = sale_all_line[115 + 40] + sale_all_line[115 + 42] + sale_all_line[
            115 + 44] + sale_all_line[115 + 46]
        sale_all_dict['sale_all_11'] = sale_all_line[115 + 48] + sale_all_line[115 + 50] + sale_all_line[
            115 + 52] + sale_all_line[115 + 54]
        sale_all_dict['sale_all_12'] = sale_all_line[115 + 56] + sale_all_line[115 + 58] + sale_all_line[
            115 + 60] + sale_all_line[115 + 62]
        sale_all_dict['sale_all_13'] = sale_all_line[115 + 64] + sale_all_line[115 + 66] + sale_all_line[
            115 + 68] + sale_all_line[115 + 70]
        sale_all_dict['sale_all_14'] = sale_all_line[115 + 72] + sale_all_line[115 + 74] + sale_all_line[
            115 + 76] + sale_all_line[115 + 78]
        sale_all_dict['sale_all_15'] = sale_all_line[115 + 80] + sale_all_line[115 + 82] + sale_all_line[
            115 + 84] + sale_all_line[115 + 86]
        sale_all_dict['sale_all_16'] = sale_all_line[115 + 88] + sale_all_line[115 + 90] + sale_all_line[
            115 + 92] + sale_all_line[115 + 94]

    all_dict = {}
    all_dict["all_rent"] = rent_all_all_dict
    all_dict["one_rent"] = rent_all_one_dict
    all_dict["two_rent"] = rent_all_two_dict
    all_dict["three_rent"] = rent_all_three_dict
    all_dict["four_rent"] = rent_all_four_dict
    all_dict["sales"] = sale_all_dict

    return all_dict

