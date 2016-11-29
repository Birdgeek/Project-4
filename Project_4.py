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
  
  
class family_room:
  isOccupied = false

  
class bedroom:
  isOccupied = false
  
  
class kitchen:
  isOccupied = false
  
  
class tv_room:
  isOccupied = false
  
  
class yard:
  isOccupied = false
  
  
def adventure():
  getInfo()
  game.isRunning = true
  game.state = "update"
  while (game.isRunning):
      if (game.state == "update"): #Update the map layout and inventory
          if (map.isCreated == false):
            map.obj= makePicture(getMediaPath("map.png"))
            show(map.obj)
            paint("kitchen")
            player.currentRoom = "kitchen"
            player.prevRoom = "yard"
            map.isCreated = true
          else:
            updatePos()
            updateInv()
            game.state = "move"
      elif (game.state == "move"): #Have the player pick a direction and move the piece
          pickDirection()
          move()
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
  text("Welcome to Room Explorer! My name is Zod and I will guide you around!\nYou will explore this world from the viewpoint of a dog.\nFirst off, a few questions!")
  player.name = requestString("What is your name?")
  player.color = requestString("Hello there, " + player.name +"!\nWhat color  dog icon do you want to be? \nOptions are: Blue/Red/Green/Purple/Yellow")
  setPlayerColor()
  
  
def writeScore():
  file = open(getMediaPath("score.txt"), "wt")
  file.write(player.name + " - " + game.points)
  file.close()
  
  
def text(input):
  showInformation(input)
  
  
def updatePos():
  #Move player icon
  #Ask room specific questions
  None
  
def updateInv():
  #Ask about picking up items within the room
  None
  
  
def pickDirection():
  #pick a new direction based on the options available
  None
  
  
def move():
  #Move the player icon to that new room
  None
  
  
def countScore():
  #Add up the points for that room and then add them to the player score
  None
  
  
def showEnd():
  #Shows stats and the final part of the adventure before exciting
  None
    
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
  if (room == "kitchen"):
    print("painting kitchen")
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