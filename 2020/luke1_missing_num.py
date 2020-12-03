import time

s=time.time()

nums = set(open("knowit2020\\1_numbers.txt").read().split(','))
missing = [i for i in range(1, 100000) if not str(i) in nums]
print(missing)

print (time.time()-s)