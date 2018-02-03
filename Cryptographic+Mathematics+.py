
# coding: utf-8

# In[3]:

# 1.1 Pythaogrean triples 
a = 2
b = 3
c = 4
print (a^2)+(b^2) == (c^2)


# In[11]:

#  1.2 Solve Equestions using sage 

var('a,b,c') #must define all the values you are using first 
eqn = [a+b*c==1, b-a*c==0, a+b==5] #write down all the equations 
s = solve(eqn, a,b,c); #first type the name of equation followed by the name of values you want to get for example a,b,c
print s

#example for solving pythagorean triple equestion from slide one
var('x,m')
eqns = [(x^2)+(m^2)*((x+1)^2)==1]
solve(eqns,x)


# In[23]:

# 1.3 Binary GCD Algorithm 
def gcd(u, v):
    """ This function will calcluate
    GCD of given two numbers.
    If the input is negative, both the
    numbers are converted to positive
    before the calculation
    """
    if u == v:
        return u
    elif u == 0:
        return v
    elif v == 0:
        return u
    # u is even
    elif u & 1 == 0:
        # v is even
        print 'v is even'
        if v & 1 == 0:
            print 'u is even as well'
            return 2*gcd(u >> 1, v >> 1)
        # v is odd
        else:
            return gcd(u >> 1, v)
    # u is odd
    elif u & 1 != 0:
        # v is even
        if v & 1 == 0:
            return gcd(u, v >> 1)
        # v is odd and u is greater than v
        elif u > v and v & 1 != 0:
            return gcd((u-v) >> 1, v)
        # v is odd and u is smaller than v
        else:
            return gcd((v-u) >> 1, u)
        
gcd(87654321,12345678)

#use this when solving the binary gcd 

u = 87654321
v = 6172839
z = (u-v)/2

print z


# In[26]:

#1.4 How is check if a number is even or odd
a = 6172839
e = is_even(a)
o = is_odd(a)
print 'the number is ',a,'Is even?',e , ' Is Odd?',o


# In[765]:

#1.5 Extended Eculidean ALgorithm 
#LEAVE THIS AS IT IS USE THE NEXT METHOD TO WORK ON YOUR VALUES USE THIS AS AN EXAMPLE TO UNDERSTAND THE CODE
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        print q,r
        m, n = x-u*q, y-v*q
        print m,n
        b,a, x,y, u,v = a,r, u,v, m,n
        print b,a,x,y,u,v
    gcd = b
    return gcd, x, y

print egcd(1398, 324)

#how to decode the output in order to write it on paper for both euclidean and extended euclidean algo
#Euclidean Algo: start from line 3 of output
# 1348 = 4x324+102
#look at line with 324 in it
# 324 = 3x102 + 18
# Follow the pattern 
# 102 = 15x8 + 12
# 18 = 1x12 + 6
# 12 = 2*16 + 0
# 6 is your GCD 

######################
#extended Euclidean algo 
# look at line next to 324 for this 
# 102 = 1348-4*325
# this means that
# 102 = a-4*b
# lets move to step 2 
# 18 = 324-3*102
# but now we know the value of 102 and we know that 324 is our b so 
# 18 = b-3*(a-4*b)
# the final solution is in 3rd line below the one with 324 102 0 1 1 -4
# it says -3 13
# so the answer we are looking for is 
# 18 = -3a+13b
# repeat this till you get the answer you are looking for.

print '=================================================='



def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        print q,r
        m, n = x-u*q, y-v*q
        print m,n
        b,a, x,y, u,v = a,r, u,v, m,n
        print b,a,x,y,u,v
    gcd = b
    return gcd, x, y

print egcd(3145,1996 )


# In[442]:

# 2.1 FIND PRIME FACTORS OF A NUMBER
factor(50)
(8*6)%10


# In[53]:

# 2.2 SQUARE ROOT (sqrt)
sqrt(200).n()


# In[7]:

# 2.3 Check divisibility 
21%12 #this means 13 divides 200 and leaves 5 as reminder


# In[5]:

# 2.4 Sieve of Eratosthenes
eratosthenes(200)


# In[64]:

# 2.5 Solving LINEAR CONGRUENCES
# DO NOT CHANGE THE VALUES COPY AND USE A NEW ONE 
# Eg. Solve x^2+3x+5 = 4 mod 11
# Answer starts from 0 and goes till 9 so valid answer is 2 and 6

[mod((x^2)+3*x+5,11)==4 for x in range(10)] 


# In[745]:

# 3.1 Eurlers pi Calculator
print factor(60)
print euler_phi(29)
print (50/16).n()
xgcd(17,-28)
(8^17)%29


# In[801]:

# 3.2 Chinese Reminder Theorem
# Solve the first equation for k 
# x=1mod3

