import random
import os
#/home/avenable11/SDEV140-40C-FW-202430-Demos/02_18_25/mydata.dat
def process_outcome():
    file = open("mydata.dat", 'r')
    #text = file.read()
    #print(text)
    userscores = {}
    gamerTotal = 0
    hobbitTotal = 0
    for line in file:
        data = line.split()
        if data[1].isnumeric():
            userscores[int(data[1])] = data[0]
            gamerTotal += int(data[1])
        else:
            userscores[int(data[2])] = data[0] + ' ' + data[1]
            hobbitTotal += int(data[2])
    #print(userscores)
    keys = list(userscores.keys())
    keys.sort(reverse=True)
    outcome = f"The winner is {userscores[keys[0]]} with a score of {keys[0]}\n"
    if gamerTotal > hobbitTotal:
        team = "Gamers"
        winscore = gamerTotal
        losescore = hobbitTotal
    else:
        team = "Hobbits"
        winscore = hobbitTotal
        losescore = gamerTotal

    outcome += f"The winning team is the {team} with a score of {winscore} to {losescore}."
    return outcome

def add_score(username):
    file = open("mydata.dat",'a')
    score = random.randint(100,10000000)
    file.write("\n" + username + " " + str(score))
    file.close()

def get_username():
    username = input("Enter the username: ")
    return username

def main():
    cwd = os.getcwd()
    if not cwd.count("02_18_25"):
        os.chdir("02_18_25")
    while True:
        print("Welcome to the tournament:")
        print("1. Add Score")
        print("2. Finish and display results")
        choice = int(input("Your choice? "))
        if choice == 1:
            username = get_username()
            add_score(username)
        else:
            results = process_outcome()
            print(results)
            break

if __name__ == "__main__":
    main()

