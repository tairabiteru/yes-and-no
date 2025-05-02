"""
This file is a copy of the same file, but with comments.
I have left the original file in place as commenting this
out with some commentary on myself is going to be nigh on
impossible to do without reformatting it at least a little.
But of course, how a programmer structures their code speaks
volumes about them. As a result, the original file is preserved,
unaltered to view. This file instead will contain alterations in
spacing and styling as I deem necessary to provide commentary on
this code without having my eyeballs implode.

It also goes almost without saying but you should be aware that
every single one of the comments present in here are NOT part
of the original code. Commenting code was not a skill I possessed
when this was written, and if I'm being honest, I probably didn't
even think about it.

Anyway this file implements the 'choices game' apparently.
"""
import time
import sys
import random


"""
Great start with no snake_casing on variable names. Man, in retrospect
of course, but this whole repeated use of raw_input() to allow selection
between choices is gross. I mean, I suppose I didn't know there was
another option.

I also love the extensive use of globals, but my favorite part of this
has to be the fact that other than the order of the procedure, there's
absolutely no rhyme or reason to the order of this entire file.

Like, we print out the starting menu and then jump to defining global
variables, and then we define a function? But then we evaluate the results
of the start menu. If I had to guess, maybe I was like, "alright, we have
the start menu set up, now we have to evaluate it, but shoot, I'm repeating
myself a lot, so let's just throw a function down right before we do that."
It's almost like I was flying by the seat of my pants...probably because
I was.
"""
print "WELCOME TO THE CHOICES GAME!"
print "TYPE 'start' TO START, OR TYPE 'stop' TO EXIT!"
startvar = raw_input("(start/stop): ")

sleeper = "y"
devmode = "y"

def progexit():
    print "The program will exit in 15 seconds."
    print "You may also close it manually."
    time.sleep(15)
    sys.exit()

if startvar == "stop":
    print "Now exiting..."
    time.sleep(5)
    sys.exit()
elif startvar == "start":
    print "Let the game begin!"
    print ""
    print ""
    print ""
"""
Fucking excellent way to store a password. Super secure, 100% unhackable.
Want to store passwords securely? It's easy! Just type it out verbatim
in a fucking OPEN SOURCE PYTHON FILE.
"""
elif startvar == "1234":
    print "You've entered the password for developer mode!"
    print "Do you want to run the program in developer mode?"
    devmode = raw_input("Run in developer mode? (y/n): ")
else:
    """
    Mmm, so this is another interesting design decision. The program in a lot
    of places will either error out, or sass you when you type in an invalid
    selection. Probably because handling invalid selections using only
    conditionals feels comparable to swimming in a pool full of legos.
    """
    print "Seriously? You're gonna goof up your typing already?"
    print "Fine."
    print "Then I'm gonna close the program already."
    progexit()

"""
Ah, a bit of cleverness actually. Rather than having 80,000 if
statements all checking a variable whenever the program sleeps,
we write a function that does it for us!

I mean, it accesses a global variable, and is partly demonstrative
of why a class would perhaps be a better decision here, but hey: at
least it's not 80,000 if statements.

Also, why on earth do I not define this first? Like, this *could* be
used above in the start menu, but isn't because....??????????
"""
def sleep(t):
    if sleeper == "y":
        time.sleep(t)


"""
I bet I thought I was real funny writing this.
Also, the irony of calling the user 'incompetant' without 
actually spelling incompetent correctly is not lost on me.
"""
def error():
    print ""
    print "AN ERROR WAS ENCOUNTERED BECAUSE YOU ARE AN INCOMPETANT TYPIST."
    sleep(2)
    print "AS PUNISHMENT, THE PROGRAM WILL NOW END."
    sleep(2)
    print "..."
    sleep(3)
    print "ALSO YOU DIED."
    sleep(1)
    progexit()

if devmode == "y":
    sleeper = raw_input("Run with delay? (y/n): ")

r = random.randrange(1,11,1)

print "You awake in a dark and musty cave"
sleep(1)
print "You can barely see anything, but luckly you have a torch."

