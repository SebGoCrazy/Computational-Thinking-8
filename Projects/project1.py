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


s1 = codesters.Sprite ("Charel 1", 100, 100)
s1. set_size(0.05)
s2 = codesters.Sprite ("Charel 2", -100, -100)
s2. set_size(0.05)
s3 = codesters.Sprite ("Charel 3", 100, -100)
s3. set_size(0.2)
s4 = codesters.Sprite ("Charel 4", -100, 100)
s4. set_size(0.06)


message1 = codesters.Text("Sebastian Tay",0,220,"black")
message1 = codesters.Text("Charles",0,-220,"black")
