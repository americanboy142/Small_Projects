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
    
def lonelyinteger(a):
    # Write your code here
    count=0
    tested = []
    while len(a) != 0:
        test= a[0]
        a.remove(test)
        if test not in a and test not in tested:
            print(test)
        tested.append(test)

def diagonalDifference(arr):
    left_index = 0
    right_index = len(arr)-1
    left_sum = 0
    right_sum = 0
    for i in arr:
        left_sum += i[left_index]
        right_sum += i[right_index]
        left_index += 1
        right_index -= 1
    print(abs(left_sum-right_sum))

def countingSort(arr):
    count = [0]*(max(arr)+1)
    for i in arr:
        count[i] += 1
    print(count)
    
def flipMatrix(arr):
    n = len(arr)
    maxx = 0
    Sum = 0

    for row in len(range(n/2)):
        for col in len(range(n/2)):
            maxx = min(min(i) for i in arr)
            maxx = max([arr[row][col],maxx])
            maxx = max([arr[row][col*n-1],maxx])
            maxx = max([arr[row*n-1][col],maxx])
            maxx = max([arr[row*n-1][col*n-1],maxx])

            Sum += maxx
    return Sum

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid-1], a[-1] = a[-1], a[mid-1]
    st = mid
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
        
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
    else:
        dirt_col_check = False
        dirt_row_check = False

        if 'd' in board[posr]:
            dirt_row = board[posr].index('d')
            row_dist = dirt_row - posr
            dirt_row_check = True


        for i in range(len(board)):
            if board[i][posc] == 'd':
                dirt_col = i
                col_dist = i - posc
                dirt_col_check = True
                break
        
        #print(dirt_col_check)
        #print(dirt_row_check)

        row_move = False
        col_move = False

        if dirt_row_check and dirt_col_check:
            if abs(row_dist) < abs(col_dist):
                row_move = True
            else:
                col_move = True
        elif dirt_row == True and dirt_col != True:
            col_move = True
        elif dirt_row != True and dirt_col == True:
            print("hi")
            row_move = True
        else:
            print("RIGHT")


        #print(row_move)
        #print(col_dist)

        if col_move:
            if col_dist < 0:
                print("UP")
            else:
                print("DOWN")

        if row_move:
            if row_dist < 0:
                print("LEFT")
            else:
                print("RIGHT")

#next_move(0,1,([['-','-','d'],['-','d','-'],['-','-','d']]))

def findMedianSortedArrays(a,b):
    mixed = sorted(a+b)

    n = len(mixed)
    middle = n//2

    if n & 1:
        print(mixed[middle])
    else:
        print((mixed[middle-1]+mixed[middle])/2)


def isMatch(s, p):
    def recur(i,j):
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if j+1 < len(p) and p[j+1] == '*':
            return recur(i,j+2) or (match and recur(i+1,j))
    
        if match:
            return recur(i+1,j+1)
        return False
    return recur(0,0)

def minDifference(nums):
        n = len(nums)
        if n > 4:
            nums.sort()
            min_diff = nums[-1]-nums[0]
            if min_diff != 0:
                for i in range(1,5):
                    test = nums[-i] -nums[0]
                    #print("yes")
                    #print(f"{nums[-i]} - {nums[0]} =" ,test)
                    #print(min_diff)
                    if test < min_diff:
                        #print("tested:" ,nums[-i])
                        #print(f"{nums[-i]} - {nums[0]} =" ,test)
                        min_diff = test
                        #print(min_diff)
                for i in range(4):
                    test = nums[-1] - nums[i]
                    #print("hi")
                    #print(test)
                    #print(f"{nums[-1]} - {nums[i]} =" ,test)
                    if test < min_diff:
                        min_diff = test
                        #print("tested:" ,nums[i])
                        #print(f"{nums[-1]} - {nums[i]} =" ,test)
                        #print(min_diff)
                
                if nums[-3] - nums[1] < min_diff:
                    min_diff = nums[-3] - nums[1]
                    #print(f"{nums[-2]} - {nums[i]} =" ,min_diff)
                if nums[-2] - nums[2] < min_diff:
                    min_diff = nums[-2] - nums[2]
                    #print(f"{nums[-2]} - {nums[2]} =" , min_diff)


            return min_diff
        return 0

def intToRoman4(num):
    s = ''
    posible = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],
                ['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    while num > 0:
        for i in posible:
            if num - i[1] >= 0:
                s+=i[0]
                num -= i[1]
                break
    return s

def intToRoman3(num):
    s = ''
    posible = [['M',1000,100],['D',500,100],['C',100,10],['L',50,10],
                ['X',10,1],['V',5,1],['I',1]]
    
    for i in posible:
        if num == i[1]:
            return i[0]

    digets = []
    base = 1
    while num > 0:
        digets.append(num%10*base)
        num//=10
        base *= 10
    digets.reverse()
    def reverse(num,posible,s):
        close = -1
        for i in range(len(posible)-1):
            if num + posible[i][2] >= posible[i][1]:
                close = posible[i][1]
                break
        
        if close > 0:
            dif = close - num
            while dif > 0:
                for i in posible:
                    if dif - i[1] >= 0:
                        s += i[0]
                        dif -= i[1]
                        num += i[1]
                        break
        return s,num
    print(digets)
    for num in digets:
        while num > 0:
            if num < 1000:
                s,num = reverse(num,posible,s)
            for i in posible:
                if num - i[1] >= 0:
                    s += i[0]
                    num -= i[1]
                    break
    return s



thin = intToRoman4(1994)
print(thin)
