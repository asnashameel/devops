def repeating_characters(list):
    count=[]
    unique_number=[]
    for num in list:
        if num in unique_number:
            index=unique_number.index(num)
            count[index]+=1
        else:
            unique_number.append(num)
            count.append(1)
    for i in range(len(unique_number)):
        print(f"{unique_number[i]} repeats {count[i]} times")
list = [1,2,4,5,5,6,3,2,1]
repeating_characters(list)