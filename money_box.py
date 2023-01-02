import random

box = [1, 2]
keep_success = 0
keep_fail = 0
change_success = 0
change_fail = 0

num = int(input("반복 횟수 입력 : "))

for i in range(0, num):
    random.shuffle(box)
    if box[0] > box[1]:
        keep_success += 1
    else:
        keep_fail += 1

for i in range(0, num):
    random.shuffle(box)
    if box[0] < box[1]:
        change_success += 1
    else:
        change_fail += 1

print("")
print("%d번 중" %num)
print("유지시 유리 : %d회" %keep_success)
print("유지시 불리 : %d회" %keep_fail)
print("")
print("%d번 중" %num)
print("변경시 유리 : %d회" %change_success)
print("변경시 불리 : %d회" %change_fail)