var('k')
z = solve_mod(35*k==1,3)
gcd()
CRT_list([2,3,2], [3,5,7])


# In[121]:

#4.1 How to calculate number of primes till given x.
pix = 100
pix/(ln(pix).n())

factor(989)


# In[514]:

#4.2 Use me for succesive squering 

main = 7
power = 32
modit = 101
k = 1
m = (main^k)%modit
print main,'^',k,'=', m,' mod ',modit

for i in range(10):
    z = k*2
    n = (main^z)%modit
    k = z
    print main,'^',z,'=', n,' mod ',modit
    
(92*24*7)%101


# In[646]:

#5.1 Farmats Pseudoprime checkers
a = 3
N = 91
if a^(N-1)%N==1:
    print 'It is a prime according to farmats little theorem but in real it is '
    print is_prime(N)
#################################################################################################################################    
#5.2 Carmicheal Number checker 
a = 2
N = 561
countCoP = 0
count = 0
for i in [2..N-1]:
    if gcd(i,N)==1:
        countCoP = countCoP+1
        if a^(N-1)%N==1:
            count = count+1
print 'This is the total numbers of co primes for the number',countCoP            
print 'This is the total numbers of co primes for which the farmats little theorem holds',count
if countCoP == count:
    print 'Entered Number is indeed a carmicheal number'
print factor(561)    
#################################################################################################################################
#5.3 Prove a number is Carmicheal 
var('n,k')
eq = [n==((6*k)+1)*((12*k)+1)*((18*k)+1)*((36*k)+1)]
print solve(eq,n)

#################################################################################################################################
#5.4 Rabin Miller Test 
n = 561
print 'Rabin Miller Test '
print factor(n-1)
#Take the values from the output in the form of p-1 = q x a^k
k = 4
q = 35
#Step 1 before entering the loop 
R = (2^q)%n
print '2 ^',q, '=',R,' mod ',n
if R==1:
    print 'The number is composite'
for i in [1..k-1]:
    q=q*2
    R = (R^2)%n
    print '2 ^',q, '=',R,' mod ',n
    if(R==1):
        print 'The number is composite'
        break 
    if(R==-1):
        print 'The number is prime'
        break

  
    
var ('y,x')
e = EllipticCurve(y^2==(x^3)+(2*x)-2)
P = e(1,1)
print 5*P



# In[85]:

# 5.5 FIND A RABIN MILLER WITNESS
N=1729
#N=2^k q+1
factor(N-1)
k=6
q=3^3

a=9
#check if a is a Rabin Miller Witness
#Check 1: a^q=?1 mod N
count = 0
for a in [10..1728]:
    if count == 1:
        break

    l=pow(a,q,N)
    if l==1:
        print 'N passes the rabbin miller test, 1.Satisfied'
        print 'a is not a Rabin Miller Witness'
    else:
        m=0 #counts how many times we get -1
        for i in [0..5]:
            y=pow(a,q*2^i,N)
            if y==-1:
                m=m+1
        if m>0:
            print 'N passes, 2.Satisfied, (but 1. is not)'
            print 'a is not a Rabin Miller Witness'
        else:
            print 'a=',a,'is a Rabin Miller witness (that n is not a prime)'
            count = count+1 
            #change the value of count to get more witness



# In[91]:

#5.6 CREATE INDIEX
#THIS IS HOW WE CAN SOLVE MOD EQUATIONS
for x in [1..12]:
    if (mod((2^x),13)==1):
        print x


# g = 2
# k = 141312
# p = 194813
# 
# #Generation of public key
# a = (g^k)%p
# print 'VALUE OF a',a
# print 'a = ',a,' ≅ ',g,'^',k,' mod ',p
# 
# #Encrypting message 
# m = 173124
# r = 136297 
# e1 = (g^r)%p
# print 'VALUE OF e1',e1
# print 'e1 = ',e1,' ≅ ',g,'^',r,' mod ',p
# 
# e2 = (m*(a^r))%p
# print 'VALUE OF e2',e2
# print 'e2 = ',e2,' ≅ ',m,'*',a,'^',r,' mod ',p
# 
# print 'Thus the message sent is (',e1,',',e2,')'
# 
# #Decrypting Message 
# c = (e1^k)%p
# print 'VALUE OF c',c
# print 'c = ',c,' ≅ ',e1,'^',k,' mod ',p
# 
# #now we calculate inverse of the mod
# im = inverse_mod(c,p)
# dM = (e2*im)%p
# print 'Decyrpted Message = ',dM,' ≅ ',e2,'*',im,' mod ',p
# 
# 
# 
# sqrt(34).n()
# 125%11
# print (7^6)%11
# print 3^4
# print 5^3
# print 7^2
# print 49%11
# for i in range(10):
#         z=i^2
#         if (z)%11==4: 
#             print i
# 
# factor(253*5)
# a = 2
# 2^6
# gcd(4,13)
# 

