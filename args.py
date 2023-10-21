#*args

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(2,4,1,34,4,5,4534,43,353))
