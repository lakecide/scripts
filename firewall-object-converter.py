import csv
from fileinput import close
from tkinter import W

data = open('ckpaddr.csv')

csv_data = csv.reader(data)
data_lines = list(csv_data)

"""
data_lines[0]
len(data_lines)
"""

host_names = []
for host in data_lines[1:]:
    host_names.append(host[0])

ip_address = []
for ips in data_lines[1:]:
    ip_address.append(ips[2])

file = open('Addresses2.txt', W)
for host in data_lines[1:]:
      addresses = f"edit {host[0]} \nset subnet {host[2]} 255.255.255.255 \nset comment '' \nnext\n"
      file.write(addresses)

file.close
print(addresses)

#wb.save('Addresses2.txt')

