from time import sleep
from random import randint
import sys
import tkinter as tk
'''
class RPS(tk.Frame):
    playerGuess = 0
    CPUGuess = 0
    playerWins = 0
    CPUWins = 0
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.rock = tk.Button(self)
        self.rock["text"] = "Choose : Rock"
        self.rock["command"] = self.set_rock
        self.rock.grid(row=1,column=1)

        self.scissors = tk.Button(self)
        self.scissors["text"] = "Choose : Scissors"
        self.scissors["command"] = self.set_scissors
        self.scissors.grid(row=1,column=2)

        self.paper = tk.Button(self)
        self.paper["text"] = "Choose : Paper"
        self.paper["command"] = self.set_paper
        self.paper.grid(row=1,column=3)
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(row=2,column=2)

    def set_rock(self):
        global playerGuess
        print("You chose rock!")
        playerGuess = 1
        self.getCPUGuess()

    def set_scissors(self):
        global playerGuess
        print("You chose scissors!")
        playerGuess = 2
        self.getCPUGuess()

    def set_paper(self):
        global playerGuess
        print("You chose paper!")
        playerGuess = 3
        self.getCPUGuess()

    def getCPUGuess(self):
        global CPUGuess
        CPUGuess = randint(1,3)
        if CPUGuess == 1:
            print("I chose rock!")
        if CPUGuess == 2:
            print("I chose scissors!")
        if CPUGuess == 3:
            print("I chose paper!")
        self.compareGuesses()

    def compareGuesses(self):
        global CPUGuess
        global playerGuess
        global playerWins
        global CPUWins
        
        if playerGuess == CPUGuess:
            print("We Tied...")
        elif playerGuess == 1:
            if CPUGuess == 2:
                print("You Win!")
                playerWins += 1
            else:
                print("You Lose")
                CPUWins += 1
        elif playerGuess == 2:
            if CPUGuess == 3:
                print("You Win!")
                playerWins += 1
            else:
                print("You Lose")
                CPUWins += 1
        elif playerGuess == 3:
            if CPUGuess == 1:
                print("You Win!")
                playerWins += 1
            else:
                print("You Lose")
                CPUWins += 1

        if CPUWins == 5 or playerWins == 5:
            if CPUWins == 5:
                print("You lost >:)")
                root.destroy
            else:
                print("You won... :3")

root = tk.Tk()
app = RPS(master=root)
app.mainloop()
'''
while True:
    userWins = 0
    CPWins = 0

    while True:
        try:
            name = input("What is your name? ").capitalize()
            if not name.isalpha():
                raise ValueError("Not a valid input")
            break
        except ValueError:
            print("This name includes numbers or special characters!")

    def game():
        while True:
            try:
                file = open(name+".txt","r+")
                frequentGuesses = [line.strip() for line in file]
                file.close()
                file = open(name+"stats.txt","r+")
                stats = [line.strip() for line in file]
                file.close()
                break
            except FileNotFoundError:
                file = open(name+".txt","w")
                file.close()
                file = open(name+"stats.txt","w")
                file.close()
        '''        
        First line in stats is wins
        second is losses
        third is rating
        '''
        if len(stats) != 5:
            while len(stats) < 5:
                stats.append("0")
                new_stats = "\n".join(stats)
                file = open(name+"stats.txt","w")
                file.write(new_stats)
                file.close()
                
        if int(stats[0]) + int(stats[1])+1 <= 10:
            print("You are in placement game %s: %s Win(s), %s Losses" % (str(int(stats[0])+int(stats[1])+1),stats[0],stats[1]))
        else:
            print("You have %s wins and %s losses. Your rating is %s" % (stats[0],stats[1],stats[2]))

        if len(frequentGuesses) != 25:
            while len(frequentGuesses) < 25:
                frequentGuesses.append(str(randint(1,3)))
                
        global userWins
        global CPWins
        rocks = 0
        paper = 0
        scissors = 0
        for i in range(len(frequentGuesses)):
            if int(frequentGuesses[i]) == 1:
                rocks += 1
            elif int(frequentGuesses[i]) == 2:
                scissors += 1
            else:
                paper += 1
        print("I'm taking my guess...")
        CPUGuess = randint(1,len(frequentGuesses))

        if frequentGuesses[23] == frequentGuesses[24]:
            if CPUGuess < 75:
                if frequentGuesses[24] == "1":
                    CPUGuess = 3
                elif frequentGuesses[24] == "2":
                    CPUGuess = 1
                else:
                    CPUGuess = 2

        elif CPUGuess > rocks and CPUGuess <= rocks+paper:
            CPUGuess = 1
            
        elif CPUGuess <= len(frequentGuesses) and CPUGuess > rocks+paper:
            CPUGuess = 2
            
        elif CPUGuess <= rocks:
            CPUGuess = 3

        playerGuess = 0
        while True:
            try:
                userInput = input("Alright %s, I got my pick... Now give me yours!(rock, paper, scissors)\n" % name)
                if userInput.lower() != "rock" and userInput.lower() != "paper" and userInput.lower() != "scissors":
                    raise ValueError("Not a valid input")
                break
            except ValueError:
                print("That isn't rock, paper, or scissors!\n")
        if userInput.lower() == "rock":
            playerGuess = 1
        elif userInput.lower() == "scissors":
            playerGuess = 2
        else:
            playerGuess = 3
        '''
        Rock is 1
        Scissors are 2
        Paper is 3
        '''
        if playerGuess == 1:
            if CPUGuess == 2:
                print("You Win!")
                frequentGuesses.append("1")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                userWins += 1
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
            elif CPUGuess == 1:
                print("We Tied...")
                frequentGuesses.append("1")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
            else:
                print("You Lose...")
                frequentGuesses.append("1")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                CPWins += 1 
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
        elif playerGuess == 2:
            if CPUGuess == 2:
                print("We Tied...")
                frequentGuesses.append("2")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
            elif CPUGuess == 1:
                print("You Lose...")
                frequentGuesses.append("2")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                CPWins += 1 
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
            else:
                print("You Win!")
                frequentGuesses.append("2")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                userWins += 1
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
        else:
            if CPUGuess == 2:
                print("You Lose...")
                frequentGuesses.append("3")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                CPWins += 1 
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
            elif CPUGuess == 1:
                print("You Win!")
                frequentGuesses.append("3")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                userWins += 1
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)
            else:
                print("We Tied...")
                frequentGuesses.append("3")
                del frequentGuesses[0]
                frequentGuesses = "\n".join(frequentGuesses)
                file = open(name+".txt","w+")
                file.write(frequentGuesses)
                file.close()
                sleep(0.5)
                print("You have",userWins,"wins. I have",CPWins,"wins.\n")
                sleep(0.5)

    def do_top10():
        numbers_of_top10 = []
        names = []
        try:
            top10file = open("top10.txt","r+")
            top10 = [line.strip() for line in top10file]
            top10file.close()
        except FileNotFoundError:
            top10file = open("top10.txt","w+")
            top10file.write("Random ELO 1950\nRANdom ELO 1500\nRANDOM ELO 1200")
            top10file.close()
            top10file = open("top10.txt","r+")
            top10 = [line.strip() for line in top10file]
            top10file.close()
        for i in range(len(top10)):
            element = top10[i]
            number = ""
            for letter in element:
                if not letter.isalpha() and letter != " ":
                    number += letter
            numbers_of_top10.append(number)

        for i in range(len(top10)):
            element = top10[i]
            letters = ""
            for letter in element:
                if letter != " ":
                    letters += letter
                else:
                    names.append(letters)
                    break

        for i in range(len(names)):
            if names[i] == name:
                del top10[i]
                del numbers_of_top10[i]

        for i in range(len(numbers_of_top10)):
            if int(stats[2]) > int(numbers_of_top10[i]):
                top10.insert(i,name+" ELO "+stats[2])
                break
        
        if len(top10) > 10:
            top10.pop()
        elif len(top10) < 10 and int(stats[2]) < int(numbers_of_top10[len(numbers_of_top10)-1]):
            top10.append(name+" ELO "+stats[2])
        else:
            pass

        top = "\n".join(top10)
                    
        top10file = open("top10.txt","w")
        top10file.write(top)
        top10file.close()

    while CPWins <= 5 or userWins <= 5:
        while True:
            try:
                file = open(name+"stats.txt","r+")
                stats = [line.strip() for line in file]
                file.close()
                break
            except FileNotFoundError:
                break
        if CPWins < 5 and userWins < 5:
            game()
        else:
            if CPWins == 5:
                if int(stats[0]) + int(stats[1]) < 4:
                    print("You Lose!")
                    sleep(0.5)
                    stats[3] = str(int(stats[3])+ CPWins)
                    stats[4] = str(int(stats[4])+ userWins)
                    CPWins += 1
                    number = int(stats[1])
                    number += 1
                    stats[1] = str(number)
                    new_stats = "\n".join(stats)
                    file = open(name+"stats.txt","w")
                    file.write(new_stats)
                    file.close()
                    do_top10()
                    break

                file = open(name+"stats.txt","r+")
                stats = [line.strip() for line in file]
                file.close()
                
                if int(stats[0]) + int(stats[1]) == 4:
                    numbers_of_top10 = []
                    names = []
                    stats[3] = str(int(stats[3])+ CPWins)
                    stats[4] = str(int(stats[4])+ userWins)
                    CPWins += 1
                    number = int(stats[1])
                    number += 1
                    stats[1] = str(number)
                    number = int(stats[4])*100 + int(stats[0]) * 100 - int(stats[3]) * 50
                    stats[2] = str(number)
                    new_stats = "\n".join(stats)
                    file = open(name+"stats.txt","w")
                    file.write(new_stats)
                    file.close()
                    print(new_stats)
                    do_top10()
                    break
                
                elif int(stats[0]) + int(stats[1]) > 4:
                    numbers_of_top10 = []
                    names = []
                    stats[3] = str(int(stats[3])+ CPWins)
                    stats[4] = str(int(stats[4])+ userWins)
                    CPWins += 1
                    number = int(stats[1])
                    number += 1
                    stats[1] = str(number)
                    number = userWins - CPWins
                    rating_change = int(stats[2]) + number*10
                    stats[2] = str(rating_change)
                    new_stats = "\n".join(stats)
                    file = open(name+"stats.txt","w")
                    file.write(new_stats)
                    file.close()
                    print(new_stats)
                    do_top10()
                    break

            elif userWins == 5:
                if int(stats[0]) + int(stats[1]) < 4:
                    numbers_of_top10 = []
                    names = []
                    print("You Win!")
                    sleep(0.5)
                    stats[3] = str(int(stats[3])+ CPWins)
                    stats[4] = str(int(stats[4])+ userWins)
                    userWins += 1
                    number = int(stats[0])
                    number += 1
                    stats[0] = str(number)
                    new_stats = "\n".join(stats)
                    file = open(name+"stats.txt","w")
                    file.write(new_stats)
                    file.close()
                    do_top10()
                    break

                file = open(name+"stats.txt","r+")
                stats = [line.strip() for line in file]
                file.close()
                
                if int(stats[0]) + int(stats[1]) == 4:
                    numbers_of_top10 = []
                    names = []
                    stats[3] = str(int(stats[3])+ CPWins)
                    stats[4] = str(int(stats[4])+ userWins)
                    userWins += 1
                    number = int(stats[0])
                    number += 1
                    stats[0] = str(number)
                    number = int(stats[4])*100 + int(stats[0]) * 100 - int(stats[3]) * 50
                    stats[2] = str(number)
                    new_stats = "\n".join(stats)
                    file = open(name+"stats.txt","w")
                    file.write(new_stats)
                    file.close()
                    print(new_stats)
                    do_top10()
                    break
                
                elif int(stats[0]) + int(stats[1]) > 4:
                    numbers_of_top10 = []
                    names = []
                    stats[3] = str(int(stats[3])+ CPWins)
                    stats[4] = str(int(stats[4])+ userWins)
                    userWins += 1
                    number = int(stats[0])
                    number += 1
                    stats[0] = str(number)
                    number = userWins - CPWins
                    rating_change = int(stats[2]) + number*10
                    stats[2] = str(rating_change)
                    new_stats = "\n".join(stats)
                    file = open(name+"stats.txt","w")
                    file.write(new_stats)
                    file.close()
                    print(new_stats)
                    do_top10()
                    break

    if CPWins > 5 or userWins > 5:
        while True:
                try:
                    view = input("Would you like to see the top 10 players?")
                    if view.lower() != "yes" and view.lower() != "no":
                        raise ValueError("Not a valid input")
                    else:
                        if view.lower() == "yes":
                            top = open("top10.txt","r+")
                            top10 = [line.strip() for line in top]
                            top.close()
                            listed_top10 = "\n".join(top10)
                            print("\n" + listed_top10 + "\n")
                        else:
                            pass
                    break
                except ValueError:
                    print("Invalid Input!")
        while True:
                try:
                    restart = input("Would you like to play again?")
                    if restart.lower() != "yes" and restart.lower() != "no":
                        raise ValueError("Not a valid input")
                    else:
                        if restart.lower() == "yes":
                            print("Restarting...")
                            sleep(1)
                        else:
                            print("Shutting Down...")
                            sleep(.5)
                            sys.exit(0)
                    break
                except ValueError:
                    print("Invalid Input!")
