import csv #dealing with csv files here
#====================
def fileLeaderboards():
  print("Choose a file")
  print("\t[1] day1.csv\n\t[2] day2.csv\n\t[3] day3.csv")
  fileNum = int(input("\t--> "))
  while fileNum not in [1,2,3]:
    fileNum = int(input("\t--> "))
  
  file = open(rf"database/day{fileNum}.csv",'r')
  reader = csv.reader(file)
  
  highscore = 0 #to be compared to later
  #saveName
  
  print("-" * 30)
  print("NAME\tGAME\t\tSCORE")
  
  for rec in reader:
    name,game,score = rec[0],rec[1],rec[2]
    print(name,game,score)
    if int(score) > highscore: #every score encountered, if higher, is saved to a variable
      highscore = int(score)
      saveRec = rec
  
  print("-" * 30)
  
  print("Best Player: %s\nGame: %s\nScore: %s" % (saveRec[0], saveRec[1], saveRec[2]))
  file.close()
#====================
# MAIN PROGRAM
print("<-- CSV Game Leaderboard -->")
print("-" * 30)
run = 'Y'
while run in ['Y','YES']:
  fileLeaderboards()
  print("-" * 30)
  run = input("Analyse another file?\n[Y] [N]\n--> ").upper()
  print("-" * 30)
print("\n• That's it! •")