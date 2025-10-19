class HeapTree:
    def __init__(self, is_min = True):
        '''
        is_min: Here we can define the type of the heapTree, 
        where is_min == True mean it's Minmum Heap Tree
        '''
        self.is_min = is_min
        self.array = [] #Our Priority Tree
        self.size = 0
        pass

    # def pop(self):
    #     if self.size > 0:
    #         self.size -= 1
    #         return self.array[-1]
    #     else:
    #         raise Exception("Empty Priority Queue")

    @staticmethod
    def swap(array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]

    #Here i'm applying the heapify, where we're trying to correctly construct the PQ
    def heapify(self, index):
        if index == 0 :
            return
        parent_index = self.parent(index)
        
        
        # Base Case for min heap:
        if self.array[index] > self.array[parent_index] and self.is_min:
            return
        
        # Base Case for max heap:
        if self.array[index] < self.array[parent_index] and not self.is_min:
            return
        
        HeapTree.swap(self.array, parent_index, index)
        self.heapify(parent_index)

            
    def push(self, value):
        self.array.append(value)
        self.size += 1

        if self.size > 1:
            self.heapify(self.size - 1)

    # As we're dealing with COMPLETE TREE let's get benfits from some of its features
    def left(self, index):
        if self.size > 0:
            left_index = 2 * index + 1
            
            if left_index < self.size:
                return left_index
            else:
                return None
            
        else:
            raise Exception("Empty Priority Queue")

    def right(self, index):
        if self.size > 0:
            right_index = 2 * index + 2
            
            if right_index < self.size:
                return right_index
            else:
                return None
            
        else:
            raise Exception("Empty Priority Queue")

    def parent(self, index):
        if self.size > 0 and index < self.size: # Ensuring that the node exist
            if index % 2 == 0:
                return (index - 2) // 2
            
            return (index - 1) // 2
        else:
            raise Exception("Empty Priority Queue")
    

    def heap_down(self, idx_value):
        # Useing index of the value we can put it in it's correct location
        left_idx, right_idx = self.left(idx_value), self.right(idx_value)
        smallest = idx_value
        if left_idx:
            # Check if left child exists and is smaller
            if left_idx < len(self.array) and self.array[left_idx] < self.array[smallest]:
                smallest = left_idx

        if right_idx:
            # Check if right child exists and is smaller
            if right_idx < len(self.array) and self.array[right_idx] < self.array[smallest]:
                smallest = right_idx
            
        if smallest != idx_value:
            HeapTree.swap(self.array, smallest, idx_value)
            self.heap_down(smallest)

    def pop_root(self):
        # First replace root with last value, then remove it
        if self.array:
            root = self.array[0]
            self.array[0] = self.array[-1] # Replacment
            del self.array[-1]
            if self.array:
                self.heap_down(0) # repair the heap
            return root



    def __str__(self):
        return str(self.array)


    #Leet Code 703:  Kth Smallest Number:
    def kth_smallest_number(self, stream_numbers, kth):
        # The idea here that we can
        maximum = float('-inf')
        for number in stream_numbers:
            if number > maximum:
                maximum = number

prioirty_queue = HeapTree()
prioirty_queue.push(5)
prioirty_queue.push(3)
prioirty_queue.push(12)
prioirty_queue.push(2)
print(prioirty_queue)