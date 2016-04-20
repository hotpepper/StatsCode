def factorial(n):
    if n-1 < 1:
        return 1
    else:
        return n*factorial(n-1)

def number_of_outcomes(n, k):
    '''
    to get the number of rows where
    outcome occurs in truth table
    where n in the number of columns
    and k is the freq of outcomes per row
    '''
    return factorial(n)/ (factorial(n-k)*factorial(k))

def binomial_distribution(n, k, p):
    '''
    flip coin n times
    what is the probability of k heads
    given probability(h) = p
    '''    
    return number_of_outcomes(n, k)*p**k*(1-p)**(n-k)
