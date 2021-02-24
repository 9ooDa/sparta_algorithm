class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        print(self.items)
        current_index = len(self.items) - 1

        while current_index > 1:
            parent_index = current_index // 2
            if self.items[parent_index] < self.items[current_index]:
                self.items[current_index], self.items[parent_index] = self.items[parent_index], self.items[current_index]
                current_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!