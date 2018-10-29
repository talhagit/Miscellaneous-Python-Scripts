# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:28:34 2017

@author: Talha.Iftikhar
"""

import pandas as pd
import csv
lista=[['a','b'],['1','2']]
####################################################################################################
zip1=pd.read_csv('ColgateScrap-Result\zip5000updated.csv')
zip2=pd.read_csv('ColgateScrap-Result\zip10000updated.csv')
zip3=pd.read_csv('ColgateScrap-Result\zip15000updated.csv')
zip4=pd.read_csv('ColgateScrap-Result\zip20000updated.csv')
zip5=pd.read_csv('ColgateScrap-Result\zip25000updated.csv')
zip6=pd.read_csv('ColgateScrap-Result\zip30000updated.csv')
zip7=pd.read_csv('ColgateScrap-Result\zip35000updated.csv')
zip8=pd.read_csv('ColgateScrap-Result\ziplastupdated.csv')

finalzip=[zip1,zip2,zip3,zip4,zip5,zip6,zip7,zip8]
filecombine=pd.concat(finalzip)

filecombine.head(4)

new=pd.read_csv('testpanda.csv')
new.drop_duplicates()
ColgateScraplist=filecombine.drop_duplicates()
filecombine.info()
ColgateScraplist.info()
ColgateScraplist.to_csv('FinalColgate_DentistList.csv')
ColgateScraplist.groupby(['Dentist Name', 'Phone']).size()
ColgateScraplist.duplicated()==True.size()
ColgateScraplist.duplicated().count()
new=ColgateScraplist.drop_duplicates()
ColgateScraplist.info()
new2.info()
new=ColgateScraplist.duplicated().sum()
new2=pd.DataFrame(new,columns=['value'])
new2.value.unique()

df['is_duplicated'] = df.duplicated(['order_id', 'order_item_cd'])
zip1['is_duplicated']=zip1.duplicated()
onemorezip=zip1[zip1['is_duplicated']==True]
new=onemorezip.sort_values(by='Dentist Name')
