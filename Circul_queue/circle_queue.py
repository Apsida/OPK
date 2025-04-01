class circ_queue():
    def __init__(self, size: int):
        self.max_size = size
        self.queue_array = [0] * size
        self.front = -1
        self.tail = -1

    def is_empty(self):
        return self.front == -1 and self.tail == -1

    def head(self):
        if not self.is_empty():
            return self.queue_array[self.front]
        else:
            return -1

    def ent_queue(self, item: int):
        if self.front == self.max_size - 1:
            return -1
        if self.is_empty():
            self.front = 0
            self.tail = 0
            self.queue_array[self.tail] = item
        else:
            self.tail = (self.tail+1) % self.max_size
            if self.tail == self.front:
                self.tail = (self.tail - 1 + self.max_size) % self.max_size
            else:
                self.queue_array[self.tail] = item
        return 0

    def del_queue(self):
        item = -1
        if not self.is_empty():
            item = self.queue_array[self.front]
            if self.front == self.tail:
                self.front = -1
                self.tail = -1
            else:
                self.front = (self.front + 1) % self.max_size

        return item


if __name__ == "__main__":
    qu = circ_queue(0)
    print(qu.head())

