import numpy as np
import scipy
import math as ma
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg, optimize
from numpy import poly1d
from scipy import stats

np.random.seed(180135)
n = 180135
m = 12
s=15

def f(x): return m+s*np.tan(np.pi*(x-0.5))

p=3
S = np.zeros((n,p))

for i in range (0,n,1):
    S[i,0] = i 
    g= np.random.uniform(size = 1)
    S[i,1] = g
    X = f(g)
    S[i,2] = X

DT = pd.DataFrame(S)
DT
DT.columns=['ID', 'U', 'X(mu = 12, sigma = 15)']
print (DT)

XX = DT['X(mu = 12, sigma = 15)']
XX

Mean = np.mean (XX)
Mean

var = np.var(XX)
var

print(var)
