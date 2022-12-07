x = [input() for i in range(int(input()))]
y = [i for i in x if len(i) <= 3]

print(f"{x} -> {y}")