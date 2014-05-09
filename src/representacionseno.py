#! encoding: utf8
# Ya puedo usar el español

import matplotlib.pylab as pl
import numpy as np

pl.figure(figsize=(8,6), dpi=80)

pl.subplot(1,1,1)

X = np.linspace(-np.pi*2, np.pi*2, 256, endpoint=True)
S = np.sin(X)
E = X*0

Y = np.linspace(0, np.pi/2, 40, endpoint=True)
A = (0.311104)*(Y**3)+(-0.733021)*(Y**2)+(1.253448)*Y

pl.plot(X,S, color="red", linewidth=2.5, linestyle="-", label="seno")
pl.plot(X,E, color="black", linewidth=1, linestyle="--")
pl.plot(Y,A, color="green", linewidth=2, linestyle="-", label="Aproximación")

pl.legend(loc='0')

#pl.xlim(-4.0,4.0)
pl.xlim(X.min()*1.02,X.max()*1.02)

#pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.xticks([-2*np.pi,-3*np.pi/2,-np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [r'$-2\pi$',r'$-3\pi/2$',r'$-\pi$',r'$-\frac{\pi}{2}$',r'$0$',r'$+\pi/2$',r'$+\pi$', r'$+3\pi/2$',r'$+2\pi$']
          )

pl.ylim(-1.1,1.1)
#pl.ylim(C.min()*1.1,C.max()*1.1)

#pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$']
         )

pl.title("Representacion grafica")

#pl.savefig("representacionseno.eps", dpi=72)

pl.show()