# -*- coding: utf-8 -*-
"""DFlab5_192063Github.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OeUJOoG3AR-MLcHnB3MKJbC9EY7564BZ
"""

import pandas as pd #biblioteka za tabelarni podatoci. Pandas ima dataframe i toa e klasata glavna za pristap do site podatoci. 
df = pd.read_csv('/content/logs.csv') #import na .csv fajlot

print(df) #print na fajlot

from sklearn.model_selection import train_test_split #biblioteka so gi deli podatocite na x i y train i test

TrenirackoX_train,TrenirackoX_test,TestirackoY_train,TestirackoY_test = train_test_split(df.iloc[:,:2],df['Action'],test_size=0.2) #pravime train i test mnozestva modeli (gi zema site redici i prvite dve koloni)

from xgboost import XGBClassifier

model = XGBClassifier(max_depth=50,n_estimators=200,learning_rate=0.16) #pomala rata za ucenje za potocno

model.fit(TrenirackoX_train,TestirackoY_train)

predict = model.predict(TrenirackoX_test) #predviduvanje

from sklearn.metrics import classification_report, confusion_matrix  #za evaluacija kolku e tocen modelot e clasification(fi-score najcesto se gleda), a confusion e za kako pogoduvalo

print(classification_report(TestirackoY_test,predict)) #pecatenje