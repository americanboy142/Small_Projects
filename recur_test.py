def gird(n,m):
    if n ==1 or m ==1:
        print(n,m)
        return 1
    else:
        print(n,m)

        return gird(n-1,m)+gird(n,m-1)
        
#thing = gird(3,3)
#print(thing)

def test(n):
    print(n)
    if n == 1:
        return 1
    else: 
        return test(n-1) * n
        
#thin = test(4)
#print(thin)

def back(n):
    if n == 3:
        print(n)
        return 1
    else:
        for i in range(n,4):
            back(n)
        return
        
#thing= back(0)
#print(thing)

def perm(x,size,piv=0):
    if piv == size:
        print(x)
        #print(x)
        return
    for i in range(piv,size):       
        x[piv],x[i] = x[i],x[piv]
        perm(x,size,piv+1)  
        x[i],x[piv] = x[piv],x[i]

            
#hting = perm([1,2,3,4,5],5)
#print(hting)

def test(n):
    if n == 1:
        return 1
    for i in range(1,n):
        print(i)
        test(n-1)
    print("after")
    
#thing = test(5)
#print(thing)

def sum(n):
    if n ==0:
        return 0
    else:
        print(f"{n} + sum({n-1})")
        return sum(n-1) + n

#thing = sum(10)
#print("sum:",thing)

def factorial(n):
    if n == 0:
        print("1")
        return 1
    else:
        #poo = factorial(n-1)
        print(f"{n} * factorial({n-1})")
        return n * factorial(n-1)
        

#thing = factorial(5)
#print("fact:",thing)

#import numpy as np

def order_list(list,l=0):
    if l == len(list):
        #print("hi")
        #print(list)
        return list
    else:
        for i in range(len(list)):
            #print("looped")
            if list[i] > list[l]:
                list[i],list[l] = list[l],list[i]
                #print(list)
        return order_list(list,l+1)


test = [[2,5,6,4,561,6514,9,11,5,4,6,1,5,61,15,65,1,1,45,16156,5],[5,2,15,5,15,52,2,51,15,256526,5],[5,2,6.56,4,5,2,5,4,5,66,2,5,6,2,5,5,2,]]        
for i in test:
    thiing = order_list(i)
    print(thiing)
#eprint(numpy.random.randint(0,5161561561,3))