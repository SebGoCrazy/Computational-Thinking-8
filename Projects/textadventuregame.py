#INTRO
print("You're a deep sea diver working on the coast of California.")
print("A full moon shines in the starry abyss, shining a bit of light onto your boat.")
print("You gaze out to the open sea, watching the moon glint on the rolling waves. Oh, right. It's almost time for your dive, you remind yourself.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Choice 1
c1 = input("Do you jump straight into the sea or check your gear first?")
if "jump" or "sea" in c1:
    print("You gaze over the edge of your boat, using a hand to check your air tank. 'All set,' you say. You jump into the sea, water quickly rushing to cover you.")
else:
    print("You turn back to your boat, checking oxygen canisters and navigation equipment. Once you've double- yes, even triple checked, you jump straight into the sea, water rushing to cover you.")

#Part 2
print("As you sink through the depths of the ocean, the light coming from above quickly dims. After a few minutes, you touch down on a outcrop.")
print("You look around, and much to your surprise, a mermaid like elfling creature swims up from the depths to you.")
print("'Wait!' It says, holding its hands up. 'I'm a peace ambassador. Just- you're a diver, right?'")
print("You nod your head.")
print("'Oh- oh, good. Listen, you don't know who I am, but- my people, we need your help.'")
c2 = input("The aquatic elf floats, waiting for your response. Do you [help] him or do you [run away]?")
if "help" in c2:
    print("You can immediately see relief wash over the elf's face as you agree. He quickly reaches out to you, tugging on you gently.")
    print("'Thank you so, so much. Please, come with me.' He says. You eventually relent to his tugs, letting him take you down through the ocean depths.")
    print("As you float through the sea, lights begin to pop up from the lightless void. Much to your surprise, a city lays beneath the waves.")
    print("The aquatic elf leads you to a small hut, adorned by large, glowing pearls. 'This is the most we can provide for you right now. I hope it's enough.' The elf turns to leave, letting you explore the hut. Before he leaves, he turns.")
    print("'My name is Adonis, by the way.'")
    c4 = input("You look around in your new...settlement. Due to some enchantment, in this space you can breathe and exist in the sea without a suit. More comfortable, you decide to look around the room. Do you look through the [bookshelf], check the [floorboards}, or check the [bed]?")
    if "book" in c4:
         print("You feel through the books, pulling some out to check titles. By chance, pulling a book happens to open a trapdoor next to your feet. You startle, moving back a bit.")
    elif "floor" in c4:
        print("You feel through the floorboards. Some are old, weathered by time, but some are perfect. You decide they must've renovated the place.")
    else:
        print("You hop on the bed. It's a bit creaky, but the sheets are nice and soft. Some of the blankets display old symbols of mermaids, from thousands of years ago. How long have they been waiting for a human?")

#BAD ENDING
else:
    print("The elf looks...startled. His face twists with emotions, before he settles to a terrifyingly blank face.")
    print("'I'm sorry, I- I didn't want it to come to this.")
    print("The elf lunges forward, leaving you only a slim second to dodge him. Where you just were, he slashes through the water. Terrified, you turn your back to him and begin desperately swimming towards the surface.")
    c5 = input("As you swim, you can see him gaining ground on you. As you desperately kick your feet, you know you have two options. To throw him off, you can either throw the [flashlight] or the [stopwatch].    ")
    if "flash" or "light" in c5:
        print("Ripping the attachment cord off the flashlight, you hit the on button and toss it down towards your attacker.")
        print("As it falls through the water, the beam of light spins erratically.")
        print("As it nears the elf, it spins, hitting him with a beam of light in the face.")
        print("He shrieks, bubbles exploding from his mouth. You can hear hisses and whines as he descends back into the depths.")
        print("Taking one last look, you can see that his face has burns and boils on it.")
        print("You finish the trek back to the surface, your sides heaving as you haul yourself onto the boat.")
        print("Collapsing onto the boat, you rip your gear off.")
        print("               ")
        print("..What just happened?")
    else:
        print("You rip the stopwatch off your wrist and send it hurtling through the water.")