def total_add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(total_add(1,2,3,4,5,6))