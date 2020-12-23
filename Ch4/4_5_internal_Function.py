"""
날짜 : 2020/12/23
이름 : 정유락
내용 : 파이썬 내장함수 실습하기
"""

# all() : 리스트에서 0이 포함되었는지 확인
list1 = [1, 2, 3, 4, 5]
list2 = [0, 2, 3, 4, 5]

r1 = all(list1)
r2 = all(list2)

print('r1 : ', r1)
print('r2 : ', r2)

# any() : 리스트에서 True값이 하나라도 있으면 전체 True, 모두 False이면 전체 False
list3 = [0, 2, 3]
list4 = [0, '', None]

r3 = any(list3)
r4 = any(list4)

print('r3 : ', r3)
print('r4 : ', r4)

# enumerate() : for문에서 리스트의 인덱스와 값을 리턴하는 함수
list5 = ['김유신', '김춘추', '장보고']
for i, name in enumerate(list5):
    print(i, name)



# lambda
# time()
# time()
# calendar()
# abs()
# ceil()
# floor()
# round()
# random()
