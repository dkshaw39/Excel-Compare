import pandas as pd

#Reading two Excel Sheets

def read_excel(file):
    return pd.read_excel(file)

def get_column_values(data1: pd.Series,data2:pd.Series):
    a,b =[],[]
    # Iterating the columns values
    for m, n in zip(data1,data2):
        a.append(m)
        b.append(n)
    # Sorting the each columns value
    a.sort()
    b.sort()
    return a,b

def compare_records(df1,df2):
    # Iterating the Columns Names of both Sheets
    for i,j in zip(df1,df2):
        # get col values
        a,b =get_column_values(df1[i],df2[j])
        # Iterating the list's values and comparing them
        for m, n in zip(range(len(a)), range(len(b))):
            if a[m] != b[n]:
                print('Column name : \'{}\' and Row Number : {}'.format(i,m))

if __name__=='__main__':
    df1 = read_excel(r'data1.xlsx')
    df2 = read_excel(r'data2.xlsx')
    compare_records(df1,df2)