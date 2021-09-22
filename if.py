n = int(input("整数値:"))

if n > 0:
    if n % 2 == 0:
        print("その値は正です")
    else:
        print("その値は負です")
else: 
    print("正でない値が入力されました。")