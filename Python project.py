#welcome note
print ("Welcome to my football quiz!")

playing = input ("Do you want to test your football knowledge? ")

if playing.lower() != "yes":
    quit()
print("Okay! let's play")
score = 0

answer = input("which country won the FIFA world cup in 2018? ")
if answer.lower() == "france":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is France")

answer = input("The last goal for the FIFA world cup in 2014 was scored by who? ")
if answer.lower() == "mario gotze":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Mario Gotze of Germany")

answer = input("The country with most wins at the world cup is? ")
if answer.lower() == "brazil":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Brazil with 73 wins")

answer = input("which country has scored the most goals at the FIFA world cup? ")
if answer.lower() == "brazil":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Brazil with 229 goals")

answer = input("Which player won the player of the tournament award at the FIFA world cup 2014? ")
if answer.lower() == "lionel messi":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Lionel Messi of Argentina")

answer = input("Do you want to continue? Yes or No? ")
if answer.lower() == "no":
    print("You got "+ str(score) + " questions correctly out of " + str(5))
    print("You got "+ str((score / 5) * 100) + "%")
    exit()
if answer.lower() == "yes":
    print("Let's go")

answer = input("which football club won the UEFA champion's league for 2020/21 season? ")
if answer.lower() == "chelsea":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Chelsea football club")

answer = input("who won the highest goal scorer in UEFA champion's league for 2020/21 season? Lewandowski, Ronaldo, Haaland or Messi? ")
if answer.lower() == "haaland":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Erling Haaland of Borussia Dotmund with 10 goals")

answer = input("which football club won the English Premier league for 2020/21 season? ")
if answer.lower() == "manchester city":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Manchester City football club")

answer = input("which football club won the french Ligue 1 league for 2020/21 season? ")
if answer.lower() == "lille":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Lille football club")

answer = input("which player won the Balon D'or for 2020/21 season? ")
if answer.lower() == "lionel messi":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
    print("Correct answer is Lionel Messi of PSG")

print("You got "+ str(score) + " questions correctly out of " + str(10))
print("You got "+ str((score / 10) * 100) + "%")