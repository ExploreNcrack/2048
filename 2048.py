import random

class Game2048:
    #---------------------------------------------------------------------------
    # constructor: initializes the empty grid with 2 "2"s in random tiles 
    #---------------------------------------------------------------------------
    def __init__(self, row=4, col=4):
        self.row = row                         # number of rows in grid
        self.col = col                         # number of columns in grid
        self.score = 0                         # initialize the game score
                
        self.grid=[]                           # initialize the grid with 0s
        for i in range(0,self.row):                    
            column = []
            for j in range(0,self.col):
                column.append(0)
            self.grid.append(column)
            
        self.emptyTiles = []
        
        # ##### You need here to initialize you matix representing the grid
        # ##### with zeros. Don't forget row lines and col columns
  
        self.RandomFillTile(2)                 #initialize 2 tiles with a 2
        self.RandomFillTile(2)
        l1 = '-----------------------------'
        print(l1)
        for i in range(0,self.row): 
            line = ''
            for j in range(0,self.col):
                if self.grid[i][j] == 0:
                    line +='|%6s'%('   ')
                else:
                    line += '|%6i'%(self.grid[i][j])    
            line += '|'
            print(line)
            print(l1)
        print('Current Score: %d|| Empty cells:  %d'%(self.getScore(),self.getNbEmptyTiles()))
        print(l1+'------')         

    #---------------------------------------------------------------------------
    # generates a 2 or 4 randomly with 3 times more chance to get a 2
    #---------------------------------------------------------------------------
    def random2or4(self):
        if random.random() > 0.90:
            return 4
        else: return 2


    #---------------------------------------------------------------------------
    # retrieving the current score
    #---------------------------------------------------------------------------
    def getScore(self):
        return self.score
    
    #---------------------------------------------------------------------------
    # adding "new" to the current score
    #---------------------------------------------------------------------------
    def setScore(self, new):
        self.score+=new
        
    #---------------------------------------------------------------------------
    # Obtaining the number of empty tiles
    #---------------------------------------------------------------------------
    def getNbEmptyTiles(self):
        empty=0
 
        # ##### You should return the number of tiles that are empty
        # ##### i.e. they contain zeros. 
        for i in self.grid:
            for c in i:
                if c == 0:
                    empty += 1       
        return empty

    #---------------------------------------------------------------------------
    # Obtaining the list of empty tiles in a list of pairs (of coordinates i,j)
    #---------------------------------------------------------------------------
    def getListEmptyTiles(self):
        emptyTiles=[]
        for i in range(0,self.row):
            for j in range(0,self.col):
                if self.grid[i][j] == 0:
                    emptyTiles.append((i,j))
 
        # ##### You should return a list of pairs where each pair
        # ##### is the x,y coordinates of a tile that is empty
    
        return emptyTiles           
        
    #---------------------------------------------------------------------------
    # Selecting a rambom empty tile and filling it with "init"    
    #---------------------------------------------------------------------------
    def RandomFillTile(self, init):
        emptyTiles=self.getListEmptyTiles()
        if len(emptyTiles) !=0:
            tile=random.randint(0,len(emptyTiles)-1)
            (i,j)=emptyTiles[tile]
            self.grid[i][j]=init
        
    #---------------------------------------------------------------------------
    # printing the current game grid, score and number of empty tiles
    #---------------------------------------------------------------------------
    def Print(self):
        l1 = '-----------------------------'
        print(l1)
        for i in range(0,self.row): 
            line = ''
            for j in range(0,self.col):
                if self.grid[i][j] == 0:
                    line +='|%6s'%('   ')
                else:
                    line += '|%6i'%(self.grid[i][j])  
            line += '|'
            print(line)
            print(l1)   
        print('Current Score: %d|| Empty cells: %d'%(self.getScore(),self.getNbEmptyTiles()))
        print(l1+'------')       

    #---------------------------------------------------------------------------
    # check if the grid is collapsible horizontally or vertically
    #---------------------------------------------------------------------------
    def collapsible(self):
        if (self.getNbEmptyTiles() != 0):
            return True

        collaps=False

        #check slide_left
        for i in range(0,self.row):
            for j in range(0,self.col-1):
                if self.grid[i][j] != 0:
                    index = j+1
                    
                    while True:
                        if index >= self.col:
                            break
                        elif self.grid[i][index] != 0 and self.grid[i][index] != self.grid[i][j]:
                            break
                        elif self.grid[i][index] == self.grid[i][j]:
                            
                            return True
    
                        index += 1


        #check slide_right
        for i in range(0,self.row):
            for j in range(self.col-1,0,-1):
                if self.grid[i][j] != 0:
                    index = j-1
                
                    while True:
                        if index <= -1:
                            break
                        elif self.grid[i][index] != 0 and self.grid[i][index] != self.grid[i][j]:
                            break
                        elif self.grid[i][index] == self.grid[i][j]:
            
                            return True
  
                        index -= 1

        #check slide_up
        for i in range(0,self.col):
            for j in range(0,self.row-1):
                if self.grid[j][i] != 0:
                    index = j+1
                    while True:
                        if index >= self.row:
                            break
                        elif self.grid[index][i] != 0 and self.grid[index][i] != self.grid[j][i]:
                            break
                        elif self.grid[index][i] == self.grid[j][i]:
                            
                            return True

                        index += 1


        #check slide_down
        for i in range(0,self.col):
            for j in range(self.row-1,0,-1):
                if self.grid[j][i] != 0:
                    index = j-1
            
                    while True:
                        if index <= -1:
                            break
                        elif self.grid[index][i] != 0 and self.grid[index][i] != self.grid[j][i]:
                            break
                        elif self.grid[index][i] == self.grid[j][i]:
                           
                            return True
   
                        index -= 1


        # ##### You should check whether there is a possibility to merge
        # ##### adjacent tiles and assign True to collaps if it is the case


        return collaps
               
    #---------------------------------------------------------------------------
    # check if the grid contains 2048
    #---------------------------------------------------------------------------
    def win(self):
        for i in self.grid:
            for c in i:
                if c == 2048:
                    return True       
        return False        

        # ##### return true is the value 2048 exists in the grid
        # ##### return false otherwise
    
    
    #---------------------------------------------------------------------------
    # collapses the columns to the left and updates the grid and score
    #---------------------------------------------------------------------------
    def slideLeft(self):

        changed = False         # indicates if there were tiles that slid
        for i in range(0,self.row):
            for j in range(0,self.col-1):
                if self.grid[i][j] != 0:
                    index = j+1
                    SUM = self.grid[i][j]
                    while True:
                        if index >= self.col:
                            break
                        elif self.grid[i][index] != 0 and self.grid[i][index] != self.grid[i][j]:
                            break
                        elif self.grid[i][index] == self.grid[i][j]:
                            SUM += self.grid[i][index]
                            self.setScore(SUM)
                            self.grid[i][j] = SUM
                            changed = True

                            self.grid[i][index] = 0
                            break    
                        index += 1
                    

        for i in range(0,self.row):
            for j in range(0,self.col-1):
                if self.grid[i][j] == 0:
                    k = j+1
                    while True:
                        if k >= self.col:
                            break
                        elif self.grid[i][k] == 0:
                            k += 1
                        elif self.grid[i][k] != 0:
                            self.grid[i][j] = self.grid[i][k]
                            self.grid[i][k] = 0
                            changed = True
                            break

        
        return changed
                
     
    #---------------------------------------------------------------------------
    # collapses the columns to the right and updates the grid and score
    #---------------------------------------------------------------------------
    def slideRight(self):
       
        changed = False         # indicates if there were tiles that slid
        for i in range(0,self.row):
            for j in range(self.col-1,0,-1):
                if self.grid[i][j] != 0:
                    index = j-1
                    SUM = self.grid[i][j]
                    while True:
                        if index <= -1:
                            break
                        elif self.grid[i][index] != 0 and self.grid[i][index] != self.grid[i][j]:
                            break
                        elif self.grid[i][index] == self.grid[i][j]:
                            SUM += self.grid[i][index]
                            self.grid[i][j] = SUM
                            self.setScore(SUM)
                            changed = True

                            self.grid[i][index] = 0
                            break    
                        index -= 1
                    

        for i in range(0,self.row):
            for j in range(self.col-1,0,-1):
                if self.grid[i][j] == 0:
                    k = j-1
                    while True:
                        if k <= -1:
                            break
                        elif self.grid[i][k] == 0:
                            k -= 1
                        elif self.grid[i][k] != 0:
                            self.grid[i][j] = self.grid[i][k]
                            self.grid[i][k] = 0
                            changed = True
                            break

        
        return changed
       

    #---------------------------------------------------------------------------
    # collapses the rows upwards and updates the grid and score
    #---------------------------------------------------------------------------
    def slideUp(self):
        changed = False         # indicates if there were tiles that slid
        for i in range(0,self.col):
            for j in range(0,self.row-1):
                if self.grid[j][i] != 0:
                    index = j+1
                    SUM = self.grid[j][i]
                    while True:
                        if index >= self.row:
                            break
                        elif self.grid[index][i] != 0 and self.grid[index][i] != self.grid[j][i]:
                            break
                        elif self.grid[index][i] == self.grid[j][i]:
                            SUM += self.grid[index][i]
                            self.grid[j][i] = SUM
                            self.setScore(SUM)
                            changed = True

                            self.grid[index][i] = 0
                            break    
                        index += 1
                    

        for i in range(0,self.col):
            for j in range(0,self.row-1):
                if self.grid[j][i] == 0:
                    k = j+1
                    while True:
                        if k >= self.row:
                            break
                        elif self.grid[k][i] == 0:
                            k += 1
                        elif self.grid[k][i] != 0:
                            self.grid[j][i] = self.grid[k][i]
                            self.grid[k][i] = 0
                            changed = True
                            break

        return changed


                
    #---------------------------------------------------------------------------
    # collapses the rows downwards and updates the grid and score
    #---------------------------------------------------------------------------
    def slideDown(self):
         changed = False         # indicates if there were tiles that slid
         for i in range(0,self.col):
             for j in range(self.row-1,0,-1):
                 if self.grid[j][i] != 0:
                     index = j-1
                     SUM = self.grid[j][i]
                     while True:
                         if index <= -1:
                             break
                         elif self.grid[index][i] != 0 and self.grid[index][i] != self.grid[j][i]:
                             break
                         elif self.grid[index][i] == self.grid[j][i]:
                             SUM += self.grid[index][i]
                             self.grid[j][i] = SUM
                             self.setScore(SUM)
                             changed = True

                             self.grid[index][i] = 0
                             break    
                         index -= 1
                     

         for i in range(0,self.col):
             for j in range(self.row-1,0,-1):
                 if self.grid[j][i] == 0:
                     k = j-1
                     while True:
                         if k <= -1:
                             break
                         elif self.grid[k][i] == 0:
                             k -= 1
                         elif self.grid[k][i] != 0:
                             self.grid[j][i] = self.grid[k][i]
                             self.grid[k][i] = 0
                             changed = True
                             break

         return changed
