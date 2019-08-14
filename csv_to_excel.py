# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:11:06 2019

@author: Luis Rodriguez
"""

from pyexcel.cookbook import merge_all_to_a_book
import pandas as pd
# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2 
import glob

df=pd.read_csv('Passwords.csv',encoding='ISO 8859-1')

df.to_csv('Passwords1.csv',index=False)

print(df)

merge_all_to_a_book(glob.glob("Passwords1.csv"), "output.xlsx")