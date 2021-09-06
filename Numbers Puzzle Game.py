import random
nine_puzzle = ["1","2","3","4","5","6","7","8"," "]
sixteen_puzzle = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"," "]
correct_answer9 =   [["1","2","3"],
                    ["4","5","6"], 
                    ["7","8"," "]]

correct_answer16 = [["1","2","3","4"],
                    ["5","6","7","8"], 
                    ["9","10","11","12"],
                    ["13","14","15"," "]]

def Print_puzzle9 ():
    while True:
        random.shuffle(nine_puzzle)
        n = 0
        temp = []
        while n <= 8:
            if nine_puzzle [n] == ' ':
                n=n+1
            else:
                temp.append(nine_puzzle[n]) 
                n = n+1
        index = 0
        test = index + 1
        inversion = 0
        while index <= 7:
            while test <= 7:
                if int(temp[index]) > int(temp[test]):
                    inversion = inversion + 1
                    test = test + 1
                else:
                    test = test + 1
            index = index + 1
            test = index + 1    
        if inversion % 2 == 0:
            i=0
            while i <= 8:
                print ("%-4s%-4s%-4s"%(nine_puzzle[i],nine_puzzle[i+1],nine_puzzle[i+2]))
                i = i+3
            break
        else:
            continue

def Print_puzzle16 ():   
    while True:
        random.shuffle(sixteen_puzzle)
        n = 0
        temp = []
        while n <= 15:
            if sixteen_puzzle [n] == ' ':
                n=n+1
            else:
                temp.append(sixteen_puzzle[n]) 
                n = n+1
        index = 0
        test = index + 1
        inversion = 0
        while index <= 14:
            while test <= 14:
                if int(temp[index]) > int(temp[test]):
                    inversion = inversion + 1
                    test = test + 1
                else:
                    test = test + 1
            index = index + 1
            test = index + 1
        z = 0
        while z <= 15:
            if sixteen_puzzle [z] == ' ':
                if int(z/4)%2 == 0:
                    if inversion % 2 == 1:
                        i = 0
                        while i <= 15:
                            print("%-4s%-4s%-4s%-4s"%(sixteen_puzzle[i],sixteen_puzzle[i+1],sixteen_puzzle[i+2],sixteen_puzzle[i+3]))
                            i = i+4
                        return 0
                    else:
                        break
                    continue        
                elif int(z/4)%2 == 1:
                    if inversion % 2 == 0:
                        i = 0
                        while i <= 15:
                            print("%-4s%-4s%-4s%-4s"%(sixteen_puzzle[i],sixteen_puzzle[i+1],sixteen_puzzle[i+2],sixteen_puzzle[i+3]))
                            i = i+4
                        return 0
                    else:
                        break
                    continue            
            else:
                z = z+1
        continue                       

def directions_9 (x):
    x_2d = 0
    while x_2d <= 2:
        y_2d = 0
        while y_2d <= 2:
            if puzzle9_2D[x_2d][y_2d] == ' ':
                x_2d_empty = x_2d
                y_2d_empty = y_2d
                break
            else:
                y_2d = y_2d + 1
        x_2d = x_2d + 1
    
    if x == left:
        if y_2d_empty != 2:
            puzzle9_2D[x_2d_empty][y_2d_empty], puzzle9_2D[x_2d_empty][y_2d_empty + 1] = puzzle9_2D[x_2d_empty][y_2d_empty + 1], puzzle9_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print ()
    elif x == right:
        if y_2d_empty != 0:
            puzzle9_2D[x_2d_empty][y_2d_empty], puzzle9_2D[x_2d_empty][y_2d_empty - 1] = puzzle9_2D[x_2d_empty][y_2d_empty - 1], puzzle9_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print ()  
    elif x == up:
        if x_2d_empty != 2:
            puzzle9_2D[x_2d_empty][y_2d_empty], puzzle9_2D[x_2d_empty + 1][y_2d_empty] = puzzle9_2D[x_2d_empty + 1][y_2d_empty], puzzle9_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print()    
    elif x == down:
        if x_2d_empty != 0:    
            puzzle9_2D[x_2d_empty][y_2d_empty], puzzle9_2D[x_2d_empty - 1][y_2d_empty] = puzzle9_2D[x_2d_empty - 1][y_2d_empty], puzzle9_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print()
    else:
        print ("invalid input, try again!")
        print ()

def directions_16 (x):
    x_2d = 0
    while x_2d <= 3:
        y_2d = 0
        while y_2d <= 3:
            if puzzle16_2D[x_2d][y_2d] == ' ':
                x_2d_empty = x_2d
                y_2d_empty = y_2d
                break
            else:
                y_2d = y_2d + 1
        x_2d = x_2d + 1
    
    if x == left:
        if y_2d_empty != 3:
            puzzle16_2D[x_2d_empty][y_2d_empty], puzzle16_2D[x_2d_empty][y_2d_empty + 1] = puzzle16_2D[x_2d_empty][y_2d_empty + 1], puzzle16_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print()
    elif x == right:
        if y_2d_empty != 0:
            puzzle16_2D[x_2d_empty][y_2d_empty], puzzle16_2D[x_2d_empty][y_2d_empty - 1] = puzzle16_2D[x_2d_empty][y_2d_empty - 1], puzzle16_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print()  
    elif x == up:
        if x_2d_empty != 3:
            puzzle16_2D[x_2d_empty][y_2d_empty], puzzle16_2D[x_2d_empty + 1][y_2d_empty] = puzzle16_2D[x_2d_empty + 1][y_2d_empty], puzzle16_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print ()    
    elif x == down:
        if x_2d_empty != 0:    
            puzzle16_2D[x_2d_empty][y_2d_empty], puzzle16_2D[x_2d_empty - 1][y_2d_empty] = puzzle16_2D[x_2d_empty - 1][y_2d_empty], puzzle16_2D[x_2d_empty][y_2d_empty]
        else:
            print ("invalid move, try again!")
            print ()
    else:
        print ("invalid input, try again!")
        print ()