if devmode == "y":
    """
    Why in god's green earth do I fucking explain the inner workings of this
    shitty program here? My guy, it abstracts a dice roll with two possible
    outcomes, and you're basically in godmode. Why not just ask the user
    if they want to fucking blow up?
    """
    print ""
    print "You are in developer mode. Therefore, any random variables must be selected by you."
    print "The variable you must currently select is 'r'."
    print "'r' determines the amount of natural gas in the cave, and it's a value between 1-10."
    print "if r=1, then you will die upon igniting the torch."
    print "Additionally, you may type 'r' to randomly select a number."
    print "The random number will be displayed after you hit enter."
    r = raw_input("Select a value for 'r' (1-10): ")
    if r == "r":
        r = random.randrange(1,11,1)
        print r
    # THIS IS SUCH
    elif r == "1":
        r = 1
    elif r == "2":
        r = 2
    elif r == "3":
        r = 3
    # HOT.
    elif r == "4":
        r = 4
    elif r == "5":
        r = 5
    elif r == "6":
        r = 6
    # FUCKING.
    elif r == "7":
        r = 7
    elif r == "8":
        r = 8
    elif r == "9":
        r = 9
    # GARBAGE.
    elif r == "10":
        r = 10
    else:
        error()
    # Hey, 19 year old me: ever heard of fucking type casting?

"""
Excellent example of game design here, damned if you do, damned
if you don't. No skill involved at all, just 100% luck.
"""
i = raw_input("Light the torch? (y/n): ")
if i == "y" and r == 1:
    print ""
    print "The second you spark your lighter you're engulfed in flames."
    print "I guess there might've been gas in the cave."
    print ""
    print "YOU DIED."
    progexit()
elif i == "y":
    print "You light the torch."
    sleep(1)

elif i == "n":
    print ""
    print "..."
    sleep(3)
    print "Sooooooo...What are you just gonna wait here in the dark?"
    i = raw_input("(y/n): ")
    if i == "y":
        print "Fine....Have fun then...."
        sleep(3)
        print "..."
        sleep(3)
        print "..."
        sleep(3)
        print "YOU DIED OF BOREDOM."
        progexit()
    elif i == "n":
        print ""
        print "Well, you need to light the torch, or we can't move the plot along..."
        i = raw_input("(fine/NEVER): ")
        if i == "NEVER":
            print ""
            print "ALIRIGHT BUB, GIMME THE TORCH."
            sleep(2)
            print "You wrestle with your mind until exhaustion sets in."
            sleep(2)
            print "Eventually the exhaustion becomes too much for you to bear"
            sleep(2)
            print "YOU HAD A MENTAL BREAKDOWN IN A DARK CAVE ALONE."
            sleep(2)
            print "..."
            sleep(3)
            print "...AND THEN YOU DIED."
            progexit()
        elif i == "fine" and r == 1:
            # Hey bud, ever hear of DRY?
            print ""
            print "The second you spark your lighter you're engulfed in flames."
            print "I guess there might've been gas in the cave."
            print ""
            print "YOU DIED."
            progexit()
        elif i == "fine" and r != 1:
            print "You light the torch."
            sleep(1)
        else:
            error()
    else:
        error()
else:
    error()


"""
Lord, god forbid we have some kind of function or something that handles
output. Nah, we'll just write sleep(2) 700 times.
"""
print ""         
print "Suddenly the cave is illuminated completely, and the newfound light seems to hurt your eyes a bit."
sleep(2)
print "You start to feel cold."
sleep(2)
print "You should probably find a way to keep warm."
print "Perhaps you can start a small fire with your torch?"
print "You'll need to find some fuel though."
i = raw_input("Go find fuel? (y/n): ")
if i == "y":
    print ""
    print "You search for fuel, but unfortunately, you're in a cave."
    sleep(2)
    print "Not much in the way of fuel in caves..."
    sleep(2)
    print "You're persistant, however, and your search yields you............."
    sleep(3)
    print "Nothing."
    sleep(1)
    print "YOU DIED OF HYPOTHERMIA."
    progexit()
