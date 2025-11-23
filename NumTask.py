

numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
squares = []
even_num =[]
for num in numbers:
    squares.append(num**2)
    sqa_num = [num**2 for num in numbers]
    if num % 2 == 0:
        even_num.append(num)

print('Original num:', numbers)
print('Square num:', sqa_num)
print('Even num:', even_num)