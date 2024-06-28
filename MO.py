import math

def mos_algorithm(arr, queries):
    n = len(arr)
    q = len(queries)
    block_size = int(math.sqrt(n))
    answers = [0] * q
    current_answer = 0
    freq = [0] * (max(arr) + 1)
    
    # Sorting queries
    queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))
    
    current_l, current_r = 0, 0
    
    for i in range(q):
        L, R, idx = queries[i]
        
        while current_r <= R:
            freq[arr[current_r]] += 1
            if freq[arr[current_r]] == 1:
                current_answer += 1
            current_r += 1
        
        while current_r > R + 1:
            current_r -= 1
            freq[arr[current_r]] -= 1
            if freq[arr[current_r]] == 0:
                current_answer -= 1
        
        while current_l < L:
            freq[arr[current_l]] -= 1
            if freq[arr[current_l]] == 0:
                current_answer -= 1
            current_l += 1
        
        while current_l > L:
            current_l -= 1
            freq[arr[current_l]] += 1
            if freq[arr[current_l]] == 1:
                current_answer += 1
        
        answers[idx] = current_answer
    
    return answers

# Ejemplo de uso
arr = [1, 2, 1]
queries = [(0, 1, 0), (0, 2, 1)]
print(mos_algorithm(arr, queries))