#-End of Class Game2048---------------------------------------------------------


# ##### write here your main program to play the game
def main():
    game = Game2048()
    end_of_game = False
    while not end_of_game:
        if game.win():
            print('Congratulations! You win!')
            end_of_game = True
        else:
            user_direction = input('"D"for right, "A" for left, "W" for up, "S" for down, "P" for exit.\nType your direction: ')
            user_direction = user_direction.upper()
            while user_direction not in ['W','A','S','D','P']:
                print('Invalid input!')
                user_direction = input('"D"for right, "A" for left, "W" for up, "S" for down, "P" for exit.\nType your direction: ')
            if user_direction == 'W':
                if game.slideUp():
                    rand_num=game.random2or4()
                    game.RandomFillTile(rand_num)
            elif user_direction == 'A':
                if game.slideLeft():
                    rand_num=game.random2or4()
                    game.RandomFillTile(rand_num)
            elif user_direction == 'S':
                if game.slideDown():
                    rand_num=game.random2or4()
                    game.RandomFillTile(rand_num)
            elif user_direction == 'D':
                if game.slideRight():
                    rand_num=game.random2or4()
                    game.RandomFillTile(rand_num)
            elif user_direction == 'P':
                end_of_game = True
                print('You exit the game!')
            a = game.random2or4()

            game.Print()
                
                
            if not game.collapsible() and game.getNbEmptyTiles() ==0:
                
                print('Sorry! Game over. You lose')
                end_of_game = True
                    
main()

                    
                
                    
                    
                


        
   

