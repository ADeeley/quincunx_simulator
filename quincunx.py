class Node():
    def __init__(self, name, box, parent_box_num, left=None, right=None):
        self.name = name
        self.box = box
        self.parent_box_num = parent_box_num
        self.left = left
        self.right = right

    def add_left(self, value):
        self.left = value
        
    def add_right(self, value):
        self.right = value
        
    def get_box(self):
        return self.box
    
    def get_parent_box(self):
        return self.parent_box_num
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def choose_direction(self):
        pass
        
    def __str__(self):
        return self.name

box_num = 0        
parent_box = 0

def gen_tree(n, box_num, parent_box):
    ''' Generates a tree of depth n 
        - number of nodes a the root will be n**2'''
    if n > 0:
        n-=1
        # create a node called p
        p = Node(n, box_num, parent_box)
        p.add_left(gen_tree(n, box_num, p.get_parent_box())) # left node   
        
        box_num = box_num + 1 + parent_box
        parent_box = p.get_box()
        p.add_right(gen_tree(n, box_num, parent_box)) # right node
        return p
    else:
        return Node("end", box_num, parent_box)
        
tree = gen_tree(3, box_num, parent_box)

def display_tree_boxes(tree):
    ''' Displays the boxes at the end branches of the tree. '''
    if tree.__str__() == "end":
        print("box", tree.get_box())
    else:
        display_tree_boxes(tree.get_left())
        display_tree_boxes(tree.get_right())
display_tree_boxes(tree)