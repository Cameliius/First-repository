# import openpyxl
# #читаем файл
# wb = openpyxl.load_workbook(filename = 'Book1.xlsx')
# sheet = wb['test']
# val = sheet['A1'].value
# vals = [v[0].value for v in sheet['A1:A2']]
#
# #записываем файл
# sheet['B1'] = val
# i = 2
# for rec in vals:
#     sheet.cell(row=i, column=2).value = rec
#     i += 1
# wb.save('Book2.xlsx')

i = 1

while i <= 10:

    print(i)

    i += 1

else:

    print('Цикл окончен, i =', i)