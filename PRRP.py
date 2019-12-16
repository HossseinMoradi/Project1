import random
import matplotlib.pyplot as plt
def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)


Total_arrival_rate = 0.67
Average_service_rate = 0.75
Xt=20
Tt=4
proportion_of_CAVs= 0.25
proportion_of_emg = 0.01
proportion_of_hv = 0.04

amber_light=2
total_number_of_vehicles1= []

x1=0
x2=random.randint(0,Xt)
x3=random.randint(0,Xt)
x4=random.randint(0,Xt)



is_heavy_vehicles_have_priority= True


number_of_heavy_vehicles1=[]
number_of_heavy_vehicles_other=[]
number_of_emergency_vehicles1=[]
number_of_emergency_vehicles_other=[]

time_for_queuing = ((x2 + x3 + x4) / Average_service_rate)+3*amber_light


y = round(time_for_queuing * random.expovariate(1/(Total_arrival_rate/8)))
m1= random.randint(0,y)
print("The location of the last CAV in lane 1: " + str(m1))
m2= random.randint(0,y)
print("The location of the last CAV in lane 2: " + str(m2))
k = m1
sum1 = 0
while k <= 100:
    sum1 = sum1 + ((pow(((1 - proportion_of_CAVs) * (Total_arrival_rate/8)*time_for_queuing), k)) / factorial(k))
    k += 1
n=m1
sum2=0
while n <= 100:
    sum2 = sum2 + (n*((pow(((1 - proportion_of_CAVs) * (Total_arrival_rate/8)*time_for_queuing), n)) / factorial(n)))/sum1
    n += 1
y1111=round(sum2)

k = m2
sum1 = 0
while k <= 100:
    sum1 = sum1 + ((pow(((1 - proportion_of_CAVs) * (Total_arrival_rate/8)*time_for_queuing), k)) / factorial(k))
    k += 1
n=m2
sum2=0
while n <= 100:
    sum2 = sum2 + (n*((pow(((1 - proportion_of_CAVs) * (Total_arrival_rate/8)*time_for_queuing), n)) / factorial(n)))/sum1
    n += 1


y111=round(sum2)
y1=y111+y1111
print ("The number of vehicles queued up during red time based on the location of the last CAV: "+str(y1))

gg=(y1/Average_service_rate)
kk=0
sumsum=[]
ssss=0
kk=0
ff=0
fn=0
while kk <= 170:
    tttt=0
    ff=kk
    while ff<=170:
        hn=0
        hnmn=0
        while hn<kk:
            hnmn=hnmn+(pow(2.71828, -1*(Total_arrival_rate/4)*gg) * pow((Total_arrival_rate/4)*gg, hn) / factorial(hn))
            hn+=1
        tttt = tttt + ((pow(2.71828, -1*(Total_arrival_rate/4)*gg) * pow((Total_arrival_rate/4)*gg, ff) / factorial(ff)))/(1-hnmn)
        ff += 1
    ssss = tttt* ((pow(2.71828,-1*Tt*(Total_arrival_rate/4)))*pow((1-(pow(2.71828,-1*Tt*(Total_arrival_rate/4)))),kk))
    fn=fn+kk*ssss
    kk+=1

j11 =round(fn)

if y1 <= Xt:
    queued_up =y1+j11
    if queued_up <= Xt:
        x1 = queued_up
        qo = 0
    else:
        x1 = Xt
        qo = queued_up-Xt

else:
    x1 = Xt
    qo = y1 - Xt


print ("The number of vehicles in the first platoon: "+str(x1))
print ("The number of queued up vehicles that cannot categorized as the first platoon according to Xt threshold: "+str(qo))


j = round(pow(2.135, ((Total_arrival_rate/4)* Tt)))

if qo==0:
    total_number_of_vehicles1.append(x1)
    i=0
    while i<=4:
        total_number_of_vehicles1.append(j)
        i+=1

    ce = ((j / Average_service_rate) + Tt)


elif qo!=0:
    total_number_of_vehicles1.append(x1)
    total_number_of_vehicles1.append((qo) + j)
    i=1
    while i<=3:
        total_number_of_vehicles1.append(j)
        i+=1
    ce = ((j / Average_service_rate) + Tt)
    ce1 = ((((qo) + j) / Average_service_rate) + Tt)



gt1=(total_number_of_vehicles1[0])/Average_service_rate
print("The required green time for this group in case of no different priority treatments: " +str(gt1))




