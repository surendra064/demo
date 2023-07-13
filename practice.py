import pandas as pd

fname = "C:\\Users\\SURENDRA\\Documents\\demoo\\files\\RRI127-Report 2.xlsx"

df = pd.read_excel(fname)

df.drop(df.head(1).index, inplace=True)
df.drop(df.tail(2).index, inplace=True)

# df.dropna()

df.dropna(how="all", axis=0, inplace=True) #row
df.dropna(how="all", axis=1, inplace=True) #columns


print(df)
print(df.columns)



s=[6]
for i in s:
    df.iloc[:,i+1] = df.iloc[:,i+1].combine_first(df.iloc[:,i])
df.drop(columns=df.columns[s],inplace=True)
# df.columns=["  ","today","MTD","YTD","sa","MTD","YTD"]
y=[5,17]
yu=lambda s1,s2:str(s2)+" "+str(s1) if str(s1)!="nan" else s2
for i in y:
    
 df.iloc[i+1,:] = df.iloc[i+1,:].combine(df.iloc[i,:],func=yu)
 
df.drop(index=df.index[y],inplace=True)
     



df.to_excel("output2.xlsx", index=None,header=None)
# df=pd.DataFrame({"name":["sure","jaga"],"age":[20,24],"qua":["btech","ms"]})
# print(df)
# df=df.pivot(index="age",columns="name",values="qua")
# print(df)
