import random
import time

# Function to check whether the list is in sorted order or not
# VERIFICATION
def increasing(l):
    for i in range(0,len(l)-1):
        if(l[i+1]<l[i]):
            return False
    return True

# Defining a list of n size with random value ranging between 0 to 101
n = 8
lt = []
for i in range(n):
    lt.append(random.randint(1,100))

# Finding Time required by Deterministic sorting algorithm
start_time1 = time.time()
sorted_list = sorted(lt)
end_time1 = time.time()

# Finding Time required by Non-Deterministic sorting algorithm
start_time2 = time.time()
while True:
    nd_sorted_list = []
    lt_len = len(lt)
    visited = {}
    i = 0
    while(i < lt_len):
        index = random.randint(0,lt_len-1)
        if index not in visited.keys():
            visited[index] = 1
            nd_sorted_list.append(lt[index]) 
            i = i+1 
    if(increasing(nd_sorted_list)):
        break
end_time2 = time.time()

print(lt)
print(nd_sorted_list)


print("Non Deterministic Sort takes: "+str(end_time2-start_time2)+"\nWhile Deterministic Sort takes: "+str(end_time1-start_time1))