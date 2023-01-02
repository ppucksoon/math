#------------------------함수 정의------------------------

def average(n, x, Px_numer, Px_denom): #이산확률 분포 표에서의 평균 값 계산
    i = 0
    j = 1
    numer = 0 #분자들의 합
    gcd = 0 #최대공약수
    lcm = 0 #최소공배수

    #분수 약분 (분자, 분모 최대공약수)
    for i in range(0, n): 
        Px_numer[i] *= x[i]
        while j <= Px_numer[i] and j <= Px_denom[i]:
            if Px_numer[i] % j == 0 and Px_denom[i] % j == 0:
                gcd = j
            j += 1
        Px_numer[i] = Px_numer[i] / gcd
        Px_denom[i] = Px_denom[i] / gcd
        j = 1

    #분수 통분 (분모끼리의 최소공배수)
    for i in range(0, n-1): 
        j = Px_denom[i] * Px_denom[i+1]
        while j >= 1:
            if j % Px_denom[i] == 0 and j % Px_denom[i+1] == 0:
                lcm = j
            j -= 1

    #통분된 분수의 분자끼리의 합
    for i in range(0, n):   
        Px_numer[i] *= lcm / Px_denom[i]
        numer += Px_numer[i]

    #분수 최종 약분
    j = 1
    while j <= numer and j <= lcm: 
        if numer % j == 0 and lcm % j == 0:
            gcd = j
        j += 1

    numer /= gcd
    lcm /= gcd
    result = [numer, lcm]

    return result

#------------------------초기 설정 및 값 입력------------------------

x = [] #이산확률변수
Px_numer = [] #확률의 분자
Px_denom = [] #확률의 분모

print("----------이산확률변수의 평균, 분산, 표준편차 계산기----------")
print("그만 입력 하려면 확률의 분자 또는 분모에 0입력")
print("")
n = 0

#값 입력
while True: 
    x.append(0)
    Px_numer.append(0)
    Px_denom.append(0)
    x[n] = int(input("%d번째 변수 값 입력(정수 n) : " %(n+1)))
    Px_numer[n], Px_denom[n] = map(int, input("%d번째 확률 입력(분수 a/b) : " %(n+1)).split("/"))

    if Px_numer[n] == 0 or Px_denom[n] == 0:
        del x[n]
        del Px_numer[n]
        del Px_denom[n]
        break
    n += 1

#입력 받은 초기 값 저장
x_mem = x[:]
Px_numer_mem = Px_numer[:]
Px_denom_mem = Px_denom[:]


#------------------------평균 값 계산------------------------

Ex = average(n, x, Px_numer, Px_denom)

#평균 출력
print("")
if Ex[1] == 1:
    print("E(x) = %d" %Ex[0])
else:
    print("E(x) = %d/%d" %(Ex[0], Ex[1]))

#초기 값 불러오기
x = x_mem[:]
Px_numer = Px_numer_mem[:]
Px_denom = Px_denom_mem[:]

#------------------------분산 값 계산------------------------  제곱 평균 - 평균 제곱

for i in range(0, n):
    x[i] *= x[i]

Ex_square = average(n, x, Px_numer, Px_denom) #(이산확률변수)제곱의 평균
square_Ex = [Ex[0]*Ex[0], Ex[1]*Ex[1]] #평균 제곱
#Ex_square, square_Ex --> 0번 항 = 분자 / 1번째 항 = 분모

#분수 통분 (분모끼리의 최소공배수)
i = Ex_square[1] * square_Ex[1]
while i >= 1:
    if i % Ex_square[1] == 0 and i % square_Ex[1] == 0:
        lcm = i
    i -= 1

#통분된 분수의 분자끼리의 차 
Ex_square[0] *= lcm / Ex_square[1]
square_Ex[0] *= lcm / square_Ex[1]
numer = Ex_square[0] - square_Ex[0]

#분산 최종 약분
i = 1
while i <= numer and i <= lcm: 
    if numer % i == 0 and lcm % i == 0:
        gcd = i
    i += 1
numer /= gcd
lcm /= gcd

#분산 출력
if lcm == 1:
    print("V(x) = %d" %numer)
else:
    print("V(x) = %d/%d" %(numer, lcm))

#------------------------표준편차 값 계산------------------------

num_fac_size = 0 #배열 numer_factor의 크기(원소 개수)
lcm_fac_size = 0 #배열 lcm_factor의 크기(원소 개수)
root_numer_int = 1 #√(numer) --> n√(m)에서 n
root_lcm_int = 1 #√(lcm) --> n√(m)에서 n
root_numer_decimal = 1 #√(numer) --> n√(m)에서 m
root_lcm_decimal = 1  #√(lcm) --> n√(m)에서 m
numer_factor = [] #numer의 모든 소인수(중복 있음)
lcm_factor = [] #lcm의 모든 소인수(중복 있음)

#numer(분산의 분자) 소인수분해
i = 2
while numer != 1:
    if numer % i == 0:
        numer /= i
        numer_factor.append(i)
        num_fac_size += 1
    else:
        i += 1
        
#lcm(분산의 분모) 소인수분해
i = 2
while lcm != 1:
    if lcm % i == 0:
        lcm /= i
        lcm_factor.append(i)
        lcm_fac_size += 1
    else:
        i += 1

#√(numer) --> n√(m)에서 m, n 구하기
i = 0
while i < num_fac_size-1:
    if numer_factor[i] == numer_factor[i+1]:
        root_numer_int *= numer_factor[i]
        del numer_factor[i]
        del numer_factor[i]
        num_fac_size -= 2
    else:
        i += 1
for i in range(0, num_fac_size):
    root_numer_decimal *= numer_factor[i]

#√(lcm) --> n√(m)에서 m, n 구하기
i = 0
while i < lcm_fac_size-1:
    if lcm_factor[i] == lcm_factor[i+1]:
        root_lcm_int *= lcm_factor[i]
        del lcm_factor[i]
        del lcm_factor[i]
        lcm_fac_size -= 2
    else:
        i += 1

#분수 유리화
for i in range(0, lcm_fac_size):
    root_lcm_decimal *= lcm_factor[i]

#표준편차 출력
root_numer_decimal *= root_lcm_decimal
if root_numer_int == 1:
    print("σ(x) = √(%d)/%d" %(root_numer_decimal, root_lcm_int))
elif root_lcm_int == 1:
    print("σ(x) = %d√(%d)" %(root_numer_int, root_numer_decimal))
else:
    print("σ(x) = %d√(%d)/%d" %(root_numer_int, root_numer_decimal, root_lcm_int))