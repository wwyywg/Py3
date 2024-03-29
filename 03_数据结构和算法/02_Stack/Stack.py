"""
Stack()创建一个新的空栈
push(item)添加一个新的元素
pop()弹出栈顶元素
peek()返回栈顶元素
is_empty()判断栈是否为空
size()返回栈的元素个数
"""

class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """"返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())

















