class Node(object):
    """
    定義單向鏈表節點
    """
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack(object):
    """
    用鏈表實作堆疊，支持 push, pop, peek, is_empty, size
    """
    def __init__(self):
        self.top = None  # 指向堆疊頂端節點
        self.count = 0   # 堆疊大小

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def push(self, item):
        node = Node(item)
        node.next = self.top  # 新節點指向原頂端
        self.top = node       # 頂端更新為新節點
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法pop")
        item = self.top.item
        self.top = self.top.next  # 頂端往下一個節點移動
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法peek")
        return self.top.item

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("堆疊大小:", stack.size())  # 3
    print("堆疊頂端:", stack.peek())  # 3
    print("pop:", stack.pop())        # 3
    print("pop:", stack.pop())        # 2
    print("堆疊頂端:", stack.peek())  # 1
    print("堆疊大小:", stack.size())  # 1
         

