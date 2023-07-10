import pandas as pd
# fname = "C:\\Users\\SURENDRA\\Documents\\demoo\\files\\RRI127-Report 3.xlsx"

# df = pd.read_excel(fname)

# df.drop(df.head(2).index, inplace=True)
# df.drop(df.tail(1).index, inplace=True)

# # df.dropna()

# df.dropna(how="all", axis=0, inplace=True) #row
# df.dropna(how="all", axis=1, inplace=True) #columns


# print(df)
# print(df.columns)



# s=[2,4,6,7,9,10,12]
# for i in s:
#     df.iloc[:,i+1] = df.iloc[:,i+1].combine_first(df.iloc[:,i])
# df.drop(columns=df.columns[s],inplace=True)
# df.columns=["  ","today","MTD","YTD","sa","MTD","YTD"]
     



# df.to_excel("output.xlsx", index=None,)
df=pd.DataFrame({"name":["sure","jaga"],"age":[20,24],"qua":["btech","ms"]})
print(df)
df=df.pivot(index="age",columns="name",values="qua")
print(df)
