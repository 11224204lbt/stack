class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法pop")
        item = self.top.item
        self.top = self.top.next
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("堆疊為空，無法peek")
        return self.top.item

def infix_to_postfix(infix_expr):
    prepare = {'*':3, '/':3, '+':2, '-':2, '(':1}

    postfix_list = []
    infix_list = infix_expr.split()
    op_stack = Stack()

    for item in infix_list:
        if item in "0123456789" or item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfix_list.append(item)
        elif item == '(':
            op_stack.push(item)
        elif item == ')':
            top = op_stack.pop()
            while top != '(':
                postfix_list.append(top)
                top = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prepare[op_stack.peek()] >= prepare[item]):
                postfix_list.append(op_stack.pop())
            op_stack.push(item)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

if __name__ == '__main__':
    print(infix_to_postfix("A * B + C * D"))     # 輸出: A B * C D * +
    print(infix_to_postfix("( A + B ) * C"))     # 輸出: A B + C *
