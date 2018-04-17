import csv
import json

csvfile = open('census_data.csv', 'r')
jsonfile = open('census_data.json', 'w')

fieldnames = ("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","race","gender","capital_gain","capital_loss","hours_per_week","native_country")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')