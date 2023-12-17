def is_palindrome(a: str) -> str:
    for i in range(len(a) // 2):
        x = len(a) - i - 1
        if a[i] != a[x]:
            return "no"
    return "yes"


while True:
    a = int(input())
    if a == 0:
        break
    print(is_palindrome(str(a)))
