numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

t = numbers[:4]
y = numbers[5::]
average = (sum(t)+sum(y))/len(numbers)
new_num = numbers
new_num[4] = average
print("Измененный список:", new_num)
