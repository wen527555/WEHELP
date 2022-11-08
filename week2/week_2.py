# 要求一
def calculate(min, max, step):
    sum=0
    while min<=max:
        sum+=min
        min+=step
    print(sum)


# 請用你的程式補完這個函式的區塊
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0
print("----------------------")

#要求二
def avg(data):
# 請用你的程式補完這個函式的區塊
    sum = 0
    count = 0
    employees = data["employees"]
    for employee in employees:
        if  employee["manager"]==False:
            sum+=employee["salary"]
            count+=1
    result=sum/count
    print(result)


avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

print("----------------------")

#要求三
def func(a):
# 請用你的程式補完這個函式的區塊
    def multiply(b,c):
         print(a + (b * c))
    return multiply
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

print("----------------------")

#要求四
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    result=[]
    for i in range(len(nums)):
        for j in range( i+1, len(nums)):
            result.append(nums[i] * nums[j])
    print(max(result))


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

print("----------------------")

#要求五
def twoSum(nums, target):
# your code here
    for i in range(len(nums)):
        dif=target-nums[i]
        if dif in nums and nums.index(dif) !=i:
            return [i,nums.index(dif)]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9 

print("----------------------")
#要求六
def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    zeros = 0
    count = 0
    for num in nums:
        if num == 0:
            count +=1
            if count>zeros:
                zeros = count
        else:
            count =0
    print(zeros)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3