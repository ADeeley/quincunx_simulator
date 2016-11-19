class Node():
    def __init__(self, name, box, left=None, right=None):
        self.name = name
        self.box = box
        self.left = left
        self.right = right

    def add_left(self, value):
        self.left = value
        
    def add_right(self, value):
        self.right = value
        
    def get_box(self):
        return self.box
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def choose_direction(self):
        pass
        
    def __str__(self):
        return self.name

box_num = 0        
def gen_tree(n, box_num):
    ''' Generates a tree of depth n 
        - number of nodes a the root will be n**2'''
    if n > 0:
        n-=1
        p = Node(n, box_num)
        p.add_left(gen_tree(n, box_num))
        box_num += 1
        p.add_right(gen_tree(n, box_num))
        return p
    else:
        return Node(n, box_num)
        
tree = gen_tree(2, box_num)

def display_tree(tree):
    if tree.__str__() == 0:
        print("box", tree.get_box())
    else:
        display_tree(tree.get_left())
        display_tree(tree.get_right())
display_tree(tree)