
from collections import deque



class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost


def bfs(Grid, dest: Grid_Position, start: Grid_Position):
    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]
    m,n = (len(Grid[0]), len(Grid))
    visited_blocks = [[False for i in range(m)]
                for j in range(n)]
    visited_blocks[start.x][start.y] = True
    queue = deque()
    sol = Node(start, 0)
    queue.append(sol)
    cells = 4
    cost = 0
    while queue:
        current_block = queue.popleft()  

        current_pos = current_block.pos

        
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Tìm kiếm BFS (đã xuất kết quả trong ouput.txt)")
            print("Số ô đã duyệt = ", cost)

            return current_block.cost
        
        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1

        
        x_pos = current_pos.x
        y_pos = current_pos.y
        for i in range(cells):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos < n and y_pos < m and x_pos >= 0 and y_pos >= 0:
               
                if Grid[x_pos][y_pos] == ' ' or Grid[x_pos][y_pos]== "E":
                    Array.append(Grid_Position(current_pos.x,current_pos.y)) 

                    if not visited_blocks[x_pos][y_pos]:
                        next_cell = Node(Grid_Position(x_pos, y_pos),
                                       current_block.cost + 1)
                        
                        visited_blocks[x_pos][y_pos] = True
                        queue.append(next_cell)
                        

    return -1

def create_node(x, y, c):
    val = Grid_Position(x, y)
    return Node(val, c + 1)


def main():
    ArrayBFS=[]; countbfs=-1
    print("Tìm kiếm BFS, Nhập map (nhập từ 1-5):")
    x="map"+ input()+ ".txt"
    with open(x) as f:
     f1=f.readline()
     m=len(f1)-1
     
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
              ArrayBFS.append(Grid_Position(i, j)) 
             
        if maze[i][j]=="S":
            starting_position = Grid_Position(i, j)

    res = bfs(maze, destination, starting_position)
    if res != -1:
        print("Số ô đã đi để thoát khỏi mê cung : ", res)
    else:
        print("Không có lời giải, vui lòng kiểm tra lại mê cung!")

    arrayX=[0,0,1,-1]
    arrayY=[1,-1,0,0]
    countbfs=0
    for i in range(2,len(Array)): 
      check=0
      for j in range(4):
        if (Array[len(Array)-i].x + arrayX[j]== ArrayBFS[countbfs].x) and (Array[len(Array)-i].y+arrayY[j]== ArrayBFS[countbfs].y):
            check=1


      if check==1:
         ArrayBFS.append(Grid_Position(Array[len(Array)-i].x, Array[len(Array)-i].y))
         countbfs=countbfs+1 

    for i in range(1,len(ArrayBFS)-1):
      if ArrayBFS[i-1].x-1==ArrayBFS[i].x :
         if maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="v" or maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="|":
             maze[ArrayBFS[i].x][ArrayBFS[i].y]= "|"
         else:
              maze[ArrayBFS[i].x][ArrayBFS[i].y]= "v"
      if ArrayBFS[i-1].x+1==ArrayBFS[i].x :
         if maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="^" or maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="|":
             maze[ArrayBFS[i].x][ArrayBFS[i].y]= "|"
         else:
              maze[ArrayBFS[i].x][ArrayBFS[i].y]= "^"
      if ArrayBFS[i-1].y-1==ArrayBFS[i].y :
         if maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]==">" or maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="-":
             maze[ArrayBFS[i].x][ArrayBFS[i].y]= "-"
         else:
              maze[ArrayBFS[i].x][ArrayBFS[i].y]= ">"
      if ArrayBFS[i-1].y+1==ArrayBFS[i].y :
         if maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="<" or maze[ArrayBFS[i-1].x][ArrayBFS[i-1].y]=="-":
             maze[ArrayBFS[i].x][ArrayBFS[i].y]= "-"
         else:
              maze[ArrayBFS[i].x][ArrayBFS[i].y]= "<"
    for i in range(0,len(maze)):
      for j in range(0,len(maze[0])):
          print(maze[i][j], end=" ")
      
      print("")
    f = open('output.txt', 'w')
    for i in range(len(maze)):
        for j in range(len(maze[0])):
           f.write(maze[i][j])   
        f.write("\n")   
    f.close()   
if __name__ == '__main__':
    while 1:
     Array=[]
     main()


