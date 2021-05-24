#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[12]:


#convert dictionary data to table
dict1={
    'Name':['Rohit','Shubham','Dhruv','Vishwajeet','Vishal','Amartya'],
    'Marks':[98,97,96,95,94,93],
    'City':['Lucknow','Allhabad','Patna','Agra','Ujjain','Pune'],
    'State':['Uttar Pradesh','Uttar Pradesh','Bihar','Uttar Pradesh','Madhya Pradesh','Maharashtra'],
    'Phone_':[12345,23456,34567,45678,56789,67890]   
}
df=pd.DataFrame(dict1)
df


# In[13]:


#from to_csv() function you can export your dictionary data to a excel file 
df.to_csv('details.csv')


# In[18]:


#here we use index=False because we dont want index column before detail
df.to_csv('details_index_false.csv',index=False)


# In[19]:


#from df.head(4) funtion you can get 4 rows from your table from upper side
df.head(3)


# In[20]:


#from df.tail(3) funtion you can get 3 rows from your table from lower side
df.tail(3)


# In[22]:


#it computes with that column which contain mathematical values (the statistics and operation on mathematical data)
df.describe()


# In[43]:


import numpy as np
import pandas as pd
#here we read csv file (import)
student_results=pd.read_csv('student_results.csv')
student_results


# In[44]:


#here we get value by slicing
student_results['Class'][0]


# In[45]:


#here we changed the value of index 4 of Class from table
student_results['Class'][4]=10


# In[46]:


student_results


# In[47]:


#again we can save this file because of last changes in the file
student_results.to_csv('student_results1.csv')


# In[49]:


# here we can also give own value to index
student_results.index=['one','two','three','four','five','six','seven','eight','nine','ten']


# In[50]:


student_results


# In[54]:


#if i have to access the row by index so i can also access from this index values
student_results['Student ID']['one']


# In[78]:


#SERIES
ans=pd.Series(np.random.randint(10))


# In[79]:


ans


# In[80]:


type(ans)


# In[81]:


# NEW DATAFRAME
newdf=pd.DataFrame(np.random.rand(100,4), index=np.arange(100)) #100 rows and 4 columns


# In[83]:


newdf


# In[84]:


type(newdf)


# In[85]:


newdf.describe()


# In[87]:


newdf.dtypes


# In[93]:


newdf.head(5)


# In[94]:


newdf[0][2]='amit'


# In[96]:


newdf.head(5)


# In[97]:


newdf[0][0]='pooja'


# In[98]:


newdf.head(5)


# In[99]:


#here i used this for to print new added data and it showing object at the palce of float data type.
# because we inserted the string value
newdf.dtypes


# In[100]:


newdf.index


# In[101]:


newdf.columns


# In[103]:


# here we can also convert the data into array
newdf.to_numpy


# In[104]:


# It transpose the rows=column and column=rows(rows =5 and column=100)
newdf.T


# In[110]:


#it prints the data into descending order,axis=0 means rows(it sorts the data from row side)
newdf.sort_index(axis=0,ascending=False)


# In[111]:


#from this indexing, your data is in series form(we can accessed the column)
newdf[0]


# In[112]:


#here we can check the column  so it is showing the type of data is series
type(newdf[0])


# In[114]:


# we have used a variable and pass newdf to this variable like views in numpy
newdf1=newdf


# In[115]:


newdf1[0][0]='1234'


# In[117]:


# here i did print the main newdf but we have changed the value of newdf1 but it also changed in newdf one so that is only view
# from newdf to newdf1
newdf


# In[118]:


#if i do use copy function
newdf1=newdf.copy()


# In[119]:


newdf1[0][1]='3456'


# In[120]:


newdf #there is not changed in original variable because of we made a copy newdf variable and changes were done on newdf1


# In[122]:


#to use loc you can change the value
newdf.loc[1,1]=8763#row 0 and col 0


# In[123]:


newdf.head(3)


# In[125]:


#here we can change the column name also
newdf.columns=list('ABCD')


# In[126]:


newdf


# In[127]:


#In this table you did set their column names is alphabatically now we add 0 column after the D column
newdf.loc[0,0]=345


# In[128]:


# here you can check the 0th column is added at the end
newdf.head(4)


# In[130]:


#if want to delete the last column so you can also do use of drop() function
newdf=newdf.drop(0,axis=1)#drop(0 is column and axis =1 is column) 


# In[131]:


newdf


# In[132]:


#want to access the rows and columns
newdf.loc[[1,2], ['C', 'D']] #first list id for rows and seconf list for columns


# In[138]:


# want to access C and D column data
newdf.loc[:, ['C','D']]


# In[139]:


# row only 2 and complete column
newdf.loc[[1,2],:]


# In[145]:


#here i can also use <> this operator sign to get result of given operator
newdf.loc[(newdf['C']<0.3)]


# In[144]:





# In[ ]:




