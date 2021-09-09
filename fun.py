def servolistfilter(servo, pos, xpwm):
    return [x[2] for x in zip(pos, xpwm, servo) if x[0] != x[1]]

a=[1,2,3]
b=[1200,20,120]
c=[1200,2000,1200]
print(servolistfilter(a,b,c))
print("2")
