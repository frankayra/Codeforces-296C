class Node():
    def __init__(self, value, index):
        self.prev = None
        self.next = None
        self.value = value
        self.index = index
class MonotonicQueue():
    def __init__(self, length):
        self.First = None
        self.Last = None
        self.max_length = length
        self.count = 0

        #### extra ####
        self.intervals = 0
        ###############

    def __str__(self):
        result = ""
        current_node = self.First
        result += current_node.value + "<-->"
        while(current_node.next):
            current_node = current_node.next
            result += current_node.value + "<-->"
    def append(self, item, index):
        if self.count == 0:
            self.First = self.Last = Node(item, index)
            self.count += 1
            return
        if index - self.First.index > self.max_length and self.First.next:
            self.First = self.First.next
            self.count -= 1
        current_node = self.Last
        while current_node.value > item:
            if not current_node.prev:
                self.First = self.Last = Node(item, index)
                # print(f"max en [{max(self.Last.index - self.max_length, 0)}, {self.Last.index}]: {self.First.value}   First index: {self.First.index}")
                return
            current_node = current_node.prev
            self.count -= 1
        newNode = Node(item, index)
        newNode.prev = current_node
        current_node.next = newNode
        self.Last = newNode
        self.count += 1
        # print(f"max en [{max(self.Last.index - self.max_length, 0)}, {self.Last.index}]: {self.First.value}   First index: {self.First.index}")