elif i == "n":
    print "Ok....So what do you plan to do? Burn the air?"
    print "Or are you just gonna sit and pout like a little baby?"
    i = raw_input("BURN/POUT: ")
    if   i == "BURN":
        print ""
        print "What are you talking about?"
        i = raw_input("(THIS/nothing): ")
        if i == "THIS":
            print ""
            print "You throw your torch against the ground"
            sleep(2)
            print "The flames ignite a nearby gas vent which causes a small explosion."
            sleep(2)
            print "You're knocked back against the wall, but you seem to be Ok."
            sleep(2)
            print "Now with the gas vent ignited, you have plenty of warmth, and you probably won't die of hypothermia. YAY!"
            sleep(1)
        elif i == "nothing":
            print ""
            print "Look, it you aren't going to help yourself, then I'm certainly not going to help you."
            sleep(2)
            print "Your mind seems to leave your body as your conscience disappears."
            sleep(2)
            print "This leaves you without a brain to think with...."
            sleep(2)
            print "YOU DIED BECAUSE YOUR BRAIN GOT FED UP WITH YOUR STUPIDITY."
            progexit()
        else:
            error()
    elif i == "POUT":
        print ""
        print "You know pouting won't help our situation at all..."
        sleep(2)
        print "Are you sure doing nothing is such a good idea?"
        i = raw_input("(y/n): ")
        if i == "y":
            print ""
            print "Fine. Freeze to death then."
            sleep(2)
            print "..."
            sleep(2)
            print "...and that's exactly what happened."
            sleep(1)
            print "YOU DIED BECAUSE YOU POUTED."
            sleep(2)
            print "AND SANTA GAVE YOU COAL."
            progexit()
        elif i == "n":
            print ""
            print "Good call."
            sleep(2)
            print "Suddenly, you accidentally drop your torch, and it rolls onto the ground to a nearby gas vent."
            sleep(2)
            print "The explosion sends you flying backwards, but other than a few bruises, you seem to be alright."
            sleep(2)
            print "What remains is a small fire fueled by the gas."
            sleep(2)
        else:
            error()
    else:
        error()
print ""
print "Now that you have a fire going, you'll need to find some food."
sleep(2)
print "You decide there are 3 options:"
sleep(2)
print "1. You can go and hunt for food."
sleep(2)
print "2. You can eat leaves off the ground in the cave."
sleep(2)
print "3. You can eat the rocks from the cave walls."
i = raw_input("Which one? (1/2/3): ")
if i == "1":
    print ""
    print "You decide hunting is the best option."
    sleep(2)
    print "As you exit the cave, the cave's entrance collapses."
    sleep(2)
    print "Unfortunately you were right underneath it."
    sleep(1)
    print "YOU DIED BECAUSE YOU GOT SMOOSHED."
    progexit()
elif i == "2":
    print ""
    print "You for some odd reason think that dead leaves will satisfy your hunger."
    sleep(2)
    print "Surprise surprise, they don't."
    sleep(2)
    print "But they do give you an idea."
    sleep(1)
    print "You decide to try to weave the fibers of the leaves into a twine."
    sleep(2)
    print "This twine may prove useful."
    sleep(2)
    print "What should you do with the twine?"
    i = raw_input("(EAT IT/make a bow): ")
    if i == "EAT IT":
        print ""
        print "You think that for some reason the twine will sate your hunger."
        sleep(2)
        print "It doesn't."
        sleep(1)
        print "And now you have no twine."
        sleep(2)
        print "You begin to feel weird in the stomach, and soon you feel pain."
        sleep(2)
        print "(Maybe it was something you ate?)"
        sleep(2)
        print "In any case, the twine caused an obstruction in your stomach."
        sleep(1)
        print "YOU DIED OF AN INTESTINAL BLOCKAGE."
        progexit()
    elif i == "make a bow":
        print ""
        print "You decide to make a bow out of the twine."
        sleep(2)
        print "You find a single stick on the ground. Sturdy, but flexible as well."
        sleep(2)
        print "The perfect kind for a bow."
        sleep(2)
    else:
        error()
elif i == "3":
    print ""
    print "You make way towards the cave wall, when you knock your head on an overhanging rock."
    sleep(2)
    print "This causes you to fall into a deep coma."
    sleep(2)
    print "..."
    sleep(2)
    print "You don't survive this."
    sleep(1)
    print "YOU DIED BECAUSE YOU ARE A MASSIVE KLUTZ."
    progexit()
