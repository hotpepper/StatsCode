import math


def ci(N, mu):
    mean = mu*N
    var = mu*mean
    var2 = var/N**2
    std = math.sqrt(var2)
    return 1.96*std

def ci2(N, p):
    return 1.96*(math.sqrt(p*(1-p)/N))

def ci3(data):
    mu = sum(data)/float(len(data))
    var = sum([(i-mu)**2 for i in data])/float(len(data))
    return mu, var, 1.96*math.sqrt(var/len(data))
