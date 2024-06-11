class BIT():
    def __init__(self, array):
        self.size = len(array)
        self.partial_sums = [0] * (self.size)
        # for i, value in enumerate(array):
        #     j = i - (i & -i)
        #     for k in range(j, i+1):
        #         self.partial_sums[i] += array[j]

        for i in range(0, self.size):
            self.Update(i, array[i]) # En caso que se quiera cambiar el elemento en lugar de sumarle algo, se pasa como parametro la diferencia de new_value - array[i]
        
    def Update(self, i, item):
        while i < self.size:
            self.partial_sums[i] += item
            i += i & -i
    def 
        