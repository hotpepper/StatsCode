from __future__ import division
def mean(data):
    return sum(data)/len(data)

def median(data):
    if len(data)%2:
        # odd nuber
        return sorted(data)[int((len(data)-1)/2)]
    else:
        # even number
        return mean([sorted(data)[int(len(data)/2)], sorted(data)[int(len(data)/2)-1]])
    
def mode(data):
    m, v = 0,0
    for i in set(data):
        if data.count(i)>v:
            m, v = i, data.count(i)
    return m

def variance(data):
    mu = mean(data)
    return mean([(i-mu)**2 for i in data])

def stddev(data):
    return variance(data)**(1/2)

##def std(data):
##    mean = sum(data)/len(data)
##    spread = [(i-mean)**2 for i in data]
##    varience = sum(spread)/len(spread)
##    return mean, varience, varience**(1/2)

def standard_score(data, x):
    return (x-mean(data))/stddev(data)


def likelihood(dist, data):
    p = 1.0
    for i in data:
        p*=dist[i]
    return p
# testing
data = [1,2,5,10,-20]
print mean(data)
data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]
print mean(data1)
