# bubble sort of dictionary

# def bubble_sort(data):
#     items=list(data.items())
#     n=len(items)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if items[j][1] > items[j+1][1]:
#                 items[j],items[j+1] = items[j+1],items[j]
#     return dict(items)


# data={"apple":3,"mango":5,"pine apple":9,"orange":4}
# print(bubble_sort(data))


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return dict(arr)



data={"apple":3,"mango":5,"pine apple":9,"orange":4}
print(bubble_sort(data))