else:
    error()
print ""
print "The way you see it now, you have 3 options:"
sleep(2)
print "1. You could go hunting with the bow."
sleep(2)
print "2. You could practice with the bow."
sleep(2)
print "3. You could eat the bow."
sleep(2)
i = raw_input("Which option? (1/2/3): ")
if i == "1":
    print ""
    print "You decide hunting is the best option."
    sleep(2)
    print "As you exit the cave, the cave's entrance collapses."
    sleep(2)
    print "Unfortunately you were right underneath it."
    sleep(1)
    print "YOU DIED BECAUSE YOU GOT SMOOSHED."
    progexit()
elif i == "2":
    print ""
    print "You decide to try to practice with the bow."
    sleep(2)
    print "You pick up an inexplicably placed arrow on the ground, and draw your bow."
    sleep(2)
    print "*THWACK*"
    sleep(1)
    print "The arrow strikes the wall of the cave."
    sleep(2)
    print "This causes the cave entrance to collapse."
    sleep(2)
    print "It's a good thing you didn't try to exit the cave!"
    sleep(2)
elif i == "3":
    print ""
    print "You decide to eat the bow."
    sleep(2)
    print "..."
    sleep(3)
    print "And you thought this was a good idea why?"
    sleep(2)
    print "YOU DIED OF AN INTESTINAL BLOCKAGE."
    progexit()
else:
    error()
print ""
print "You see a small opening in the rubble from the collapse that you can squeeze through."
sleep(2)
print "You decide to go outside of the cave for the first time."
sleep(2)
print "Once outside, you look around and find yourself in a beautiful forest."
sleep(2)
print "Once again you're presented with three options:"
sleep(2)
print "1. You can go hunting"
sleep(1)
print "2. You can take a look around"
sleep(1)
print "3. You can do a whale call"
i = raw_input("(1/2/3)")
if i == "1":
    print ""
    print "You decide to go hunting"
    sleep(2)
    print "You find a bush, and hide in it, bow drawn, waiting for something to come along"
    sleep(2)
    print "Unfortunately it seems as though nothing is coming along."
    sleep(2)
    print "You become impatient, and begin to fiddle around with the bow while waiting"
    sleep(2)
    print "Suddenly, you accidentally shoot the arrow, and it flies off into the trees."
    sleep(2)
    print "While looking for the arrow, a heard of deer run past you. Maybe 20-30 deer."
    sleep(2)
    print "You can't even believe your own misfortune."
    sleep(2)
    print "Nothing else ends up coming along. It doesn't matter because you couldn't find your arrow anyway"
    sleep(2)
    print "YOU DIED OF YOUR INCREDIBLE MISFORTUNE."
    progexit()
elif i == "3":
    print ""
    print "You decide to do a whale call."
    sleep(2)
    print "The whale call doesn't sit well with some nearby bears."
    sleep(2)
    print "YOU DIED BECAUSE YOU DID A WHALE CALL IN THE MIDDLE OF A FOREST."
    sleep(2)
    print "SERIOUSLY. ARE YOU THAT STUPID?"
    progexit()
