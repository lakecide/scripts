
#the function starts 
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


#the main program starts here
print("Enter Number: ")
#iterate between user input
while True:
    user_input = int(input())
    returned_number = collatz(user_input)
    if returned_number != 1:
    
        print(returned_number)
    else:
        print(returned_number)
        break
  
    