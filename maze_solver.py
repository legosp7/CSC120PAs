def main():
    filename = input()
    fileopen = open(filename,'r')
    command = input()
    maze_list = []
    maze_coords = []
    y = 0
    for line in fileopen:
        x = 0
        maze_line = []
        line = line.strip('\n')
        for character in line:
            maze_line.append(character)
            maze_coords.append(((x,y),character))
            x += 1
        y += 1
        maze_list.append(line)
    print(maze_coords)
main()