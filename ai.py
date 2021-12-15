from __future__ import absolute_import, division, print_function
import copy, random
from game import Game

MOVES = {0: 'up', 1: 'left', 2: 'down', 3: 'right'}
MAX_PLAYER, CHANCE_PLAYER = 0, 1 

def get_best_tile(tile_matrix):
    best_tile = 0
    for i in range(0, len(tile_matrix)):
        for j in range(0, len(tile_matrix[i])):
            tile = tile_matrix[i][j]
            if tile > best_tile:
                best_tile = tile
    return best_tile

# Tree node. To be used to construct a game tree. 
class Node: 
    # Recommended: do not modify this __init__ function
    def __init__(self, state, player_type):
        self.state = (copy.deepcopy(state[0]), state[1])

        # to store a list of (direction, node) tuples
        self.children = []

        self.player_type = player_type

    
      # returns whether this is a terminal state (i.e., no children)
    def is_terminal(self):
        #TODO: complete this
        if len(self.children) == 0:
            return True
        
        else:
            return False

# AI agent. To be used do determine a promising next move.
class AI:
    # Recommended: do not modify this __init__ function
    def __init__(self, root_state, search_depth=1): 
        self.root = Node(root_state, MAX_PLAYER)
        self.search_depth = search_depth
        self.simulator = Game(*root_state)

    # recursive function to build a game tree
    def build_tree(self, node=None, depth=0, ec=False):
        
        if node == None:
            node = self.root
        if depth == self.search_depth: 
            return 
        
        
        
        if node.player_type == MAX_PLAYER:
            # TODO: find all children resulting from 
            # all possible moves (ignore "no-op" moves)

            # self.simulator.reset(*(node.state))
            # self.simulator.get_state()
            # self.simulator.move(direction)
            
            tm, sc = self.simulator.get_state()
            
            for i in MOVES.keys():
                if self.simulator.can_move():
                    self.simulator.move(i)
                    a,b = self.simulator.get_state()
                    ch = Node((a,b),CHANCE_PLAYER)
                    self.build_tree(ch,depth+1)
                    node.children.append((i,ch))
                    self.simulator.reset(tm,sc)
            
            #for child in node.children:
             #   self.build_tree(child[1],depth+1)

        elif node.player_type == CHANCE_PLAYER:
            # TODO: find all children resulting from 
            # all possible placements of '2's
            # self.simulator.get_open_tiles():
            
            tm1,sc1 = self.simulator.get_state()
            lst = self.simulator.get_open_tiles()
            for i in lst:
                tm,sc = self.simulator.get_state()
                a,b = i[0],i[1]
                if tm[a][b] == 0:
                    tm[a][b] = 2
                    
                    ch = Node((tm,sc1),MAX_PLAYER)
                    self.build_tree(ch,depth+1)
                    node.children.append((None,ch))
                    self.simulator.reset(tm1,sc1)
                    
            
            #for child in node.children:
             #   self.build_tree(child[1],depth+1)
        
        # TODO: build a tree for each child of this nod
       
        
    # expectimax implementation; 
    # returns a (best direction, best value) tuple if node is a MAX_PLAYER
    # and a (None, expected best value) tuple if node is a CHANCE_PLAYER
    def expectimax(self, node = None):
    
        if node == None:
            node = self.root

        if node.is_terminal:
            return (random.randint(0,3),node.state[1])

        elif node.player_type == MAX_PLAYER:
            # TODO: MAX_PLAYER logic
            value = -100
            dire = 0
            for n in node.children:
                dire2,val2 = self.expectimax(n)
                if val2 > value:
                    dire = dire2
                    value = val2
            
            return (dire,value)

        elif node.player_type == CHANCE_PLAYER:
            # TODO: CHANCE_PLAYER logic
            value = 0
            for n in node.children:
                value += self.expectimax(n)*1/len(node.children)
                
            return (None,value)


    def expectimax2(self, node = None):
    
        if node == None:
            node = self.root

        if node.is_terminal:
            return (random.randint(0,3),node.state[1],get_best_tile(node.state[0]))

        elif node.player_type == MAX_PLAYER:
            # TODO: MAX_PLAYER logic
            value = -100
            best_tile = 0
            dire = 0
            for n in node.children:
                dire2,val2,bt = self.expectimax2(n)
                if bt > best_tile:
                    dire = dire2
                    value = val2
                    best_tile = bt
            
            return (dire,value,best_tile)

        elif node.player_type == CHANCE_PLAYER:
            # TODO: CHANCE_PLAYER logic
            value = 0
            for n in node.children:
                value += self.expectimax2(n)*1/len(node.children)
                
            return (None,value,None)
    # Do not modify this function
    def compute_decision(self):
        self.build_tree()
        direction, _ = self.expectimax(self.root)
        return direction

    # Implement expectimax with customized evaluation function here
    def compute_decision_ec(self):
        """Choose node with highest expected tile score rather than game score"""
        # TODO delete this
        self.build_tree()
        direction,_,_ = self.expectimax2(self.root)
        return direction
