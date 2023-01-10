print('Welcome to the ultimate computer quiz!!!')

playing = input('Do you want to play my game? ' )

if playing.lower() != 'yes' :
    quit()

print("Okay! Let's hope you have the smarts ;)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What slot would you install a GPU on the motherboard? ")
if answer.lower() == "pci-e" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What is kind of ram does laptops require? ")
if answer.lower() == "sodimm" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What brand CPUs use the casacade lake platform? ")
if answer.lower() == "intel" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
    
answer = input("What port on the motherboard is responsible for a wired internet connection? ")
if answer.lower() == "ethernet" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
    
answer = input("Whats the fastest storage hardware on the market for a pc as of 01/09/2023? ")
if answer.lower() == "nvme" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What kind of cooling method is more efficient for computer hardware components but costs more? ")
if answer.lower() == "water cooling" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("Wasn't this the best little quiz game? ")
if answer.lower() == "yes" :
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str((score / 10) * 100) + "%. " )