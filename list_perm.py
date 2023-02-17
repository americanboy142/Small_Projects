""" def main(x,piv,size):
    if piv == size:
        print(x)
        #print(x)
        return
    for i in range(piv,size):
        
        x[piv],x[i] = x[i],x[piv]
        main(x,piv+1,size)  
        x[i],x[piv] = x[piv],x[i]

x= [1,2,3,4,5]       
main(x,0,len(x)) """

x= [1,2,3,4]

""" def swap(x,l=0):
    if l==len(x):
        print(x)
        return
    else:
        for i in range(l,len(x)):
            x[i],x[l] = x[l],x[i]
            print("x[i]: ", x[i])
            print("x[l]: ", x[l])
            print("l: ", l)
            print("i: ", i)
            swap(x,l+1)
            x[l],x[i] = x[i],x[l]
            
    
    

swap(x) """

def main(n):
    thing = [[i+1] for i in range(len(x)) if (i+1)/x[i]%1==0 or x[i]/(i+1)%1!=0]


    print(thing[-1])

main(3)