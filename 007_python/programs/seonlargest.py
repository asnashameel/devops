
def second_largest(list):
    n=len(list)
    fm=0
    sm=0
    for i in range(0,n):
        fm=max(fm, list[i])
        if list[i]!=fm:
            sm=max(sm, list[i])
    return sm

list=[4,3,6,8,9,1,2]
print(second_largest(list))