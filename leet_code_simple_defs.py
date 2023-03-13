def runningSum(nums):
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

def pivotIndex(nums):
        Sum_left = 0
        Sum_right = sum(nums)
        print(Sum_right)
        for i in range(len(nums)):
            Sum_right -= nums[i]
            print(Sum_right,Sum_left)
            if Sum_left == Sum_right:
                return i
            Sum_left += nums[i]
        return -1

def getMaxProfit(nums):
    maxx = max(nums)
    profit = []
    lenn = len(nums)
    for i in range(lenn):
        test = []
        if i != maxx:
            for j in range(i,lenn):
                test.append(nums[j] - nums[i])
            profit.append(max(test))
        else:
            profit.append(0)
    return max(profit)

def reverse_int(int):
    int = str(int)
    thing = ""
    for i in range(len(int)-1,-1, -1):
        #print(i)
        thing += int[i]
    return thing
                 
def unique_char(string):
    string = string.lower()
    thing = len(string)
    for i in range(thing):
        if string[i].isalnum():
            unique = True
        for j in range(i+1,thing):
            if string[i] == string[j]:
                unique = False
                break
        if unique:
            return i
    return -1

def is_anagram(a,b):
    if len(a) == len(b):
        for i in a:
            b = b.replace(i,"",1)
        if b == "":
            return True
    return False

def is_palendrome(string):
    backword = ""
    string = string.lower()
    for i in string:
        if not i.isalnum():
            string = string.replace(i,"")
    for i in range(len(string)-1,-1,-1):
        backword += string[i]
    print(backword)
    if backword == string:
        return True
    return False

def fact_rec(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * fact_rec(n-1)
    else:
        return -1
    
def plusMinus(arr):
    # Write your code here
    main_list = [0,0,0]
    lenn = len(arr)
    for i in arr:
        if i < 0:
            main_list[1] += 1
        elif i> 0:
            main_list[0] += 1
        else:
            main_list[2] += 1
    for i in main_list:
        print(round((i/lenn),6))

def miniMaxSum(arr):
    # Write your code here
    maxx = max(arr)
    minn = min(arr)
    summ = sum(arr)
    print(summ-maxx, summ-minn)

def timeConversion(s):
    # Write your code here
    split = s.split(":")
    if s[-2] == 'P' and int(split[0]) != 12:
        s = s.replace(s[0],str(int(s[0])+1),1)
        s = s.replace(s[1],str(int(s[1])+2),1)
            
    if s[-2] == 'A' and int(s[0]) == 1 and int(s[1]) == 2:
        s = s.replace(s[0],str(int(s[0])-1),1)
        s = s.replace(s[1],str(int(s[1])-2),1) 
            
    s = s.replace(s[-1],'')
    s = s.replace(s[-1],'')
    print(s)

def findMedian(arr):
    # Write your code here
    arr.sort()
    print(arr[int(len(arr)/2)])
    

print(int(25/2))


