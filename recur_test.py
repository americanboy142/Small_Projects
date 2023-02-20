import numpy as np

test_arrays = []
test_num_array =[]

for i in range(10):
    temp=[]
    for i in range(np.random.randint(5,15)):
        temp.append(np.random.randint(0,10000))
    test_arrays.append(temp)

for i in range(10):
    test_num_array.append(np.random.randint(0,100))


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
""" 
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

        
for i in test_arrays:
    thiing = order_list(i)
    print(thiing) """
#eprint(numpy.random.randint(0,5161561561,3))

thing = np.array(([7.0,-6.0,3.0],[-8.0,9.0,-4.0]))
sol_vec = np.array([3.0,-4.0])
#return solved for matrix
def solver(matrix,row=0,col=0):
    if row == len(matrix):
        #print(matrix)
        #print("hi")
        return matrix
    else:
        #print("i before",i)
        #print(matrix[row][col])
        """ for element in range(len(matrix[row])):
            matrix[row][element] = float(matrix[row][element])
        print(matrix) """
        
        #print(matrix[row])
        #print(matrix[row][col])
        #print(matrix)
        matrix[row][-1] /= float(matrix[row][col])
        for element in range(len(matrix[row])-1):
            if element != col:
                #print(matrix[row][element])
                matrix[row][element] /= - float(matrix[row][col])
                #print("after: ", matrix[row][element])
        #print("before: ", matrix[row][-1])    
        matrix[row][col] /= float(matrix[row][col])
        
        #print("after: ", float(matrix[row][col]) / float(matrix[row][-1]))
        #matrix[row][col],matrix[row][0] = matrix[row][0],matrix[row][col]
        #print(matrix)
        return solver(matrix,row+1,col+1)

# given a solved matrix and x0 vector
# return a solution vector

def itersolve(s_matrix,x0,row=0,col=0,count=0):
    if count == 2:
        #print("thing", x0)
        return x0
    else:
        if col == len(s_matrix):
            
            #print("ran")
            return itersolve(s_matrix,x0,0,0,count+1)
            #return x0

        else:
            #x_vec = s_matrix[row].copy()
            for i in range(len(x0)):
                #print(i)
                if i != row:
                    x0[row] += (s_matrix[row][i]*x0[i])
                #else:
                    #print("diagonal: ", s_matrix[row][i])
                    

            x0[col] += s_matrix[row][-1]
            #print(x0)

            
            return itersolve(s_matrix,x0,row+1,col+1,count)
                

def itersolve2(s_matrix,x0,temp_vec,row=0,col=0,count=0):
        print("temp_vec:", temp_vec)
        if col == len(s_matrix):
            #needs prev vector to only change on row change
            #print(x0)
            #print("ran")
            x0 = temp_vec.copy()
            if count == 3:
                return x0
            else:
                return itersolve2(s_matrix,x0,temp_vec,0,0,count+1)
            #return x0

        else:
            #x_vec = s_matrix[row].copy()
            for i in range(len(x0)):
                #print(i)
                if i != row:
                    temp_vec[row] += (s_matrix[row][i]*x0[i])
                #else:
                    #print("diagonal: ", s_matrix[row][i])
                    

            temp_vec[col] += s_matrix[row][-1]
            #print(x0)

            print("temp_vec after:", temp_vec)
            return itersolve2(s_matrix,x0,temp_vec,row+1,col+1,count)
                



    

    #print("hi")

temp_matrix = thing.copy()

x0 = [0,0]

thin = solver(temp_matrix)
#print(len(thin))

thing = itersolve2(thin,x0,x0.copy())

print("thing:",thing)

