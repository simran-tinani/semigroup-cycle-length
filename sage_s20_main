import sage_S20_arithmetic.py
import sage_S20_functions.py


# Cycle length and start computations for random elements of S20

for i in range(0,100):
    a= random.choice([0,1,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'])
    l=cycle_length(a)
    s=cycle_start(a,l)
    print l,s


# Cycle length and start computations for random 5x5 matrices over S20

for i in range(0,100):
    M=Matrix2(5,5)
    M=M.makeRandom(5,5)
    l=matrix_cycle_length(M)
    s=matrix_cycle_start(M,l)
    print l,s