elif i == "2":
    print ""
    print "You decide to take a look around."
    sleep(2)
    print "Almost immediately you find a plant bearing fruit."
    sleep(2)
    print "It has red berries with some purple and yellow flowers."
    sleep(2)
    print "Will you eat them?"
    i = raw_input("(y/n): ")
    if i == "y":
        print ""
        print "You decide to eat the berries."
        sleep(2)
        print "They sate your hunger."
        sleep(2)
        print "..."
        sleep(2)
        print "For a while."
        sleep(1)
        print "It isn't long before you have huge stomach pains, and you start to have delusions."
        sleep(2)
        print "Turns out, those berries were from the Deadly Nightshade plant."
        sleep(2)
        print "YOU DIED BECAUSE YOU DIDN'T PAY ATTENTION IN PLANT TAXONOMY CLASS."
        progexit()
    elif i == "n":
        print ""
        print "You decide not to eat those berries."
        sleep(2)
    else:
        error()
    print "You walk a bit further and come across a weird thorny plant with oddly shaped whitish red flowers."
    sleep(2)
    print "The flowers seem to have multiple tiny petals, and it's unlike any plant you've seen before."
    sleep(2)
    print "The berries are a deep red with lots of bumps, and they seem hairy."
    sleep(2)
    print "Will you eat them?"
    i = raw_input("(y/n): ")
    if i == "y":
        # Whoa, declaring variables is a little advanced, isn't it?
        raspberries = 1
        print ""
        print "You eat the berries."
        sleep(2)
        print "..."
        sleep(2)
        print "The taste...It's familiar..."
        sleep(2)
        print "It's...It's..."
        sleep(2)
        print "RASPBERRIES!"
        sleep(1)
        print "You heartily pick most of the berries off of the bush and gobble them down."
        sleep(2)
        print "Luckly, there are a dozen such bushes, so at least for now, you have food."
    elif i == "n":
        raspberries = 0
        print ""
        print "You decide not to eat them."
    else:
        error()
    # Also if all I do is use it here, why don't I just use a boolean?
    if raspberries == 0:
        print ""
        print "You next come across a bush with three leaves on it's stem."
        sleep(2)
        print "It doesn't have any fruit, but at this point, the hunger is making you dizzy."
        sleep(2)
        print "The leaves are a deep green, like a spinich plant."
        sleep(2)
        print "Will you eat it?"
        i = raw_input("(y/n): ")
        if i == "y":
            print ""
            print "You decide to eat the leaves."
            sleep(2)
            print "You regret this only 30 seconds after consuming them as your hands and mouth begin to itch like crazy."
            sleep(2)
            print "It's immediately apparent what you just ate:"
            sleep(2)
            print "Poison Ivy."
            sleep(1)
            print "Eventually your stomach begins to itch as well, and your entire body is consumed by itching."
            sleep(2)
            print "YOU DIED OF EXCESSIVE INTERNAL ITCHING."
            progexit()
        elif i == "n":
            print ""
            print "You decide not to eat the leaves."
            sleep(2)
            print "Unfortunately you don't find anything else to eat."
            sleep(2)
            print "You eventually succumb to hunger."
            sleep(2)
            print "YOU DIED OF HUNGER."
            progexit()
        else:
            error()
else:
    error()


"""
It is at this point that I started to realize that none of what I just wrote
is sustainable in the long term, so I guess it's time to learn about functions.
"""
def option1():
    print ""
    print "You go back to your cave to find that it has collapsed."
    sleep(2)
    print "If it collapsed that easily, it probably wasn't a good idea to stay in it anyway."
    sleep(2)
    print ""
    print "Well, you have three options left:"
    sleep(2)
    print "2. You can build a small lean-to out of sticks and leaves."
    sleep(1)
    print "3. You can dig a hole in the ground and live in that."
    sleep(1)
    print "4. You could do the same as option 2, but reinforce it by weaving twine. This will take considerably longer."
    i = raw_input("(2/3/4): ")
    if i == "2":
        option2()
    elif i == "3":
        option3()
    elif i == "4":
        option(4)
    elif i == "1":
        triedagain()
    else:
        error()
        

def option2():
    print ""
    print "You decide to build a small lean-to."
    sleep(2)
    print "This will take you some time..."
    sleep(2)
    print "..."
    sleep(2)
    print "..."
    sleep(2)
    print "..."
    sleep(2)
    print "..."
    sleep(2)
    print "DONE!"
    # And learn about the concept of namespaces too,
    # only to completely stamp all over them.
    global house_type
    house_type = "leanto"
"""
I remember specifically being really frustrated by the fact that I have to type
'global' over and over in order to access house_type and thought it was stupid.

AS IF WRITING sleep(2) A MILLION TIMES OVER ISN'T.
"""

def option3():
    print ""
    print "You decide to dig a hole in the ground."
    sleep(2)
    print "This digging only takes a minute, as the soil is soft and somewhat sandy."
    sleep(2)
    print "..."
    sleep(3)
    print "DONE!"
    sleep(1)
    print "Not the most comfortable thing in the world, but homely!"
    sleep(2)
    global house_type
    house_type = "hole"
    

