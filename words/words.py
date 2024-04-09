dictionary = {

}

word = input().upper().replace(" ", "")

for letter in word:
    print(letter)
    if letter in dictionary:
        dictionary[letter] += 1
    else: 
        dictionary[letter] = 1 

print(dictionary)