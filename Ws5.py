import numpy as np
import scipy.stats as stats

arr = np.random.randn(1000)
mean = np.mean(arr)
median = np.median(arr)
variance = np.var(arr)

print(f"Mean: {mean:.6f}, Median: {median:.6f}, Variance: {variance:.6f}")

import numpy as np
from scipy import fftpack

a2 = np.random.rand(8,8)
dft2 = fftpack.fft2(a2)
print("DFT of 2D array:\n", dft2)

import numpy as np
from scipy import linalg

A = np.array([[4,2,1],[0,1,-1],[2,3,5]], dtype=float)
detA = linalg.det(A)
invA = linalg.inv(A)
eigvals, eigvecs = linalg.eig(A)

print("Determinant:", detA)
print("Inverse:\n", invA)
print("Eigenvalues:", eigvals)


import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0,10,11)
y = np.sin(x)
f_cubic = interpolate.interp1d(x,y,kind='cubic')

xnew = np.linspace(0,10,201)
y_cub = f_cubic(xnew)

plt.plot(x, y, 'o', label='data')
plt.plot(xnew, y_cub, '-', label='cubic interp')
plt.legend(); plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

fs = 500
t = np.linspace(0,1,fs,endpoint=False)
sig = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*80*t)

numtaps = 101
cutoff = 20
fir = firwin(numtaps, cutoff/(fs/2))
filtered = lfilter(fir, 1.0, sig)

plt.plot(t, sig, label='noisy')
plt.plot(t, filtered, label='filtered')
plt.legend(); plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
np.random.seed(0)
sales = np.random.randint(200,1000,size=(12,4))
products = ["P1","P2","P3","P4"]
df = pd.DataFrame(sales, index=months, columns=products)
df['Total'] = df.sum(axis=1)

print(df)
print("Best month:", df['Total'].idxmax())
print("Worst month:", df['Total'].idxmin())

df['Total'].plot(marker='o')
plt.show()

import numpy as np
import pandas as pd

students = ["Arin","Aditya","Chirag","Gurleen","Kunal"]
marks = np.array([[85,78,92,88],[79,82,74,90],[90,85,89,92],[66,75,80,78],[70,68,75,85]])
df = pd.DataFrame(marks, index=students, columns=["Math","Physics","Chemistry","English"])
df['Total'] = df.sum(axis=1)
df['Average'] = df.mean(axis=1)

print(df)
print("Top student:", df['Total'].idxmax())
print("Bottom student:", df['Total'].idxmin())

import numpy as np
from scipy import optimize

tdata = np.array([0,1,2,3,4,5], dtype=float)
vdata = np.array([2,3.1,7.9,18.2,34.3,56.2], dtype=float)

def quad(t,a,b,c):
    return a*t**2 + b*t + c

popt, _ = optimize.curve_fit(quad, tdata, vdata)
print("Fitted coefficients:", popt)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = ["Arin","Aditya","Chirag","Gurleen","Kunal"]
marks = np.array([[85,78,92,88],[79,82,74,90],[90,85,89,92],[66,75,80,78],[70,68,75,85]])
df = pd.DataFrame(marks, index=students, columns=["Math","Physics","Chemistry","English"])

df.plot(kind='bar')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

tdata = np.array([0,1,2,3,4,5], dtype=float)
vdata = np.array([2,3.1,7.9,18.2,34.3,56.2], dtype=float)

def quad(t,a,b,c):
    return a*t**2 + b*t + c

popt, _ = optimize.curve_fit(quad, tdata, vdata)
tfine = np.linspace(tdata.min(), tdata.max(), 200)
plt.scatter(tdata, vdata, label='data')
plt.plot(tfine, quad(tfine, *popt), label='fit')
plt.legend(); plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, interpolate

years = np.array([2000,2005,2010,2015,2020])
pop = np.array([50,55,70,80,90])

r, _ = stats.pearsonr(years, pop)
print("Pearson r:", r)

f = interpolate.interp1d(years, pop, kind='linear')
xnew = np.arange(2000,2021)
ynew = f(xnew)

plt.plot(years, pop, 'o')
plt.plot(xnew, ynew, '-')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

coeffs = [3, -5, 2, -8]
roots = np.roots(coeffs)
print("Roots:", roots)

x = np.linspace(-3,3,400)
pvals = np.polyval(coeffs, x)

plt.plot(x, pvals)
plt.axhline(0, color='k')
plt.show()

import os, time, random, string
import matplotlib.pyplot as plt

def random_text_mb(mb):
    N = mb * 1024 * 1024
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=N))

sizes = [1,2,4]
times = []

for s in sizes:
    fname = f"temp_{s}MB.txt"
    with open(fname,'w') as f:
        f.write(random_text_mb(s))
    t0 = time.time()
    with open(fname,'r') as f:
        data = f.read().upper()
    elapsed = time.time() - t0
    times.append(elapsed)
    os.remove(fname)
    print(f"Size {s}MB -> Time {elapsed:.3f}s")

plt.plot(sizes, times, marker='o')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x): return x**4 - 3*x**3 + 2
def df(x): return 4*x**3 - 9*x**2

crit = np.roots([4, -9, 0, 0])
crit_real = [r.real for r in crit if abs(r.imag) < 1e-8]
print("Critical points:", crit_real)

x = np.linspace(-2,3,400)
y = f(x)

plt.plot(x, y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

wn = 2.0
zeta = 0.2

def deriv(y, t):
    theta, omega = y
    dtheta = omega
    domega = -2*zeta*wn*omega - (wn**2)*theta
    return [dtheta, domega]

tspan = np.linspace(0,20,1000)
y0 = [1.0, 0.0]
sol = odeint(deriv, y0, tspan)

theta = sol[:,0]
plt.plot(tspan, theta)
plt.show()