def option4():
    print ""
    print "You decide it would be best to build a strong and sturdy house out of twine and sticks."
    sleep(2)
    print "This will take you a while..."
    sleep(10)
    print "..."
    sleep(10)
    print "..."
    sleep(10)
    print "..."
    sleep(2)
    print "DONE!"
    sleep(1)
    print "Now, THIS is a house."
    sleep(2)
    print "It's well built, and has a nice roof. You've even made yourself a nice area to sleep in."
    sleep(2)
    global house_type
    house_type = "goodleanto"

def triedagain():
    print ""
    print "So you STILL insist on going in the cave..."
    sleep(2)
    print "Let me make it clear:"
    sleep(2)
    print "You CANNOT go back in the cave."
    sleep(2)
    print "It's gone."
    sleep(1)
    print "Get over it."
    sleep(1)
    print "Now, which option are you going to choose?"
    i = raw_input("(2/3/4): ")
    if i == "2":
        option2()
    elif i == "3":
        option3()
    elif i == "4":
        option4()
    elif i == "1":
        print ""
        print "FINE. HAVE YOUR STUPID CAVE THEN."
        sleep(2)
        print "You never do get into the cave."
        sleep(2)
        print "Maybe you should've listened to the voice of reason."
        sleep(2)
        print "YOU DIED BECAUSE YOU LISTENED TO THE VOICE OF IGNORANCE."
        progexit()
    else:
        error()
    
print ""
print "Now that your hunger is satisfied, you think it's time to get some shelter."
sleep(2)
print "You consider four options:"
sleep(1)
print "1. You can go back to the cave."
sleep(1)
print "2. You can build a small lean-to out of sticks and leaves."
sleep(1)
print "3. You can dig a hole in the ground and live in that."
sleep(1)
print "4. You could do the same as option 2, but reinforce it by weaving twine. This will take considerably longer."
sleep(2)
i = raw_input("(1/2/3/4): ")
if i == "1":
    option1()
elif i == "2":
    option2()
elif i == "3":
    option3()
elif i == "4":
    option4()
else:
    error()

print ""
print "Now that you have a shelter, you create a small campfire, with wood on the ground."
sleep(2)
print "You use your torch (which you still have, by the way) to light the fire."
sleep(2)
print "The fire begins burning immediately, as it seems you've found some nice dry wood."
sleep(2)
print "Unfortunately it seems as though a storm is brewing."
sleep(2)
print "You stow away some wood and quickly get into your house."

"""
Oh good, more RNG that you can't do anything about. I'm also about 95% sure
that I had no intentions of having which shelter you build affect anything at all
other than braving the storm or not. So like...you could just always build the
strongest one. The only downside is that you have to wait longer. Like, literally,
the game sleeps for longer, and it's like, 30 seconds or some shit.

I don't need to say it, but that's horrendously stupid.
"""
storm_intensity = random.randrange(1,11,1)

if devmode == "y":
    print ""
    print "You are in developer mode."
    print "You may now select a number for the variable storm_intensity."
    print "It is a random variable 1-10. Please type the number, and hit enter,"
    print "or type 'r' for a random number"
    print "The value of the variable will be printed after it is selected."
    si = raw_input("Select a value for storm_intensity (1-10): ")
    if si == "r":
        r = random.randrange(1,11,1)
        print r
    elif si == "1":
        storm_intensity = 1
    elif si == "2":
        storm_intensity = 2
    elif si == "3":
        storm_intensity = 3
    elif si == "4":
        storm_intensity = 4
    elif si == "5":
        storm_intensity = 5
    elif si == "6":
        storm_intensity = 6
    elif si == "7":
        storm_intensity = 7
    elif si == "8":
        storm_intensity = 8
    elif si == "9":
        storm_intensity = 9
    elif si == "10":
        storm_intensity = 10
    else:
        error()
    print "storm_intensity=", storm_intensity

