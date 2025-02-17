import pandas as pd

data = {'name':['sanju','vilas','asna'],'subject':['maths','java','python'],'marks':[23,56,74]}
df = pd.DataFrame(data)
print('data')
print(df)

# for index, row in df.iterrows():
#     print(f'{index}')
#     print(f'{row[ 'name']}')

# for index,row,marks in df.iterrows():
#     print(f'{index}')
#     print(f'{row}')
#     print(f'{marks}')

#  A list of date strings
date_list = ['2025-02-01 12:00:00', '2025-02-02 11:00:00', '2025-02-03 10:00:00', '2025-02-04 09:00:00']

# Convert to a DatetimeIndex (Pandas handles conversion)
dates = pd.to_datetime(date_list)
print(dates)

# Creating a DataFrame with datetime index
data = {'temperature': [22, 23, 21, 19]}
df = pd.DataFrame(data, index=dates)

print(df)



