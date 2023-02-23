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
print(len(x))
for i in range(3,3):
    print(i)
#for i in range(1):
    #print(i)