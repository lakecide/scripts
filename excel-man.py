import openpyexcel as xl
from openpyexcel.chart import BarChart, Reference


wb = xl.load_workbook('Customer.xlsx')
sheet = wb['Sheet2']
cell = sheet['a1']
cell = sheet.cell(1, 1)

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet.cell(row, 5)
    corrected_price_cell.value = corrected_price
    print(corrected_price_cell.value)


values = Reference(sheet, min_row=2, max_row=sheet.max_row,
          min_col =5, 
          max_col= 5)
chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'h2')

wb.save('Customer2.xlsx')