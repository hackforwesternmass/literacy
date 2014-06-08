import csv

with open('industries-csv.csv', 'r') as handle:
    for row in csv.DictReader(handle):
        print("""
- model: literacy_network.Industry
  fields:
    name: {0}
    code: {1}
""".format(row["Industry_Name"], row["Industry_Code"]))