if house_type == "leanto" and (storm_intensity >= 3 and storm_intensity <= 5):
    print ""
    print "The storm certainly isn't the worst you've ever seen."
    sleep(2)
    print "Unfortunately your little lean-to isn't strong enough to bear the force of the winds."
    sleep(2)
    print "Your house is knocked down, and you begin to bear the full force of the winds,"
    sleep(2)
    print "which from what you can tell are anywhere between 30-50 miles per hour."
    sleep(2)
    print "You may have survived were it not for the fact that it was also a cool 40 degrees."
    sleep(2)
    # 2009 called, they want their shitty meme back.
    print "DAT WINDCHILL."
    sleep(1)
    print "YOU DIED OF HYPOTHERMIA."
    progexit()
    """
    Also it's secondary to the programming aspect of this, but dying from
    wind chill due to a storm that is apparently also capable of spawning
    tornadoes doesn't make any fucking sense. I don't know what season I thought
    it was in the context of this game, but it doesn't match any season I've
    seen on earth, that's for sure...

    ...well, okay, maybe it kind of resembles Spring in Michigan.
    """
elif house_type == "leanto" and (storm_intensity > 5 and storm_intensity <= 7):
    print ""
    print "The storm is pretty bad."
    sleep(2)
    print "Within the first few minutes, your house is whipped away by gale force winds of up to 70 miles per hour."
    sleep(2)
    print "The debris battered your face constantly, and you managed to survive this."
    sleep(2)
    print "You did NOT however manage to survive the 30 degree windchill brought by the storm."
    sleep(2)
    print "YOU DIED OF HYPOTHERMIA."
    """
    But ok, like, wind chill isn't even defined for temperatures above 50 degrees F.
    So let's be conservative here and assume this storm - capable of spawning tornadoes,
    mind you - is somehow forming at 50 F. What wind speed is required at that temperature
    to produce wind chill values of 30 degrees F?

    I don't know is the answer, but it's greater than 110 mph, because the wind chill in
    110 mph winds at 50 F is only 36 degrees.

    Like, either the game changes seasons randomly (in which case explain the presence
    of the fucking raspberries above) or this storm is inconsistent with meteorological
    science. Alternately, the correct answer: it's bullshit, and I thought none of this through.
    """
    progexit()
elif house_type == "leanto" and (storm_intensity > 8):
    print ""
    print "The storm is really bad."
    sleep(2)
    print "The winds reach speeds as high as 90 miles per hour."
    sleep(2)
    print "Although you suvive the initial battery, you certainly aren't unscathed."
    sleep(2)
    print "It seems your lean-to faired much worse. It was ripped apart by the wind."
    sleep(2)
    print "You suddenly hear the sound of what seems to be a freight train."
    sleep(2)
    print "Perhaps there's a railroad nearby."
    sleep(2)
    print "Perhaps you can find your way back to civilization."
    sleep(2)
    print "..."
    sleep(2)
    print "LOL NO."
    sleep(1)
    print "It's a tornado."
    sleep(2)
    print "People talk of mysterious stories of eggs and stuff getting picked up by tornadoes,"
    sleep(2)
    print "and being carefully placed back down."
    sleep(2)
    print "As far as you now know, these stories are full of crap."
    sleep(2)
    print "Because you died."
    sleep(1)
    print "YOU DIED BECAUSE A BIG MEAN SCARY TWEESTUR GOBBLED YOU UP."
    progexit()
elif house_type == "leanto" and (storm_intensity < 3):
    print "The storm is weak."
    sleep(2)
    print "Your little lean-to gets weathered a little bit, but ultimately, it survives."
    sleep(2)
    print "And you do as well."
    sleep(2)
    print "Although you definitely got lucky."
elif house_type == "goodleanto" and (storm_intensity >= 8):
    print ""
    print "The storm is really bad."
    sleep(2)
    print "The winds reach speeds as high as 90 miles per hour."
    sleep(2)
    print "Although you survive the initial battery, you certainly aren't unscathed."
    sleep(2)
    print "And although it put up a fight, your reinforced lean-to didn't make it."
    sleep(2)
    print "You suddenly hear the sound of what seems to be a freight train."
    sleep(2)
    print "Perhaps there's a railroad nearby."
    sleep(2)
    print "Perhaps you can find your way back to civilization."
    sleep(2)
    print "..."
    sleep(2)
    print "LOL NO."
    sleep(1)
    print "It's a tornado."
    sleep(2)
    print "People talk of mysterious stories of eggs and stuff getting picked up by tornadoes,"
    sleep(2)
    print "and being carefully placed back down."
    sleep(2)
    print "As far as you now know, these stories are full of crap."
    sleep(2)
    print "Because you died."
    sleep(1)
    print "YOU DIED BECAUSE A BIG MEAN SCARY TWEESTUR GOBBLED YOU UP."
    progexit()
