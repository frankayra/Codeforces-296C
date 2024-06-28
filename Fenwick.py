class BIT():
    def __init__(self, array):
        self.length = len(array)
        self.partial_sums = [0] * (self.length + 1)
        for i, value in enumerate(array):
            j = i - (i & -i)
            for k in range(j, i):
                self.partial_sums[i] += array[j]

        # for i in range(1, self.length + 1):
        #     self.Update(i, array[i-1]) # En caso que se quiera cambiar el elemento en lugar de sumarle algo, se pasa como parametro la diferencia de new_value - array[i]
        
    def Update(self, i, item):
        while i < (self.length + 1):
            self.partial_sums[i] += item
            i += i & -i
        
    def partial_sum_query(self, i):
        sum = 0
        i += 1
        if i >= self.length:
            return self.partial_sums[-1]
        while i > 0:
            sum += self.partial_sums[i]
            i -= i & -i
        return sum
    def RangeQuery(self, l, r):
        return self.partial_sum_query(r) - self.partial_sum_query(l-1)


def main():
    array = [1] * 8
    operations = [(1, 2, 3), (3, 4, 5), (2, 7, 3), (3, 3, 3), (3, 7, 7), (0, 5, 4)]
    queries = [(1, 4), (3, 5), (0, 2), (4, 5), (3, 5), (0, 5)]


