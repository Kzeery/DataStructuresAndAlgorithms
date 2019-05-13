def isPalindrome(s):
    return all(s[x] == s[-1-x] for x in range(len(s)//2))

print(isPalindrome("123221"))