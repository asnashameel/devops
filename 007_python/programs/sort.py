# Fruits=["Apple","Mango","Banana","Orange"]
# Fruits.sort()
# print(Fruits)


# def sort_list(fruits):
#     #  fruits.sort(reverse=True)
#     #  return fruits
#      return sorted(fruits, reverse=True)
# fruits=["Apple","Mango","Banana","Orange"]
# print(sort_list(fruits))


# List=[4,5,3,7,8,10]
# List.sort()
# max=List[0]
# min=List[-1]
# print(max)
# print(min)


# def max_min(list):
#     max_value=max(list)
#     min_value=min(list)
#     return(max_value,min_value)
# list=[1,4,5,6,2,3]
# print(max_min(list))


# def max_min(list):
#     n_largest=max(list)
#     min=min(list)
#     return(max,min)
# list=[1,4,5,6,2,3]
# print(max_min(list))

# def nth_max_min(list, n):
#     if n > len(list) or n < 1:
#         return "Invalid value of n"

#     sorted_list = sorted(list)  
#     nth_smallest = sorted_list[n - 1]  
#     nth_largest = sorted_list[-n]  

#     return (nth_largest, nth_smallest)


# list = [1, 4, 5, 6, 2, 3]
# n = 2
# print(nth_max_min(list, n))  

# def second_largest_smallest(lst):
#     first_min = second_min = float('inf')  # Initialize to infinity
#     first_max = second_max = float('-inf')  # Initialize to negative infinity

#     for num in lst:
#         # Find smallest and second smallest
#         if num < first_min:
#             second_min = first_min
#             first_min = num
#         elif num < second_min and num != first_min:
#             second_min = num

#         # Find largest and second largest
#         if num > first_max:
#             second_max = first_max
#             first_max = num
#         elif num > second_max and num != first_max:
#             second_max = num

#     return (second_min, second_max)

# # Example list
# lst = [1, 7, 4, 9, 3, 2, 5]
# second_smallest, second_largest = second_largest_smallest(lst)

# print("Second Smallest:", second_smallest)
# print("Second Largest:", second_largest)


# def second_largest_smallest(lst):
#     first_min = min(lst)  # Find the smallest element
#     first_max = max(lst)  # Find the largest element

#     lst_without_min = [num for num in lst if num != first_min]  # Remove smallest
#     lst_without_max = [num for num in lst if num != first_max]  # Remove largest

#     second_min = min(lst_without_min)  # Find new smallest
#     second_max = max(lst_without_max)  # Find new largest

#     return (second_min, second_max)

# # Example list
# lst = [1, 7, 4, 9, 3, 2, 5]
# second_smallest, second_largest = second_largest_smallest(lst)

# print("Second Smallest:", second_smallest)
# print("Second Largest:", second_largest)


# def second_largest_smallest(lst):
#     first_min = min(lst)  # Find the smallest element
#     first_max = max(lst)  # Find the largest element

#     lst_without_min = [num for num in lst if num != first_min]  # Remove smallest
#     lst_without_max = [num for num in lst if num != first_max]  # Remove largest

#     second_min = min(lst_without_min)  # Find new smallest
#     second_max = max(lst_without_max)  # Find new largest

#     return (second_min, second_max)

# # Example list
# lst = [1, 7, 4, 9, 3, 2, 5]
# second_smallest, second_largest = second_largest_smallest(lst)

# print("Second Smallest:", second_smallest)
# print("Second Largest:", second_largest)



# def second_largest(list):
#     n=len(list)
#     fm=0
#     sm=0
#     for i in list:
#         fm=max(fm,list[i])
#         if list[i]!=fm:
#             sm=max(sm,list[i])
#     return sm

# list=[4,3,6,8,9,1,2]
# print(second_largest(list))

def repeating_character(list):
    unique_numbr=[]
    count=[]
    n=len(list)
    for num in list:
        if num in unique_numbr:
            index=unique_numbr.index(num)
            count[index]+=1
        else:
            unique_numbr.append(num)
            count.append(1)
    for i in range(len(unique_numbr)):
        print(f"{unique_numbr[i]} appears {count[i]} times")

list=[3,5,2,7,9,9,7,8,3,2,4]
print(repeating_character(list))   

