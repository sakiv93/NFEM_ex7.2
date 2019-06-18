import numpy as np
import matplotlib.pyplot as plt
import math

#Input Parameters
sigma_m=0
gamma=10
eta=1e5
c=1
delta_t_c=2/gamma
delta_t_0_1=0.1*delta_t_c
delta_t_0_3=0.3*delta_t_c
delta_t_1=1*delta_t_c
#delta_t=0.1
final_time=5
c=1
epsilon=c


#function which returns sigma and times
def sigma(gamma,delta_t,eta,epsilon,final_time,sigma_m):
    sigmas=np.array([sigma_m])
    times=np.array([0])
    iterations=final_time/delta_t
    print('iterations:',iterations)
    for i in range(round(iterations)):
        sigma_m_1=(sigma_m*(1-gamma*(delta_t)))+(eta*epsilon*delta_t)
        sigmas=np.append(sigmas,sigma_m_1)
        times=np.append(times,(i+1)*delta_t)
        sigma_m=sigma_m_1
    return times,sigmas


fig,ax=plt.subplots()
times_0_1,sigmas=sigma(gamma,delta_t_0_1,eta,epsilon,final_time,sigma_m)
ax.plot(times_0_1,sigmas)
times_0_3,sigmas=sigma(gamma,delta_t_0_3,eta,epsilon,final_time,sigma_m)
ax.plot(times_0_3,sigmas)
times_1,sigmas=sigma(gamma,delta_t_1,eta,epsilon,final_time,sigma_m)
ax.plot(times_1,sigmas)

plt.show()



