import csv #Dealing with csv files here
def fileLeaderboards():
    DAY1, DAY2, DAY3 = 'database/day1.csv', 'database/day2.csv', 'database/day3.csv' #List of files
    SelectFile = int(input("Select file number\n[1-3]\n--> ")) #Select file
    if SelectFile == 1:
      ChosenFile = DAY1
    elif SelectFile == 2:
      ChosenFile = DAY2
    elif SelectFile == 3:
      ChosenFile = DAY3

    file = open(ChosenFile,'r') #Opens the chosen file
    reader = csv.reader(file)
    highscore = 0 #To be compared to later
    saveName = ''
    print("NAME\tGAME\tSCORE")
    for rec in reader: #rec is a record
      name, game, score = rec[0], rec[1], rec[2] #Having commas split the record means we do not have to worry about lengths, unlike with a single record where we need to know which parts to index
      print(name, game, score)
      if int(score) > highscore: #Every score encountered, that is higher, is saved to a variable
        highscore = int(score)
        saveRecord = rec
    print("\n")
    print("Highest Player: %s\nGame: %s\nScore: %s" % (saveRecord[0], saveRecord[1], saveRecord[2]))
    #ChosenFile.close() -- Doesn't work because ChosenFile is a string!
    close() #Closes the program


# MAIN PROGRAM
fileLeaderboards()
Y_or_N = input("Analyse another file?\n[Y] [N]\n--> ") #Find whether user wants to see more
while Y_or_N == 'Y':
  fileLeaderboards()
print("\n• That's it! •")
