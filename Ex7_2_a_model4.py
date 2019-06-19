import numpy as np
import matplotlib.pyplot as plt
import math
from newton_raphson import newton_raphson

#Input Parameters
sigma_m=0
sigma_0=100
alpha=1e5
gamma=10
eta=1e5
c=1
n=1
delta_t_0_1=0.1
delta_t_0_3=0.3
delta_t_1=1
final_time=5
sigma_initial_guess=0


#function which returns sigma and times
def sigma(sigma_m,final_time,delta_t,alpha,c,sigma_0,n,sigma_initial_guess):
    sigmas=np.array([sigma_m])
    times=np.array([0])
    iterations=final_time/delta_t
    #print('iterations:',iterations)
    for i in range(round(iterations)):
        #sigma_m_1=sigma_m+(alpha*c*delta_t/(1+(sigma_m_1/sigma_0)**n))
        sigma_m_1=newton_raphson(sigma_initial_guess,sigma_m,alpha,delta_t,sigma_0,n,c)
        sigmas=np.append(sigmas,sigma_m_1)
        times=np.append(times,(i+1)*delta_t)
        sigma_m=sigma_m_1
    return times,sigmas

#Analytical solution
t=np.linspace(0,5,100)
#print(t)
sigma_analyticals=np.array([])
for i in range(len(t)):
    sigma_analytical=(sigma_0**2+2*alpha*c*sigma_0*t[i])**(1/2)-sigma_0
    sigma_analyticals=np.append(sigma_analyticals,sigma_analytical)

print(len(t))
print(len(sigma_analyticals))




fig,ax=plt.subplots()
times_0_1,sigmas=sigma(sigma_m,final_time,delta_t_0_1,alpha,c,sigma_0,n,sigma_initial_guess)
ax.plot(times_0_1,sigmas,marker='o')
times_0_3,sigmas=sigma(sigma_m,final_time,delta_t_0_3,alpha,c,sigma_0,n,sigma_initial_guess)
ax.plot(times_0_3,sigmas,marker='x')
times_1,sigmas=sigma(sigma_m,final_time,delta_t_1,alpha,c,sigma_0,n,sigma_initial_guess)
ax.plot(times_1,sigmas,marker='^')

ax.plot(t,sigma_analyticals,marker='*')

plt.show()



