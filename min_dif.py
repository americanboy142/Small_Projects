def switch(x,mean,swaps):
    if swaps == 3:
        print(x)
        return x
    to_swap = False
    if abs(mean - max(x)) < abs(min(x) - mean):
        to_swap = True # true if max(x) < min(x)

         
    for i in range(len(x)):
        if to_swap == False and x[i] == max(x) or to_swap == True and x[i] == min(x):
            x[i] = mean
            break
    switch(x,mean,swaps+1)

    

def main(x):
    if len(x) <= 4:
        return 0
    else:
        median = x.sort()
        switch(x,int(mean),0)
        print(x)
        return abs(min(x)-max(x))
        
        
thing = main([1,5,0,10,14])

print(thing)