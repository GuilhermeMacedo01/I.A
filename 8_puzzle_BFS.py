#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from collections import deque
import copy
class Tabuleiro():

  def __init__(self,state, movement, depth, parent=None):
    self.goal = [[0,1,2],[3,4,5],[6,7,8]]
    self.state = state
    self.parent = parent
    self.pos_x = 0
    self.pos_y = 0
    self.movement = movement
    self.depth = depth

    if parent != None:
      self.path_to_goal = parent.path_to_goal
      self.path_to_goal.append(movement)
    else:
      self.path_to_goal = []
      self.path_to_goal.append(movement)
   
    self.index(state)
 

  def print_matrix(self,matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()
    print("\n")

  def verificar(self):
    verifica = 0
    for i in range(len(self.goal)):
      for j in range(len(self.goal[0])):
        if(self.goal[i][j]!=self.state[i][j]):
          return False
      
    return True

  def swap(self,state, atual_x, atual_y, novo_x, novo_y):
    new_state = copy.deepcopy(state)
    temp = new_state[atual_x][atual_y]
    new_state[atual_x][atual_y]= new_state[novo_x][novo_y]
    new_state[novo_x][novo_y] = temp
    #print("original")
    #self.print_matrix(state)
    #print("nova")
    #self.print_matrix(new_state)
    return new_state
  
  def index(self, state):
      for i in range(len(state)):
        for j in range(len(state[0])):
          if(state[i][j]==0):
            self.pos_x = i
            self.pos_y = j

  def left(self,state):
    if(self.pos_y!=0 and self.movement != "Right"):
      self.index(state)
      return (self.swap(state,self.pos_x,self.pos_y,self.pos_x,self.pos_y-1))
    else:
      #print("movimento invalido")
      return None

  def right(self,state):
    if(self.pos_y!=2 and self.movement != "Left"):
      self.index(state)
      return (self.swap(state,self.pos_x,self.pos_y,self.pos_x,self.pos_y+1))
    else:
      #print("movimento invalido")
      return None

  def up(self,state):
    if(self.pos_x!=0 and self.movement != "Down"):
      self.index(state)
      return (self.swap(state,self.pos_x,self.pos_y,self.pos_x-1,self.pos_y))
    else:
      #print("movimento invalido")
      return None

  def down(self,state):
    if(self.pos_x!=2 and self.movement != "Up"):
      
      self.index(state)
      return (self.swap(state,self.pos_x,self.pos_y,self.pos_x+1,self.pos_y))
    else:
      #print("movimento invalido")
      return None

  def vizinhos(self):
    up_state = copy.deepcopy(self.state)
    down_state = copy.deepcopy(self.state)
    left_state = copy.deepcopy(self.state)
    right_state = copy.deepcopy(self.state)
    vizinhos = [(self.up(up_state),"Up"),(self.down(down_state),"Down"),(self.left(left_state),"Left"),(self.right(right_state),"Right")]

    return vizinhos


# In[2]:


from collections import deque

def BFS(estado_inicial):
  goal = [[0,1,2],[3,4,5],[6,7,8]]
  node = Tabuleiro(estado_inicial,None,0, None)
  memory_before = process.memory_info().rss

  if(testa(estado_inicial,goal)):
    return node
  borda = deque()
  borda.append(node)
  explored_nodes = set()
  matrizTuple = tuple(map(tuple,node.state))
  explored_nodes.add(matrizTuple)
  nodes_expanded = 1 
  fringe_size = 0
  max_fringe_size = 0

  while borda:
    node = borda.popleft()
    explored_nodes.add(tuple(map(tuple,node.state)))
  
    for vizinho in node.vizinhos():
        if vizinho[0]!=None:
          if tuple(map(tuple,vizinho[0])) not in explored_nodes:
          
    
            filho = Tabuleiro(vizinho[0],vizinho[1],node.depth+1,node)
            explored_nodes.add(tuple(map(tuple,vizinho[0])))
            
            if(filho.verificar()==True):
              memory_after = process.memory_info().rss

              memoria = memory_after - memory_before
              memoria = round(memoria / (1024 * 1024), 2)
              print_matriz(vizinho[0])
              print("path_to_goal:",filho.path_to_goal)
              print("cost_of_the_path: ",filho.depth)
              print("nodes_expanded: ",nodes_expanded)
              print("search_depth: ",filho.depth)
              print("max_search_depth: ",filho.depth)
              print("max_fringe_size: ",max_fringe_size/2)
              print("memory_usage: ",memoria)
              print("\n")
              return filho
            borda.append(filho)
            fringe_size = fringe_size + 1
            nodes_expanded = nodes_expanded + 1 
    if(fringe_size>max_fringe_size):
        max_fringe_size = fringe_size
 
          #print_matriz(vizinho[0])
          #print(filho.path_to_goal)
       

          #print(vizinho[1])



# In[3]:


def print_matriz(matrix):
  for row in matrix:
      for element in row:
          print(element, end="\t")
      print()
  print("\n")


# In[4]:


def testa(state,goal):
  verifica = 0
  for i in range(len(goal)):
    for j in range(len(goal[i])):
      if(goal[i][j]!=state[i][j]):
        return False
    
  return True


# In[6]:


import psutil
get_ipython().system('pip install psutil')
import psutil
process = psutil.Process()


# In[7]:


x = [[0,8,7],[6,5,4],[3,2,1]]
print_matriz(x)
node = BFS(x)

#print_matriz(node.state)
#print(node.path_to_goal)
#print(node.depth


# In[ ]:




