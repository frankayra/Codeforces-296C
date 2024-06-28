import math
import sys
# import os

def MO(array, queries):
    n = len(array)
    q = len(queries)
    L, R = 0, -1
    sqrt_size = int(math.sqrt(n))

    queries.sort(key=lambda x: (x[0] // sqrt_size, -x[1] if (x[0] // sqrt_size) % 2 == 0 else x[1]))
    frequencies = [0]*(max(array) + 1)
    answers = [0]*len(queries)
    last_q = -1
    for (Li, Ri, i) in queries:
        Li -= 1
        Ri -= 1
        if last_q != -1:
            answers[i] += answers[last_q]
        last_q = i

        while L > Li:
            L-=1
            s=array[L]
            answers[i]+=s*(2*frequencies[s]+1)
            frequencies[s]+=1
        while R > Ri:
            s=array[R]
            answers[i]-=s*(2*frequencies[s]-1)
            frequencies[s]-=1
            R-=1
        while R < Ri:
            R+=1
            s=array[R]
            answers[i]+=s*(2*frequencies[s]+1)
            frequencies[s]+=1
        while L < Li:
            s=array[L]
            answers[i]-=s*(2*frequencies[s]-1)
            frequencies[s]-=1
            L+=1
    for q in answers:
        print(q)

def main():
    input = sys.stdin.buffer.readline

    firstline = input().strip().split()
    secondline = input().strip().split()
    n = int(firstline[0])
    t = int(firstline[1])
    array = [int(item) for item in secondline]

    queries = []
    for i in range(t):
        line = input().strip().split()
        queries.append((int(line[0]), int(line[1]), i))

    MO(array, queries)
    

if __name__ == "__main__":
    main()