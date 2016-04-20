def f(p):
    """
    probability that coin fliped 3 times will be heads exactly once
    sum(
        htt = p*(1-p)*(1-p)
        tht = p*(1-p)*(1-p)
        tth = p*(1-p)*(1-p)
    )
    """
    return 3* p*(1-p)*(1-p)

def f(p1, p2):
    """
    probability that 2 different coins will both be heads - one flip
        hh = p1*p2
    """
    return p1*p2

print f(0.5, 0.8)


def f(p0, p1, p2):
    """
    pick 1 coin (of 2) each with own probability
    what is the prob of heads
    p(h|c1) = p1
    p(h|c2) = p2
    """
    pc1 = p0
    pc2 = 1-p0
    phc1 = p1
    phc2 = p2
    pc1h = pc1*phc1
    pc2h = pc2*phc2
    return pc1h+pc2h
print f(0.3, 0.5, 0.9)

def f(pc, p_pos_c, p_neg_notc):
    """
    prob pos given p(c), p(pos|c), and p(neg|not c)
    """
    pc_pos_c = pc*p_pos_c
    pc_pos_notc = (1-pc)*(1-p_neg_notc)# notc and pos|notc
    return pc_pos_c + pc_pos_notc
print f(0.1, 0.9, 0.8)


def bayes(p0, p1, p2):
    """
    p0 = p(c)
    p1 = p(pos | c)
    p2 = p(neg | !c)
    return: p(c | pos)
    """
    # p(c,pos) + p(!c, pos)
    ppos = (p0*p1) + ((1-p0)*(1-p2))
    # p(c, pos) / p(pos)
    return (p0*p1)/ppos # p(c | pos)
print bayes(0.1,0.9, 0.8)

def nbayes(p0, p1, p2):
    """
    p0 = p(c)
    p1 = p(pos | c)
    p2 = p(neg | !c)
    return: p(c | neg)
    """
    # p(c,neg) + p(!c, neg)
    pneg = p0*(1-p1) + (1-p0)*p2
    # p(c, neg) / p(neg)
    return p0*(1-p1) / pneg
print nbayes(0.001,0.7, 0.9)
    
# p(c | neg) = 0.00336  
