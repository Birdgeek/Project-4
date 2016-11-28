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
  
def writeScore():
  file = open(getMediaPath("score.txt"), "wt")
  file.write(player.name + " - " + game.points)
  file.close()
  
def text(input):
  showInformation(input)
  
def updatePos():
  #Move player icon
  #Ask room specific questions
  
def updateInv():
  #Ask about picking up items within the room
  
def pickDirection():
  #pick a new direction based on the options available
  
def move():
  #Move the player icon to that new room
  
def countScore():
  #Add up the points for that room and then add them to the player score

def showEnd():
  #Shows stats and the final part of the adventure before exciting
  
def createIcon():
  #Takes the players color and creates the icon stored in player.icon
  src = makePicture(getMediaPath("dog.png"))
  scaleDown(src, 4)
  for px in getPixels(src):
    if (px.getBlue() == 0) and (px.getRed() == 0) and (px.getGreen() == 0)
      setPixelColor(px, player.color)
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