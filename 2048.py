import random 
khopi_attempt = 0
points = 0
print "----------Game Rules----------\n"
print "Points are granetd on squared basis. Combining 2 tiles of 4 gives 16 pts."
print "Use w a s d as controls."
game_box = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
first_position_list = [0,1,2,3]
first_row_to_begin = random.choice(first_position_list)
first_column_to_begin = random.choice(first_position_list)
game_box[first_row_to_begin][first_column_to_begin] = 2 
 
 
def up_movement(game_box): 
    i =0
    for j in range(0,4): 
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0: 
            if game_box[i][j]==0: 
                while game_box[i][j] == 0: 
                    game_box[i][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
                     
            if game_box[i+1][j]==0 and (game_box[i+2][j]!=0 or game_box[i+3][j]!=0): 
                while game_box[i+1][j]==0:
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
            if game_box[i+2][j] == 0 and game_box[i+3][j]!=0: 
                while game_box[i+2]==0: 
                    game_box[i+2] = game_box[i+3]
                    game_box[i+3][j] = 0
 
def up_addition(game_box): 
    i=0
    global points
    for j in range(0,4): 
        if game_box[i][j]==game_box[i+1][j]: 
            game_box[i][j]=game_box[i][j]+game_box[i+1][j] #
            points += game_box[i][j] ** 2 
            game_box[i+1][j]=game_box[i+2][j] 
            game_box[i+2][j]=game_box[i+3][j] 
            game_box[i+3][j]=0
            
        if game_box[i+1][j]==game_box[i+2][j]: 
            game_box[i+1][j]=game_box[i+1][j]+game_box[i+2][j] 
            points += game_box[i+1][j] ** 2 
            game_box[i+2][j]=game_box[i+3][j] 
            game_box[i+3][j]=0 
 
        if game_box[i+2][j]==game_box[i+3][j]: 
            game_box[i+2][j]=game_box[i+2][j]+game_box[i+3][j] 
            points += game_box[i+2][j] ** 2 
            game_box[i+3][j]=0 
     

 
def down_movement(game_box): 
    i=0
    for j in range(0,4): 
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0: 
            if game_box[i+3][j]==0: 
                while game_box[i+3][j]==0: 
                    game_box[i+3][j]=game_box[i+2][j]
                    game_box[i+2][j]=game_box[i+1][j]
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i+2][j]==0 and (game_box[i+1][j]!=0 or game_box[i][j]!=0):
                while game_box[i+2][j]==0: 
                    game_box[i+2][j]=game_box[i+1][j]
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i+1][j]==0 and game_box[i][j]!=0: 
                while game_box[i+1][j]==0: 
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
 
 
def down_addition(game_box): 
    i=0
    global points
    for j in range(0,4): 
        if game_box[i+3][j]==game_box[i+2][j]: 
            game_box[i+3][j]=game_box[i+3][j] + game_box[i+2][j]
            points += game_box[i+3][j] ** 2 
            game_box[i+2][j]=game_box[i+1][j] 
            game_box[i+1][j]=game_box[i][j]
            game_box[i][j]=0 
 
        if game_box[i+2][j]==game_box[i+1][j]:
            game_box[i+2][j]=game_box[i+2][j]+game_box[i+1][j] 
            points += game_box[i+2][j] ** 2
            game_box[i+1][j]=game_box[i][j] 
            game_box[i][j]=0 
 
        if game_box[i+1][j]==game_box[i][j]:
            game_box[i+1][j]=game_box[i+1][j]+game_box[i][j] 
            points += game_box[i+1][j] ** 2 
            game_box[i][j]=0 
    
 
def left_movement(game_box): 
    j=0
    for i in range(0,4): 
 
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0: 
            if game_box[i][j]==0: 
                while game_box[i][j]==0:
                    game_box[i][j]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3]=0
 
            if game_box[i][j+1]==0 and (game_box[i][j+2]!=0 or game_box[i][j+3]!=0): 
                while game_box[i][j+1]==0: 
                    game_box[i][j+1]=game_box[i][j+2]
                    game_box[i][j+2]=game_box[i][j+3]
                    game_box[i][j+3]=0
 
            if game_box[i][j+2]==0 and (game_box[i][j+3]!=0): 
                while game_box[i][j+2]==0: 
                    game_box[i][j+2]=game_box[i][j+3]
                    game_box[i][j+3]=0
 
                                         
