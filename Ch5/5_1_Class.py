"""
날짜 : 2020/12/23
이름 : 정유락
내용 : 파이썬 클래스 실습하기
"""
from Ch5.sub1.Account import Account
from Ch5.sub1.Calc import Calc as c

# Account 객체 생성
kb = Account('국민은행', '101-12-1234', '김유신', 10000)
kb.deposit(20000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '101-11-1111', '김춘추', 30000)
wr.deposit(20000)
wr.withdraw(7000)
wr.show()

# Calc 객체 생성
c1 = c()
r1 = c1.plus(2, 3)
r2 = c1.minus(2, 3)
r3 = c1.multi(2, 3)
r4 = c1.div(6, 3)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)