#begin
soccer_points = 0
Basketball_points = 0

#middle
answer = input ("on a weekend would you rather stay indoor A) or go outdoors or B ")
if answer == "A":
    Basketball_points += 1
elif answer =="B":
    soccer_points += 1
    

if Basketball_points > soccer_points:
    print("you are a Basketball person")
elif soccer_points > Basketball_points:
    print("you are a Soccer person")
elif Basketball_points == soccer_points:
    print (" You like Basketball or Soccer")


answer = input ("Bonce  A) or dribble or B ")
if answer == "A":
    Basketball_points += 1
elif answer =="B":
    soccer_points += 1


if Basketball_points > soccer_points:
    print("you are a Basketball person")
elif soccer_points > Basketball_points:
    print("you are a Soccer person")
elif Basketball_points == soccer_points:
    print (" You like Basketball or Soccer")


answer = input ("2k A) or FC25 or B ")
if answer == "":
    Basketball_points += 1
elif answer =="B":
    soccer_points += 1


if Basketball_points > soccer_points:
    print("you are a Basketball person")
elif soccer_points > Basketball_points:
    print("you are a Soccer person")
elif Basketball_points == soccer_points:
    print (" You like Basketball or Soccer")


answer = input ("Movie Hustle A) or Ted Lasso or B ")
if answer == "":
    Basketball_points += 1
elif answer =="B":
    soccer_points += 1


if Basketball_points > soccer_points:
    print("you are a Basketball person")
elif soccer_points > Basketball_points:
    print("you are a Soccer person")
elif Basketball_points == soccer_points:
    print (" You like Basketball or Soccer")


answer = input ("dumbbells A) or Treadmill or B ")
if answer == "":
    Basketball_points += 1
elif answer =="B":
    soccer_points += 1

#End
if Basketball_points > soccer_points:
    print("you are a Basketball person")
elif soccer_points > Basketball_points:
    print("you are a Soccer person")
elif Basketball_points == soccer_points:
    print (" You like Basketball or Soccer")