# In[143]:




# In[449]:

# 6.2 Shanks’ Baby-step Giant-step algorithm
#Example 2^x = 7 mod 11

a = 7
y = 2
p = 19

s = ceil(sqrt(p))
print s

A = []
B = []
C = [] #STORE LOCATION OF A IN THIS 
D = []

for i in range(0,s):
    value = a*(y^i) % p
    A.append(value)
    C.append(i)

for j in range(1,s+1):
    value = y^(j*s) % p
    B.append(value)
    js=j*s
    D.append(js)

print A
print C
print B
print D

x1,x2 =0,0
 
for r in A:
    for t in B:
        if r == t:
            x1 = A.index(r)            
            x2 = B.index(t)
            print x1,x2
            break
            
print 'the value of x is ', ((x2+1)*s - x1) % p


# In[749]:

#7.1 Legendre Symbol and Qudaratic reciprocity
p = 1
q = 3
print is_prime(p)
print is_prime(q)
f = 0
if(is_prime(p)&is_prime(q)):
    print 'First Condition true flip with positive sign'
    f = f+1
#Condition 1 p=q==3 mod 4
if ((p%4==3) & (q%4==3)):
    print 'First contion failed Flip it with minus'
if (f == 0):
    print factor (p)
    print factor (q)
z = 9
if (z%8==1 or z%8==7):
    print 'Put 1 in place of the value you have '
if (z%8==3 or z%8==5):  
    print 'Put -1 in place of the value you have '
    
#USE THIS TO GET THE ANSWER DIRECTLY VERIFY WITH THIS 
kronecker(17,2015)
print legendre_symbol(5,3)
jacobi_symbol(17,2015)


# In[753]:

#7.2 Solovay Strassen Primality Test 
#a^(n-1)/2 = (a/n) mod n 
a = 5
n = 33
b = kronecker(a,n)
k = (n-1)/2
print k
print b
z = (a^k)%n
print z
if (b == z):
    print 'The given number passes the solovay Strassen Primality Test'


# In[318]:

#8.1 Calculate the third point on elliptic curve if the first and second points are known 
# eq =[(y^2) == (x^3)+a*(x^2)+(b*x)+c]
a = 0
b = 0
c = 17
x1 = -2
y1 = 3
x2 = -1
y2 = 4
m = (y2-y1)/(x2-x1)
x3 = (-a)+(m^2)-x1-x2
y3 = y1+m*(-a+(m^2)-(2*x1)-x2)
print x3,',',y3


# In[264]:

#8.2 Calculate the second point on an elliptic curve if only one point is known 
# eq =[(y^2) == (x^3)+a*(x^2)+(b*x)+c]
a = 0
b = 0
c = 17
x1 = -2
y1 = 3
m = (3*(x1^2)+(2*a*x1)+b)/(2*y1)
x2 = (-a)+(m^2)-2*x1
y2 = y1+m*(-a+(m^2)-(3*x1))
print x2,',',y2


# In[445]:

#9.1 To Calculate multiples of Point modulo prime
# NOTE IF y1 =0 2P is point of infinity 
x1 = 7
y1 = 5
a = 0
b = 0
p = 11
m = (((3*x1^2)+(2*a*x1)+b)/(2*y1))%p
print 'Value of M is = ',m
x = ((-a)+(m^2)-2*x1)%p
print 'Value of X is = ',x
k = m*(x1-x)
y = (k-y1)%p
print 'Value of Y is =',y
print 'The point 2P is = (',x,',',y,')'
calCulateMore(2,3,x1,y1)
#Use this to find 3P and so one, after finding 3P plug in 3P+P to find 4P and so on.
def calCulateMore(x1,y1,x2,y2):
    m = ((y2-y1)/(x2-x1))%p
    x = (-a+(m^2)-x1-x2)%p
    y = (-y1+m*(x1-x))%p
    print 'The this point is = (',x,',',y,')'


# In[271]:

#9.2 Finding all points on an elliptic Curve modulo p 
# Equation of curve y^2 = x^3 - 3*x^2 + 3*x mod 5
p = 5
X = []
X2 = []
Y2 = []
for i in range(p):
    print 'ITRATION No',i
    k = i%p
    print 'X = ',k
    X.append(k)
    l = (i^2)%p
    print 'X^2 = ',l
    X2.append(l)
    e = (i^3)-3*(i^2)+3*i
    eq = e%p
    Y2.append(eq)
    print 'Y^2 = ', eq

print 'Table for x =   ',X
print 'Table for X^2 = ',X2
print 'Table for Y^2 = ',Y2


# In[330]:

#9.3 Succesive Squaring 
n = 2008
n.digits(2)


# In[789]:

