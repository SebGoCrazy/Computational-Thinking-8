###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
q1 = codesters.Square (100, 100, 200, 'black')
q2 = codesters.Square (-100, 100, 200, 'white')
q3 = codesters.Square (-100, -100, 200, 'black')
q4 = codesters.Square (100, -100, 200, 'white')


s1 = codesters.Sprite ("Franck", 100, 100)
s1. set_size(0.5)
s2 = codesters.Sprite ("Sarah", -100, -100)
s2. set_size(0.8)