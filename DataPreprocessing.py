#author: Schweikardt & Spenner
#version: 1.0 May 2017

import pandas as pd
import numpy as np
import os
from scipy.stats import skew

# ###Only apply if default directories are not working###
#
# ###Change working directory###
# os.chdir("C:\\Users\\Felix Schweikardt\\PycharmProjects\\project_bold_eagle_V3")
#
# ###check if change of working directory worked###
# cwd = os.getcwd()

#read the csv files
training_data = pd.read_csv('train1.csv')