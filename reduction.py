while True:
    a = int(input("a/b에서 a값(분자) 입력(정수) : "))
    b = int(input("a/b에서 b값(분모) 입력(정수) : "))
    i = 1; temp_a = 1; temp_b = 1

    if b == 0:
        print("분모에는 0이 올 수 없습니다.")
        print("나가려면 Ctrl + c")
        print("")
        continue

    if a < 0:
        a *= -1
        temp_a = -1
    if b < 0:
        b *= -1
        temp_b = -1

    while True:
        if i <= a and i <= b:
            if a % i == 0 and b % i == 0:
                gcd = i
            i += 1
        else: break

    result_a = (temp_a * a) / gcd
    result_b = (temp_b * b) / gcd
    if result_b < 0:
        result_b *= -1
        result_a *= -1

    if result_b == 1:
        print("%d/%d = %d" %(a, b, result_a))
    else:
        print("%d/%d = %d/%d" %(a, b, result_a, result_b))
    print("나가려면 Ctrl + c")
    print("")