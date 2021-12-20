import numpy as np
import matplotlib.pyplot as plot

m1 = 0.05
m2 = 0.3
v0 = 100
k = 0.01
t = 3
k1 = 0.05
k2 = 0.01
tmax = 10
m = m1 + m2 
g=9.8

arguments = []
labels = []


def euler(dt, showVelocity, showHeight):
    v = v0
    v_arr = []
    v_arr.append(v)
    dv_dt = 0

    h = 0
    h_arr = []
    h_arr.append(0)

    t_arr = []
    t_arr.append(0)
    t_now = 0

    isRising = True
    isLanded = False

    v2 = v0
    v2_arr = []
    v2_arr.append(v)
    dv2_dt = 0

    h2 = 0
    h2_arr = []
    h2_arr.append(0)

    t2_arr = []
    t2_arr.append(0)
    t2_now = 0

    isRising2 = True
    isLanded2 = False
    now = 0

    while now < tmax:
        if now < t: 
            if isRising:
                dv_dt = (m*g + k*np.square(v))/m
                dv2_dt = dv_dt
                v = v - dv_dt * dt
                v2 = v
                v_arr.append(np.abs(v))
                v2_arr.append(np.abs(v2))
                isRising = True if v > 0 else False
                isRising2 = True if v > 0 else False
                h = h + v*dt
                h2 = h
                h_arr.append(h)
                h2_arr.append(h2)
            else:
                dv_dt = (m*g - k*np.square(v))/m
                dv2_dt = dv_dt
                v = v - dv_dt * dt
                v2 = v
                v_arr.append(np.abs(v))
                v2_arr.append(np.abs(v2))
                h = h + v*dt
                h2 = h
                h_arr.append(h)
                h2_arr.append(h2)
                if(h <= 0):
                    isLanded = True
                    isLanded2 = True
            t_now += dt
            t_arr.append(t_now)
            t2_now += dt
            t2_arr.append(t2_now)
            if isLanded:
                break
        else:
            if not isLanded:
                if isRising:
                    dv_dt = (m1*g + k1*np.square(v))/m1
                    v = v - dv_dt * dt
                    v_arr.append(np.abs(v))
                    isRising = True if v > 0 else False
                    h = h + v*dt
                    h_arr.append(h)
                else:
                    dv_dt = (m1*g - k1*np.square(v))/m1
                    v = v - dv_dt * dt
                    v_arr.append(np.abs(v))
                    h = h + v*dt
                    h_arr.append(h)
                    if(h <= 0):
                        isLanded = True
                t_now += dt
                t_arr.append(t_now)
            if not isLanded2:
                if isRising2:
                    dv2_dt = (m2*g + k2*np.square(v2))/m2
                    v2 = v2 - dv2_dt * dt
                    v2_arr.append(np.abs(v2))
                    isRising2 = True if v2 > 0 else False
                    h2 = h2 + v2*dt
                    h2_arr.append(h2)
                else:
                    dv2_dt = (m2*g - k2*np.square(v2))/m2
                    v2 = v2 - dv2_dt * dt
                    v2_arr.append(np.abs(v2))
                    h2 = h2 + v2*dt
                    h2_arr.append(h2)
                    if(h2 <= 0):
                        isLanded2 = True
                t2_now += dt
                t2_arr.append(t2_now)
            if isLanded and isLanded2:
                break
            
        now+=dt


    pirmoMax = 0
    antroMax = 0
    for i in range(0, len(h_arr)):
        if pirmoMax < h_arr[i]:
            pirmoMax = h_arr[i]

    for i in range(0, len(h2_arr)):
        if antroMax < h2_arr[i]:
            antroMax = h2_arr[i]

    print("Aukščiausias Pirmo kūno taškas:",pirmoMax)
    print("Aukščiausias Antro taškas:", antroMax)

    if showVelocity:
        pirmo_greitis = plot.plot(t_arr, v_arr)
        antro_greitis = plot.plot(t2_arr, v2_arr)
        arguments.append(pirmo_greitis)
        arguments.append(antro_greitis)
        labels.append("Pirmo greitis žings:" +str(dt))
        labels.append("Antro greitis žings:" +str(dt))
        #plot.legend([pirmo_greitis, antro_greitis, taskas], labels=["Pirmo greitis zings:" +str(dt),"Antro greitis zings:" +str(dt), "Issiskirimo momentas"])

    if showHeight:
        pirmo_aukstis = plot.plot(t_arr, h_arr)
        antra_aukstis = plot.plot(t2_arr, h2_arr)
        arguments.append(pirmo_aukstis)
        arguments.append(antra_aukstis)
        labels.append("Pirmo aukštis žings:" +str(dt))
        labels.append("Antro aukštis žings:" +str(dt))
        #taskas = plot.axvline(x=t, color='r', linestyle='dotted')
        #plot.legend([pirmo_aukstis, antra_aukstis, taskas], labels=["Pirmo aukstis zings:" +str(dt),  "Antro aukstis zings:" +str(dt), "Issiskirimo momentas"])

euler(0.15, True, False)
euler(0.1, True, False)
euler(0.05, True, False)
taskas = plot.axvline(x=t, color='r', linestyle='dotted')
arguments.append(taskas)
labels.append("Issiskirimo momentas")
plot.ylim(0)
plot.legend(arguments, labels=labels)
plot.ylabel("Greitis")
plot.xlabel("Laikas s")
plot.show()

arguments=[]
labels=[]

euler(0.2, False, True)
euler(0.1, False, True)
euler(0.05, False, True)
taskas = plot.axvline(x=t, color='r', linestyle='dotted')
arguments.append(taskas)
labels.append("Iššiskirimo momentas")
plot.ylim(0)
plot.legend(arguments, labels=labels)
plot.ylabel("Aukštis")
plot.xlabel("Laikas s")
plot.show()