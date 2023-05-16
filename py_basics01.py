
print("hrllo world")

for i,count in  enumerate(range(500)):
    print(i, count,end = "\n============\n", sep = "-")
    
# ================================================================
    
test = print(int((input("enter")))*2)

# ================================================================
# positive even, positive odd, negative even, negative odd, zero

x = float(input("enter no: "))

print()

if(x>0):
    if(x % 2 ==0):
        print(x,"is positive even")
    else:
        print(x,"is positive odd")
elif(x<0):
    if(x % 2 ==0):
        print(x,"is negative even")
    else:
        print(x,"is negative odd")
else:
    print(x,"is zero")
print()



if(x > 0) and (x % 2 == 0):
    print(x,"is positive even")

elif(x > 0) and (x % 2 == 1):
    print(x,"is positive odd")

elif(x < 0) and (x % 2 == 0):
    print(x,"is negative even")

elif(x < 0) and (x % 2 == 1):
    print(x,"is negative odd")

else:
    print(x,"is zero")
# ================================================================


print("camparision program")

a = float(input("enter a: "))
b = float(input("enter b: "))

if(a > b):
    print(a,"is greater than",b)
elif(a < b):
    print(b,"is greater than",b)
else:
    print(f"{a} amd {b} are the same")


a = int(input("enter your current salary: "))
k = int(input("enter increment per month: "))
y = int(input("years: "))
# your salary will be b after 5 yrs

t = y * 12   # t is duration in months
b = a + k*t

print(f"your salary will be {b} rs after {y} years")

# sum of n natural numbers

n = int(input("till which number you want sum ? "))

# using for loop
sum=0
for i in range(1,n+1):
    sum += i

# using formula
sum = n*(n+1)/2

print(sum)

# table of n

n = int(input("you want table of ? "))

for i in range(1,11):
    print(i*n,end = " ")
    
r = range(6)
print(r)
print(type(r))
print(list(r))

print(list(range(20,10,-2)))
print(list(range(20,10,2)))

# smallest divisor of given number n 

n = int(input("enter number: "))

for i in range(2,n+1):
    if(n % i == 0):
        print(f"{i} is the smallest divisor of {n}")
        break


i = 2
while (i<=n):
    if(n % i == 0):
        print(f"{i} is the smallest divisor of {n}")
        break
    i += 1


# print numbers in the given list which are not divisible by 5


l = [10, 16, 17, 18, 20, 22, 35]


for x in l:
    if( x % 5 == 0):
        continue
    print(x,end = " ")


# print tables of numbers from 1 to n

n = int(input("enter number : "))

for i in range(1,n+1):
    print(i,": ", end = " ")
    for j in range(1,11):
        print(i*j, end = " ")
    print()

def f(): pass
print(type(f()))


n = int(input("enter number : ")) 

for i in range(n):
    if i == 0:
        print("*")
    elif i == n-1:
        print("*"*n)
    else:
        print("*"," "*(i-2),"*")
        
def fib(n):
    if (n == 1) or (n == 2):
        return 1
    res = fib(n-1) + fib(n-2)
    return res

print(fib(6))

a = int(input("enter number a : ")) 
b = int(input("enter number b : ")) 

def gcd(a, b):
    
    # code here to calculate and return gcd of a and b
    counter = a if (a<b) else b
    for i in range(counter,0,-1):
        if(b % i ==0) and (a % i ==0):
            return i

print(f"GCD of {a}, {b} is",gcd(a,b))

d = {0,1,2}

for i in d:
    print(i)
print(False)

test = "ari"
print("A" in test)
print(not("a"or"")not in test )

print(oct(23))

print(oct(23) + oct(23))

print(~(~2))


def myFunc(*c):
    for i in c:
        print(i)
myFunc(1,62378,0,"saha")

def myTest(**t):
    for key, value in t.items():
        print(key,value)
        
myTest(a="test",b=3,t=5148)

# pattern finding 

''' i/p : text -> geeks for geeks
           pat -> geeks
        o/p -> 0 10
'''

text = "geeks for geeksgeeksgeefs geeksian "
pat = "geeks"

i = 0

while True:
    pos = text.find(pat,i)
    if pos == -1:
        break
    print(pos, end = " ")
    i = pos + len(pat) 
    
    
''' i/p : text -> AAAAA
           pat -> AAA
        o/p -> 0 1 2
'''

#method01
text = "AAAAA"
pat = "AAA"

i = 0

while True:
    pos = text.find(pat,i)
    if pos == -1:
        break
    print(pos, end = " ")
    i = pos + 1


#method02
text = "AAAAA"
pat = "AAA"

pos = text.find(pat)
while pos >= 0:
    print(pos, end = " ")
    pos = text.find(pat,pos+1)
    
    
def reverseString(s):
    #Write your code below to reverse s and return it
    s_list = list(s)
    reverse_string = []
    for i in range(len(s_list)):
        j = len(s_list)-(i+1)
        reverse_string.append(s_list[j])
    return "".join(reverse_string)

def reverseString(s):
    return s[::-1]

print(reverseString("hello"))



