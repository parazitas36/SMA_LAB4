import matplotlib.pyplot as plot
import numpy as np

m1 = 0.05
m2 = 0.3
v0 = 100
k = 0.01
ts = 3
k1 = 0.05
k2 = 0.01
t0 = 0
h0 = 0
tmax = 10
m = m1 + m2 
g=9.8

def dvdts(time, v1, v2):
    if time <= ts:
        # Kunai kartu
        if v1 >= 0:
            # Kyla
            dvdt1 = (m * g + k * np.square(v1)) / m
            dvdt2 = (m * g + k * np.square(v2)) / m
            return dvdt1, dvdt2
        else:
            # Krenta
            dvdt1 = (m * g - k * np.square(v1)) / m
            dvdt2 = (m * g - k * np.square(v2)) / m
            return dvdt1, dvdt2
    if time > ts:
        # Pirmas kunas
        if v1 >= 0:
            dvdt1 = (m1 * g + k1 * np.square(v1)) / m1 # Kyla
        else:
            dvdt1 = (m1 * g - k1 * np.square(v1)) / m1 # Krenta
        # Antras kunas
        if v2 >= 0:
            dvdt2 = (m2 * g + k2 * np.square(v2)) / m2 # Kyla
        else:
            dvdt2 = (m2 * g - k2 * np.square(v2)) / m2 # Krenta
        return dvdt1, dvdt2

velocities = []
labelsv = []

heights = []
labelsh = []

def rk4(dt):
    t= t0
    v1 = v0
    v2 = v0
    h1 = h0
    h2 = h0

    tt = []
    v1_arr = []
    v2_arr = []
    h1_arr = []
    h2_arr = []

    while t <= tmax:
        tt.append(t)
        v1_arr.append(np.abs(v1))
        v2_arr.append(np.abs(v2))
        h1_arr.append(h1)
        h2_arr.append(h2)

        dvdt1_1, dvdt2_1 = dvdts(t, v1, v2)
        v1_1 = v1 - dt / 2 * dvdt1_1
        v2_1 = v2 - dt / 2 * dvdt2_1

        dvdt1_2, dvdt2_2 = dvdts(t, v1_1, v2_1)
        v1_2 = v1 - dt / 2 * dvdt1_2
        v2_2 = v2 - dt / 2 * dvdt2_2

        dvdt1_3, dvdt2_3 = dvdts(t, v1_2, v2_2)
        v1_3 = v1 - dt / 2 * dvdt1_3
        v2_3 = v2 - dt / 2 * dvdt2_3

        dvdt1_4, dvdt2_4 = dvdts(t, v1_3, v2_3)

        v1 -= dt / 6 * (dvdt1_1 + 2 * dvdt1_2 + 2 * dvdt1_3 + dvdt1_4)
        v2 -= dt / 6 * (dvdt2_1 + 2 * dvdt2_2 + 2 * dvdt2_3 + dvdt2_4)
        h1 += dt * v1
        h2 += dt * v2
        t += dt
    
    velocities.append(plot.plot(tt, v1_arr))
    velocities.append(plot.plot(tt, v2_arr))
   
    labelsv.append("Pirmo kūno greitis žingsn:" + str(dt))
    labelsv.append("Antro kūno greitis žingsn:" + str(dt))

    heights.append(plot.plot(tt, h1_arr))
    heights.append(plot.plot(tt, h2_arr))
    
    labelsv.append("Pirmo kūno aukštis žingsn:" + str(dt))
    labelsv.append("Antro kūno aukštis žingsn:" + str(dt))


rk4(0.3)
rk4(0.1)
rk4(0.01)

taskas = plot.axvline(x=ts, color='r', linestyle='dotted')
plot.ylim(0)
plot.ylabel("Aukštis")
plot.xlabel("Laikas s")
velocities.append(taskas)
labelsv.append("Išsiskirimo momentas")
plot.legend(velocities, labels=labelsv)
plot.show()
