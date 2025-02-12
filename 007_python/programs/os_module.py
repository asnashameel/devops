import os
print("current working directory",os.getcwd())
try:
    f = open("file.txt")
    # print(f.read())
    # print(type(f.readline()))
    # print(type(f.readlines()))
except FileNotFoundError:
    print("file not found")
    os.remove("C:\\Users\\Administrator\\Desktop\devops\\007_python\day1\\hello.txt")
    # f = open("test.txt")
finally:
    f.close()