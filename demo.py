#!/usr/bin/env python
# coding: utf-8

import datetime
import os

import matplotlib.dates as mdates
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import pandas

import benford

pandas.set_option('use_inf_as_na', True)

COVID_Raw = pandas.read_csv("./COVID_Raw.csv")
COVID_Raw['Date'] = pandas.to_datetime(COVID_Raw['Date'])
COVID_Raw = COVID_Raw.set_index('Date')
COVID_Raw[['Tested_Cum']] = COVID_Raw[['Tested_Raw']].cumsum()
COVID_Raw[['Tested_Delta']] = COVID_Raw[['Tested_Raw']].pct_change()
COVID_Raw[['Positive_Cum']] = COVID_Raw[['Positive_Raw']].cumsum()
COVID_Raw[['Positive_Delta']] = COVID_Raw[['Positive_Raw']].pct_change()
COVID_Raw[['Recovered_Cum']] = COVID_Raw[['Recovered_Raw']].cumsum()
COVID_Raw[['Recovered_Delta']] = COVID_Raw[['Recovered_Raw']].pct_change()
COVID_Raw[['Died_Cum']] = COVID_Raw[['Died_Raw']].cumsum()
COVID_Raw[['Died_Delta']] = COVID_Raw[['Died_Raw']].pct_change()
COVID_Raw[['Hospitalizations_Cum']] = COVID_Raw[['Hospitalizations_Raw']].cumsum()
COVID_Raw[['Hospitalizations_Delta']] = COVID_Raw[['Hospitalizations_Raw']].pct_change()

COVID_Raw['Tested_Positive_Ratio'] = (COVID_Raw['Positive_Raw'] / COVID_Raw['Tested_Raw']) * 100
COVID_Raw['Active_Infections'] = (COVID_Raw['Positive_Cum'] - (COVID_Raw['Recovered_Cum'] + COVID_Raw['Died_Cum']))

COVID_Raw[['Positive_2D_Mean']] = COVID_Raw[['Positive_Raw']].rolling(2).mean()
COVID_Raw[['Positive_3D_Mean']] = COVID_Raw[['Positive_Raw']].rolling(3).mean()

COVID_Raw = COVID_Raw.fillna(0)

column_order = ['Tested_Raw', 'Tested_Cum', 'Tested_Delta', 'Positive_Raw', 'Positive_Cum', 'Positive_Delta', 'Positive_2D_Mean', 'Positive_3D_Mean', 'Recovered_Raw', 'Recovered_Cum', 'Recovered_Delta', 'Died_Raw', 'Died_Cum', 'Died_Delta', 'Hospitalizations_Raw', 'Hospitalizations_Cum', 'Hospitalizations_Delta', 'Tested_Positive_Ratio', 'Active_Infections']


