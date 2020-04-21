#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:06:39 2020

@author: yibeihe
"""


import pandas as pd

df = pd.read_csv('../input/complaints.csv')
df = df[['Date received', 'Product', 'Company', ]]
df['Date received'] = pd.to_datetime(df['Date received'])
df = df.set_index('Date received')
df = df.groupby([df['Product'],df.index.year]).agg(['count','nunique'])

df.columns = ['Total Num of Complaints','Numb of Companies Receiving a Complaint']
df['Highest Percentage'] = df['Numb of Companies Receiving a Complaint'] / df['Total Num of Complaints'] * 100
df['Highest Percentage'] = df['Highest Percentage'].round(0).astype(int)
df = df.reset_index()
df.to_csv('../output/report.csv', index=False, header=False)