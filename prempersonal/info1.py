N = int(input('enter the limit'))
A = []
for i in range(N):
    x = int(input('enter the value'))
    A.append(x)

for i in range(N):
    i += 1
    x = A[N - i]
    y = x - 1
    z = x + 1
    if y in A:
        A.remove(A[A.index(y)])
        if z in A:
            A.remove(A[A.index(z)])
print('The Maximum power is:', sum(A))


