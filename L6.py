#Math Project
#2.Monty Hall Problem
from random import randint
def printcell(cells):
    print("", "-" * 4, "", "-" * 4, " ", "-" * 4)
    for i in range(0, 3):
        print("| %s" % cells[0][i], "|", "| %s " % cells[1][i], "|", "| %s " % cells[2][i], "|")
    print("", "-" * 4, "", "-" * 4, " ", "-" * 4)
        
cells = [['1', ' ', ' '],
         ['2', ' ', ' '],
         ['3', ' ', ' ']]
attempt = 0
no_change = 0
while attempt < 10 and no_change < 10:
    printcell(cells)
    car = randint(1,3)
    sheep = randint(1,3)
    print("Monty Hall Problem \n There is one sheep in two of the doors respectively \n")
    print("and behind the remianing door is a brand car")
    print("If you choose the brand car, you win.")
    door = input("Choose a door.")
    print("Player chooses Door %s" % door)
    while sheep == car and sheep == door:
        sheep = randint(1,3)
    print("Door %s is a sheep" % sheep)
    door2 = input("Would you like to change? \nPress 1 to change. \nPress 2 to stay. \n")
    if door2 == 1:
            door2 = randint(1, 3)
    while sheep == car and sheep == door:
        sheep = randint(1,3)
    else:
        door2 = door
    print(door2, car)
    if door2 == car:
        print("You win! You get the brand car!!!")
        attempt = attempt + 1
    else:
        print("You lose. You get the sheep.")
        no_change = no_change + 1

print("You win ")
#1.Nearest Number
print("Please enter 10 numbers.")
for i in range(0, 3):
    r = input ("%i. Enter a number.")


#3.Adjacent number






   
                          
                             
                                  
                                
                                        
                                     
                                        
                                         
                                      
                                 
