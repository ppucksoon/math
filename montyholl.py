import random

change_success = 0
change_fail = 0
keep_success = 0
keep_fail = 0
blind = ["car", "goat", "goat"]

num = int(input("반복 횟수 : "))

for i in range(0, num):
    random.shuffle(blind)

    choice = random.choice(blind)

    if choice == "goat":
       change_success += 1
    elif choice == "car":
        change_fail += 1

for i in range(0, num):
    random.shuffle(blind)

    choice = random.choice(blind)

    if choice == "goat":
       keep_fail += 1
    elif choice == "car":
        keep_success += 1

print("")
print("%d회 중" %num)
print("변경시 성공 횟수(확률) : %d회" %change_success)
print("변경시 실패 횟수(확률) : %d회" %change_fail)
print("")
print("%d회 중" %num)
print("유지시 성공 횟수(확률) : %d회" %keep_success)
print("유지시 실패 횟수(확률) : %d회" %keep_fail)