while True:
    try:
        directions = str(input("Enter 4-letter keys for left, right, up, and down (without spaces): "))
        left = directions [0]
        right = directions [1]
        up = directions [2]
        down = directions [3]
        game_type = int(input("Please enter '1' to play 3x3 puzzle or '2' to play 4x4 puzzle: "))
        
        puzzle9_2D = []
        puzzle9_2D.append ([])
        puzzle9_2D.append ([])
        puzzle9_2D.append ([])
        
        puzzle16_2D = []
        puzzle16_2D.append ([])
        puzzle16_2D.append ([])
        puzzle16_2D.append ([])
        puzzle16_2D.append ([])
        
        if game_type == 1:
            Print_puzzle9 ()
            number_moves = 0
            x2 = 0 
            x1 = 0
            while x2 <= 2:
                while x1 <= 8:    
                    index = 0
                    while index <= 2:
                        puzzle9_2D[x2].append(nine_puzzle[x1])
                        x1 = x1+1
                        index = index+1
                    x2 = x2+1
            while puzzle9_2D != correct_answer9:
                x_2d = 0
                while x_2d <= 2:
                    y_2d = 0
                    while y_2d <= 2:
                        if puzzle9_2D[x_2d][y_2d] == ' ':
                            x_2d_empty = x_2d
                            y_2d_empty = y_2d
                            break
                        else:
                            y_2d = y_2d + 1
                    x_2d = x_2d + 1
                available_moves = []
                available_moves.append (left)
                available_moves.append (right)
                available_moves.append (up)
                available_moves.append (down)
                available_moves_string = ["left", "right", "up", "down"]
                if x_2d_empty == 0:
                    available_moves.remove (down)
                    available_moves_string.remove ("down")
                if x_2d_empty == 2:
                    available_moves.remove (up)
                    available_moves_string.remove ("up")
                if y_2d_empty == 0:
                    available_moves.remove (right)
                    available_moves_string.remove ("right")
                if y_2d_empty == 2:
                    available_moves.remove (left)
                    available_moves_string.remove ("left") 
                print ("Enter your move (", available_moves_string, " - ", available_moves, ": ")
                moves = str(input())
                print ()
                directions_9 (moves)
                a = 0
                while a <= 2:
                    b = 0
                    print ("%-4s%-4s%-4s"%(puzzle9_2D[a][b], puzzle9_2D[a][b+1], puzzle9_2D[a][b+2]))
                    a = a+1
                number_moves = number_moves + 1
        
        elif game_type == 2:
            Print_puzzle16 ()
            number_moves = 0
            x2 = 0 
            x1 = 0
            while x2 <= 3:
                while x1 <= 15:    
                    index = 0
                    while index <= 3:
                        puzzle16_2D[x2].append(sixteen_puzzle[x1])
                        x1 = x1+1
                        index = index+1
                    x2 = x2+1
            while puzzle16_2D != correct_answer16:
                x_2d = 0
                while x_2d <= 3:
                    y_2d = 0
                    while y_2d <= 3:
                        if puzzle16_2D[x_2d][y_2d] == ' ':
                            x_2d_empty = x_2d
                            y_2d_empty = y_2d
                            break
                        else:
                            y_2d = y_2d + 1
                    x_2d = x_2d + 1
                available_moves = []
                available_moves.append (left)
                available_moves.append (right)
                available_moves.append (up)
                available_moves.append (down)
                available_moves_string = ["left", "right", "up", "down"]
                if x_2d_empty == 0:
                    available_moves.remove (down)
                    available_moves_string.remove ("down")
                if x_2d_empty == 3:
                    available_moves.remove (up)
                    available_moves_string.remove ("up")
                if y_2d_empty == 0:
                    available_moves.remove (right)
                    available_moves_string.remove ("right")
                if y_2d_empty == 3:
                    available_moves.remove (left)
                    available_moves_string.remove ("left") 
                print ("Enter your move (", available_moves_string, " - ", available_moves, ": ")
                moves = str(input())
                print ()
                directions_16 (moves)
                a = 0
                while a <= 3:
                    b = 0
                    print ("%-4s%-4s%-4s%-4s"%(puzzle16_2D[a][b], puzzle16_2D[a][b+1], puzzle16_2D[a][b+2], puzzle16_2D[a][b+3]))
                    a = a+1
                number_moves = number_moves + 1
        
        else:
            print("invalid input, try again!")
            continue
        
        print ("Congratulations! You have completed the puzzle in", number_moves, "moves!")
        print ()
        Next = int(input("Press 'any number key' to end game or 'any letter key' to play another game: "))
        print ("Thankyou for playing!")
        break
    
    except:
        continue  

input ()