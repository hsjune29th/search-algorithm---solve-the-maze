
class Node:
    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0 
        self.f = 0
   
    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
         return self.f < other.f
    
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


def best_first_search(map, start, end):

    open = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    open.append(start_node)
    s=0
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
           
            return path[::-1]
      
        (x, y) = current_node.position
        
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for next in neighbors:
            map_value = map.get(next)
            if(map_value == 'X'):
                continue
            neighbor = Node(next, current_node)
            if(neighbor in closed):
                continue
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.h
            s=s+1;
            if neighbor.f==0:
             print("Số ô đã duyệt: ", s)
            if(add_to_open(open, neighbor) == True):
                open.append(neighbor)
   
    return None
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
def main():
    print("Tìm kiếm G-BFS,Nhập map (nhập từ 1-5):")
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
              end= (j,i)
             
        if maze[i][j]=="S":
            start=(j,i)
        map[j,i]=maze[i][j]
    print("Best First Search (đã xuất kết quả trong ouput.txt): ")
    path = best_first_search(map, start, end)
    for i in range(1,len(path)):
      
      if path[i-1][0]-1== path[i][0]:
        maze[path[i-1][1]][path[i-1][0]]  ="<"
      if path[i-1][0]+1== path[i][0]:
         maze[path[i-1][1]][path[i-1][0]]  =">"
      if path[i-1][1]-1== path[i][1]:
        maze[path[i-1][1]][path[i-1][0]]  ="^"
      if path[i-1][1]+1== path[i][1]:
        maze[path[i-1][1]][path[i-1][0]]  ="v"
    for i in range(1,len(path)):
      
      if maze[path[i-1][1]][path[i-1][0]]==maze[path[i][1]][path[i][0]]:
        if maze[path[i][1]][path[i][0]]  =="<" or maze[path[i][1]][path[i][0]]  ==">":
         maze[path[i-1][1]][path[i-1][0]]  ="-"
        if maze[path[i][1]][path[i][0]]  =="v" or maze[path[i][1]][path[i][0]]  =="^":
         maze[path[i-1][1]][path[i-1][0]]  ="|"
    
    print('Số ô đã đi để thoát khỏi mê cung : {0}'.format(len(path)))

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end=" ")
        print("")
           
             
       
              


if __name__ == '__main__':
    while 1:
      map={}
      main()
      
