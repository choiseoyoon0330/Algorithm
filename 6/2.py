# swap
data =  [3, 5]
data[0], data[1] = data[1], data[0]
print(data)

temp = data[0]
data[0] = data[1]
data[1] = temp
print(data)