i=0
h1=0
h2=0
while i <= 9:
    h1 = h1 + random.expovariate((Total_arrival_rate/4) * proportion_of_hv)
    number_of_heavy_vehicles1.append(h1)
    h2 = h2 + random.expovariate(3 * (Total_arrival_rate/4)* proportion_of_hv)
    number_of_heavy_vehicles_other.append(h2)
    i += 1

i=0
e1=0
e2=0
while i <= 9:
    e1 = e1 + random.expovariate((Total_arrival_rate/4)* proportion_of_emg)
    number_of_emergency_vehicles1.append(e1)
    e2 = e2 + random.expovariate(3 * (Total_arrival_rate/4) * proportion_of_emg)
    number_of_emergency_vehicles_other.append(e2)
    i += 1


if qo==0:

    m0 = 0
    m1 = 0
    m2 = 0
    m3 = 0

    i = 0
    while i <= 9:
        me = number_of_emergency_vehicles1[i]

        if me <= gt1:
            m0 += 1
        if me > gt1 and me <= gt1 + ce:
            m1 += 1
        if me > gt1 + ce and me <= gt1 + 2 * ce:
            m2 += 1
        if me > gt1 + 2 * ce and me <= gt1 + 3 * ce:
            m3 += 1

        i += 1

    print("There is " + str(m0) + " emergency vehicle in the first platoon, " + str(
        m1) + " in the second platoon, " + str(
        m2) + " in the third platoon, and " + str(
        m3) + " in the fourth platoon of the current group. ")


    gt222 = gt1
    if m0 == 0 and m1 == 0 and m2 == 0 and m3 == 0:
        gt1 = gt1
    elif m0 != 0 and m1 == 0 and m2 == 0 and m3 == 0:
        gt1 = gt1
    elif m0 != 0 and m1 != 0 and m2 == 0 and m3 == 0:
        gt1 = gt1 *  + ce
    elif m0 != 0 and m1 != 0 and m2 != 0 and m3 == 0:
        gt1 = gt1 + 2 * ce
    elif m0 != 0 and m1 != 0 and m2 != 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 == 0 and m1 != 0 and m2 == 0 and m3 == 0:
        gt1 = gt1 + ce
    elif m0 == 0 and m1 != 0 and m2 != 0 and m3 == 0:
        gt1 = gt1  + 2 * ce
    elif m0 == 0 and m1 != 0 and m2 != 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 == 0 and m1 == 0 and m2 != 0 and m3 == 0:
        gt1 = gt1 + 2* ce
    elif m0 == 0 and m1 == 0 and m2 != 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 == 0 and m1 == 0 and m2 == 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 != 0 and m1 == 0 and m2 != 0 and m3 == 0:
        gt1 = gt1 + 2*ce
    elif m0 != 0 and m1 == 0 and m2 == 0 and m3 != 0:
        gt1 = gt1 + 3*ce
    elif m == 0 and m1 != 0 and m2 == 0 and m3 != 0:
        gt1 = gt1 +3* ce

    print("The required green time for this group by considering the priority of Emergency vehicles: " + str(gt1))



    n0 = 0
    n1 = 0
    n2 = 0
    n3 = 0

    i = 0
    while i <= 9:
        mh = number_of_heavy_vehicles1[i]

        if mh <= gt222:
            n0 += 1
        if mh > gt222 and mh <= gt222 + ce:
            n1 += 1
        if mh > gt222 + ce and mh <= gt222 + 2 * ce:
            n2 += 1
        if mh > gt222 + 2 * ce and mh <= gt222 + 3 * ce:
            n3 += 1

        i += 1

    print("There is " + str(n0) + " heavy vehicle in the first platoon, " + str(
        n1) + " in the second platoon, " + str(n2) + " in the third platoon, and " + str(
        n3) + " in the fourth platoon of the current group.")


    if n0 == 0 and n1 == 0 and n2 == 0 and n3 == 0:
        gt222 = gt222
    elif n0 != 0 and n1 == 0 and n2 == 0 and n3 == 0:
        gt222 = gt222
    elif n0 != 0 and n1 != 0 and n2 == 0 and n3 == 0:
        gt222 = gt222 + ce
    elif n0 != 0 and n1 != 0 and n2 != 0 and n3 == 0:
        gt222 = gt222 + 2 * ce
    elif n0 != 0 and n1 != 0 and n2 != 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 == 0 and n1 != 0 and n2 == 0 and n3 == 0:
        gt222 = gt222 + ce
    elif n0 == 0 and n1 != 0 and n2 != 0 and n3 == 0:
        gt222 = gt222  + 2 * ce
    elif n0 == 0 and n1 != 0 and n2 != 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 == 0 and n1 == 0 and n2 != 0 and n3 == 0:
        gt222 = gt222 + 2* ce
    elif n0 == 0 and n1 == 0 and n2 != 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 == 0 and n1 == 0 and n2 == 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 != 0 and n1 == 0 and n2 != 0 and n3 == 0:
        gt222 = gt222 + 2*ce
    elif n0 != 0 and n1 == 0 and n2 == 0 and n3 != 0:
        gt222 = gt222 + 3*ce
    elif n == 0 and n1 != 0 and n2 == 0 and n3 != 0:
        gt222 = gt222 +3* ce

    gt1= max(gt1,gt222)

    print("The required green time for this group by considering the priority of both heavy and emergency vehicles: " + str(gt1))


    if m0 + m1 + m2 + m3 != 0:
        print("There is an emergency vehicle in the current group and ,therefore, green time cannot be interrupted.")

    if m0 + m1 + m2 + m3 == 0:
        i = 0
        j = 0
        out_of_loop = False
        while i <= 9 and not (out_of_loop):
            me = number_of_emergency_vehicles_other[i]
            if me <= gt1:
                print("There isn't any emergency vehicle in the current group. On the other hand, there is an emergency vehicle in conflicting groups.")
                gt1 = me
                out_of_loop = True
            else:
                i += 1
                continue
        if not (out_of_loop):
            print("There isn't any emergency vehicle at the intersection. ")

        print("The green time for the current group by considering all approaching emergency vehicles : " + str(gt1))



    if m0 + m1 + m2 + m3 == 0 and n0 + n1 + n2 + n3 == 0 and gt1 != me:
        i = 0
        j = 0
        out_of_loop = False
        while i <= 9 and not (out_of_loop):
            mh = number_of_heavy_vehicles_other[i]
            if mh <= gt1:
                print("There isn't any emergency vehicle and heavy vehicle in the current or other groups. However, there is a heavy vehicle in conflicting groups.")
                gt1 = mh
                out_of_loop = True
            else:
                i += 1
                continue
        if not (out_of_loop):
            print("There isn't any heavy vehicle at the intersection. ")

        print("The green time for the current group by considering all approaching special vehicles : " + str(gt1))




