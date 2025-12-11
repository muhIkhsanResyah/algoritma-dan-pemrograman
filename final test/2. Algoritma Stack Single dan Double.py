# IMPLEMENTASI STACK SINGLE
class StackSingle:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

# IMPLEMENTASI DOUBLE STACK DALAM SATU ARRAY
class DoubleStack:
    def __init__(self, size):
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, value):
        if self.top1 + 1 == self.top2:
            print("Stack 1 penuh!")
            return
        self.top1 += 1
        self.array[self.top1] = value

    def push2(self, value):
        if self.top2 - 1 == self.top1:
            print("Stack 2 penuh!")
            return
        self.top2 -= 1
        self.array[self.top2] = value

    def pop1(self):
        if self.top1 == -1:
            return None
        value = self.array[self.top1]
        self.top1 -= 1
        return value

    def pop2(self):
        if self.top2 == len(self.array):
            return None
        value = self.array[self.top2]
        self.top2 += 1
        return value


# Contoh penggunaan
s = StackSingle()
s.push(10)
s.push(20)
print("Pop Single Stack:", s.pop())

d = DoubleStack(10)
d.push1(1)
d.push2(100)
print("Pop Stack1:", d.pop1())
print("Pop Stack2:", d.pop2())

