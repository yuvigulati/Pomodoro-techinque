import random
from tkinter import *          #don't import like this except for Tkinter
root = Tk() #create main window
root.title('Atarashi Sozo')
# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.grid() #Puts the canvas in the main Tk window

#Create lists
creature = ['is an Animal', 'is a Human', 'is an Artificial Intelligence',
        'is an Alien', 'is a Mage','is a Reptillian','is a Shapeshifter',
        'is Undead', 'is a Scorpion Hedgehog', 'is an Angel', 'is a Demon']
element = ['controls lightning', 'controls fire', 'controls nature','controls water', 'controls mater', 'controls time', 'controls gravity', 'controls life', 'controls     death', 'controls wind',
       'can bend any metal','controls the sun', 'controls the moon', 'controls love']
features = ['has wings', 'has markings', 'has large fangs', 'has claws', 'has a tail', 'has a weapon',
        'has cybernetic parts', 'has wolf ears', 'has broken teeth', 'has a horn', 'has big ears',
        'has eyes with two colors', 'has a mp3']
wildcard = ['is cursed', 'is bewitched', 'has no soul', 'killed someone', 'just learned magic',
        'has no wifi', 'has unlimited memory', 'is poor', 'won the lottery', 'set the world on fire', 'visited another dimension']
colors = ['is primarily blue', 'is primarily grey', 'is primarily red', 'is primarily green', 'is primarily orange',
      'is secondarily blue', 'is secondarily grey', 'is secondarily red', 'is secondarily green', 'is seconarily orange',
      'is primarily black', 'is primarily purple', 'is secondarily purple', 'has all the colors of the rainbow']
handicap = ['is blind', 'is deaf', 'lost limbs', 'fears everything', 'has broken bones','has a small head','has an illness',
        'has amnesia', 'is allergic to almost everything', 'is deformed']
habitat = ['lives in cyberspace', 'lives in a desert', 'lives in the mountains', 'lives in a volcano', 'lives in grasslands',
        'lives on the moon', 'lives in space', 'lives on a deserted island', 'lives in a virtual world', 'lives in the underworld']
personality = ['is clingy', 'is depressed', 'is energetic', 'is angry', 'is kind', 'is a jerk', 'is goofy', 'is immature', 'is happy',
           'is insane']
profession = ['is a teacher', 'is an assassin', 'is a graphic designer', 'is a programmer', 'is a photographer', 'is a blacksmith',
          'is a bounty hunter', 'is an inventor', 'is a mage', 'is a monster hunter']
hobby = ['likes to cook', 'likes to draw and paint', 'likes to build things', 'likes to play games', 'likes to shop',
     'studies alchemy', 'likes to write', 'likes to make music', 'likes to design', 'likes sports']
#Sets categories to choose from
categoryList = [hobby,profession,personality,habitat,handicap,colors,wildcard,features,element]
#Removes category from list if it has been choosen to remove the possibility of duplicates
catOne = random.choice(categoryList)
if catOne in categoryList: categoryList.remove(catOne)
catTwo = random.choice(categoryList)
if catTwo in categoryList: categoryList.remove(catTwo)
catThree = random.choice(categoryList)
if catThree in categoryList: categoryList.remove(catThree)
#Chooses item from category choosen
itemOne = random.choice(catOne)
itemTwo = random.choice(catTwo)
itemThree = random.choice(catThree)

#Creates the main visual almost the same as Atarashi Sozo in App Inventor
Title_box = canvas.create_rectangle(500, 90, 100, 18, outline = 'purple',width = 10, fill = 'violet')
Title_text = canvas.create_text(300, 50, text='Your Character', font=('Impact', -50))
Display_box1 = canvas.create_rectangle(600, 200, 8, 125, outline = 'blue', width = 10, fill = 'sky blue')
Label1 = canvas.create_text(300, 160, text=random.choice(creature), font=('Impact', -30,))
Display_box2 = canvas.create_rectangle(600, 300, 8, 225, outline = 'red', width = 10, fill = 'pink')
Label2 = canvas.create_text(300, 260, text=itemOne, font=('Impact', -30))
Display_box3 = canvas.create_rectangle(600, 400, 8, 325, outline = 'goldenrod', width = 10, fill = 'gold')
Label3 = canvas.create_text(300, 360, text=itemTwo, font=('Impact', -30))
Display_box4 = canvas.create_rectangle(600, 500, 8, 425, outline = 'saddle brown', width = 10, fill = 'chocolate')
Label4 = canvas.create_text(300, 460, text=itemThree, font=('Impact', -30))

#Create dummy button
class Outcomes(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.button = Button(self, text = 'Generate Character')
        self.button['command'] = self.print_text
        self.button.grid()
    def print_text():
        print
app = Outcomes(root)

# Enter event loop. This displays the GUI and starts listening for events.
# The program ends when you close the window.
root.mainloop()

# Timer mechanism





