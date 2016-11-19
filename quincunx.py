class Node():
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right
        
    def add_left(self, value):
        self.left = value
        
    def add_right(self, value):
        self.right = value
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def __str__(self):
        return self.name
        
def gen_tree(n):
    if n > 0:
        n-=1
        p = Node(n)
        p.add_left(gen_tree(n))
        p.add_right(gen_tree(n))
        return p
    else:
        return Node(n)
        
tree = gen_tree(2)

def display_tree(tree):
    print(tree.__str__())
    
    if tree.get_left() == None or tree.get_right() == None:
        return None
    else:
        display_tree(tree.get_left())
        display_tree(tree.get_right())

display_tree(tree)