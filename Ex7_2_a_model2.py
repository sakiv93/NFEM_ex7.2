import numpy as np
import matplotlib.pyplot as plt
import math

#Input Parameters
sigma_m=0
sigma_0=100
gamma=10
eta=1e5
alpha=1e5
n=1
c=1
delta_t_c=2/gamma
delta_t_0_1=0.05*delta_t_c
delta_t_0_3=0.15*delta_t_c
delta_t_1=1*delta_t_c
#delta_t=0.1
final_time=5
c=1


#function which returns sigma and times
def sigma(sigma_m,final_time,delta_t,alpha,c,sigma_0,n):
    sigmas=np.array([sigma_m])
    times=np.array([0])
    iterations=final_time/delta_t
    for i in range(round(iterations)):
        sigma_m_1=sigma_m+(alpha*c*delta_t)/(1+(sigma_m/sigma_0)**n)
        sigmas=np.append(sigmas,sigma_m_1)
        times=np.append(times,(i+1)*delta_t)
        sigma_m=sigma_m_1
    return times,sigmas


fig,ax=plt.subplots()
times_0_1,sigmas=sigma(sigma_m,final_time,delta_t_0_1,alpha,c,sigma_0,n)
ax.plot(times_0_1,sigmas,marker='o')
times_0_3,sigmas=sigma(sigma_m,final_time,delta_t_0_3,alpha,c,sigma_0,n)
ax.plot(times_0_3,sigmas,marker='*')
times_1,sigmas=sigma(sigma_m,final_time,delta_t_1,alpha,c,sigma_0,n)
ax.plot(times_1,sigmas)

plt.show()



