# 1)  Print characters from a string that are present at an even index number
name = "America"

for i in range(len(name)):
    if i == 0:
        continue
    if i % 2 == 0:
        print(name[i])



