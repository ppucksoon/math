def factorial(n):
    i = 1; result = 1
    while i <= n:
        result *= i
        i += 1
    return result

while True:
    permutation = 1

    choice = int(input("1. 순열 (nPr)\n2. 조합 (nCr)\n>>> "))

    if choice == 1:
        combi = 0
    elif choice == 2:
        combi = 1
    else:
        print("1또는 2중에서 선택해 주세요.\n")
        continue
        
    print("")
    n = int(input("n : "))
    r = int(input("r : "))
    temp = n - r + 1

    if combi == 0:
        print("%dP%d =" %(n, r), end=" ")
    elif combi == 1:
        print("%dC%d =" %(n, r), end=" ")

    while n >= temp:
        permutation *= n
        n -= 1

    if combi == 1:
        combination = permutation / factorial(r)
        print(combination)
    else:
        print(permutation)
    print("")