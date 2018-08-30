"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Russel Staples.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

a = rg.SimpleTurtle('turtle')
a.pen = rg.Pen('red', 1)
a.speed = 11

b = rg.SimpleTurtle('turtle')
b.pen = rg.Pen('blue', 2)
b.speed = 25

sizea = 250
sizeb = 30


a.right(90)
a.forward(200)
a.left(90)

b.left(270)
b.forward(100)
b.right(225)

for k in range(10):
    a.draw_circle(sizea)
    a.pen_down()
    sizea = sizea - 25

    b.draw_square(sizeb)
    b.pen_down()
    sizeb = sizeb + 25

window.close_on_mouse_click()