class game:
  state = None
  points = 0
  isRunning = false
  
  
class player:
  color =None
  name = None
  prevRoom = None
  currentRoom = None
  nextRoom = None
  icon = None
  
class map:
  isCreated = false
  obj = None
  
class inv:
  hasPizza = None
  hasToy = None
  hasCatPoop = None
  
  
class family_room:
  isOccupied = false
  hasPlayed = false

  
class bedroom:
  isOccupied = false
  hasPlayed = false
  
class kitchen:
  isOccupied = false
  hasPlayed = false
  
class tv_room:
  isOccupied = false
  hasPlayed = false
  
class yard:
  isOccupied = false
  hasPlayed = false
  
def adventure():
  getInfo()
  game.isRunning = true
  game.state = "update"
  while (game.isRunning):
      if (game.state == "update"): #Update the map layout and inventory
          if (map.isCreated == false):
            map.obj= makePicture(getMediaPath("map.png"))
            show(map.obj)
            player.currentRoom = "kitchen"
            player.prevRoom = "yard"            
            paint("kitchen")
            map.isCreated = true
          else:
            updatePos()
            updateInv()
            game.state = "move"
      elif (game.state == "move"): #Have the player pick a direction and move the piece
          pickDirection()
          game.state = "score"
      elif (game.state == "score"): #Count the score of the player
          countScore()
          game.state = "update"
      elif (game.state == "end"): #End-game state
            countScore()
            writeScore()
            showEnd()
            game.isRunning = false
      else: #Hopefully this never comes up.
          showError("There was an error in the main game state!\nThis shouldn't have happened.")
          
          
def getInfo():
  text("Welcome to Room Explorer!\nYou will explore this world from the viewpoint of a dog.\nFirst off, a few questions!")
  player.name = smartRequest("What is your name?")
  player.color = smartRequest("Hello there, " + player.name +"!\nWhat color  dog icon do you want to be? \nOptions are: Blue/Red/Green/Purple/Yellow")
  setPlayerColor()
  
  
def writeScore():
  file = open(getMediaPath("score.txt"), "wt")
  file.write(player.name + " - " + game.points)
  file.close()
  
  
  
def updatePos():
  #Move player icon
  if (player.nextRoom == "kitchen"):
    paint("kitchen")
    player.prevRoom = player.currentRoom
    player.currentRoom = "kitchen"
  elif (player.nextRoom == "family_room"):
    paint("family_room")
    player.prevRoom = player.currentRoom
    player.currentRoom = "family_room"
  elif (player.nextRoom == "yard"):
    paint("yard")
    player.prevRoom = player.currentRoom
    player.currentRoom = "yard"
  elif (player.nextRoom == "tv_room"):
    paint("tv_room")
    player.prevRoom = player.currentRoom
    player.currentRoom = "tv_room"
  elif (player.nextRoom == "bedroom"):
    paint("bedroom")
    player.prevRoom = player.currentRoom
    player.currentRoom = "bedroom"
  else:
    None
    
    
def updateInv():
  #Ask about picking up items within the room also tells story
  if (player.currentRoom == "kitchen"):
    playSound("kitchen")
    if not (inv.hasPizza):
      choice = smartRequest("You find some pizza on the ground, do you want to pick it up?\nY/N"):
      if (choice == "Y") or (choice == "y"):
        inv.hasPizza = true
        paint("pizza")
      else:
        continue
      text("You see some cake pops up on the counter, I wonder if you can find a way to get up on the counter and eat them")
  elif (player.currentRoom == "family_room"):
    playSound("family_room")
    if not (inv.hasCatPoop):
      choice = smartRequest("You find some Cat Poop on the couch, do you want to eat it?\nY/N"):
      if (choice == "Y") or (choice == "y"):
        inv.hasCatPoop = true
        game.state = "end"
        return
      else:
        text("Smart choice not eating the cat poop. That would have killed you")
      text("In the family room you see your human rearranging the furniture again!\nWill she ever find one that works?")
  elif (player.currentRoom == "yard"):
    playSound("yard")
  elif (player.currentRoom == "tv_room"):
    playSound("tv_room")
  elif (player.currentRoom == "bedroom"):
    playSound("bedroom")
  else:
    None
  
  
  
def pickDirection():
  #pick a new direction based on the options available
  if (player.currentRoom == "kitchen"):
    choice = smartRequest("You can go up or left\nPIck a Direction")
    if (choice == "up") or (choice == "left"):
      player.nextRoom = "family_room"
    elif (game.isRunning == false):
      return
    else:
      text("That isnt an okay direction there doggo")
      pickDirection()
        
  elif (player.currentRoom == "family_room"):
    choice = smartRequest("You can go up, right, or down\nPick a Direction")
    if (choice == "up"):
      player.nextRoom = "bedroom"
    elif (choice == "right"):
      player.nextRoom = "tv_room"
    elif (choice == "down"):
      player.nextRoom = "kitchen"
    elif (game.isRunning == false):
      return
    else:
      text("That isnt an okay direction there doggo")
      pickDirection()
      
  elif (player.currentRoom == "yard"):
    choice = smartRequest("You can go up or left\nPick a Direction")
    if (choice == "left"):
      player.nextRoom = "kitchen"
    elif (choice == "up"):
      player.nextRoom = "tv_room"
    elif (game.isRunning == false):
      return
    else:
      text("That isnt an okay direction there doggo")
      pickDirection()
      
  elif (player.currentRoom == "tv_room"):
    choice = smartRequest("You can go down or left\nPick a Direction")
    if (choice == "down"):
      player.nextRoom = "yard"
    elif (choice == "left"):
      player.nextRoom = "family_room"
    elif (game.isRunning == false):
      return
    else:
      text("That isnt an okay direction there doggo")
      pickDirection()
        
  elif (player.currentRoom == "bedroom"):
    choice = smartRequest("You can go down, or right\Pick a Direction")
    if (choice == "down"):
      player.nextRoom = "family_room"
    elif (choice == "right"):
      player.nextRoom = "tv_room"
    elif (game.isRunning == false):
      return
    else:
      text("That isnt an okay direction there doggo")
      pickDirection()
        
  else:
    showError("There was an error in the main game state!\nThis shouldn't have happened.")
  
  
