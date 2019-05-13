def reverseInt(num):
    rev = 0
    rem = 0

    while num > 0:
        rem = num%10
        num //= 10
        rev = rev * 10 + rem
    return rev
