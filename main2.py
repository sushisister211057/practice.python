#應用練習：密碼登入系統(for loop 迴圈)

正確帳號密碼="1234"

#回傳0~4值
for 次數 in range(5):
    密碼 = input("請輸入密碼: ")

    if 密碼 == 正確帳號密碼:
        print("歡迎登入")
        break

    elif 密碼 != 正確帳號密碼 and 次數 <4:
        print("請重新輸入")
        print(f'您還有{4-次數}次機會')

    else:
        print("您已輸入太多次帳號密碼，帳號已被鎖定")
