print("Hello ! Welcome to My Quiz !")

playing = input("Do you want to play?(Yes/No) ")

if playing.lower() != "yes":
    print("Thank you !")
    quit()

print("Okay ! Let's Play :) ")
score = 0

answer = input("What is CPU Stands for? ")
if answer.lower() ==  "central processing unit":
    print("The Answer is Correct🔥✅")
    score += 1
else:
    print("The Answer is Incorrect😓❌")


answer = input("What is GPU Stands for? ")
if answer.lower() ==  "graphics processing unit":
    print("The Answer is Correct🔥✅")
    score += 1
else:
    print("The Answer is Incorrect😓❌")


answer = input("What is RAM Stands for? ")
if answer.lower() ==  "random access memory":
    print("The Answer is Correct🔥✅")
    score += 1
else:
    print("The Answer is Incorrect😓❌")


answer = input("What is ROM Stands for? ")
if answer.lower() ==  "read only memory":
    print("The Answer is Correct🔥✅")
    score += 1
else:
    print("The Answer is Incorrect😓❌")


answer = input("What is SSD Stands for? ")
if answer.lower() ==  "solid state drive":
    print("The Answer is Correct🔥✅")
    score += 1
else:
    print("The Answer is Incorrect😓❌")  


answer = input("What is HDD Stands for? ")
if answer.lower() ==  "hard disk drive":
    print("The Answer is Correct🔥✅")
    score += 1
else:
    print("The Answer is Incorrect😓❌")

print("----------------------------")
print("You got " + str(score) + " questions Correct🔥!")
print("----------------------------")
print("The Correct answers :")
print("----------------------------")
print("1. Central Processing Unit")
print("2. Graohics Processing Unit")
print("3. Random Acess Memory")
print("4. Read Omly Memory")
print("5. Solid State Drive")
print("6. Hard Disk Drive")
print("----------------------------")
print("Thank you for Participating in the Quiz🥰👍")