# def hello_world(num1,num2):
#     print(num1+num2)
# hello_world(5,4)

# def hello_world(nums):
#     sum=0
#     for i in nums:
#         sum+=i
#     print(sum)
# hello_world([1,2,3,4,5,6])



# def check_is_prime(num):
#     for i in range(2,num//2):
#         if num%i==0:
#             print("not prime")
#             return
#     print("prime")
# check_is_prime(1)

def repeating_characters(num):
    set=[]
    for i in num:
        if i in set:
            return i
        else:
            set.append(i)
print(repeating_characters([1,2,4,3,3,4,5]))


