# def check_is_prime(num):
#     for i in range(2,num//2):
#         if num%i==0:
#             print("not prime")
#             return
#     print("prime")
# check_is_prime(1)

def f(fname,lname):
    return fname+" "+lname

def sum2no(a,b):
    return a+b

person = {"first_name":"asna","last_name":"shameel","uid":290419,"friends":["abc","cdf"],
          "skills":{
              "backend_skills":["nodejs","ruby"],
              "databases":["redis","mysql","postgres"]
          }}
print(len(person))
print(person.get("skills").get("backend_skills"))