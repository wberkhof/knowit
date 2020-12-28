import math  
import time
  
# method to get sum of the divisors 
def sum_of_div(n) : 
    
    s = 0

    # Note that this loop runs till square root 
    i = 1
    square_root = math.sqrt(n)
    while i <= square_root: 
          
        if n % i == 0: 
            s += i
            s += n/i
        i += 1
        
    return (s)
 

def get_ab_num_with_sq_diff(n):
    res = 0
    for i in range(2, n):
        i2 = i * 2
        s = sum_of_div(i)
        if s > i2:
            sqr = math.sqrt(s - i2)
            if sqr == int(sqr):
                res += 1

    return(res)

def main():
    print(get_ab_num_with_sq_diff(1000000))

def get_divisors(num):
    divisors = set()
    square_root = math.sqrt(num)
    for i in range(1, math.ceil(square_root) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num//i)
    return divisors

s=time.time()
rikelige_square = 0
#for n in range(1, 1000000 + 1):
#    divisors_sum = sum(get_divisors(n))
#    n2 = n*2
#    if divisors_sum > n2:
#        divisor_n2_diff = divisors_sum - n2
#        if math.ceil(math.sqrt(divisor_n2_diff)) ** 2 == divisor_n2_diff:
#            rikelige_square += 1


main()
#print(rikelige_square)
print (time.time()-s)
