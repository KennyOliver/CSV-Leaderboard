import csv #dealing with csv files here
#====================
def scrape_leaderboard():
  print("Choose a file")
  for i in range(1,3+1):
    print(f"\t[{i}] day{i}.csv")
  fileNum = int(input("\t--> "))
  while fileNum not in range(1,3+1):
    fileNum = int(input("\t--> "))
  
  file = open(rf"database/day{fileNum}.csv",'r')
  reader = csv.reader(file)
  
  highscore = 0 #to be compared to later
  #saveName
  
  print("-" * 30)
  
  print(f"<-- day{fileNum}.csv -->")
  print("NAME\tGAME\t\tSCORE")
  next(reader,None) #skips header line
  for rec in reader:
    name,game,score = rec[0],rec[1],rec[2]
    print(name,game,score)
    if int(score) > highscore: #every score encountered, if higher, is saved to a variable
      highscore = int(score)
      saveRec = rec
  
  print("-" * 30)
  
  print("Best Player: %s\nGame: %s\nHighscore: %s" % (saveRec[0], saveRec[1], saveRec[2]))
  file.close()
#====================
# MAIN PROGRAM
print("<-- CSV Game Leaderboard -->")
print("-" * 30)
run = 'Y'
while run in ['Y','YES']:
  scrape_leaderboard()
  print("-" * 30)
  run = input("Scrape another file?\n\t[Y] [N]\n\t--> ").upper()
  print("-" * 30)
print("\n• That's it! •")