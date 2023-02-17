""" def order_list(perm,i,x):
    list_list = []
    temp_list = x

    for it in range(1,perm):
        for j in x:
            fisrt = x[j]
            for f in range(len(x)-1):
                




x = [1,2,3]
def factorial(n):
    fact = n
    for i in range(1,n):
        fact *= i
    return fact


perm = factorial(len(x))


thing = order_list(perm,1,x)
print(thing)

"""

""" x=[1,2,3]
templist=[]
for j in x:
    templist=[]
    templist.append(j)
    print("j: ",j)
    for i in x:
        print("i: ",i)
        if i != j:
            templist.append(i)
    print(templist)

for i in range(len(x)):
    curr_first = x[i]
    for j in range(len(x)):
        curr_second = x[j]

 """

x = [1,2]

""" if x & 1:
    print("odd")
else:
    print("even")
     """
list_list = []
count = 0

class thing:
    def __init__(self,n):
        x = list(range(1,n+1))       
        #print("x: ",x)
        self.count = 0
        self.swap(x,n)
        print(self.count)

    def check(self,x):
        check_i = 0
        for i in range(len(x)):
            #print("thing")
            if (i+1) / x[i] % 1 == 0 or x[i] / (i+1) % 1 == 0:
                #print("i/x[i]: ", (i+1)/x[i])
                #print("x[i]/i: ", x[i]/(i+1))
                #print("true")
                check_i += 1       
        if check_i == len(x):
            self.count += 1
            #print(self.count)

    def swap(self,x,length):
        #print(size)
        if length == 1:
            self.check(x)
            return
            
        for i in range(length):
            #print("call")
            self.swap(x,length-1)
            #print(size)
            if length & 1:
                x[0],x[length-1] = x[length-1],x[0]
                #print("if called")
                #print(a)
            else:
                x[i], x[length-1] = x[length-1],x[i]
                #print("else called")
                #print(a)

n=10
thing(n)
