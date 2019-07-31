
                        
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 5
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamp = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen
def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    snake_stamp_id = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(snake_stamp_id)


for x in range(START_LENGTH) :
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor()
    x_pos+=SQUARE_SIZE 

    snake.goto(x_pos, y_pos) #Move snake to new (x,y)
   
 
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

snake.direction = "Up"
#defines edges
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    snake.direction="Up" 
    print("You pressed the up key!")
   

def down():
    snake.direction="Down"
    print("You pressed the down key")
    

def left():
    snake.direction="Left"
    print("You pressed the left key")
   

def right():
    snake.direction="Right"
    print("you pressed the right key")
  



turtle.onkeypress(up, "Up") # Create listener for up key


turtle.onkeypress(down, "Down")

turtle.onkeypress(left, "Left")

turtle.onkeypress(right, "Right")

turtle.listen()



turtle.register_shape("pizza.gif") 
food = turtle.clone()
food.shape("pizza.gif") 

turtle.register_shape("taco.gif")
super_food = turtle.clone()
super_food.shape("taco.gif")


#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamp = []
super_food_pos = []
super_food_stamp = []
#generates "food"
    

food_pos_num = 0
for this_food_pos  in food_pos:
    food.penup()
    food.goto(food_pos[food_pos_num])
    food.pendown()
    food_stamp_id=food.stamp()
    food_stamp.append(food_stamp_id)
    food_pos_num += 1
    if food_pos_num == 4:
        break

 
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    
    food.penup()##position
    food.goto(food_x, food_y)
    food_pos.append(food.pos())
    food_stamp.append(food.stamp())
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
   
#makes super 
def make_superfood():

    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    super_food.penup()
    super_food.goto(food_x, food_y)
    super_food_pos.append(super_food.pos())
    super_food_stamp.append(super_food.stamp())


food_eaten_count = 0

def move_snake():
    global food_eaten_count
    for i in pos_list[1:-1]:
            if i == snake.pos():
                print("what are you blind? you ate yourself! game over!")
                quit()
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    new_stamp()
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos())#What does this do?
        food.clearstamp(food_stamp[food_index])
        food_pos.pop(food_index) #Remove eaten food position
        food_stamp.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        print(new_stamp())
        food_eaten_count += 1
          
    elif snake.pos() in super_food_pos:
        super_food_index=super_food_pos.index(snake.pos())
        super_food.clearstamp(super_food_stamp[super_food_index])
        super_food_pos.pop(super_food_index) 
        super_food_stamp.pop(super_food_index)
        print("you have eaten super food!!!!!")
        print(new_stamp())
        print(new_stamp())
        print(new_stamp())
        print(new_stamp())
        print(new_stamp())
    remove_tail()
    turtle.ontimer(move_snake,TIME_STEP)   
    

  


    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge you suck! my grandma plays better than you! Game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge you suck! my grandma plays better than you! Game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the botom edge you suck! my grandma plays better than you! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the bottom edge you suck! my grandma plays better than you! Game over!")
        quit()
        
 
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
  
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")

    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
  
    if len(food_stamp) <= 3 :


        make_food()
    
    
    

if food_eaten_count % 5:
                make_superfood()
            
  
    
move_snake()

  
turtle.mainloop()



