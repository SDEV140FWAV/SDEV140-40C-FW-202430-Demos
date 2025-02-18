
file = open("mydata.dat", 'r')
#text = file.read()
#print(text)
userscores = {}
i = 0
hobbitTotal = 0
while i < 30:
    i+=1
    line = file.readline()
    data = line.split()
    #print(data)
    userscores[int(data[2])] = data[0] + ' ' + data[1]
    hobbitTotal += int(data[2])

i = 0
gamerTotal = 0
while i < 30:
    i+=1
    line = file.readline()
    data = line.split()
    userscores[int(data[1])] = data[0]
    gamerTotal += int(data[1])

#print(userscores)
keys = list(userscores.keys())
keys.sort(reverse=True)
print(f"The winner is {userscores[keys[0]]} with a score of {keys[0]}")
if gamerTotal > hobbitTotal:
    team = "Gamers"
    winscore = gamerTotal
    losescore = hobbitTotal
else:
    team = "Hobbits"
    winscore = hobbitTotal
    losescore = gamerTotal

print(f"The winning team is the {team} with a score of {winscore} to {losescore}.")