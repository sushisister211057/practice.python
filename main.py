#題目:學生成績管理系統
#(A)查詢(B)新增(C)刪除(D)修改

成績系統=["小明",82,"小杰",94,"阿花",85]
操作=input("請輸入操作指令(A)查詢(B)新增(C)刪除(D)修改 = ").upper()

# (A)查詢>無查到>有查到姓名跟成績
if 操作 == "A":
    姓名 = input("請輸入要查詢的姓名 : ")
    if 姓名 not in 成績系統:
        print("查無此人")
    else:
        順位=成績系統.index(姓名)
        print(f"{姓名}的成績是{成績系統[順位+1]}分")

#(B)新增姓名與成績
elif 操作 == "B":
    學生資料 = input("請輸入要新增的姓名/成績 : ")
    成績系統.extend(學生資料.split("/"))
    print("新增完畢")
    print(f"目前已登錄的學生人數為{int(len(成績系統)/2)}人")
    print(成績系統) 


#(C)刪除姓名與成績
elif 操作 == "C":
    姓名 = input("請輸入要刪除的姓名 : ")
    姓名位置 = 成績系統.index(姓名)
    成績系統.pop()
    成績系統.pop()
    print(成績系統)    

#(D)修改姓名及分數
elif 操作 =="D":
    姓名 = input("請輸入要修改的姓名 : ")
    成績 = input("請輸入要修改的成績 : ")
    姓名位置 = 成績系統.index(姓名)
    成績系統[姓名位置+1]=成績
    print(成績系統)

