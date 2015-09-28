class Queue(object):

    def __init__(self):
        self.l = []

    def is_empty(self):
        return self.l == []

    def add(self, obj):
        self.l.insert(0, obj)

    def remove(self):
        self.l.pop()

    def size(self):
        return len(self.l)

qu = Queue()

qu.size()
qu.add('Gogu')
qu.add(6)
qu.add(90)
qu.is_empty()
qu.size()
qu.remove()
qu.size()
