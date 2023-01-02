import matplotlib.pyplot as plt

def odd(num):
    if num%2 == 0:
        return False
    return True

progress = [[i] for i in range(1, 11)]

for i in progress:
    progress_num = i[0]

    while progress_num != 1:
        if odd(progress_num):
            progress_num *= 3
            progress_num += 1
            i.append(progress_num)
        else:
            progress_num /= 2
            i.append(progress_num)

for x in progress:
    plt.plot(x)

plt.title("collatz_conjecture")
plt.xlabel("progress")
plt.ylabel("num")
plt.show()