# list=[i*i for i in range(10)]
# print(list)
lang="python"
# lst=list(lang)
# print(type(lst))
# print(lst)

# lst1=[i for i in lang]
# print(lst1)
# print(type(lst1))

# lst2=[i for i in range(20)]
# print(lst2)

# lst3=[i*i for i in range(4)]
# print(lst3)

# lst4=[(i,i*i) for i in range(5)]
# print(lst4)
# print(type(lst4))
# print(lst4[2][1])

# lst5=[(i*2) for i in range(10)]
# print(lst5)


# lst6=[i for i in range(10) if (i%2==1)]
# print(lst6)
# lst7=[(i*2+1) for i in range(10)]
# print(lst7)

# lst8=[i for i in range(10) if i>3 and i%2==0]
# print(lst8)

lst9=[[1,2,4],[5,6,7],[9,8,5]]#flatten the list
flat_list=[number for row in lst9 for number in row]
print(flat_list)

