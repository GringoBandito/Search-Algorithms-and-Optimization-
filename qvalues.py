import numpy as np
import matplotlib.pyplot as plt

gamma = 0.9

def board_check(board):
    
    length, width = np.shape(board)
    columns = np.sum(board, axis = 0)
    rows = np.sum(board, axis = 1)
    
    if 3 in columns or 3 in rows:
        return -10
    
    if -3 in columns or -3 in rows:
        return 10
    
    diag = sum(np.diagonal(board))
    diagr = sum(np.fliplr(board).diagonal())
    
    if diag == -3 or diagr == -3:
        return 10
    
    if diag == 3 or diagr == 3:
        return -10
        
    if 0 not in board:
        return 0
    
    return 'continue'

board1 = np.array([[1,0,0],[0,0,0],[0,0,0]])



class TreeNode:
    
    def __init__(self,board,player_type):
        self.board = board
        self.player_type = player_type
        self.children = []
        self.parent = None
        self.q = 0
        if board_check(board) == 'continue':
            self.reward = 1
            
        else:
            self.reward = board_check(board)
        
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    
    def qvalue(self):
        if self.children:
            total = 0
            for i in self.children:
                total += i.reward
                
            return total/len(self.children)
            
        else:
            self.q = self.reward
            
    def print_qvalue(self):
        print(self.q)
        if self.children:
            for child in self.children:
                child.print_qvalue()
        

def build_tree(node=None):
    
    if node == None:
        node = TreeNode(board1,'Environment')
        node.qvalue()
    
        
    if board_check(node.board) != 'continue':
        node.qvalue()
        return
    
    
    if node.player_type == 'Environment':
        
        b = node.board
        lst = []
        
        for i in range(3):
            for j in range(3):
                if node.board[i][j] == 0:
                    lst.append((i,j))
                    
        for move in lst:
            node.board[move[0]][move[1]] = -1
            ch = TreeNode(node.board,'Human')
            node.add_child(ch)
            node.board = b
            node.qvalue()
            build_tree(ch)
            
            
    
    elif node.player_type == 'Human':
        
        b = node.board
        lst = []
        
        
        for i in range(3):
            for j in range(3):
                if node.board[i][j] == 0:
                    lst.append((i,j))
                    
        for move in lst:
            node.board[move[0]][move[1]] = 1
            ch = TreeNode(node.board,'Environment')
            node.add_child(ch)
            node.board = b
            node.qvalue()
            build_tree(ch)
            

    
    node.print_qvalue()
     
            
    
build_tree() 
    