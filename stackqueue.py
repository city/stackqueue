ass Stack: #FIFO

    a = []
    def __init__(self, data):
        self.a.append(data)

    def push(self, data):
        self.a.insert(0,data)

    def print(self):
        for e in self.a:
            print(e)

    def pop(self):
        return self.a.pop(len(self.a)-1)

#s = Stack(20)
##s.push(40)
#s.push(5)
##s.print()
#print("pop: "+str(s.pop()))
#s.print()
#print("----------")

class Queue: #LIFO

    a = []
    def __init__(self, data):
        self.a.insert(0,data)

    def print(self):
        for e in self.a:
            print(e)

    def enqueue(self, data):
        self.a.insert(0, data)

    def dequeue(self):
        return self.a.pop()

q = Queue(10)
#q.enqueue(330)
#q.enqueue(9)
#q.print()
#print("dequeue: "+str(q.dequeue()))
#q.print()
#print("-----------")
q.enqueue(12)
q.enqueue(13)
q.enqueue(16)
q.enqueue(23)
q.enqueue(28)
q.print()


