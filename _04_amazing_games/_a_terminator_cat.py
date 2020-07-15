import turtle
from PIL import Image

class Eye():
    def __init__(self, turtle=None, x=0, y=0, radius=30):
        self.turtle = turtle
        self.x = x
        self.y = y
        self.radius = radius
        
        self.turtle.penup()
        
    def draw(self):
        self.turtle.begin_fill()
        self.turtle.goto(self.x, self.y)
        self.turtle.circle(radius=self.radius, steps=20)
        self.turtle.end_fill()

def setBackground(filename):
    
    try:
        image = Image.open(filename)
    except:
        print( "ERROR: Unable to find file " + filename )
        return
    
    window.setup(image.width+100, image.height+100, startx=0, starty=0)
    window.bgpic(filename)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))

def keyPressed():
    print('You pressed the space key')
    
    # LASER BEAM.  This code will make your ellipse move down and to the right when you press 
    # the space bar. Run the program to test it.
    
    
    # 10. Increment the x and y variables of the 2 eye variables by 5:
    leftEye.x -= 5
    leftEye.y -= 5
    rightEye.x += 5
    rightEye.y -= 5
    
    # 11. Call the .draw() method for both eye variables.
    leftEye.draw()
    rightEye.draw()


if __name__ == '__main__':
    window = turtle.Screen()
    
    # 1. Find an image of a cat with BIG eyes OR use one of the 2 images provided
    #    a. Find an image using google to search. The image must be a .gif file
    #    b. Right click on the image and select 'Save image As'
    #    c. Rename the image something short (e.g. cat.gif)
    #    d. Save the image to your computer's desktop
    #    e. Drag and drop the image into your _04_amazing_games python package
    
    # 2. Call the setBackground() function with your variable inside of the parenthesis
    #    for example, setBackground(bgImage)
    setBackground("bigEyedCat2.gif")
 
    # 3. Make a new turtle
    nathanael = turtle.Turtle()
    
    # 4. Set the turtle color and pen color to red (or any color you want)
    #    using .color('red', 'red')
    nathanael.color("blue")
    
    # 5. Set the turtle width to 0 so no outlines are drawn
    nathanael.width(0)
    
    # 6. Set the turtle speed to 0 (fastest)
    nathanael.speed(0)
    
    # 7. Run the program and click on one of the cat's eyes. 
    #    The x,y position of the eye will be printed at the bottom of your processing window. 
    #    Variables for x and y have been created at the top of your sketch, 
    #    now you can set them equal to the values you just found. Watch for negative signs!
    
    
    # 8. After you've found the x and y for the eyes create 2 eye variables and initialize them:
    leftEye = Eye(turtle=nathanael, x=-47, y=54, radius=20)  
    rightEye = Eye(turtle=nathanael, x=4, y=49, radius=20)
    
    
    # 9. Call the .draw() method on both eye variables
    leftEye.draw()
    rightEye.draw()
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screenClicked)
    window.onkeypress(keyPressed, 'space')
    window.listen()
    turtle.done()
