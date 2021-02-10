#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[2]:


df = pd.read_csv("Final_Train.csv", error_bad_lines = False )
df.info()


# In[3]:


df = df[df["Fees"] > 500]
df


# In[14]:


#Sorting the values by fees in ascending order 
df1 = df.sort_values(['Fees'] , inplace = False )
df1


# In[5]:


# Finding average fees of a doctor

sum = df['Fees'].sum()
print(sum)
total_no = len(df.index)
print(total_no)


# In[6]:


avg = sum/total_no 
print(avg)


# In[7]:


dprofiles = df['Profile'].unique()
dprofiles


# In[8]:


# finding and counting all types of doctors, using unique()

df2 = df[df['Profile'].str.contains("Dentist")]  
print("no of Dentists  : " , len(df2.index)) 
df2 = df[df['Profile'].str.contains("Dermatologists")]  
print("no of Dermatologists  : " , len(df2.index)) 
df2 = df[df['Profile'].str.contains("General Medicine")]  
print("no of General Medicine doctors  : " , len(df2.index)) 
df2 = df[df['Profile'].str.contains("Homeopath")]  
print("no of Homeopathy Doctors  : " , len(df2.index)) 
df2 = df[df['Profile'].str.contains("Ayurveda")]  
print("no of Ayurvedic doctors  : " , len(df2.index)) 
df2 = df[df['Profile'].str.contains("ENT Specialist")]  
print("no of ENT Specialists  : " , len(df2.index)) 


# In[9]:


# finding states  of all these doctors and finding the state having the most 
df3 = df[df['Place'].str.contains("Delhi")]
print("Doctors in delhi  : " , len(df3.index))
dfbang = df[df['Place'].str.contains("Bangalore")]
print("Doctors in Banglore  : " , len(dfbang.index))
dfchen = df[df['Place'].str.contains("Chennai")]
print("Doctors in chennai  : " , len(dfchen.index))
dfmum = df[df['Place'].str.contains("Mumbai")]
print("Doctors in mumbai  : " , len(dfmum.index))
dfhyd = df[df['Place'].str.contains("Hyderabad")]
print("Doctors in Hyderabad  : " , len(dfhyd.index))

plotdata = pd.DataFrame(
        {"States" : [len(df3.index), len(dfbang.index), len(dfchen.index) , len(dfmum.index), len(dfhyd.index)] } ,
           index = ['Delhi' , 'Banglore', 'Chennai' , 'Mumbai', 'Hyderabad']
            )

plotdata.plot(kind = "bar" )


# In[18]:


# finding average rating of doctors in state 
df4 = df[df["Rating"].notna()]
df4



# In[16]:


# finding average years of experience of these doctors
df5 = df4["Rating"].apply(lambda x: x.strip("%")).astype(int)
length = len(df5.index)
sum = df5.sum()
avg = sum/length 
print("Average rating of doctors in the dataset is : " , avg )


# In[17]:


df6 = df["Experience"].apply(lambda x: x.strip("years experience")).astype(int)
print(df6)
sum = df6.sum()
length = len(df6.index)
avg = sum/length 
print("The avg experience of doctors in the dataset is : ", avg )


# In[ ]:




