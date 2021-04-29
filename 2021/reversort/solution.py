import math

def reversort_cost(N, L):
    cost = 0
    for i in range(N):
        min_val = math.inf
        min_val_idx = 0
        for j in range(i, N):
            if L[j] < min_val:
                min_val = L[j]
                min_val_idx = j
        cost += min_val_idx - i + 1

    return cost
            

T = int(input())
for t in range(1, T+1):
    N = input()    
    L = list(map(int, input().split()))    

    cost = reversesort_cost(N, L)
    print('Case #{}: {}'.format(t, cost))