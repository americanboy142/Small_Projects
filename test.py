def sigma(a,b,prev_x,row):
    return (1/a[row]) * -sum(a[i]*prev_x[i] for i in range(len(a)) if i != row) + b[row]

def sigma_Gauss(a,b,x,prev_x,row):
    return (1/a[row]) * (-sum(a[i]*prev_x[i] for i in range(row-1) if i != row) - sum(a[i]*x[i] for i in range(row+1)) + b[row])

def thing(x,prev_x):
    return abs(max((x[i]-prev_x[i] for i in range(len(x))), key=abs))

a = [1,2,3]
b= [4,5,6]
x= [1,2,3]
x_prev = [5,0,0]
#thing = sigma_Gauss(a,b,x,x_prev,2)
#print(thing)
""" thin = thing(a,x_prev)
print(thin)
for i in range(len(x)):
    print(x[i]-x_prev[i]) """
""" print(len(x))
for i in range(3,3):
    print(i) """
#for i in range(1):
    #print(i)


a = [1,2,3]

def two_norm(U):
    return (sum(U[i]**2 for i in range(len(U))))**(1/2)

thing = []
for i in range(len(a)):
    thing.append(a[i]/two_norm(a))
print(thing)

a = [[1,2,3],[1,2,3],[1,2,3]]
b = [[1,2,3],[1,2,3],[1,2,3]]
thing = []
final = []
for i in range(len(a)):
    thing = []
    for deal in range(len(a[i])):
        thing.append(a[i][deal]+b[i][deal])
    final.append(thing)
if type(a) == list:
    print("hi")

import numpy as np

a = np.array([[1,2],[1,2]])
b = np.array([[1,2],[1,2]])

#print(a[0])
deal = np.array([[]])

#deal = np.concatenate((deal,[[1,2,3]]))
print("deal: ",deal)

#deal = np.concatenate((deal,[[4,5,6]]), axis=0)
print("deal:",deal)

c = np.array([1,2])
print(5*c)

poo = [[1,2,3],[1,2,3]]

thing1 = np.array([])
thing2 = np.array([])

poo.append([1,2,3])
print(poo)

shoot = np.add(poo[0],poo[1])
print("shoot: ",shoot)

thing1 = np.concatenate((thing1,poo[0]))
thing2 = np.concatenate((thing2,poo[1]))
print(thing1-thing2)
for i in poo:
    thing = np.array([])
    thing = np.append(thing,i)
    print(thing)

