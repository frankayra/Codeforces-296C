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
        # print(f"frecuencies-{i}: {frequencies}")
        # print(answers[i])
    for q in answers:
        print(q)


def main():
    # input = sys.stdin.buffer.readline

    # firstline = input().strip().split()
    # secondline = input().strip().split()
    # n = int(firstline[0])
    # t = int(firstline[1])
    # array = [int(item) for item in secondline]

    # queries = []
    # for i in range(t):
    #     line = input().strip().split()
    #     queries.append((int(line[0]), int(line[1]), i))


    #### Example 1 ####
    array = [i for i in range(100000)]
    queries = [ (1,     100000, 0),
                (1,     50000,  1),
                (50001, 100000, 2),
                (25001, 75000,  3),
                (1,     25000,  4)]

    #### Example 2 ####
    # array = [1, 2, 1]
    # queries = [ (1,     2, 0),
    #             (1,     3,  1)]

    #### Example 3 ####
    # array = [1, 1, 2, 2, 1, 3, 1, 1]
    # queries = [ (2,     7,      0),
    #             (1,     6,      1),
    #             (2,     7,      2)]



    # os.system('cls')
    # print("\033c", end="")
    # print(f"array: {array}")
    # print(f"queries: {queries}")
    
    print(MO_FuerzaBruta(array, queries))
    MO(array, queries)


def MO_FuerzaBruta(array, queries):
    response = [0] * len(queries)
    for Li, Ri, i in queries:                       #
        Li -= 1                                     #
        Ri -= 1                                     #
        frequencies = [0]*(max(array[Li:Ri+1]) + 1) #
        for j in array[Li:Ri+1]:                    #
            frequencies[j] += 1                     #
        # print(f"Intervalo: [{Li}, {Ri}] -------------")
        for f_i, f in enumerate(frequencies):
            # print(f"elemento: {f_i}  |  frec: {f}  |  suma: {f**2 *f_i}")
            # print(f"f**2: {f**2}")
            response[i]+= f**2 *f_i
    return response
    
if __name__ == "__main__":
    main()
