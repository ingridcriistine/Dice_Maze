import random

def isValid(board, dices):
    x = 0
    y = 7
    
    while True: 
        # print(y,x)
        if (y == 0 and x == 7):
            print("Caminho encontrado!")
            return True
        
        try: 
            crrValue = board[y][x]
            match dices[board[y][x] -1]:
                case "top":
                    y -= crrValue
                case "down":
                    y += crrValue
                case "left":
                    x -= crrValue
                case "right":
                    x += crrValue
                case "top-right":
                    y -= crrValue
                    x += crrValue
                case "top-left":
                    y += crrValue
                    x -= crrValue
                case "down-right":
                    x += crrValue
                    y += crrValue
                case "down-left":
                    y += crrValue
                    x -= crrValue

        except:
            return False;
        
        if(x < 0 or y < 0 or x > 7 or y > 7):
            return False;


board = [
    [6,3,1,1,2,2,3,1],
    [6,4,6,3,4,2,4,1],
    [3,2,4,2,4,5,2,3],
    [2,4,4,4,2,1,2,3],
    [1,2,3,4,2,2,2,5],
    [5,5,4,4,5,1,5,5],
    [3,3,4,4,3,4,2,2],
    [1,2,3,6,2,4,1,2]
]

tries = []


# directions = ["top", "down", "left", "right", "top-right", "top-left", "down-right", "down-left"]
# dices = [directions[0],directions[3],directions[2],directions[1],directions[4],directions[5],directions[6],directions[7]]
# isValid(board, dices)


while True:
    while True:
        directions = ["top", "down", "left", "right", "top-right", "top-left", "down-right", "down-left"]
        dices = []
        
        while len(directions)>0:
            indx = int(random.random() * (len(directions))) #if int(random.random() * (len(directions)))>=0 else 0
            dices.append(directions.pop(indx))
            
        if dices not in tries:
            tries.append(dices)
            break
    print(len(tries))
    if isValid(board, dices):
        print(dices)
        break;
        print("Achou!!")
        
        
