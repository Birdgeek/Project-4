class game:
  state = "null"
  points = 0
  isRunning = false
  
class player:
  color ="null"
  name = "null"
  
  
def adventure():
  getInfo()
  game.isRunning = true
  game.state = "update"
  while (isRunning):
      if (game.state == "update"): #Update the map layout and inventory
        
def getInfo():
  text("Welcome to System Explorer! My name is Zod and I will guide you around \nFirst off, a few questions!")
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