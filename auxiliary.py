import math

#could use scipy.special.binom
def binomCoeff(n,k):
  binomC = math.factorial(n)/math.factorial(k)/math.factorial(n-k)
  return binomC

