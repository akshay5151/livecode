# 2)-Print downward Half-Pyramid Pattern with Star (asterisk)
def pyramid(row):
    for i in range(row,0,-1):
        for j in range(0,i):
            print('*',end = " ")
        print('')

pyramid(8)