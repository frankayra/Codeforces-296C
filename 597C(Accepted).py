
######################################################################    

class BIT():
    def __init__(self, length):
        self.length = length + 1
        self.partial_sums = [0] * self.length

    def Update(self, i, item):
        while i < self.length:
            self.partial_sums[i] += item
            i += i & -i

    def partial_sum_query(self, i):
        sum = 0
        while i > 0:
            sum += self.partial_sums[i]
            i -= i & -i
        return sum

    def RangeQuery(self, l, r):
        return self.partial_sum_query(r) - self.partial_sum_query(l - 1)


def main():
    import sys
    input = sys.stdin.buffer.readline

    firstline = input().strip().split()
    n = int(firstline[0])
    k = int(firstline[1])
    
    Fenwick_Forest = []
    for _ in range(k + 1):
        Fenwick_Forest.append(BIT(n))
    # A = []
    # for _ in range(n):
    #     val = int(input().strip())
    #     A.append(val)
    
    for i in range(n):
        val = int(input().strip())
        Fenwick_Forest[0].Update(val, 1)
        for j in range(1, len(Fenwick_Forest)):
            subsequences_ending_with_lte_count = Fenwick_Forest[j - 1].partial_sum_query(val - 1)
            Fenwick_Forest[j].Update(val, subsequences_ending_with_lte_count)
    
    print(Fenwick_Forest[k].partial_sum_query(n))
    # print(f"Solution: {Fenwick_Forest[k].partial_sum_query(n)}")
    # for ft in Fenwick_Forest:
    #     for i in range(n):
    #         print(ft.partial_sum_query(i), end="| ")
    #     print("---")

    # Hacer Update en el Ft j, en la posicion VAL con la cantidad de subsecuencias acumuladas 
    # de tamaño j-1 que terminan en un numero menor que VAL
    # 
    # Que esto se traduce a FF[j].Update(pos=VAL, FF[j-1].PartialSums(VAL-1))



if __name__ == "__main__":
    main()
