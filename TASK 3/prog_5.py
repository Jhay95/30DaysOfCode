## 5. Write a Python program to sum two given integers. However, if the sum is between 15 to 20 it will return 20

def sum_two(x,y):
    sum_ = x+y
    if sum_ >= 15 and sum_ <= 20:
        sum_ = 20
    return sum_