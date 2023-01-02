print("a/b 형태로 입력 : ", end="")
a, b = map(int, input().split('/'))

print(f"{a//b}.", end="")

for i in range(100):
# while True:
    if a >= b:
        print(a//b, end="")
        a = a % b
    elif a == 0:
        print(0)
        break
    else:
        a *= 10
        print(a//b, end="")
        a = a % b