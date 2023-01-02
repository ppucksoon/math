point_1 = [0, 0]
point_2 = [0, 0]

print("--------두 점 사이의 거리 계산 프로그램--------")
point_1[0], point_1[1] = map(int, input("첫 번째 점의 좌표 : ").split(", "))
point_2[0], point_2[1] = map(int, input("두 번째 점의 좌표 : ").split(", "))

minus_x = point_1[0] - point_2[0]
minus_y = point_1[1] - point_2[0]

square_minus_x = minus_x ** 2
square_minus_y = minus_y ** 2

sum_square = square_minus_x + square_minus_y
distance = sum_square ** 0.5

print("")
print("두 점 (%d, %d), (%d, %d) 사이의 거리 : %f" %(point_1[0], point_1[1], point_2[0], point_2[1], distance))