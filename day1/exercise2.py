#BMI
'''
height = float(input("키를 입력하세요(m)"))
weight = float(input("몸무게를 입력하세요"))

bmi = weight/(height**2)

if bmi < 18.5:
    print("저체중")
elif bmi < 24.9:
    print("정상")
elif bmi < 29.9:
    print("과체중")
else:
    print("비만")


# 커피 자판기
money = int(input("돈을 넣으세요"))

if money < 2500:
    print("금액이 부족합니다. 다시 넣어주세요")
else:
    change = money - 2500
    print("커피 나왔습니다! 거스름돈은", change, "입니다.")

'''

#구구단
def multi(x):
    for i in range(10):
        print(x, "X", i, "=", x*i)

x = int(input("구구단 몇단?"))
multi(x)
