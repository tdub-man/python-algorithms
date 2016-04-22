class Node():
    def __init__(self, value, connections = None):
        self.value = value
        self.connections = connections
    def addConnection(self, node):
        if self.connections is None:
            self.connections = [node]
        else:
            self.connections.append(node)
    def setConnection(self, index, value):
        self.connections[index] = value
    def clearConnection(self, index):
        self.connections[index] = None
    def removeConnection(self, index):
        self.connections.pop(index)

x = Node(1)
y = Node(2)
z = Node(3)
# Make a list cycle
x.addConnection(y)
y.addConnection(z)
z.addConnection(x)

t = x
for i in range(0,100):
    print(t.value)
    t = t.connections[0]
