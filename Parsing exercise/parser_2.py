#   py -m pip install parse
import parse
import pandas as pd

with open('Parsing exercise/headers.txt') as f:
    headers = f.readlines()

results = []
for header in headers:
    results.append(parse.parse('##INFO=<ID={ID},Number={Number},Type={Type},Description="{Description}">\n',header).named)

#   print (results[:2])
#   print (type(results))
#   print (type(results[0]))

df = pd.DataFrame.from_dict(results)

print(df)