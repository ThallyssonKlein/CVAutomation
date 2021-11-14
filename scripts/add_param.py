param_key = input("Enter the parameter key: ")
param_value = input("Enter the parameter value: ")

import csv

with open('../data.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow([param_key, param_value])