# Create a maxheap algo recommendation system
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None

        max_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._sift_down(0)
        return max_item

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
            largest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index

        if largest_index != index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self._sift_down(largest_index)

class MaxHeapTree:
    def __init__(self):
        self.heap = MaxHeap()

    def insert(self, item):
        self.heap.insert(item)

    def extract_max(self):
        return self.heap.extract_max()

    def insert_tree(self, tree):
        self._insert_tree(tree.root)

    def _insert_tree(self, node):
        if node is None:
            return

        self.insert(node)
        self._insert_tree(node.left)
        self._insert_tree(node.right)