import re
string= "Good morning all,kerala is good ,trivandrum is good"
# match = re.search("morning",string,re.I)
# # match = re.findall("morning",string,re.I)
# print(match)
# if match:
#     print(match.group(0))

match1 = re.findall("(?i)morning",string)
# print(match1)

match2  = re.findall("good",string,re.I | re.DOTALL)
# print("Find all",match2)

match3 = re.search("good.morning",string,re.I | re.DOTALL)
# print(match3)
# myspan = match3.span()
# print(myspan)

# l=[]
# for i in re.finditer(re.escape("Good"),string,re.I):
#     l.append(i.span())
#     print(i)
# print(l)

# match4=re.sub("(?i)Good","Awesome",string)
# print(match4)
# print(string)

# string1 = '''Hi
# Hello
# Welcome'''
# match5 = re.split('\n',string1)
# print(match5)

pattern = r'[k].*'
match6 = re.findall(pattern,string)
print(match6)


