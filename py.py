print('0～100 までの得点（整数値）を２つ入力してください')
a = int(input('１つ目の得点：'))
b = int(input('２つ目の得点：'))
a,b = sorted([a,b])
if a == b:
    print(a)
else:
    print(b,a)