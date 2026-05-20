class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._count = 0

    def add(self, value):
        new_node = Node(value)
        new_node.next = self._top
        if self._top:
            self._top.prev = new_node
        self._top = new_node
        self._count += 1

    def remove(self):
        if self._top is None:
            raise RuntimeError("Стек пуст - нечего снимать")
        result = self._top.data
        self._top = self._top.next
        if self._top:
            self._top.prev = None
        self._count -= 1
        return result

    def look(self):
        return None if self._top is None else self._top.data

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._count

    def __str__(self):
        if self.is_empty():
            return "Стек: [пусто]"
        items = []
        current = self._top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Стек (вершина -> дно): " + " -> ".join(items)


class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._count = 0

    def push(self, value):
        new_node = Node(value)
        if self._rear is None:
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            new_node.prev = self._rear
            self._rear = new_node
        self._count += 1

    def pop(self):
        if self._front is None:
            raise RuntimeError("Очередь пуста - нечего забирать")
        result = self._front.data
        self._front = self._front.next
        if self._front:
            self._front.prev = None
        else:
            self._rear = None
        self._count -= 1
        return result

    def first(self):
        return None if self._front is None else self._front.data

    def is_empty(self):
        return self._front is None

    def size(self):
        return self._count

    def __str__(self):
        if self.is_empty():
            return "Очередь: [пусто]"
        items = []
        current = self._front
        while current:
            items.append(str(current.data))
            current = current.next
        return "Очередь (начало -> конец): " + " -> ".join(items)


class Deque:
    def __init__(self):
        self._left = None
        self._right = None
        self._count = 0

    def append_left(self, value):
        new_node = Node(value)
        if self._left is None:
            self._left = self._right = new_node
        else:
            new_node.next = self._left
            self._left.prev = new_node
            self._left = new_node
        self._count += 1

    def append_right(self, value):
        new_node = Node(value)
        if self._right is None:
            self._left = self._right = new_node
        else:
            new_node.prev = self._right
            self._right.next = new_node
            self._right = new_node
        self._count += 1

    def pop_left(self):
        if self._left is None:
            raise RuntimeError("Дек пуст - нечего забирать слева")
        result = self._left.data
        self._left = self._left.next
        if self._left:
            self._left.prev = None
        else:
            self._right = None
        self._count -= 1
        return result

    def pop_right(self):
        if self._right is None:
            raise RuntimeError("Дек пуст - нечего забирать справа")
        result = self._right.data
        self._right = self._right.prev
        if self._right:
            self._right.next = None
        else:
            self._left = None
        self._count -= 1
        return result

    def peek_left(self):
        return None if self._left is None else self._left.data

    def peek_right(self):
        return None if self._right is None else self._right.data

    def is_empty(self):
        return self._left is None

    def size(self):
        return self._count

    def __str__(self):
        if self.is_empty():
            return "Дек: [пусто]"
        items = []
        current = self._left
        while current:
            items.append(str(current.data))
            current = current.next
        return "Дек (слева -> справа): " + " <-> ".join(items)


if __name__ == "__main__":
    print("=" * 50)
    print("СТЕК (LIFO)")
    st = Stack()
    for v in [5, 15, 25, 35]:
        st.add(v)
    print(st)
    print(f"Верхушка: {st.look()}")
    print(f"Снимаем: {st.remove()}")
    print(st)
    print(f"Пустой? {st.is_empty()}")
    print(f"Размер: {st.size()}")

    print("\n" + "=" * 50)
    print("ОЧЕРЕДЬ (FIFO)")
    q = Queue()
    for v in [1, 2, 3, 4]:
        q.push(v)
    print(q)
    print(f"Первый в очереди: {q.first()}")
    print(f"Забираем: {q.pop()}")
    print(q)
    q.push(100)
    print(f"Добавили 100 -> {q}")
    print(f"Размер: {q.size()}")

    print("\n" + "=" * 50)
    print("ДЕК (двусторонняя очередь)")
    d = Deque()
    d.append_right(10)
    d.append_right(20)
    d.append_left(5)
    d.append_left(1)
    print(d)
    print(f"Забрали справа: {d.pop_right()}")
    print(f"Забрали слева: {d.pop_left()}")
    print(d)
    print(f"Левый край: {d.peek_left()}")
    print(f"Правый край: {d.peek_right()}")
    d.append_right(999)
    print(f"Добавили 999 справа -> {d}")
    print(f"Размер дека: {d.size()}")
