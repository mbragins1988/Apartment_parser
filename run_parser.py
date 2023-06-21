from parser import data

import xlsxwriter


def writer(data):
    book = xlsxwriter.Workbook(r'/Users/bragin/Desktop/Apartment_parsing.xlsx')
    page = book.add_worksheet('квартиры')

    row = 0
    column = 0

    page.set_column('A:A', 25)
    page.set_column('B:B', 12)
    page.set_column('C:C', 15)
    page.set_column('D:D', 80)

    for item in data():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1

    book.close()


writer(data)