#10.1 Fermat Factorisation
n = 7663
s = ceil(sqrt(n))
print s
m = 0
i = 0
while m==0:
    print 'I am round Number ',i
    z = (s^2)-n
    print 's^2 - n = ',s^2,'-',n
    print '=',z
    if(z.is_perfect_power()):
        print 'The number is a perfect square so we have ',sqrt(z)
        print 'The factors are (',s-sqrt(z),',',s+sqrt(z),')'
        break
    s = s+1
    i = i+1
    print 'The number ',z,'is not a perfect square so we try a new value'
    
79*97
factor(7663)
is_prime(97)


# In[783]:

#10.2 Pollard's Rho Method 
n = 2717
x = 2
x1 = ((x^2)+4)%n
x2 = ((x1^2)+4)%n
s=abs(x1-x2)
print x1,x2
print gcd(s,n)
count =0
m=0
while m==0:
    print 'I am counting ',count
    x1=((x1^2)+4)%n
    x2=((x1^2)+4)%n
    s=abs(x1-x2)
    print x1,x2,s,gcd(s,n)
    if gcd(s,n)>1:
        print 'DONE Found a factor'
        print gcd(s,n)
        m=1
        break
    print 'Value of x2 is ',x2
    x1=x2
    print 'value of x1 is ',x1
    count = count+1
print 2717/19 
is_prime(143)
19*143


# In[418]:

#polards ro -1 factors 
B = 12
factorOfB = factorial(4)
N = 1711
for i in [2..20]:
    k = ((i^factorOfB))%N
    g = gcd(k-1,N)
    if gcd(k-1,N)>1:
        print 'VALUE OF a IS ',i
        print 'THIS IS THE ANSWER',k-1
        otherfactor = N/g
        print 'I am the factor',g,otherfactor
        break 


# In[660]:

var ('y,x')
e = EllipticCurve(y^2==(x^3)+(2*x)-2)
P = e(1,1)
print P

# USE THIS TO FIND NUMBER OF POINTS ON AN CURVE
x,y = var('x,y')
EllipticCurve(GF(5,'a'),[0,0,0,2,1]).cardinality()
E = EllipticCurve(GF(5,'a'),[0,0,0,2,1])


E=EllipticCurve(GF(101,'a'),[2,53])
E.plot(thickness=2)


# In[775]:

143%7

for i in range(2):
    print 7*i
print '========'
for i in range(2):
    print 143*i    
    
(5*143)%7
5*56
7-280
-273%7

for i in range(20):
    if ((i*13)%7)==1:
        print 'This is what you want ',i 
        break
-670%7
143*2
286+135
7+11+13
421%1001
421%7
10%11
4*7*13

a = (3^2)%43
b = ((7^3)+(13*7)+5)%43
print a , b

#multiplicative Inverse 
inverse_mod(2,101)

(15*3)%91


# In[ ]:

.GF


# In[752]:

#CALCULATE 2P for non mod values as well.
x1 = -1
y1 = 4
a = 0
b = 0

m = (((3*x1^2)+(2*a*x1)+b)/(2*y1))
print 'Value of M is = ',m
x = ((-a)+(m^2)-2*x1)
print 'Value of X is = ',x
k = m*(x1-x)
y = (k-y1)
print 'Value of Y is =',y
print 'The point 2P is = (',x,',',y,')'
calCulateMore(2,3,x1,y1)
#Use this to find 3P and so one, after finding 3P plug in 3P+P to find 4P and so on.
def calCulateMore(x1,y1,x2,y2):
    m = ((y2-y1)/(x2-x1))
    x = (-a+(m^2)-x1-x2)
    y = (-y1+m*(x1-x))
    print 'The this point is = (',x,',',y,')'
    
na = ((137/64)^3)+17
nb = (-2651/512)^2
print na,nb

print factor(580023740921)
is_prime(9203)
-13%7
factor(117)
is_prime(117)
(5^16)%33


# In[800]:

#p = random_prime(10^10-1,False,10^8)
#q = random_prime(10^10-1,False,10^8)
p = 2011
q = 2017
print 'Prime Numbers:',p,q
n = p*q
z = (p-1)*(q-1)
pi = euler_phi(n)
e = 2999
#while gcd(e,pi)!=1:
#    e=ZZ.random_element(pi)
print 'The Value of e =',e

d = lift(Mod(e,pi)^(-1))
print 'The value of N = ',n
print 'The value of e (Public Key) = ',e
print 'The value of d (Private Key) = ',d

m = 123456
ET = (Mod(m,n)^e)
print 'I am the encrypted message',ET
ET = 1721829
DT = (Mod(ET,n)^d)
print 'I am Decryption',DT

#SOLUTION PART 2
#nn = 580023740921
#factor (nn)
#pil = euler_phi(nn)
#print pil
#ek = 18481137817
#d = lift(Mod(ek,pil)^(-1))
#print d

