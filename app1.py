import pandas as pd
fname="files//reviews.csv"
df=pd.read_csv(fname,encoding="unicode_escape")
# print(df.columns)
# print(df.shape)
# print(df.index)
# print(df.loc[:,"rating"])#rows,coloumn
# print(df.iloc[4])#roww(indexing type)

#addings rows and columns to df
df.loc[33396]=df.columns #adds row if 33396 is nnot present or chnges the content of ot is present
df['d']=df.index #adds coloumn named d to df

#deleting rows and coloumns
df.drop('d',axis=1,inplace=True)#drops coloumn d axis 1 means coloumn and 0 means row ,usee inplace true to get output 
df.drop(df.columns[[1]],axis=1)#drops coloumn at index 1
df.drop(df.index[33396],inplace=True)#drops roe at index 33396
#changing index of df
df1=df.set_index('reviewer_id')
#slicing dataframe
df2=df.loc[(df["rating"]=="1 star"),['store_name',"review"]]#gives stire name and review of 1 star ratings
df3=df.iloc[:2,:]#rows,coloumn
print(df)#only rows can be sliced

