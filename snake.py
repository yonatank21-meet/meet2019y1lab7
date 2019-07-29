                        
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
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

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



def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
   


    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge you suck! Game over!")
         quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge you suck! Game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the botom edge you suck! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the bottom edge you suck! Game over!")

        
 
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
                   
   
    new_stamp()
    turtle.ontimer(move_snake,TIME_STEP)
  
    remove_tail()
move_snake()

turtle.mainloop()




