import numpy as np
import scipy
import math as ma
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg, optimize
from numpy import poly1d
from scipy import stats

n = 180135
m = 7
s=5
np.random.seed(180135)

Z1 = np.zeros((n))
Z2= np.zeros((n)) 
X1= np.zeros((n))
X2 = np.zeros((n))

L1 = np.zeros((n))
L2 = np.zeros((n))

k = 0
j = 0

while(k<n):
   
    U1 = np.random. uniform (size = 1)
    U2 = np.random. uniform (size = 1)
    V1 = (2*U1)-1
    V2 = (2*U2)-1
    W = V1**2+V2**2
    j+=1
    if W<1:

        Y = np.sqrt((-2* np.log(W))/W)
        Z1[k] = V1*Y
        Z2[k] = V2*Y
        X1[k] = m+s*Z1[k]
        X2[k] = m+s*Z2[k]
        L1[k] = np.exp(X1[k])
        L2[k] = np.exp(X2[k])
        k+=1
    if (k == n): break 

D1 = pd.DataFrame(X1)
D1.head()
D1.tail()

D2 = pd.DataFrame(X2)
D2.head()
D2.tail()

D3 = pd.DataFrame (L1)
D3.head()
D3.tail()
