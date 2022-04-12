class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

class MazeTree:
    def __init__(self,information):
        self.coords = information
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.children = []
    def get_children(self):
        return self.children
    def get_coords(self):
        return self.coords
    def build_children(self,child):
        self.children.append(child)
    


def main():
    filename = input()
    try:
        fileopen = open(filename,'r')
    except FileNotFoundError:
        print("Error")
    command = input()
    maze_list = []
    for line in fileopen:
        maze_line = []
        line = line.strip('\n')
        end = 0
        start = 0
        for character in line:
            assert character in ('S',"E","#",' ','\n')
            if character == "S":
                start += 1
            elif character == "E":
                end += 1
            assert start < 2
            assert end < 2
            maze_line.append(character)
        maze_list.append(maze_line)
    maze_coords = create_coord_list(maze_list)
    start_coords = find_start(maze_list)
    end_coords = find_end(maze_list)
    built_array = []
    start_node = MazeTree(start_coords)
    built_array.append(start_node.coords)
    start_of_path = ListNode(start_node)
    create_maze_tree(maze_coords,start_node,built_array)
    find_path(start_of_path,end_coords)
    iterate(start_of_path)
    if command == "dumpCells":
        dump_cells(maze_list)
    if command == 'dumpTree':
        print('DUMPING OUT THE TREE THAT REPRESENTS THE MAZE:')
        dump_tree(start_node)
    
def find_path(start_of_path,end_coords):
    for child in start_of_path.val.children:
        if child is not None:
            if child.coords == end_coords:
                start_of_path.next = ListNode(child)
                return start_of_path
            else:
                start_of_path.next = ListNode(child)
                find_path(start_of_path.next,end_coords)
            

def iterate(start_of_path):
    if start_of_path is None:
        return None
    cur = start_of_path
    while cur is not None:
        print(cur.val.coords)
        cur = cur.next


    
                
def dump_tree(start_node,indent='  '):
    print(f'{indent}{start_node.coords}')
    for child in start_node.children:
        dump_tree(child , indent+'| ')


def dump_cells(maze_list):
    list_of_cells = []
    y = 0
    print(f'DUMPING OUT ALL CELLS FROM THE MAZE:')
    for maze_part in maze_list:
        x = 0
        for value in maze_part:
            list_of_cells.append((x,y,value))
            x += 1
        y += 1
    for value in sorted(list_of_cells):
        x = value[0]
        y = value[1]
        if value[2] == 'S':
            print(f'  ({x},{y})    START')
        elif value[2] == 'E':
            print(f'  ({x},{y})    END')
        elif value[2] == '#':
            print(f'  ({x},{y})')

def find_start(maze_list):
    list_of_cells = []
    y = 0
    for maze_part in maze_list:
        x = 0
        for value in maze_part:
            list_of_cells.append((x,y,value))
            x += 1
        y += 1
    for value in sorted(list_of_cells):
        x = value[0]
        y = value[1]
        if value[2] == 'S':
            return x,y

def find_end(maze_list):
    list_of_cells = []
    y = 0
    for maze_part in maze_list:
        x = 0
        for value in maze_part:
            list_of_cells.append((x,y,value))
            x += 1
        y += 1
    for value in sorted(list_of_cells):
        x = value[0]
        y = value[1]
        if value[2] == 'E':
            return x,y

def create_coord_list(maze_list):
    maze_coords = []
    y = 0
    for maze_part in maze_list:
        x = 0
        for value in maze_part:
            if value == '#' or value == "S" or value == 'E':
                maze_coords.append((x,y))
            x += 1
        y += 1
    return maze_coords

def create_maze_tree(maze_coords,node,built_array):
    x = node.x
    y = node.y
    up_coords = (x,y-1)
    if up_coords in maze_coords and up_coords not in built_array:
        new_node = MazeTree(up_coords)
        node.build_children(new_node)
        built_array.append(up_coords)
        create_maze_tree(maze_coords,new_node,built_array)
    down_coords = (x,y+1)
    if down_coords in maze_coords and down_coords not in built_array:
        new_node = MazeTree(down_coords)
        node.build_children(new_node)
        built_array.append(down_coords)
        create_maze_tree(maze_coords,new_node,built_array)
    left_coords = (x-1,y)
    if left_coords in maze_coords and left_coords not in built_array:
        new_node = MazeTree(left_coords)
        node.build_children(new_node)
        built_array.append(left_coords)
        create_maze_tree(maze_coords,new_node,built_array)
    right_coords = (x+1,y)
    if right_coords in maze_coords and right_coords not in built_array:
        new_node = MazeTree(right_coords)
        node.build_children(new_node)
        built_array.append(right_coords)
        create_maze_tree(maze_coords,new_node,built_array)






main()

