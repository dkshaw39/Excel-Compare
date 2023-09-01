import pandas as pd

#Reading two Excel Sheets

sheet1 = pd.read_excel(r'data\data1.xlsx')
sheet2 = pd.read_excel(r'data\data2.xlsx')
sheet1=sheet1.set_index(['Name'])
sheet2=sheet2.set_index(['Name'])
print(sheet1)
print(sheet2)

idx = sheet1.index.intersection(sheet2.index)

df_diff = sheet1.loc[idx].compare(sheet2.loc[idx],keep_equal=True)

print(df_diff)

df_diff.to_csv('diff.csv')