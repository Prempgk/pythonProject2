N = int(input('Enter the no of students in even number:'))
if N % 2 == 0:
    class_A = []
    class_B = []
    for i in range(N):
        a = int(input('Enter the time for class A:'))
        b = int(input('Enter the time for class B:'))
        class_A.append(a)
        class_B.append(b)
    print(class_A)
    print(class_B)
    res = []
    for j in range(int(N/2)):
        x = min(class_A)
        k = class_A.index(x)
        if x <= class_B[k]:
            res.append(x)
            class_A.remove(x)
            class_B.remove(class_B[k])
        else:
            class_A.remove(x)
            res.append(class_B[k])
            class_B.remove(class_B[k])
    print(class_A)
    print(class_B)
    print(res)









else:
    print('Please enter the even number')