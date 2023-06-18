def mySqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


num = int(input("Enter a number  "))
print(mySqrt(num))  