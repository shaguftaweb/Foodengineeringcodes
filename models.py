import numpy as np
def Page(x,n):
    y=np.exp(-x)**n
    return y
def Newton(x,k):
    y=np.exp(-(k*x))
    return y
def ModifiedPage(x,k,n):
    y=np.exp(-(k*x)**n)
    return y
def HendPabis(x,a):
    y=a*np.exp(-k*x)
    return y
def Logaritmic(a,k,c,x):
    y=a*np.exp(-k*x)+c
    return y
def Twoterm(a,b,k,K,x):
    y=a*np.exp(-(k*x))+b*np.exp(-(K*x))
    return y
def Twotermexp(a,k,x):
    y=a*np.exp(-k*x)+(1-a)*np.exp(-k*a*x)
    return y
def WangSingh(a,b,x):
    y=1+a*t+b*x**2
    return y
def Thompson(y,a,b):
    x=a*np.log(y)+b*(np.log(y))**2
    return x
def Diffusion(a,b,k,x):
    y=a*np.exp(-k*x)+(1-a)*np.exp(-k*b*x)
    return y
def Midilli(a,b,k,n,x):
    y=a*np.exp(-k*x*n)+b*x
    return y
