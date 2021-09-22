print('AからBまでの和を求めます')
while True:
    A = int(input('Aの値'))
    if A > 0:
        break
B = int(input('Bの値'))
sum = 0
i = A
while i <= B:
    sum += i
    i += 1
print(A, 'から', B, 'までの和は', sum, 'です。')