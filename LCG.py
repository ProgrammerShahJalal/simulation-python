import numpy as np
import scipy
import math as ma
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg, optimize
from numpy import poly1d
from scipy import stats

a = 8**5
c= 11211
m = 2**(31)-3 
x = 180135
n = 200000

def f(X): return (a*x + c)%m 
def f1(z): return 9/(np.pi*(1+(9*z-4)**2))

p = 4 
S = np.zeros((n,p))

for i in range (0,n,1):
    S[i,0] = i
    if i == 0: S[i,1] = f(x) 
    elif i > 0: S[i,1] = f(S[i-1,1])
    S[i,2]= round(S[i,1]/m, 3)
    S[i,3]= round(f1(S[i,2]),3)
    
DT= pd.DataFrame(S) 
DT.columns = ['ID', 'X', 'U(0,1)', 'f(U)']
DT.head()
DT.tail()

UU = DT['f(U)']
UU
Ical = np.mean(UU)
Ical

from scipy.integrate import quad
Integ = quad (f1,0,1)
Integ
