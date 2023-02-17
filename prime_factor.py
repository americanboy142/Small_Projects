import asyncio
import time
x = []
# split split the number into the two biggest divisors
# will be used for all numbers multiple times until in form (1,prime)
async def split(n):
    biggest_Split = n**(1/2)
    #print("biggest_Split: ", biggest_Split)
    if biggest_Split % 1 == 0:
        return (biggest_Split,biggest_Split)
    else:
        #print(biggest_Split%1)
        #print("bigsdas: ", int(biggest_Split))
        biggest_Split = int(biggest_Split)

        for i in range(biggest_Split-1):
            test_num = n/biggest_Split

            if test_num % 1 == 0:
                #print("thingw: ",biggest_Split,test_num)
                return (biggest_Split,test_num)
            if biggest_Split & 1:
                biggest_Split -= 2
            else:
                biggest_Split -= 1
    return(1,n)


#%{
# if split[i][0] == 1 then print split[i][1]
# else check( split( tuple[0] and tuple[1] ) )
#
# recursive function continues untill all prime factors are printed
#}
async def check(tuple,x):
    #print(tuple)
    lowest_split = tuple[0]
    if lowest_split == 1:
        # star added to check work at end
        #print("tuple[1]: ", tuple[1])
        #if tuple[1] != None:
        x.append(int(tuple[1]))
        return
        #factors = factors + str(tuple[1]) + ","
    else:
        await asyncio.gather(*[check(tup,x) for tup in (await asyncio.gather(split(int(tuple[0])),split(int(tuple[1]))))])


#%{
#   where everything is ran
#       - calls check() with split(n)
#   n is number that needs to be factored
#   Start, Ends and Prints timer to see how long factoring took
#}
async def main(n):
    s = time.perf_counter()
    x=[]
    #first_Split = await split(44215651515)
    #print("first split" , first_Split)
    #await check(first_Split)
    while n % 2 == 0:
        x.append(2)
        n/=2
    while n %  3 == 0:
        x.append(3)
        n/=3
    while n % 5 == 0:
        x.append(5)
        n/=5
    while n % 7 == 0:
        x.append(7)
        n/=7

    #print(n)
    await check(await split(n),x)

    elapsed = time.perf_counter() - s
    print(f"Time: {elapsed:0.3f} seconds.")
    return x

def test_list(factors_list, original):
    prod = 1
    for p in factors_list:
        prod *= p
    if prod == original:
        print(f"Test Passed: {prod} = {original}")
    else:
        print(f"Test Failed: {prod} != {original}")
     


test = [56152125616156255616148941146141488498,515612615,15126589489,598,48894894,89,489489489,48914894189,5,2348923847938743]
for i in range(len(test)):
    list = []
    #print(list)
    print("======================= Test =========================")
    list = asyncio.run(main(test[i]))
    print("List: ", list)
    test_list(list,test[i])
    



