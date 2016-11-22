class game:
  state = None
  points = 0
  isRunning = false
  
class player:
  color =None
  name = None
  prevRoom = None
  currentRoom = None
  
class map:
  isCreated = false
  obj = None
  
def adventure():
  getInfo()
  game.isRunning = true
  game.state = "update"
  while (game.isRunning):
      if (game.state == "update"): #Update the map layout and inventory
          if (map.isCreated == false):
            map.obj= makePicture(getMediaPath("map.png"))
            show(map.obj)
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
  text("Welcome to Meta Explorer! My name is Zod and I will guide you around \nFirst off, a few questions!")
  player.name = requestString("What is your name?")
  player.color = requestString("Hello there, " + player.name +"!\nWhat color do you want to be? \nOptions are: Blue/Red/Green/Purple/Yellow")
  setPlayerColor()
  
def setPlayerColor():
  txtColor = player.color
  if (txtColor == "Blue") or (txtColor == "blue"):
    player.color = blue
  elif (txtColor == "Red") or (txtColor == "red"):
    player.color = red
  elif (txtColor == "Green") or (txtColor == "green"):
    player.color = green
  elif (txtColor == "Purple") or (txtColor == "purple"):
    player.color = makeColor()
  elif (txtColor == "Yellow") or (txtColor == "yellow"):
    player.color = makeColor()
  else:
    showError("None of the colors you entered were legit so now you're blue.\nHope you like it.")
    player.color = blue
  
def writeScore():
  file = open(getMediaPath("score.txt"), "wt")
  file.write(player.name + " - " + game.points)
  file.close()
  
def text(input):
  showInformation(input)