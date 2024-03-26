total = 0

while total < 21:
    player1 = int(input("Write a number between 1-3"))
    
    if player1 < 4 and player1 > 1:
        total += player1
        if total > 21:
            print("You lose") 
            break
        elif total == 21: 
            print("You win player 1")
            break
        print(total)
    
       
    
    player2 = int(input("Write a number between 1-3")) 
    if player2 < 4 and player2 > 0:
        total += player2
    
    if total > 21:
        print("You lose")
        break
    elif total == 21: 
        print("You win player 2")
        break
        
        
    print(total)
    
    