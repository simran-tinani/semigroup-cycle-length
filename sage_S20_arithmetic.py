
import math   
import os
import sys
import random

## defining the ring S20

def add2(x,y): # addition rules in S_20
    if x==0:
        return y
    if y==0:
        return x
    if x==1 and y!=0:
        if y=='a' or y=='b' or y=='c' or y=='d' or y=='e' or y=='f' or y=='g' or y=='h' or y=='j' or y=='k' or y=='l' or y=='m' or y==1:
            return 1
        elif y=='i':
            return 'n'
        elif y=='o':
            return 'p'
        else:
            return y
    if y==1 and x!=0:
        return add2(y,x)
    if x>y:
        x,y=y,x
    if x=='a' and y!=0 and y!=1:
        return y
    if x=='b' and y!=0 and y!=1:
        if y=='a' or y=='b':
            return 'b'
        elif y=='c':
            return 'c'
        elif y=='d' or y=='e':
            return 'e'
        elif y=='j':
            return 'k'
        else:
            return y
    if x=='c' and y!=0:
        if y=='a' or y=='b' or y=='c':
            return 'c'
        if y=='d' or y=='e' or y=='f':
            return 'f'
        if y=='g' or y=='h':
            return 'h'
        if y=='i' or y=='n' or y=='p' or y=='q' or y=='r' or y=='l':
            return y
        if y=='j' or y=='k':
            return 'l'
        if y=='m':
            return 1
        if y=='o':
            return 'p'
    if x=='d' and y!=0:
        return y
    if x=='e' and y!=0:
        if y=='j':
            return 'k'
        else:
            return y
    if x=='f' and y!=0:
        if y=='g':
            return 'h'
        elif y=='j' or y=='k':
            return 'l'
        elif y=='m':
            return 1
        elif y=='o':
            return 'p'
        else:
            return y
    if x=='g' and y!=0:
        if y=='j' or y=='k':
            return 'm'
        elif y=='l':
            return 1
        else:
            return y
    if x=='h' and y!=0:
        if y=='j' or y=='k' or y=='l' or y=='m':
            return 1
        elif y=='o':
            return 'p'
        else:
            return y
    if x=='i' and y!=0:
        if y=='j' or y=='k' or y=='l' or y=='m':
            return 'n'
        elif y=='o' or y=='p':
            return 'q'
        elif y==1:
            return 'n'
        else:
            return 'r'
    if x=='j' and y!=0:
        return y
    if x=='k' and y!=0:
        return y
    if x=='l' and y!=0:
        if y=='m':
            return 1
        elif y=='o':
            return 'p'
        else:
            return y
    if x=='m' and y!=0:
        return y
    if x=='n' and y!=0:
        if y=='o' or y=='p':
            return 'q'
        elif y==1:
            return 'n'
        else:
            return y
    if x=='o' and y!=0:
        if y==1:
            return 'p'
        else:
            return y
    if x=='p' and y!=0:
        if y==1:
            return 'p'
        else:
            return y
    if x=='q' and y!=0:
        if y==1:
            return 'q'
        else:
            return y
    if x=='r' and y!=0:
        return 'r'
    
    
def sum2(l):
    s=0
    for a in l:
        s=add2(s, a)
    return s
   
    