def left_addition(game_box):
    j=0
    global points
    for i in range(0,4): 
        if game_box[i][j]==game_box[i][j+1]: 
            game_box[i][j]=game_box[i][j]+game_box[i][j+1] 
            points += game_box[i][j] ** 2 
            game_box[i][j+1]=game_box[i][j+2] 
            game_box[i][j+2]=game_box[i][j+3] 
            game_box[i][j+3]=0
 
        if game_box[i][j+1]==game_box[i][j+2]: 
            game_box[i][j+1]=game_box[i][j+1]+game_box[i][j+2] 
            points += game_box[i][j+1] ** 2 
            game_box[i][j+2]=game_box[i][j+3] 
            game_box[i][j+3]=0 
 
        if game_box[i][j+2]==game_box[i][j+3]:
            game_box[i][j+2]=game_box[i][j+2]+game_box[i][j+3] 
            points += game_box[i][j+2] ** 2 
            game_box[i][j+3]=0 
 
def right_movement(game_box): 
    j=0
    for i in range(0,4):
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0: 
            if game_box[i][j+3]==0: 
                while game_box[i][j+3]==0: 
                    game_box[i][j+3]=game_box[i][j+2]
                    game_box[i][j+2]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i][j+2]==0 and (game_box[i][j+1]!=0 or game_box[i][j]!=0): 
                while game_box[i][j+2]==0: 
                    game_box[i][j+2]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i][j+1]==0 and game_box[i][j]!=0: 
                while game_box[i][j+1]==0: 
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
 

def right_addition(game_box): 
    j=0
    global points
    for i in range(0,4): 
        if game_box[i][j+3]==game_box[i][j+2]: 
            game_box[i][j+3]=game_box[i][j+3] + game_box[i][j+2] 
            points += game_box[i][j+3] ** 2 
            game_box[i][j+2]=game_box[i][j+1] 
            game_box[i][j+1]=game_box[i][j] 
            game_box[i][j]=0 
 
        if game_box[i][j+2]==game_box[i][j+1]: 
            game_box[i][j+2]=game_box[i][j+2]+game_box[i][j+1] 
            points += game_box[i][j+2] ** 2 
            game_box[i][j+1]=game_box[i][j] 
            game_box[i][j]=0
            
        if game_box[i][j+1]==game_box[i][j]: 
            game_box[i][j+1]=game_box[i][j+1]+game_box[i][j] 
            points += game_box[i][j+1] ** 2 
            game_box[i][j]=0 
                                         

 
while True:
    print "Points>>>>>>"
    print str(points)
    print "\n\n"
    print game_box[0][0],"\t",game_box[0][1],"\t",game_box[0][2],"\t",game_box[0][3],"\n"
    print game_box[1][0],"\t",game_box[1][1],"\t",game_box[1][2],"\t",game_box[1][3],"\n"
    print game_box[2][0],"\t",game_box[2][1],"\t",game_box[2][2],"\t",game_box[2][3],"\n"
    print game_box[3][0],"\t",game_box[3][1],"\t",game_box[3][2],"\t",game_box[3][3],"\n"
    movement_choice = raw_input("Make your move:   ") 
    if movement_choice == "w":
        up_movement(game_box)
        up_addition(game_box)
    elif movement_choice == "s":
        down_movement(game_box)
        down_addition(game_box)
    elif movement_choice == "a":
        left_movement(game_box)
        left_addition(game_box)
    elif movement_choice == "d":
        right_movement(game_box)
        right_addition(game_box)
    else:
        khopi_attempt += 1
        continue
    row_indexes_with_zero = []
    column_indexes_with_zero = []
    for i in range(0,4):
        for j in range(0,4):
            if game_box[i][j] == 0:
                row_indexes_with_zero.append(i)
                column_indexes_with_zero.append(j)
            if game_box[i][j] == 2048:
                print "Congratulations!! You've successfully created a 2048 tile"
                break
    if len(row_indexes_with_zero) > 1:
        random_index = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))
        row_to_place_entry = row_indexes_with_zero[random_index]
        column_to_place_entry = column_indexes_with_zero[random_index]
        game_box[row_to_place_entry][column_to_place_entry] = 2
    elif len(row_indexes_with_zero) == 1:
        row_to_place_entry = row_indexes_with_zero[0]
        column_to_place_entry = column_indexes_with_zero[0]
        game_box[row_to_place_entry][column_to_place_entry] = 2
    else:
        break
 
print "Congratulations!! You scored ", str(points), "points"
