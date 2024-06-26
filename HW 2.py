def BAT_AVG(): #Calculates batting average of every player and displays it on a new file
  start=open("Players.txt", 'r') #Opens the "Players" file in read mode
  ba=open("players_battingaverage.txt", 'w') #Creates a new file to display each players' batting average
  for line in start: #Goes over each player's info
    bat=line.split(';')[3]
    hit=line.split(';')[5]
    avg=int(hit)/int(bat) #Calculates batting average
    ba.write(line+"Batting average is: "+str(avg)+"\n") #Writes the player's info and batting average on the newly created file
    ba.write('\n')
  print("Batting average has been printed on a new file")
  start.close() #Closes file to prevent any data errors
  ba.close() #Closes file to prevent any data errors
    
def SLUG_PERC():
  start=open("Players.txt", 'r')
  sp=open("players_sluggingaverage.txt", 'w')
  for line in start:
    bat=line.split(';')[3]
    hit=line.split('; ')[5]
    doubles=line.split('; ')[6]
    triples=line.split('; ')[7]
    home=line.split('; ')[8]
    singles=int(hit)-(int(doubles)+int(triples)+int(home))
    total=singles+2*int(doubles)+3*int(triples)+4*int(home)
    slugging=(total/int(bat)) #Calculates slugging percentage
    sp.write(line+"Slugging percentage is: "+str(slugging)+"\n")
    sp.write('\n')
  print("Slugging percentage has been printed on a new file")
  start.close() #Closes file to prevent any data errors
  sp.close() #Closes file to prevent any data errors
    
def Main (): #Asks the user to input 1 of the 4 available starting commands
  with open("Players.txt", 'r') as start: #Opens the "Players" file in read mode
    data=start.readline()
    plist=[]
    while (data):
      data=data.strip().split(';')
      plist.append(data)
      data=start.readline()
    
  direct=input("Please enter 1 of the following COMMANDS: 'QUIT', 'HELP', 'TEAM', 'REPORT': ") #Prompts the user to enter a command
  direct=direct.upper()
  if direct!= "QUIT" and direct!= "HELP" and direct != "TEAM" and direct != "REPORT": #Checks to see if the user gave a valid input
    print("I'm sorry, but that's not a valid command")
    Main()
  if direct == "QUIT":
    print("End of program")
  if direct == "HELP":
    print("The 'QUIT' command will exit the entire program")
    print("The 'TEAM' command will display the information about all the players from a team of your choice")
    print("The 'REPORT' command will display the Batting average or the slugging percenatge of all the players")
    Main()
  if direct == "TEAM":
    team=input("Enter team name: ")
    team=team.upper()
    if team != "CWS" and team != "DET" and team != "LAA" and team != "CIN" and team != "ATL" and team != "SF" and team != "NYY" and team != "STL" and team != "SD" and team != "CLE" and team != "TEX" and team != "HOU" and team != "COL" and team != "CHC" and team != "NYM": #Checks to see if the user gave a valid input
      print("That's not a valid teamname")
      Main()
    for i in range(20): #Detects and prints the info of each player on a specific team
      if team == plist[i][1].lstrip():
        print(plist[i])
  if direct == "REPORT":
    choice=input("BATTING or SLUGGING: ")
    if choice.upper() != "BATTING" and choice.upper() != "SLUGGING": #Checks to see if the user gave a valid input
      print("I'm sorry, but you must enter 'BATTING' or 'SLUGGING'")
      Main()
    if choice.upper() == "BATTING":
      BAT_AVG()
    if choice.upper() == "SLUGGING":
      SLUG_PERC()
                    
Main() #Starts the entire program
          
