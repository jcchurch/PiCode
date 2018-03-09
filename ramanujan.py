import math

def nCr(n,r): return math.factorial(n) / math.factorial(r) / math.factorial(n-r)
def PiRamanujan(n): return 1/sum([nCr(2*i,i)**3 * (42*i+5) / 2**(12*i+4) for i in range(n)])

print(PiRamanujan(10))
