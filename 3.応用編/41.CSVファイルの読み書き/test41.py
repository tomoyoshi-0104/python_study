import csv
csv_file = open('./python.csv', 'w', newline='')
writer = csv.writer(csv_file)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()


csv_file = open('./python2.csv', 'w', newline='')
writer = csv.writer(
    csv_file,
    quoting=csv.QUOTE_ALL,
    delimiter=':',
    quotechar='`'
)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()


csv_file = open('./python3.csv', 'w', newline='')
writer = csv.writer(
    csv_file,
    dialect=csv.excel_tab,
)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()


class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL

csv_file = open('./python4.csv', 'w', newline='')
writer = csv.writer(
    csv_file,
    dialect=CustomFormat(),
)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()


class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL

# 登録しておく
csv.register_dialect('myformat', CustomFormat)

csv_file = open('./python5.csv', 'w', newline='')
writer = csv.writer(
    csv_file,
    dialect='myformat',
)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()


csv_file = open('./python.csv', 'r', newline='')
reader = csv.reader(csv_file)

for row in reader:
    print('-------------------')
    for cell in row:
        print(cell)

csv_file.close()
