
from collections import deque

class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost


def create_node(x, y, c):
    val = Grid_Position(x, y)
    return Node(val, c + 1)

def dfs(Grid, dest: Grid_Position, start: Grid_Position):
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]
    m,n = (len(Grid[0]), len(Grid))
    visited_blocks = [[False for i in range(m)]
               for j in range(n)]
    visited_blocks[start.x][start.y] = True
    stack = deque()
    sol = Node(start, 0)
    stack.append(sol)
    neigh = 4
    neighbours = []
    cost = 0
    while stack:
        current_block = stack.pop()
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Tìm kiếm DFS (đã xuất kết quả trong ouput.txt)")
            print("Số ô đã duyệt: ", cost)
            return current_block.cost
        x_pos = current_pos.x
        y_pos = current_pos.y
     
        for i in range(neigh):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos != n and x_pos != -1 and y_pos != m and y_pos != -1:
                if Grid[x_pos][y_pos] == ' ' or Grid[x_pos][y_pos] == "E":
                    Array.append(Grid_Position(current_pos.x,current_pos.y)) 
                    if not visited_blocks[x_pos][y_pos]:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack.append(create_node(x_pos, y_pos, current_block.cost))
    return -1

def main():
    
    ArrayDFS=[]; countbfs=-1
    print("Tìm kiếm DFS, Nhập map (nhập từ 1-5):")
    x="map"+ input()+ ".txt"
    #f = open('map3.txt', 'r')
    with open(x) as f:
     f1=f.readline()
     m=len(f1)-1
    #f.close()
    with open(x) as f:
     str= f.read()
     n= int((len(str)+1)/(m+1))



    maze = [ [0]*m for i in range(n)]
    for i in range(n):
      for j in range(m):
        maze[i][j]= str[i*(m+1)+j]
        if i==0 or i==n-1 or j==0 or j==m-1:
           if maze[i][j]== " ":
              maze[i][j]="E"
              destination = Grid_Position(i, j)
              ArrayDFS.append(Grid_Position(i, j)) 
             
        if maze[i][j]=="S":
            starting_position = Grid_Position(i, j)
          
    res = dfs(maze, destination, starting_position)
    if res != -1:
        print("Số ô đã đi để thoát khỏi mê cung : ", res)
    else:
        print("Không có lời giải, vui lòng kiểm tra lại mê cung!")

    arrayX=[0,0,1,-1]
    arrayY=[1,-1,0,0]
    countbfs=0; #ArrayDFS.append(Grid_Position(4, 0)) 

    for i in range(2,len(Array)): 
      check=0
      for j in range(4):
        if (Array[len(Array)-i].x + arrayX[j]== ArrayDFS[countbfs].x) and (Array[len(Array)-i].y+arrayY[j]== ArrayDFS[countbfs].y):
            check=1


      if check==1:
         ArrayDFS.append(Grid_Position(Array[len(Array)-i].x, Array[len(Array)-i].y))
         countbfs=countbfs+1 

    for i in range(1,len(ArrayDFS)-1):
      if ArrayDFS[i-1].x-1==ArrayDFS[i].x :
         if maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="v" or maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="|":
             maze[ArrayDFS[i].x][ArrayDFS[i].y]= "|"
         else:
              maze[ArrayDFS[i].x][ArrayDFS[i].y]= "v"
      if ArrayDFS[i-1].x+1==ArrayDFS[i].x :
         if maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="^" or maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="|":
             maze[ArrayDFS[i].x][ArrayDFS[i].y]= "|"
         else:
              maze[ArrayDFS[i].x][ArrayDFS[i].y]= "^"
      if ArrayDFS[i-1].y-1==ArrayDFS[i].y :
         if maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]==">" or maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="-":
             maze[ArrayDFS[i].x][ArrayDFS[i].y]= "-"
         else:
              maze[ArrayDFS[i].x][ArrayDFS[i].y]= ">"
      if ArrayDFS[i-1].y+1==ArrayDFS[i].y :
         if maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="<" or maze[ArrayDFS[i-1].x][ArrayDFS[i-1].y]=="-":
             maze[ArrayDFS[i].x][ArrayDFS[i].y]= "-"
         else:
              maze[ArrayDFS[i].x][ArrayDFS[i].y]= "<"
    for i in range(len(maze)):
        for j in range(len(maze[0])):
           
           print(maze[i][j], end=" ")
        print("")
    
    f = open('output.txt', 'w')
    for i in range(len(maze)):
        for j in range(len(maze[0])):
           f.write(maze[i][j])   
        f.write("\n")   
    f.close()   
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
      Array=[]
      main()


