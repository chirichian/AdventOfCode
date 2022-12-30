from re import I
from tkinter.tix import InputOnly


with open('input.txt') as file:
    #data = [i for i in file.read().strip().split('\n')]
    data = file.read().strip().split("\n")

list_result = []
count = 0
for item in data:
    if item!='':
        num = int(item)
        count+= num
    else:
        list_result.append(count)
        count=0
        

list_result.sort(reverse=True)

print(f"Max value is: {max(list_result)}")

print(f"Max value for top three: {sum(list_result[0:3])}")