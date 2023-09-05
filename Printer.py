# INSTRUCTIONS
# This script is to be copied into our colab assignments.
# Once we have downloaded the necessary dataset, converted it into csv,
# and uploaded it onto our github, we can use this script to
# dynamically access the dataset as a dataframe from our colab.
# Replace the csv0 in lines 18 and 24 with the name of the csv we need.


import requests
import io
import pandas as pd

headers = {
    'Accept':'*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://github.com',
    'Referer': 'https://github.com/Skywaterr/CSVs/blob/main/csv0.csv',
    "Sec-Ch-Ua":'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'"
}


r = requests.get('https://raw.githubusercontent.com/Skywaterr/CSVs/main/csv0.csv', headers = headers)
data = r.content

df = pd.read_csv(io.StringIO(data.decode('ISO-8859-1')))
print(df)