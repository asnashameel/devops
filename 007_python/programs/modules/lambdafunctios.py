# def add(a,b):
#      return a+b
# print(add(1,2))

# mySum=lambda a,b : a+b
# print((lambda a,b: a+b)(2,4))

# print(mySum(3,4))

# example of lambda function in another function
# def power(x):
#      return lambda n: x**n
# print(power(4)(2))

# higher order functions
def Sum_number(x):
    return sum(x)

def higher_order_function(f,list):
    var = f(list)
    return var
result=higher_order_function(Sum_number,[1,2,3,4,5])
print(result)
