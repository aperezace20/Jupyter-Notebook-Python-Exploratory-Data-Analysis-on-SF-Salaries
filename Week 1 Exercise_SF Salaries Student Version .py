#!/usr/bin/env python
# coding: utf-8

# # Week 1 Exercise: SF Salaries 
# 
# 

# ### Step 1: Import libraries: pandas and seaborn
# 

# In[3]:


import pandas as pd
import seaborn as sns 


# In[ ]:





# ### Step 2: Read Data
# 
# ##### code for reference
# 
# #### If you are using Jupyter notebook:
# first save the salaries.csv to your local folder:
# 
# sal = pd.read_csv("`your path here`/salaries.csv")
# 
# #### If you are using google colab, please mount your Google Drive on your runtime using an authorization code:
# from google.colab import drive
# 
# drive.mount('/content/drive')
# 
# path = '/content/drive/`your path here`/salaries.csv'
# 
# sal = pd.read_csv(path)
# 
# 
# 
# #### Feel free to use any other prefered IDEs for python.
# 

# In[4]:


sal = pd.read_csv('C:/Users/apere/OneDrive/Desktop/CIS 508/Salaries.csv')


# In[ ]:





# ### Step 3: Follow the instructions below and answer questions.
# 
# 

# **Check the head of the DataFrame**
# ##### code for reference:
# sal.head()
# 

# In[5]:


sal.head()


# **Q1: How many columns and rows are there in the dataset?** 
# 
# ##### code for reference:
# sal.shape
# 
# 

# In[6]:


sal.shape


# **Q2: What the average of total pay ['TotalPay'] of San Francisco’s city employees?**
# 
# ##### code for reference:
# You can either use:
# 
# sal.desribe() or 
# 
# sal["TotalPay"].mean()

# In[7]:


sal["TotalPay"].mean()


# 
# 
# 
# **Q3: What is the maximum benefit received by a city employee?** 
# 
# ##### code for reference:
# 
# sal.desribe()  or 
# 
# sal['Benefits'].max()

# In[8]:


sal['TotalPay'].max()


# **Q4: How much benefits did JOSEPH DRISCOLL receive?** (Hint: Use 'TotalPayBenefits' variable)
# 
# ##### code for reference:
# sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

# In[15]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# **Q5: What is the average ’total benefits’ received by Special Nurse?**
# 
# ##### code for reference
# sal[sal['JobTitle']=='Special Nurse']['TotalPayBenefits'].mean()

# In[9]:


sal[sal['JobTitle']=='Special Nurse']['TotalPayBenefits'].mean()


# **Q6: What is the name of the employee in the 3500th record?**
# 
# ##### code for reference
# sal.iloc[ ]

# In[11]:


sal.iloc[:3500]


# In[ ]:





# **Q7: How many missing values does variable 'BasePay' have?** 
# 
# ##### code for reference
# 
# sal.isnull().sum()

# In[18]:


sal.isnull().sum()


# **Q8: Create a boxplot of TotalPay variable across different job status (Status). Which of the following statements is NOT true?** 
# 
# ##### code for reference
# sns.boxplot(x=,y=,data=)

# In[23]:


sns.boxplot(x='Status',y='TotalPay',data=sal)


# **Q9: Create a boxplot of BasePay variable across different years (Year variable). Which of the following statement is NOT true?** 
# ##### code for reference 
# sns.boxplot(x=,y=,data=)

# In[24]:


sns.boxplot(x='Year',y='BasePay',data=sal)


# **Q10: Create a histogram for TotalPay variable. Which of the following statement is NOT true?** 
# 
# ##### code for reference 
# sns.histplot(sal['variable name here'])

# In[25]:


sns.histplot(sal['TotalPay'])

