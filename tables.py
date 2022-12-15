n = int(input('Enter the table numbers you want:'))
m = int(input('Enter the column value:'))
for i in range(1, n+1):
    print('Multiplication table for number:', i)
    for j in range(1, m+1):
        print(i, '*', j, '=', i * j)