elif house_type == "hole" and (storm_intensity >= 8):
    print ""
    print "You're sitting inside your hole waiting for the storm to pass."
    sleep(2)
    print "Luckly, there doesn't seem to be much rain, so your hole's walls seem to stay sturdy."
    sleep(2)
    print "Outside you can hear the sound of an approaching freight train."
    sleep(2)
    print "Wait...FREIGHT TRAIN?"
    sleep(2)
    print "That's no freight train...IT'S A TORNADO."
    sleep(2)
    print "Fear immediately strikes your heart as you realize your life is in grave danger."
    sleep(2)
    print "However, all you can do is sit and wait..."
    sleep(2)
    print "...You black out..."
    sleep(4)
    print "When you wake up, you find yourself still in your hole. You peek out of the hole and see a bunch of downed trees."
    sleep(2)
    print "Now you're certain. A tornado DEFINITELY came through here."
    sleep(2)
    print "It's a good thing you chose to dig a hole. Anything else would've been absolutely obliterated."
    sleep(2)
elif house_type == "hole" and (storm_intensity < 8):
    print ""
    print "Immediately as the storm starts, the ground above begins to flood."
    sleep(2)
    print "The water softens the already soft dirt, which causes the hole to collapse."
    sleep(2)
    print "Although you survive the collapse, you don't survive the blistering cold windchill."
    sleep(2)
    print "YOU DIED OF HYPOTHERMIA."
    progexit()
elif house_type == "goodleanto" and (storm_intensity >= 5 and storm_intensity <= 7):
    print ""
    print "The storm is pretty bad."
    sleep(2)
    print "The wind speeds are anywhere between 50 to 70 miles per hour."
    sleep(2)
    print "It's something a normal lean-to wouldn't withstand..."
    sleep(2)
    print "Luckly, your lean-to is a SUPER-LEAN-TO."
    sleep(2)
    print "Your lean-to successfully endures the storm, albeit a bit battered."
    sleep(2)
elif house_type == "goodleanto" and (storm_intensity < 5):
    print ""
    print "The storm isn't the worst thing in the world."
    sleep(2)
    print "Still, the winds gust up to 40 miles per hour."
    sleep(2)
    print "Fortunately, they're no match for your SUPER-LEAN-TO!"
    sleep(2)
    print "Your lean-to easily endures the storm."
    sleep(2)
else:
    """
    Or you could, I don't know, write some tests to see if there is a
    condition under which this can happen, and then omit the else statement
    here. But nah, we'll just throw the burden onto the user.
    """
    print "IF YOU HAVE GOTTEN THIS MESSAGE, THIS MEANS YOU'VE SOMEHOW GOTTEN THROUGH THE STORM"
    print "DETECTION MODULE. PLEASE REPORT THIS TO THE DEVELOPER IMMEDIATELY."
    print "PLEASE PRESENT THE FOLLOWING INFORMATION:"
    print "house_type=", house_type
    print "storm_intensity=", storm_intensity
    stop = raw_input("Press enter to stop the program")
    sys.exit()
print ""
print "Now that the storm has subsided, you need to decide what to do next."
sleep(2)

"""
Yes, the storm has subsided, and what I decide to do next is quit writing
this garbage. I have thought to myself multiple times while writing these comments,
"I wonder if I could go back and rewrite this using the skills I have now. What would
it look like?"

Here's the thing: I don't think I will. At the end of the day, as interesting as it 
might be, I don't think it's even worth doing. Bad code or not, the game's fundamental
concept is bad, and it's flat out not fun to play. But at the very least,
it's been interesting to see how much progress I've made.
"""



    


