#coding: utf-8
"""
Created on 08/05/2022
Domaine : Optique CPGE
Sous-Domaine : Diffraction
Chapitre : Diffraction par des structures périodiques
Appellation : Etude de la fonction des réseaux
@author: Antonin
"""
#-Clean Workspace
get_ipython().magic('reset -sf')
#
#-Import libraries
import numpy as np
# import scipy.interpolate as spinterp
#
#-Plot figures
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.close('all')
# mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.family'] = 'STIXGeneral'
# mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['grid.linestyle'] = '--'
mpl.rcParams['figure.dpi'] = 110
# mpl.rcParams['axes.grid'] = True
# mpl.rcParams['axes.grid.axis'] = 'both'
# mpl.rcParams['axes.grid.which'] = 'minor'
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['figure.subplot.hspace']=  0.6
mpl.rcParams['lines.linewidth']  = 1.4
mpl.rcParams['legend.fontsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['figure.figsize'] = 1.5*7.4, 1.5*5.8
from mpl_toolkits.mplot3d import Axes3D
#
nf = 0 #index for figures
# 
"""
Etude de l'influence de N
"""
# # 
# x = np.linspace(0,2*np.pi,1000)
# # 
# nf = nf+1
# plt.figure(nf)
# # 
# N = 2
# N1 = N
# F = (np.sin(N*x)/np.sin(x))**2/N**2
# plt.plot(x,F,'--')
# N = 4
# N10 = N
# F = (np.sin(N*x)/np.sin(x))**2/N**2
# plt.plot(x,F,'-.')
# N = 20
# N2 = N
# F = (np.sin(N*x)/np.sin(x))**2/N**2
# plt.plot(x,F)
# N = 200
# N3 = N
# F = (np.sin(N*x)/np.sin(x))**2/N**2
# plt.plot(x,F)
# # 
# plt.ylabel("$(1/N^2)\cdot(\sin(Nx)/\sin(x))^2$")
# plt.xlabel("$x=\\pi a \\left(\sin(i')\\pm \sin(i)\\right)/\\lambda$")
# plt.grid(True,'major','both')
# plt.legend((('N=%.0f'%N1),('N=%.0f'%N10),('N=%.0f'%N2),('N=%.0f'%N3)),loc='upper right')
# plt.xlim([x[0],x[-1]])
# plt.title("Fonction des réseaux")
# 
"""
Etude de l'influence de lambda pour une direction de diffraction donnée
"""
# 
N = 20
sini = np.linspace(-0.999999,0.999999,1000)
# 
lam1 = 500*10**-9
a = 0.5*10**-3
lam2 = 503*10**-9
# 
nf = nf+1
plt.figure(nf)
plt.subplot(2,1,1)
lam = lam1
F = (np.sin(N*np.pi*(a/lam)*sini)/np.sin(np.pi*(a/lam)*sini))**2
F = F/N**2
plt.plot(sini,F)
plt.subplot(2,1,2)
lam = lam2
F = (np.sin(N*np.pi*(a/lam)*sini)/np.sin(np.pi*(a/lam)*sini))**2
F = F/N**2
plt.plot(sini,F)