def multiply2(x,y): # Multiplication rules in S_20
    if x==0 or y==0:
        return 0
    if y==1:
        return x
    if x==1:
        return y
    if x=='a' and y!=0 and y!=1:
        if y=='j' or y=='k' or y=='l' or y=='m' or y=='n':
            return 'a'
        elif y=='o' or y=='p' or y==1:
            return 'b'
        elif y=='r':
            return 'c'
        else:
            return 0
    if x=='b' and y!=0 and y!=1:
        if y=='d' or y=='e' or y=='f' or y=='j' or y=='k' or y=='l': 
            return 'a'
        elif y=='g' or y=='h' or y=='m' or y=='o' or y=='p':
            return 'b'
        else:
            return 'c'
    if x=='c' and y!=0 and y!=1:
        if y=='a' or y=='b' or y=='c':
            return y
        elif y=='d' or y=='j':
            return 'a'
        elif y=='e' or y=='g' or y=='k' or y=='m' or y=='o':
            return 'b'
        else:
            return 'c'
    if x=='d' and y!=0 and y!=1:
        if y=='j' or y=='k' or y=='l' or y=='m' or y=='n':
            return 'd'
        elif y=='o' or y=='p' or y=='q':
            return 'g'
        elif y=='r':
            return 'i'
        else:
            return 0
    if x=='e' and y!=0 and y!=1:
        if y=='a' or y=='b' or y=='c':
            return 0
        elif y=='d' or y=='e' or y=='f':
            return 'a'
        elif y=='g' or y=='h':
            return 'b'
        elif y=='i':
            return 'c'
        elif y=='j' or y=='k' or y=='l':
            return 'd'
        elif y=='m':
            return 'e'
        elif y=='n':
            return 'f'
        elif y=='o' or y=='p':
            return 'g'
        elif y=='q':
            return 'h'
        elif y=='r':
            return 'i'
    if x=='f' and y!=0 and y!=1:
        if y=='j':
            return 'd'
        elif y=='k' or y=='m':
            return 'e'
        elif y=='l' or y=='n':
            return 'f'
        elif y=='o':
            return 'g'
        elif y=='p' or y=='q':
            return 'h'
        elif y=='r':
            return 'i'
        else:
            return multiply2('c',y)
    if x=='g' and y!=0 and y!=1:
        if y=='a' or y=='b' or y=='c':
            return 0
        elif y=='d' or y=='e' or y=='f' or y=='j' or y=='k' or y=='l':
            return 'd'
        elif y=='g' or y=='h' or y=='m' or y=='o' or y=='p':
            return 'g'
        else:
            return 'i'
    if x=='h' and y!=0 and y!=1:
        if y=='j':
            return 'd'
        elif y=='k':
            return 'e'
        elif y=='l':
            return 'f'
        elif y=='m' or y=='o':
            return 'g'
        elif y=='n' or y=='q' or y=='r':
            return 'i'
        elif y=='p':
            return 'h'
        else:
            return y
    if x=='i' and y!=0 and y!=1:
        if y=='a' or y=='d' or y=='j':
            return 'd'
        elif y=='b' or y=='f' or y=='g' or y=='k' or y=='m' or y=='o':
            return 'g'
        else:
            return 'i'
    if x=='j' and y!=0 and y!=1:
        if y=='j' or y=='k' or y=='l' or y=='m' or y=='n':
            return 'j'
        elif y=='o' or y=='p' or y=='q':
            return 'o'
        elif y=='r':
            return 'r'
        else:
            return 0
    if x=='k' and y!=0 and y!=1:
        if y== 'a' or y=='b' or y=='c':
            return 0
        elif y=='d' or y=='e' or y=='f':
            return 'a'
        elif y=='g' or y=='h':
            return 'b'
        elif y=='i':
            return 'c'
        elif y=='j' or y=='k' or y=='l':
            return 'j'
        elif y=='m':
            return 'k'
        elif y=='n':
            return 'l'
        elif y=='o' or y=='p':
            return 'o'
        elif y=='q':
            return 'p'
        else:
            return 'r'
    if x=='l' and y!=0 and y!=1:
        if y=='j' or y=='k' or y=='l' or y=='o' or y=='p' or y=='r':
            return y
        elif y=='m':
            return 'k'
        elif y=='n':
            return 'l'
        elif y=='q':
            return 'p'
        else:
            return multiply2('f',y)
    if x=='m' and y!=0 and y!=1:
        if y=='a' or y=='b' or y=='c':
            return 0
        elif y=='d' or y=='e' or y=='f':
            return 'd'
        elif y=='g' or y=='h':
            return 'g'
        elif y=='i' or y=='j' or y=='m' or y=='n' or y=='o' or y=='q' or y=='r':
            return y
        elif y=='k' or y=='l':
            return 'j'
        elif y=='p':
            return 'o'
    if x=='n' and y!=0 and y!=1:
        if y=='a' or y=='d':
            return 'd'
        elif y== 'b' or y=='e' or y=='g':
            return 'g'
        elif y=='c' or y =='f' or y=='h' or y=='i':
            return 'i'
        elif y=='k':
            return 'm'
        elif y=='l':
            return 'n'
        elif y=='p':
            return 'q'
        else:
            return y
    if x=='o' and y!=0 and y!=1:
        if y=='d' or y=='e' or y=='f' or y=='j' or y=='k' or y=='l':
            return 'j'
        elif y=='n' or y=='q' or y=='r':
            return 'r'
        elif y=='a' or y=='b' or y=='c':
            return 0
        else:
            return 'o'
    if x=='p' and y!=0 and y!=1:
        if y=='a' or y=='b' or y=='c' or y=='j' or y=='k' or y=='l' or y=='p' or y=='r':
            return y
        elif y=='d':
            return 'j'
        elif y=='e':
            return 'k'
        elif y=='f':
            return 'l'
        elif y=='g' or y =='m':
            return 'o'
        elif y=='h':
            return 'p'
        else:
            return 'r'
    if x=='q' and y!=0 and y!=1:
        if y=='a':
            return 'q'
        elif y=='b':
            return 'g'
        elif y=='c':
            return 'i'
        elif y=='d':
            return 'j'
        elif y=='e' or y=='k':
            return 'm'
        elif y=='f' or y=='l':
            return 'n'
        elif y=='g' or y=='m' or y=='o':
            return 'o'
        elif y=='h' or y=='p':
            return 'q'
        else:
            return 'r'
    if x=='r' and y!=0 and y!=1:
        if y=='a' or y =='d' or y=='j':
            return 'j'
        elif y=='b' or y=='e' or y=='g' or y=='k' or y=='m' or y=='o':
            return 'o'
        else:
            return 'r'
        
