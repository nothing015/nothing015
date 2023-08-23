'''
Suppose there is a spaceship leaving Earth.

The spaceship has only a limited amount of fuel so it can only travel a certain distance before coming back.

The spaceship can change direfction every 1 km.

Take input from the user the directions the spaceship will be travelling in and then workout the amount of the maximum distance it can travel.
Afterwards take input of the amount of fuel in litres and the distance the spaceship can travel per litre of fuel.
Finally determine if the rocket will be able to return back to Earth travelling the SAME DIRECTIONS it first travelled in, return a value of True or False
Together with that, if the spaceship changes directions more than x times, then the engine fails and the spaceship shuts down if it is out of fuel.
So return False if the spaceship changes direction more than x times and runs out of fuel.

Take the input of directions in a form of 'u,' 'd', 'l', 'r' for 'up', 'down', 'left', 'right'

1. To implement decisions using if statements
2. To write statements using the boolean primitive data types.
3. To compare strings and/or characters.
4. To write loops using while or for.
5. To write functions


'''
userInput =' '
while userInput != 'u', 'd', 'r', 'l':
    userInput = input("Enter the direction the spaceship will travel \n to stop, enter ")
directionArray = input("")
def Distance(directions):
    
    

distance = Distance(directionArray)
print(distance)
def Spaceship(directions):
    Fuel
    x = 
    Verticaldistance = 0
    Horizontaldistance = 0
    flag = False
    count = 0
    for c in directions:
        if c == 'u':
            Verticaldistance += 1
            count += 1
        elif c == 'd':
            Verticaldistance -= 1
            count += 1
        elif c == 'r':
            Horizontaldistance += 1
            count += 1
        elif c == 'l':
            Horizontaldistance -= 1
            count += 1
    if Verticaldistance == 0 and Horizontaldistance == 0 and count <= x:
        flag = True
     return flag

spaceship = Spaceship(directionArray)
print(spaceship)
