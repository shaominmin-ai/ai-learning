try:

    number=int(input("请输入数字:"))
    print(number)

except ValueError:
    print("输入错误")

finally:
    print("程序结束")