def int_to_bin_string(i): # conversion of integers to binary strings
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s
  
def prod2(l):
    s=1
    for a in l:
        s=multiply2(s, a)
    return s

def exp2(a,n): # exponentiation by square and multiply algorithm
    r=1
    for k in range(0,n):
        r=multiply2(r,a)
    return r            
        
class Polynomial:
    
    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0 
        """
        self.coefficients = list(coefficients) # tuple is turned into a list
     
    def __repr__(self):
        """
        method to return the canonical string representation 
        of a polynomial.
   
        """
        return "Polynomial" + str(self.coefficients)
            
    def __call__(self, x):    # evaluation of the polynomial
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res = add2(res,multiply2(coeff, exp2(x,index)))
        return res
    
    def __add__(self, other): # addition with another polynomial
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [add2(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    
    def derivative(self):
       derived_coeffs = []
       exponent = len(self.coefficients) - 1
       for i in range(len(self.coefficients)-1):
           derived_coeffs.append(multiply2(self.coefficients[i], exponent))
           exponent -= 1
       return Polynomial(*derived_coeffs)
    
    def __pmul__(self, other): # multiplication with another polynomial
        "Return self*other"
        if isinstance(other, Polynomial):
            _s = self.coefficients[::-1]
            _v = other.coefficients[::-1]
            res = [0]*(len(_s)+len(_v)-1)
            for selfpow,selfco in enumerate(_s):
                for otherpow,otherco in enumerate(_v):
                    #print(res)
                    #print(selfpow+otherpow, res[selfpow+otherpow])
                    res[selfpow+otherpow]=add2((res[selfpow+otherpow]), multiply2(selfco,otherco))
                    res=res[::-1]
        else:
            res = [multiply2(co,other) for co in self.coefficients]
        if(len([x for x, val in enumerate(res) 
                                  if val != 0])!=0)>0:
            x=next(x for x, val in enumerate(res) 
                                  if val != 0)
        else:
            x=0
        res=res[x:]
        return Polynomial(*res)
    
    def __pexp__(self, n): #  polynomial exponentiation by square and multiply
        a=self
        coeffs= [1]
        rpoly=Polynomial(*coeffs)
        for k in range(0,n):
            rpoly=rpoly.__pmul__(a)
        return rpoly        
            
def gen_rand_poly(d1, d2): # generate a random polynomial with degree between d1 and d2
    deg=random.randint(d1,d2)
    coeffs=[0]*deg
    coeffs= [random.choice([0,1,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']) for i in range(0,deg)]
    rpoly=Polynomial(*coeffs)
    return rpoly     


def pexp2(p, n): #  polynomial exponentiation by square and multiply
        coeffs= [1]
        rpoly=Polynomial(*coeffs)
        for k in range(0,n):
            rpoly=rpoly.__pmul__(p)
        return rpoly 


class Matrix2(object):
    """ A simple Python matrix class with
    basic operations and operator overloading """
    
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
        
    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return rep
    
    def reset(self):
        """ Reset the matrix data """
        self.rows = [[] for x in range(self.m)]
                     
    def transpose(self):
        """ Transpose the matrix. Changes the current matrix """
        
        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]

    def getTranspose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """
        
        m, n = self.n, self.m
        mat = Matrix2(m, n)
        mat.rows =  [list(item) for item in zip(*self.rows)]
        
        return mat

    def getRank(self):
        return (self.m, self.n)

    def __eq__(self, mat):
        """ Test equality """

        return (mat.rows == self.rows)
        
    def __add__(self, mat):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getRank() != mat.getRank():
            raise MatrixError, "Trying to add matrixes of varying rank!"

        ret = Matrix2(self.m, self.n)
        
        for x in range(self.m):
            row = [sum2(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        """ Subtract a matrix from this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getRank() != mat.getRank():
            raise MatrixError, "Trying to add matrixes of varying rank!"

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [item[0]-item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        """ Multiple a matrix with this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        matm, matn = mat.getRank()
        
        if (self.n != matm):
            raise MatrixError, "Matrices cannot be multipled!"
        
        mat_t = mat.getTranspose()
        mulmat = Matrix2(self.m, matn)
        
        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum2([multiply2(item[0],item[1]) for item in zip(self.rows[x], mat_t.rows[y])])
        return mulmat
    
    def __exp__(self, exponent):
        mat=self
        matm, matn = mat.getRank()
        mulmat = Matrix2(self.m, matn)
        for z in range(0,matm):
            mulmat[z][z]=1
        for i in range(0,exponent):
            mulmat=mulmat.__mul__(mat)
        return mulmat

    def __iadd__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Calls __add__
        tempmat = self + mat
        self.rows = tempmat.rows[:]
        return self

    def __isub__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Calls __sub__
        tempmat = self - mat
        self.rows = tempmat.rows[:]     
        return self

    def __imul__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Possibly not a proper operation
        # since this changes the current matrix
        # rank as well...
        
        # Calls __mul__
        tempmat = self * mat
        self.rows = tempmat.rows[:]
        self.m, self.n = tempmat.getRank()
        return self

    def save(self, filename):
        open(filename, 'w').write(str(self))
        
    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError, "inconsistent row length"
        mat = Matrix2(m,n, init=False)
        mat.rows = rows

        return mat
        
    @classmethod
    def makeRandom(cls, m, n):
        """ Make a random matrix with elements in range (low-high) """
        
        obj = Matrix2(m, n, init=False)
        for x in range(m):
   #         obj.rows.append([random.randrange(low, high) for i in range(obj.n)])
            obj.rows.append([random.choice([0,1,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']) for i in range(obj.n)])
        return obj

    @classmethod
    def makeZero(cls, m, n):
        """ Make a zero-matrix of rank (mxn) """

        rows = [[0]*n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def makeId(cls, m):
        """ Make identity matrix of rank (mxm) """

        rows = [[0]*m for x in range(m)]
        idx = 0
        
        for row in rows:
            row[idx] = 1
            idx += 1

        return cls.fromList(rows)
    
    @classmethod
    def readStdin(cls):
        """ Read a matrix from standard input """
        
        print 'Enter matrix row by row. Type "q" to quit'
        rows = []
        while True:
            line = sys.stdin.readline().strip()
            if line=='q': break

            row = [int(x) for x in line.split()]
            rows.append(row)
            
        return cls._makeMatrix(rows)

    @classmethod
    def readGrid(cls, fname):
        """ Read a matrix from a file """

        rows = []
        for line in open(fname).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)

        return cls._makeMatrix(rows)

    @classmethod
    def fromList(cls, listoflists):
        """ Create a matrix by directly passing a list
        of lists """

        # E.g: Matrix.fromList([[1 2 3], [4,5,6], [7,8,9]])

        rows = listoflists[:]
        return cls._makeMatrix(rows)


