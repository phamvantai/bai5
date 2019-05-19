## File: mymath.py ##
def square(n):
    return n*n

def cube(n):
    return n*n*n

def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return fload(sum)/nvals


## My script using the math module ##
import mymath #Note no .py

values = [2 ,4,6,8,10]
print('squares:')
for v in values:
    print(mymath.square(v))
print ('Cube:')
for v in values:
    print(mymath.cube(v))
print('Average:'+str(mymath.average(values)))