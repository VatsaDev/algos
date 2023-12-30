import timeit

test_arr = []
target = 9999999

for i in range(10000000):
    test_arr.append(i)

# linear search, o(n) time
# 807 ns ± 259 ns

def linear(ar, tar):
    for i in range(len(ar)):
        if ar[i] == tar:
            print(i)
            break
        else: 
            continue

# binary search o(log n) time, needs sorted array
# 1.56 µs ± 383 ns for my code, 1.36 µs ± 362 ns default       

def bs(ar, tar):
    med = int(len(ar)/2)

    while True:
        if tar==0 or tar==len(ar):
          #print(tar)
          break
        if med == tar:
          #print(med)
          break
        if med==0 or med==(len(ar)-1):
          #print('none')
          break
        if med > tar:
          #print(med)
          med = int(med/2)
        if med < tar:
          #print(med)
          med = med + int((len(ar)-med)/2)

