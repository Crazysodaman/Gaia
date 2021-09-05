def posmakera(servo, posa, posb):
    pwm = []
    for i in range(len(servo)):
        if i%2 == 0:
            pwm.append(posa)
        else:
            pwm.append(posb)
    return pwm

a=[1,2,3]
print(posmakera(a,1500,750))
print("1500,750,1500")