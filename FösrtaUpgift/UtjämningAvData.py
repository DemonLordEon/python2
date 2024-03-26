print("write a number")
print("To Utjämna data")
numbers = input().split()
numbers = list(map(int, numbers))

output = []

for i in range(len(numbers)):
    print(numbers[i])
    if i == 0 or i == len(numbers) - 1:
        output.append(numbers[i])
    else:
        output.append((numbers[i] + numbers[i - 1] + numbers[i + 1]) /3)


print(output) 