# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:06:39 2020

@author: N.VISHWANATH
"""

import pandas as pd
import os
os.chdir(r'C:\Users\N.VISHWANATH\\Downloads')

data1 = pd.read_csv("locations5.csv",encoding = 'iso-8859-1')
data2 = pd.read_csv("locations6.csv",encoding = 'iso-8859-1')
data=data1.append(data2, ignore_index = True)
data.head(2)
data.shape

df = data[['Place Name','review']].copy()

df['review'] = df.groupby(['Place Name'])['review'].transform(lambda x : ' '.join(x)) 
df = df.drop_duplicates().reset_index(drop=True)
df

df['review'] = df['review'].replace('...','.')
df['review'] = df['review'].replace('..','.')

review_summ = str()
for review in df['review']:
    review_summ = review_summ + " " + review
review_summ = review_summ.replace('...','.')
review_summ = review_summ.replace('..','.')

import gensim
from gensim.summarization import summarize

a=0
df_gensim = df.copy()
for i,review in enumerate(df_gensim['review']):
    result = summarize(review,ratio=0.2)
    #full_summ = "".join(result)
    result= result.replace("\n"," ")
    df_gensim.loc[i,'summary'] = result
    a=a+1
    print(a)
    
text= df_gensim['summary'][0]#.replace("\n"," ")
text

df_gensim.iloc[:2]


new_data = df_gensim[['Place Name','summary']]
#new_data.drop('review',axis=1,inplace=True)
new_data.to_csv(r'G:\Praxis\Capstone\data\five.csv', index = False, header=True)