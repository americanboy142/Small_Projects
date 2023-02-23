'''
 will be used for each row in the matrix/b/x^(k-1)
 just returns x(i)^(k) as diffiend by lecture
 a[i] is entries from the given row or A
 if is there to stop from icluding diagonal entries of A 
2/22/2023  
'''
def sigma_Jacobi(a,b,prev_x,row):
    return (sum(-a[i]*prev_x[i] for i in range(len(a)) if i != row) + b) / a[row]
'''
 same idea as above but for Gauss-Seidel
 difference is i added a check if it is the first row of matrix
 if it is then it just does Jacobi sum
 if not then it sums elements before diagonal with x and then sums elements after diagonal with prev_x
 returns x(i)^(k) using x(j)^(k) when possible as diffiend by lecture
2/22/2023  
'''
def sigma_Gauss(a,b,x,prev_x,row):
    if row != 0:
        return (sum(-a[i]*x[i] for i in range(row)) + sum(-a[j]*prev_x[j] for j in range(row+1,len(x))) + b) / a[row]
    return sigma_Jacobi(a,b,prev_x,row)

'''
 check def from Jacobi
 checks the condition given in the homework
2/22/2023
'''
def check(prev_x,x,TOL):
    if abs(max((x[i]-prev_x[i] for i in range(len(x))), key=abs)) / abs(max(x)) < TOL:
        return True
    else:
        return False

def Jacobi(A, b, x, TOL, max_iterations):
    '''
     stop condition only on max_iterations
     will have a check function for norm stop condition, to allow for recurtion
    2/22/2023
    '''
    if max_iterations == 0:
        return x
    else:
        prev_x = x.copy()
        '''
         loops through all rows of A and sum up all elements mulitplied by prev_x
        2/22/2023
        '''
        for row in range(len(b)):
            x[row] = sigma_Jacobi(A[row],b[row],prev_x,row)

        '''
         if within Tolerance as difined by homework page then print within and return x
        2/22/2023
        '''
        if check(prev_x, x, TOL):
            print(f"Within Tolerance After: {25-max_iterations} iterations")
            return x
        else:
            '''
             if not within Tolerance then call Jacobi again passing the next iteration
             subtracted because stopping condition of zero is easier for general cases
            2/22/2023
            '''
            return Jacobi(A, b, x, TOL, max_iterations-1)

'''
 this is basicaly the same as Jacobi, i even copy and pasted from above
 it just calles sigma_gauss instead of sigma_jacobi which requiers x and prev_x

2/22/2023
'''
def Gauss_Seidel(A, b, x, TOL, max_iterations):
    if max_iterations == 0:
        return x
    else:
        prev_x = x.copy()
        for row in range(len(b)):
            x[row] = sigma_Gauss(A[row],b[row],x,prev_x,row)
        if check(prev_x, x, TOL):
            print(f"Within Tolerance After: {25-max_iterations} iterations")
            return x
        else:
            return Gauss_Seidel(A, b, x, TOL, max_iterations-1)

   
'''
 testing
2/22/2023
'''
A = [[1,2,-2],[1,1,1],[2,2,1]] 
b = [7,2,5]
x = [0,0,0]
TOL = 10**(-5)
max_iterations = 25       
        
thin = Jacobi(A,b,x,TOL,max_iterations)
print(thin)

x = [0,0,0]

thing = Gauss_Seidel(A,b,x,TOL,max_iterations)
print(thing)

A1 = [[2,-1,1],[2,2,2],[-1,-1,2]] 
b1 = [-1,4,-5]
x1 = [0,0,0]

#max_iterations = 500 
thin = Jacobi(A1,b1,x1,TOL,max_iterations)
print(thin)

x1 = [0,0,0]

thin = Gauss_Seidel(A1,b1,x1,TOL,max_iterations)
print(thin)