if qo!=0:

    m0 = 0
    m1 = 0
    m2 = 0
    m3 = 0

    i = 0
    while i <= 9:
        me = number_of_emergency_vehicles1[i]

        if me <= gt1:
            m0 += 1
        if me > gt1 and me <= gt1 + ce1:
            m1 += 1
        if me > gt1 + ce1 and me <= gt1 + ce1 + ce:
            m2 += 1
        if me > gt1 + ce1 + ce and me <= gt1 +ce1 + 2*ce:
            m3 += 1

        i += 1


    print("There is " + str(m0) + " emergency vehicle in the first platoon, " + str(
        m1) + " in the second platoon, " + str(
        m2) + " in the third platoon, and " + str(
        m3) + " in the fourth platoon of the current group. ")


    gt222 = gt1
    if m0 == 0 and m1 == 0 and m2 == 0 and m3 == 0:
        gt1 = gt1
    elif m0 != 0 and m1 == 0 and m2 == 0 and m3 == 0:
        gt1 = gt1
    elif m0 != 0 and m1 != 0 and m2 == 0 and m3 == 0:
        gt1 = gt1 *  + ce
    elif m0 != 0 and m1 != 0 and m2 != 0 and m3 == 0:
        gt1 = gt1 + 2 * ce
    elif m0 != 0 and m1 != 0 and m2 != 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 == 0 and m1 != 0 and m2 == 0 and m3 == 0:
        gt1 = gt1 + ce
    elif m0 == 0 and m1 != 0 and m2 != 0 and m3 == 0:
        gt1 = gt1  + 2 * ce
    elif m0 == 0 and m1 != 0 and m2 != 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 == 0 and m1 == 0 and m2 != 0 and m3 == 0:
        gt1 = gt1 + 2* ce
    elif m0 == 0 and m1 == 0 and m2 != 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 == 0 and m1 == 0 and m2 == 0 and m3 != 0:
        gt1 = gt1 + 3 * ce
    elif m0 != 0 and m1 == 0 and m2 != 0 and m3 == 0:
        gt1 = gt1 + 2*ce
    elif m0 != 0 and m1 == 0 and m2 == 0 and m3 != 0:
        gt1 = gt1 + 3*ce
    elif m == 0 and m1 != 0 and m2 == 0 and m3 != 0:
        gt1 = gt1 +3* ce

    print("The required green time for this group by considering the priority of Emergency vehicles: " + str(gt1))



    n0 = 0
    n1 = 0
    n2 = 0
    n3 = 0

    i = 0
    while i <= 9:
        mh = number_of_heavy_vehicles1[i]

        if mh <= gt222:
            n0 += 1
        if mh > gt222 and mh <= gt222 + ce:
            n1 += 1
        if mh > gt222 + ce and mh <= gt222 + 2 * ce:
            n2 += 1
        if mh > gt222 + 2 * ce and mh <= gt222 + 3 * ce:
            n3 += 1

        i += 1

    print("There is " + str(n0) + " heavy vehicle in the first platoon, " + str(
        n1) + " in the second platoon, " + str(n2) + " in the third platoon, and " + str(
        n3) + " in the fourth platoon of the current group.")


    if n0 == 0 and n1 == 0 and n2 == 0 and n3 == 0:
        gt222 = gt222
    elif n0 != 0 and n1 == 0 and n2 == 0 and n3 == 0:
        gt222 = gt222
    elif n0 != 0 and n1 != 0 and n2 == 0 and n3 == 0:
        gt222 = gt222 + ce
    elif n0 != 0 and n1 != 0 and n2 != 0 and n3 == 0:
        gt222 = gt222 + 2 * ce
    elif n0 != 0 and n1 != 0 and n2 != 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 == 0 and n1 != 0 and n2 == 0 and n3 == 0:
        gt222 = gt222 + ce
    elif n0 == 0 and n1 != 0 and n2 != 0 and n3 == 0:
        gt222 = gt222  + 2 * ce
    elif n0 == 0 and n1 != 0 and n2 != 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 == 0 and n1 == 0 and n2 != 0 and n3 == 0:
        gt222 = gt222 + 2* ce
    elif n0 == 0 and n1 == 0 and n2 != 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 == 0 and n1 == 0 and n2 == 0 and n3 != 0:
        gt222 = gt222 + 3 * ce
    elif n0 != 0 and n1 == 0 and n2 != 0 and n3 == 0:
        gt222 = gt222 + 2*ce
    elif n0 != 0 and n1 == 0 and n2 == 0 and n3 != 0:
        gt222 = gt222 + 3*ce
    elif n == 0 and n1 != 0 and n2 == 0 and n3 != 0:
        gt222 = gt222 +3* ce

    gt1= max(gt1,gt222)

    print("The required green time for this group by considering the priority of both heavy and emergency vehicles: " + str(gt1))


    if m0 + m1 + m2 + m3 != 0:
        print("There is an emergency vehicle in the current group and ,therefore, green time cannot be interrupted.")

    if m0 + m1 + m2 + m3 == 0:
        i = 0
        j = 0
        out_of_loop = False
        while i <= 9 and not (out_of_loop):
            me = number_of_emergency_vehicles_other[i]
            if me <= gt1:
                print("There isn't any emergency vehicle in the current group. On the other hand, there is an emergency vehicle in conflicting groups.")
                gt1 = me
                out_of_loop = True
            else:
                i += 1
                continue
        if not (out_of_loop):
            print("There isn't any emergency vehicle at the intersection. ")

        print("The green time for the current group by considering all approaching emergency vehicles : " + str(gt1))



    if m0 + m1 + m2 + m3 == 0 and n0 + n1 + n2 + n3 == 0 and gt1 != me:
        i = 0
        j = 0
        out_of_loop = False
        while i <= 9 and not (out_of_loop):
            mh = number_of_heavy_vehicles_other[i]
            if mh <= gt1:
                print("There isn't any emergency vehicle and heavy vehicle in the current or other groups. However, there is a heavy vehicle in conflicting groups.")
                gt1 = mh
                out_of_loop = True
            else:
                i += 1
                continue
        if not (out_of_loop):
            print("There isn't any heavy vehicle at the intersection. ")

        print("The green time for the current group by considering all approaching special vehicles : " + str(gt1))

