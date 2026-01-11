datas = input()
alphabet = []
digit = 0

for data in datas:
    if data.isalpha():
        alphabet.append(data)
    else:
        digit += int(data)

alphabet.sort()

print("".join(alphabet) + str(digit))