# -*- coding: utf-8 -*-

#author: Schweikardt & Spenner
#version: 1.0 May 2017

import pandas as pd
import numpy as np
import os
from scipy.stats import skew

###Only apply if default directories are not working###

###Change working directory###
f = "C:\\Users\\Felix Schweikardt\\Dropbox\\Seminararbeit FZI - Softsensor\\Datensätze\\12-05-2017"
l = "/Users/leopoldspenner/Dropbox/Seminararbeit FZI - Softsensor/Datensätze/12-05-201/Fertige_Sets/"
os.chdir(l)

###check if change of working directory worked###
cwd = os.getcwd()

#read the csv files
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
training_data = pd.read_csv('Predictors_1.csv', parse_dates=['Time'], date_parser=dateparse)
training_data = training_data.set_index('Time')
