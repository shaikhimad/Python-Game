def start():
  answer = input("Are you ready for a challenge? (yes/no)")
  if answer == "yes":
    first()
  else:
    print("Should've known you'd chicken out!")

def first():
  answer1 = input("Gotcha! Now you are stuck in this maze >:D To escape you must remember these directions or else you will perish! It's pretty easy, all you have to do is go straight, left, straight, right, left, right, right, straight, left, right. Easy huh? Hope you can remember. One wrong turn and you will be swallowed up by the Maze Monster! Now, I'll let you peek on your first direction. Type in 'straight' to begin!")
  if answer1 == "straight":
    second()
  else:
    print("Really?... Looks like you were more dense than I thought! The Maze Monster will have a feast tonight, and YOU are on the menu!")
  
def second():
  answer2 = input("Congrats, if you had gotten that one wrong, you would have deserved to perish! Now, which way next? (left/right/straight)")
  if answer2 == "left":
    third()    
  else:
     print("tsk tsk tsk, could't even remember the first turn! Better watch out, the Maze Monster is hot on your tail and there's a dead end up ahead! HA!")

def third():
  answer3 = input("Good job, you went on the correct path. But don't celebrate just yet, there's a long ways to go! >:D Now, which way next? (left/right/straight)")
  if answer3 == "straight":
    fourth()
  else:
    print("Knew you didn't have it in you! Get ready to become monster chow!")

def fourth():
  answer4 = input("Not doing so bad I see! Now, which way next? (left/right/straight)")
  if answer4 == "right":
    fifth()
  else:
    print("Knew you wouldn't get the RIGHT answer, bwahahaha! Time to meet your maker! The Maze Monster should be here RIGHT about now hahaha!")

def fifth():
  answer5 = input("Right again! see what I did there? What? Just trying to be extra cheesey since you're bound to be a snack for the Maze Monster soon enough! Now, which way next? (left/right/straight)")
  if answer5 == "left":
    sixth()
  else:
    print("Ha! Too bad you didn't get it correct, I was starting to enjoy your company. But not as much as the Maze Monster will enjoy devouring you! Bwahahaha!")

def sixth():
  answer6 = input("Okay, okay, not bad. You may have gotten this one correct, but let's see how much further you can get! Now, which way next? (left/right/straight)")
  if answer6 == "right":
    seventh()
  else:
    print("WRONG! Say hi to the Maze Monster for me! Heard he's very playful... with his food! Bwahaahaha!")

def seventh():
  answer7 = input("Impressive.... NOT! Let's see if you can get further. Now, which way next? (left/right/straight)")
  if answer7 == "right":
    eight()
  else:
    print("So close, but you picked the wrong path! Prepare to be swallowed whole by the Maze Monster!")

def eight():
  answer8 = input("Nice work, let's hope your luck doesn't run out! Now, which way next? (left/right/straight)")
  if answer8 == "straight":
    ninth()
  else:
    print("Ha! I knew you didn't have it in you to find your way out! You found your way STRAIGHT into the Maze Monster's den! Bwahahaha!")

def ninth():
  answer9 = input("Amazing how far pure luck can get ya! But it won't get you to the end! Now, which way next? (left/right/straight)")
  if answer9 == "left":
    tenth()
  else: 
    print("You had me worried there. Thought you might have actually gotten to the end. But luckily, my Maze Monster will be well fed on this glorious day! Bwahahaha!")

def tenth():
  answer10 = input("Didn't expect you to get this far. But don't celebrate yet, you have one last hurdel before you reach the end, and I have a feeling you're luck will finally run out! Now, which way next? (left/right/straight)")
  if answer10 == "right":
    print("Wow... Can't believe you actually managed to get out of the Maze. My poor Maze Monster will stay hungry today and it's all your fault! >:( Well now that you're out here is your reward for risking your life, a gift card to olive garden. Be greatful. And, uh... Mind getting me a few bread sticks?")
  else:
    print("Almost is never enough. So close, yet so far away from escaping. You fumbled it up on the last path. Ha! Have fun being munched on by the Maze Monster!")

start()




