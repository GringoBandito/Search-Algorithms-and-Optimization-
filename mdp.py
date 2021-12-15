import numpy as np
import random
import matplotlib.pyplot as plt

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



board2 = np.array([[1,-1,1],[1,-1,1],[-1,1,-1]])


print(board_check(board2))


def mdp(epochs):
    
    games = []
    gamma = 0.9
    epoch = 0
    board = np.array([[1,0,0],[0,0,0],[0,0,0]])
    lst = []
    reward = []
    boards = []
    while epoch < epochs:
        
        
        
        if board_check(board) == 'continue':
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        lst.append((i,j))
            
            reward.append(1)
            agent_choice = random.choice(lst)
            lst.remove(agent_choice)
            board[agent_choice[0]][agent_choice[1]] = -1
            print(board)
            
            


            cho = random.choice(lst)
            lst.remove(cho)
        
            board[cho[0]][cho[1]] = 1
            print(board)
    
        else:
            reward.append(board_check(board))
            epoch += 1
            for i in range(len(reward)):
                for j in range(i+1,len(reward)):
                    reward[i] += reward[j] * (gamma ** (j-i))
            games.append(reward)
            boards.append(board)
            board = np.array([[1,0,0],[0,0,0],[0,0,0]])
            lst = []
            reward = []
            
        
    
    return games

bigL = mdp(1)


plt.xlabel('State')
plt.ylabel('Reward To Go')
plt.title('MDP Reward To Go For Random Placement of "O"')

for i in bigL:
    plt.plot(np.arange(len(i)),i)

plt.show()