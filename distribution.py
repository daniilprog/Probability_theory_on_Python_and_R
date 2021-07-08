import numpy as np
import pylab
import matplotlib.pyplot as plt
x=np.linspace(-1, 1)
import sympy as sp
x=sp.symbols("x")
y=sp.symbols("y")

def gaussx (x):
    return (0.5*(sp.erf((x-62)/(67**0.5))+1))
def gaussy (p):
    return (0.5*(sp.erf((p-91.75)/(81.38**0.5))+1))
def burrx (x):
    return 1-(1+((x-33.5)/35)**6.45)**(-2.92)
def burry (p):
    return 1-(1+((p-63.5)/36.4)**5.72)**(-3.29)


fx=[]
fy=[]
gx=[]
gy=[]
for i in range (53):
    gx.append(gaussx(i+37))
    gy.append(gaussy(i+67))
    fx.append(burrx(i+37))
    fy.append(burry(i+67))
    
x = np.arange(37,90)
y = np.arange(67, 120)

pylab.plot (x, fx, color='yellow',label='Burr(x)', linewidth = 4)
pylab.plot (y, fy, color='violet',label='Burr(y)', linewidth = 4)
pylab.plot (x, gx, linestyle = '-.', color='red',label='Gauss(x)', linewidth = 1)
pylab.plot (y, gy, color='black', linestyle = '-.',label='Gauss(y)', linewidth = 1)
pylab.xlabel('x,y')
pylab.ylabel('F(x),F(y)')
pylab.legend()
pylab.grid()
pylab.title ("График функций распределения")
plt.show()

"""
Поиск отклонений
"""
supx=0
supy=0
for i in range (53):
    razx=abs(gaussx(i+37)-burrx(i+37))
    razy=abs(gaussy(i+67)-burry(i+67))
    if razx>supx:
        supx=razx
    if razy>supy:
        supy=razy
lamx=supx*(1000**0.5)
lamy=supy*(500**0.5)
print (supx, supy)
print(lamx, lamy)    

"""
Плотность вероятности
"""  
x=sp.symbols("x")
y=sp.symbols("y")
def ngaussx(x):
    return (1/(5.788*(2*3.14)**0.5)*sp.exp(-(x-62)**2/67))*5
def ngaussy(y):
    return (1/(6.38*(2*3.14)**0.5)*sp.exp(-(y-91.75)**2/81.38))*5
def nburrx (x):
    return (18.834*((x-33.5)/35)**(5.45)/(1+((x-33.5)/35)**6.45)**3.92)/35*5
def nburry (y):
    return (18.82*((y-63.5)/36.4)**(4.72)/(1+((y-63.5)/36.4)**5.72)**4.29)/36.4*5

gx=[]
gy=[]
bx=[]
by=[]
for i in range (53):
    gx.append(ngaussx(i+37))
    gy.append(ngaussy(i+67))
    bx.append(nburrx(i+37))
    by.append(nburry(i+67))  
    
x = np.arange(37,90)
y = np.arange(67, 120)
nx=[[45,50,55,60,65,70,75,80],[0,0.05,0.15,0.35,0.3,0.1,0.05,0]]
ny=[[75,80,85,90,95,100,110,120],[0,0.05,0.15,0.45,0.2,0.1,0.05,0]]

pylab.plot (x, bx, color='yellow',label='Burr(x)', linewidth = 4)
pylab.plot (y, by, color='violet',label='Burr(y)', linewidth = 4)
pylab.plot (x, gx, linestyle = '-.', color='red',label='Gauss(x)', linewidth = 1)
pylab.plot (y, gy, color='black', linestyle = '-.',label='Gauss(y)', linewidth = 1)
pylab.plot (nx[0], nx[1], color='indigo', linestyle = '--',label='Empirical(x)', linewidth = 1)
pylab.plot (ny[0], ny[1], color='blue', linestyle = '--',label='Empirical(y)', linewidth = 1)
pylab.xlabel('x,y')
pylab.ylabel('f(x),f(y)')
pylab.legend()
pylab.grid()
pylab.title ("График функций плотности вероятности")
plt.show()