def countScore():
  #Add up the points for that room and then add them to the player score
  None
  
  
def showEnd():
  #Shows stats and the final part of the adventure before exciting
  None
    
    
def playSound(room):
  if (room == "kitchne"):
    if (kitchen.hasPlayed == false):
      play(makeSound(getMediaPath("sounds/kitchen.wav")))
      kitchen.hasPlayed = true
  elif (room == "yard"):
    if (yard.hasPlayed == false):
      play(makeSound(getMediaPath("sounds/yard.wav")))
      yard.hasPlayed = true
  elif (room == "family_room"):
    if (family_room.hasPlayed == false):
      play(makeSound(getMediaPath("sounds/family_room.wav")))
      family_room.hasPlayed = true
  elif (room == "tv_room"):
    if (tv_room.hasPlayed == false):
      play(makeSound(getMediaPath("sounds/tv_room.wav")))
      tv_room.hasPlayed = true
  elif (room == "bedroom"):
    if (bedroom.hasPlayed == false):
      play(makeSound(getMediaPath("sounds/bedroom.wav")))
      bedroom.hasPlayed = true
  else:
    None

def text(input):
  showInformation(input)
  
def smartRequest(str):
  input = requestString(str)
  input = input.lower()
  if (input == "end") or (input == "exit") or (input == "quit"):
    game.isRunning = false
  else:
    return input
 #
 #
 #  EVERY FUNCTION USED TO INTERACT WITH THE PLAYER ICON
 #
 #
 
def setPlayerColor():
  txtColor = player.color
  if (txtColor == "Blue") or (txtColor == "blue"):
    player.color = blue
    createIcon()
  elif (txtColor == "Red") or (txtColor == "red"):
    player.color = red
    createIcon()
  elif (txtColor == "Green") or (txtColor == "green"):
    player.color = green
    createIcon()
  elif (txtColor == "Purple") or (txtColor == "purple"):
    player.color = makeColor() #TODO find colors for this
    createIcon()
  elif (txtColor == "Yellow") or (txtColor == "yellow"):
    player.color = makeColor() #TODO find colors for this
    createIcon()
  else:
    showError("None of the colors you entered were legit so now you're blue.\nHope you like it.")
    player.color = blue
 
 
def paint(room):
  whiteout(player.currentRoom)
  if (room == "kitchen"):
    copyColor(432, 288)
    repaint(map.obj)
  elif (room == "family_room"):
    copyColor(338, 179)
    repaint(map.obj)
  elif (room == "bedroom"):
    copyColor(377, 38)
    repaint(map.obj)
  elif (room == "tv_room"):
    copyColor(556, 65)
    repaint(map.obj)
  elif (room == "yard"):
    copyColor(596, 293)
    repaint(map.obj)
  else:
    repaint(map.obj)
    
    
def createIcon():
  #Takes the players color and creates the icon stored in player.icon
  src = makePicture(getMediaPath("dog.png"))
  src = scaleDown(src, 40)
  player.icon = src

  
def scaleDown(src, scaleFactor):
  newSize = makeEmptyPicture(getWidth(src)/int(scaleFactor), getHeight(src)/int(scaleFactor))
  sourceX = 0
  for x in range(0,getWidth(src)/scaleFactor):
    sourceY = 0
    for y in range(0, getHeight(src)/scaleFactor):
      setColor(getPixel(newSize, x, y), getColor(getPixel(src, sourceX, sourceY)))
      sourceY = sourceY + scaleFactor
    sourceX = sourceX + scaleFactor
  return newSize
  
  
  #Copys a chunk from one picture to another, also paints the whole thing to be copied to a unified color
def copyColor(locX, locY):
  #Copies from input picture from Start-end px and puts it to the target in corresponding location
  storeY = locY
  for x in range(0, getWidth(player.icon)):
    for y in range(0, getHeight(player.icon)):
      px = getPixel(player.icon, x, y)
      if (getRed(px) != 255) and (getGreen(px) != 255) and (getBlue(px) != 255):
        setColor(getPixel(map.obj, locX, locY), player.color)
      locY = locY + 1
    locX = locX + 1
    locY = storeY
    
def whiteout(room):
  locX = 0
  locY = 0
  if (room == "kitchen"):
    locX = 432
    locY = 288
  elif (room == "family_room"):
    locX = 338
    locY = 179
  elif (room == "yard"):
    locX = 596
    locY = 293
  elif (room == "tv_room"):
    locX = 556
    locY = 65
  elif (room == "bedroom"):
    locX = 377
    locY = 38
  else:
    locX = 0
    locY = 0
  storeY = locY
  for x in range(0, getWidth(player.icon)):
    for y in range(0, getHeight(player.icon)):
      px = getPixel(map.obj, locX, locY)
      setColor(px, white)
      locY = locY + 1
    locX = locX + 1
    locY = storeY