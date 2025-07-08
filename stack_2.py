class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('pop from empty stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('pop from empty stack')

    def size(self):
        return len(self.items)


def is_balanced(brackets):
    stack = Stack()
    open_brackets = {'(', '[', '{'}
    close_brackets = {')': '(', ']': '[', '}': '{'}

    for a in brackets:
        if a in open_brackets:
            stack.push(a)
        elif a in close_brackets:
            if stack.is_empty() or stack.pop() != close_brackets[a]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    input_string = input("Введите строку со скобками: ")
    if is_balanced(input_string):
        print("Сбалансированно")
    else:
        print("Несбалансированно")


