#Week 4 Programming Assignment
#North Seattle College, CSC 110
#Author: Micah Hogan
#Email: hogan.micah.j@gmail.com


#Constants
#Initial User Input
name = str(input("Please select a name: "))
print("")
mount = str(input("Please select an animal to ride: "))
print("")
weapon = str(input("Please select a weapon: "))
print("")
role = str(input("Please select a role; (Sorcerer), (Brawler), or (Priest): "))
print("")
while not(role == "Sorcerer" or role == "Brawler" or role == "Priest"):
    print ("Please select (Sorcerer), (Brawler), or (Priest).")
    print("")
    role = str(input("Please select a role; (Sorcerer), (Brawler), or (Priest): "))
    print("")
race = str(input("Please select a race; (Human), (Elf), or (Troll): "))
print("")
while not(race == "Human" or race == "Elf" or race == "Troll"):
    print("Please select (Human), (Elf), or (Troll).")
    print("")
    race = str(input("Please select a race; (Human), (Elf), or (Troll): "))
print("")

#Main function
#This function guides the user through a choose-your-own adventure style story
#The story has different outcomes based on the user's choices

def main ():
        
#Output
#This is introductory flavor text based on the constants created by intial user input
#This text creates the setting and style for the story
#After the introductory flavor text, this function calls the first function which requires a decision from the user, wake_up_groggy
    
    if race == "Human":
        print("You have selected "+race+".  While perhaps not the most exciting choice, it does sound safe.")
        print("")
    elif race == "Elf":
        print("You have selected "+race+".  You begin to feel as one with the Earth as a tiny charm of hummingbirds works together in concert to lower a crown made of thistle and ivy upon your head.")
        print("")
    else:
        print("You have selected "+race+". Your features and appendages begin to swell as your skin thickens and becomes cracked and leathery with a distinct green hue.")    
        print("")
    if role == "Sorcerer":
        print("You have selected "+role+".  You put on your pointy hat, mutter something unintelligble and wiggle the fingers attached to your gangly arms poking out of the billowy sleeves of your long, flowing robe.")
        print("")
    elif role == "Brawler":
        print("You have selected "+role+". You clench your jaws and cock your head to the side as you crack your knuckles loudly.")
        print("")
    else:
        print("You have selected "+role+". A heavenly aura envelops you as your hands begin to pulse with a glowing warmth.")
        print("")

    print("Welcome to Arcana, "+name+", the land of fantasy and adventure!")
    print("")
    print("So, "+name+", you've been training as a "+role+"?  We'll see if that helps you while you're here... In any case, be sure to always keep your "+weapon+" with you.  It's your only means of protecting yourself.")
    print("")
    print("Lastly, "+name+", I've rounded up the largest, strongest and most well-trained "+mount+" I could find for you to ride.  It's being fitted in the stables for a saddle right now. Have fun, and happy adventuring, "+ name+"!")
    print("")
    wake_up_groggy()
    
#This function begins the adventure story, and serves as the restarting function if the user fails to win the game
#This function invites the user to go for a ride on their mount after waking up groggy and requires an answer of (yes) or (no) from the user
#This function calls one of two functions based on the answer: upset_stomach_story and breakfast_invitation, each of which begin either a questline or another decision

def wake_up_groggy():
    print("")
    print("You slowly begin to awaken, your body sore from the prior evening, but your memory is fuzzy.  You're unsure how you've arrived in the corner of the bazaar you've woken up in, bustling with the sounds of morning commerce. It's clear to you that you've spent the night here, but you have no memory of arriving the prior evening. You check your knapsack for your "+weapon+", relieved to find it in it's place.  A noise behind you startles you, and you whip your head around only to find yourself face-to-face with your trusty "+mount+", who proceeds to sloppily and lovingly lick your face. You sense that it is eager for some exercise as it nuzzles it's saddle.")
    print("")
    ride_choice = str(input("Would you like to go for a ride? "))
    while not(ride_choice == "yes" or ride_choice == "no"):
        print("")
        print ("Please choose (yes) or (no).")
        print("")
        ride_choice = str(input("Would you like to go for a ride? "))
    if ride_choice == "yes":
        print("")
        print("You laugh as your "+mount+" tickles your nose with his tongue.  ‘Ok, ok. I get it! You want to go for a ride and get a little exercise before breakfast, eh?’ You swing yourself up on the saddle and grab the reins with one hand as you steady yourself with the other, your "+mount+" excitedly racing off underneath you as the two of you escape from view over the horizon.")
        print("")
        print("Your stomach begins to churn with the steady, rhythmic bouncing of your "+mount+"’s pace, and you yank hard on one rein, curtailing the morning sprint and redirecting your heading back towards the open-air market where you awoke earlier.  ‘Alright, ok, there you are.  Good boy, let’s go now.  Let’s go get some breakfast.’")
        print("")
        print("The jostling ride continues back to where you began, and the combination of the bouncing and your empty stomach is making you feel a bit ill.  As you dismount and hitch up your "+mount+" you hear a squeaky voice behind you.")
        upset_stomach_story()
    else:
        print("")
        breakfast_invitation()
        
#This function invites the user to have breakfast with a kind elderly woman and requires an answer of (yes) or (no) from the user
#This function calls one of two functions based on the user's answer: breakfast_story or upset_stomach_story, each of which begin either a questline or another decision
        
def breakfast_invitation ():
    print("")
    choice = input("A kind elderly woman crooks a wrinkled finger toward you as you look around, rubbing your eyes.  Behind her, you see a bowl full of speckled brown eggs sitting on the counter next to bacon sizzling on a griddle, a table set with bread, rolls, butter and jam and a pitcher of milk and orange juice.  She smiles and asks you in a gravelly voice, 'Would you care to join me for breakfast?' ")
    print("")
    while not(choice == "yes" or choice == "no"):
        print ("Please choose (yes) or (no).")
        print("")
        choice = input("'Would you care to join me for breakfast?' ")
        print("")

    if choice == "yes":
        breakfast_story()
    else:
        upset_stomach_story()

#This function introduces the user to the questline "Slay the Grenwald"
#This function invites the user to play a game of rock, paper, scissors with the kind elderly woman who invited the user to breakfast
#This function determines who will do the dishes in the story and requires an answer of (rock), (paper), or (scissors) from the user
#This function calls one of three functions based on the user's answer: rock_story, paper_story or scissors_story, each of which have 3 different endings to the "Slay the Grenwald" questline
    
def breakfast_story ():
    print("")
    choice = input("You sit down at the wizened old woman's table and enjoy a hearty breakfast.  As the two of you finish sopping up egg yolk with bits of bread from your plates, you overhear two young boys whispering excitedly as they scurry past you through the open-air market. 'Did you hear about the Grenwald last night? It seems she's taken another, and I understand the King has issued a ransom for her head!'  The old woman laughs as your gaze follows the young boys. 'So, you fancy yourself an adventurer, do you?  The last "+race+" that set out to slay the Grenwald never came back... Although, it is quite the handsome reward that the King is offering! Anyways, before you get carried away with all of that malarkey, you owe me a game of Rock, paper, scissors,' she said with a twinkle in her eye. 'Loser does the dishes!' Which would you like to play: rock, paper, or scissors? ")
    print("")
    while not(choice == "rock" or choice == "paper" or choice == "scissors"):
        print ("Please choose (rock), (paper) or (scissors).")
        print("")
        choice = input("(Rock), (paper), (scissors)? ")
        print("")
    if choice == "rock":
        rock_story()
    elif choice == "paper":
        paper_story()
    else:
        scissors_story()
    print("")

#This function introduces the user to a kind stranger who notices that the user has an upset stomach
#This function invites the user to choose a red pill or a blue pill to treat their upset stomach and requires an answer of (red) or (blue) from the user
    
def upset_stomach_story ():
    print("")
    choice = str(input("A well-dressed and fidgety gnome who speaks excitedly with his hands approaches you, 'Well aren’t you a funny-looking "+race+"! Or maybe you’re just not feeling well? Anyways, why don’t you take a look at what I have up my sleeve, one of these is sure to make you feel better!' You peer at him curiously as he furtively digs in his pockets. 'Erm, ah, they were just right here...' he mutters to himself. 'Aha! Here they are! Your choice, one pill ought to due, red or blue?' he proclaims as he thrusts forward both palms, each proudly displaying a healthy sized pill: one red and one blue.  Would you like the red pill or the blue pill? "))
    print("")
    while not (choice == "red" or choice == "blue"):
        print("Please choose (red) or (blue).")
        print("")
        choice = str(input("Would you like the red pill or the blue pill? "))
        print("")

    if choice == "red":
        print("You place your open palm in front of the red pill, and the squeaky-voiced gnome drops the pill in your open hand, 'Quite brave, didn't even ask what it is! You remind me of my aunt. She was a mighty "+role+", and I bet you could be a "+role+" someday also, if you trained hard enough.  Anyways, that's another story for another time. I hope the pill suits you well!'")
        print("")
        print("Immediately after ingesting the red pill your head begins to swim. Your consciousness floats away until you are unsure what is real and what is make-believe. You find yourself at the foot of a castle, where a young man has set up a shell game, 'Watch the pea, use your eyes, get it right and win a prize!' he exclaims as you watch a passerby wager a coin on a round of the game.  The huckster slides a pea under one of 3 empty half-walnut shells and lays them flat on a board in front of him.  Slowly at first, and then ever-faster, he nimbly and dextrously maneuvers the shells beneath his fingers, faster and faster until all you can see is a blur of hands, all while they lay flat on the board in front of him.  At once he stops. The passerby grins sheepishly and half-heartedly points to one of the shells.  The showman flashes a wide, toothy smile as he flips up the empty shell, revealing that this was not the winner.  With a flourish, he reshuffles the shells in front of him and gestures towards you, 'And you, charming young "+race+" with the smile of a "+role+".  How about a free turn at my game? What do you say? Nothing to lose, don't you see?'")  
        print("")
        red_pill_story()
    else:
        print("Your gaze moves to the blue pill, and before you can get a word out edge-wise, the sneaky little sucker tosses it in your mouth with a gleeful cackle, 'Roses are red, this pill is blue.  Not sure what's in it, but let's hope it's good for you!'.")
        print("")
        print("Your reality fades and mutes as you shift dimensions. You hear a loud, audible *SNAP* and your teeth flash cold momentarily.  Your eyelids flit and flutter as you come to, making out your surroundings.  Before you is a path, and on either side are thick blackberry bushes surrounding tall, wide-based evergreen trees.")
        print("")
        print("As you walk down the path, you come across an old man resting under a tree.  'Could you do me a favor young whippersnapper?' he asks you, 'I need your help.  My daughter has gone on ahead of me, and I told her I would catch up, but I am injured.  She needs your protection.  After she left, word was sent to me by a messenger that a gang of thieves is laying in wait for her, just a short ways past where we are now.  There is a 3-way fork in the road, and I'm not sure which path she has chosen.  You'll need to guess correctly in order to find her.  Please, "+name+", you're our only hope! I have my own kingdom not many days travel from here; should you save my daughter the Princess I shall reward you handsomely.'")
        print("")
        blue_pill_story()
    
#This function features three different endings to the "Slay the Grenwald" questline
#This function wins the game if the user has previously selected "Sorcerer" as role and "rock" as option in game with kind elderly woman
#This function loses and restarts the game if the user has previously selected either "Brawler" or "Priest" as role and "rock" as option in game with kind elderly woman

def rock_story():
    if role == "Sorcerer":
        print("You set off to find the Grenwald with a spring in your step after helping the kind elderly woman with the breakfast dishes. You find the behemoth alone on top of a rocky mesa.  The beast squares off against you and charges.  You use your powers as a "+role+" to cause an avalanche of rocks to fall on the Grenwald's head, stopping the charging monster dead in it's tracks.  You have slain the Grenwald!")
        print("")
        congratulations()
    elif role == "Brawler":
        print("Your loins warm with anticipation, you set out on your mission to locate the Grenwald after helping the kind elderly woman with the breakfast dishes.  Soon, you find the gargantuan matriarch as she is sleeping.  You find a perch above her, and roll a large rock over the precipice to drop on her head, in hopes of incapacitating her.  As you are rolling the rock into place to drop on her head, another, larger rock falls from above you, and hits you on the head.  You begin to lose consciousness from internal hemorrhaging.")
        print("")
        wake_up_groggy()
    else:
        print("After you finish doing the dishes for the kind elderly woman, you head off to vanquish the Grenwald.  After a time, you come to a rock quarry.  There, you find the Grenwald hard at work, carving large chunks of granite out of the walls of the quarry and smashing them into smaller, more uniform pieces.  You attempt to take her by surprise, but her reflexes catch you off guard, and she whips around as you try to sneak up on her.  She has you dead to rights.  She picks up two large slabs of granite, each larger than you, and slowly squeezes you between them.  You begin to lose consciousness from a collapsed lung.")
        print("")
        wake_up_groggy()

#This function features three different endings to the "Slay the Grenwald" questline
#This function wins the game if the user has previously selected "Brawler" as role and "paper" as option in game with kind elderly woman
#This function loses and restarts the game if the user has previously selected either "Sorcerer" or "Priest" as role and "paper" as option in game with kind elderly woman

def paper_story():
    if role == "Sorcerer":
        print("You finish helping the kind elderly woman with the breakfast dishes, then set out to slay the Grenwald.  After several days travel, you locate the mythical beast.  You cast a spell from afar, and it does nothing but anger her.  Perhaps a "+role+" isn't meant to be slaying the Grenwald. You begin to faint and lose consciousness from low blood pressure.")
        print("")
        wake_up_groggy()
    elif role == "Brawler":
        print("After finishing helping the kind elderly woman with the breakfast dishes, you set out to slay the Grenwald.  It takes you several days to find her, but when you finally do, you've had time to think of a clever plan.  Although you are strong, you conclude that she is much stronger, and decide to use your brains instead of your brawn to defeat her.  You bring out a storybook, and while she is resting after a meal, you begin to read her stories from a hiding place, so that she can only hear you and not see you.  She grows sleepy from listening to the stories on a full belly, and is soon snoring loudly.  You take this opportunity to take her life mercilessly so that you may collect the bounty and protect the citizens from her wrath.  You have slain the Grenwald!")
        print("")
        congratulations()
    else:
        print("After doing the breakfast dishes with the kind elderly woman, you begin your mission to slay the Grenwald.  After several days of hunting, you have the opportunity to come face-to-face with her.  You summon your power of the "+role+" and attempt to heal the evil out of her, but this only enrages her.  She mauls your face.  You begin to lose consciousness due to loss of blood.")
        print("")
        wake_up_groggy()

#This function features three different endings to the "Slay the Grenwald" questline
#This function wins the game if the user has previously selected "Priest" as role and "scissors" as option in game with kind elderly woman
#This function loses and restarts the game if the user has previously selected either "Sorcerer" or "Brawler" as role and "scissors" as option in game with kind elderly woman

def scissors_story():
    if role == "Sorcerer":
        print("You and the kind elderly woman finish the dishes from breakfast, and then you ignore her advice and go off to find the Grenwald.  When you come across the monster alone in an open field, you charge towards her.  With a swat of her tail you fly high into the air, and fall straight into her throat.  You begin to lose consciousness from the smell of her innards.")
        print("")
        wake_up_groggy()
    elif role == "Brawler":
        print("You finish up doing the breakfast dishes with the kind elderly woman and head out to find the Grenwald.  You keep your "+weapon+" drawn and are ready for a battle at any moment, but when you happen upon her you find that her sheer brute strength is no match for any "+role+", let alone one of your prowess.  She toys with you like a cat with a mouse, then swats your feet out from underneath you.  You begin to lose consciousness from nerve damage in your spinal cord.")
        print("")
        wake_up_groggy()
    else:
        print("You and the kind elderly woman finish the breakfast dishes together before you set out to slay the Grenwald.  You come across her after days of searching out in the countryside and she bellows '"+name+"! I have been waiting for you!'  You shiver in anticipation of a battle to end all battles.  Your hands glow with a priestly aura as you summon the power of the deities above.  You charge at the Grenwald and strike her once, twice, three times with your "+weapon+".  She lies still.  You have slain the Grenwald!")
        print("")
        congratulations()

#This function introduces the user to the "Find the Treasure" questline, invites the user to play a game of Three Card Monte and requires an answer of (1), (2) or (3) from the user
#This function features three different questline story endings for each choice of card 1, 2, or 3 for a total of 9 questline story endings

def red_pill_story():
    try:
        number_choice = int(input("What'll it be, 1, 2, or 3? " ))
        print("")
        while not(number_choice == 1 or number_choice == 2 or number_choice == 3):
            print("Please choose (1), (2) or (3).")
            print("")
            number_choice = int(input("What'll it be, 1, 2 or 3? " ))
            print("")
            number_punishments_angels_singing()
        print("The shell game host laughs uproariously as he shows you your empty shell, 'Lady luck may not be on your side just yet, but don't let that stop you from finding the treasure inside the castle!' he intones as he gestures with a grand sweep of his hand toward the entrance just behind him.")
        print("")

#This section of the function features three different questline story endings for the "Find the Treasure" questline
#This section of the function wins the game if the user has previously selected "Sorcerer" as role and 3 as the card in the game of Three Card Monte
#This section of the function loses the game if the user has previously selected "Sorcerer" as role and either 1 or 2 as the card in the game of Three Card Monte

        if role == "Sorcerer":
            if number_choice == 1:
                print("Following the confidence man's lead, you enter the castle in search of the storied treasure.  You hear the creak of a door opening in the room to your left. Entering the room, you are temporarily blinded by a flash of light as a torch is ignited.  'Ewww! It's a "+race+" and it's ALIVE! Quick, get the switch!  This one smells like a "+role+"!'  You count", number_punishments_angels_singing(number_choice), "lashings before you collapse in pain, unconscious.")
                print("")
                wake_up_groggy()
            elif number_choice == 2:
                print("'Treasure, eh?' you think to yourself as you step through the threshold into the castle, 'I could always use a little extra pocket money.' You see a set of stairs leading up from the entryway, and make your way up the first flight. '"+name+"...' You hear a ghostly whisper from behind a curtain in the corner.  Slowly, you make your way to the curtain, and pull it back. '"+name+"... Thank you for joining us.  I hope you weren't planning on leaving any time soon!'  A sharp blow from behind drops you to the floor.  You count", number_punishments_angels_singing(number_choice), "lashings before you lose consciousness.")
                print("")
                wake_up_groggy()
            else:
                print("Upon entering the castle, a giant ogre is standing in front of you, ready to fight.  'Fee fi, fo fum. I smell the blood of someone dumb!'  Although you are unprepared for battle, your quick reactions and prowess with your "+weapon+" make for a short fight against the ogre. Once he is vanquished, you rummage through his knapsack and find the diamond-crusted golden tiara. You have found the treasure!  You count", number_punishments_angels_singing(number_choice), "angels singing your praises.")
                print("")
                congratulations()

#This section of the function features three different questline story endings for the "Find the Treasure" questline
#This section of the function wins the game if the user has previously selected "Brawler" as role and 1 as the card in the game of Three Card Monte
#This section of the function loses the game if the user has previously selected "Brawler" as role and either 2 or 3 as the card in the game of Three Card Monte

        elif role == "Brawler":
            if number_choice == 1:
                print("Carefully withdrawing your "+weapon+", you enter the castle. Instantly, you are besieged by a wild pack of angry dwarves.  'You'll never have our treasure of precious gems you smelly "+role+"! You'll never make it out alive!'  Coolly and calmly you dispatch the horde of bearded bullies, and as you stop to catch your breath, you notice a glint of gold peeking out from under the rug in front of you.  Sweeping away the rug, you uncover a pile of precious gems and metals.  You have found the treasure!  You count", number_punishments_angels_singing(number_choice), "angels singing your praises.")
                print("")
                congratulations()
            elif number_choice == 2:
                print("As you enter the castle you notice a trap door in the far corner. A thick iron hoop is attached to the wooden door, which you use to pull the hatch open slowly as it emits a low groan.  Stairs lead below you, and you hear a small voice calling out in the distance, 'Help. Help me. I'm just a little lonely "+race+" down here all by myself.  My mother is too busy training to be a "+role+" to take care of me.  Oh, someone please help me, and all of this treasure down here will be yours!'  You race down the stairs, eager to lend a helping hand and line your pockets.  'Sucker,' snickers a deep sinister voice behind you as you come around the corner. The last thing you see is a flash of light as you feel a thick thud on the back of your head. You count", number_punishments_angels_singing(number_choice), " tiny birds flying around your head before you lose consciousness.")
                print("")
                wake_up_groggy()
            else:
                print("You storm the entrance of the castle, your "+weapon+" drawn and your mind fresh with the tactics passed down from generations of "+role+"s before you.  There, in front of you, lies the treasure.  It is within your reach.  But, just before the treasure sits a small table laden with dozens and dozens of donuts.  You decide it couldn't possibly hurt to stop and have a quick snack before collecting the treasure. You count", number_punishments_angels_singing(number_choice), "donuts put away before you doze off.  Mmmmm, donuts.")
                print("")
                wake_up_groggy()

#This section of the function features three different questline story endings for the "Find the Treasure" questline
#This section of the function wins the game if the user has previously selected "Priest" as role and 2 as the card in the game of Three Card Monte
#This section of the function loses the game if the user has previously selected "Priest" as role and either 1 or 3 as the card in the game of Three Card Monte

        else:
            if number_choice == 1:
                print("You enter the castle with your senses on full alert.  You pass through the foyer into the courtyard, lush, green and lit by the sun.  At the top of the tallest tree there is a platform laden with jewels, gold, and silver.  You have found the treasure.  Now, it's just a matter of getting to it.  You begin to climb the tree when you feel something whistle past your ear, narrowly missing you.  Seconds later, you hear a thud above you and you quickly look up to find an arrow quivering in the trunk of the tree above your head. You're being shot at by guards with bows. One sinks into your thigh, and the pain is unbearable. You count", number_punishments_angels_singing(number_choice), "arrows sunk into your body before you lose consciousness.")
                print("")
                wake_up_groggy()
            elif number_choice == 2:
                print("You slowly enter the castle, more concerned with your safety than with obtaining treasure.  You see a peasant girl bent low over a figure laying in bed, weeping, 'My kingdom, all of it, for my father's health!' she wails.  Smiling, your hands begin to glow.  You approach the man slowly with intent and place your hands on his temples. A slow smile plays across his lips as his eyes blink twice and he regains consciousness.  The King notes your pious deeds, and bestows upon you the greatest honors and riches.  You count", number_punishments_angels_singing(number_choice), "angels singing your praises.")
                print("")
                congratulations()
            else:
                print("You enter the castle with great aplomb. Certain of success, you storm through room through room with great bravado.  You come to a great room, and you see a pile of jewels centered in the middle.  You sprint towards the treasure, only to fall down a trap door stairway that was loosely covered with a rug as a booby trap.  You count", number_punishments_angels_singing(number_choice), "stairs that your head bounces off of before you lose consciousness.")
                print("")
                wake_up_groggy()

            print("")
    except ValueError:
        print("")
        print("Please choose (1), (2), or (3). ")
        print("")
        red_pill_story()
        
#This function takes the value entered as the choice of cards in the Three Card Monte game, adds two and squares the total to return a value
#This function uses the value returned as the number of punishments the user counts before losing consciousness in the event of a loss in the "Find the Treasure" questline
#This function uses the value returned as the number of angels in the choir singing the user's praises in the event of a win in the "Find the Treasure" questline
            
def number_punishments_angels_singing(number_choice):
    punishments_angels_singing = (number_choice + 2) ** 2
    return punishments_angels_singing

#This function introduces the user to the "Save the Princess" questline and invites the user to select from a trio of paths before them
#This function requires an answer of (left), (right) or (middle)
#This function features three different questline story endings for each choice of (left), (right) or (middle) for a total of 9 questline story endings

def blue_pill_story():
    road_choice = str(input("Determined to help the worried, injured King, you set off down the path.  Soon, you come to a fork with three trails in the path.  Left, right or middle? "))
    print("")
    while not(road_choice == "left" or road_choice == "right" or road_choice == "middle"):
            print("Please choose (left), (right), or (middle).")
            print("")
            road_choice = str(input("Left, right or middle? "))
            print("")

#This section of the function features three different questline story endings for the "Save the Princess" questline
#This section of the function wins the game if the user has previously selected "Sorcerer" as role and "middle" as the path before them
#This section of the function loses the game if the user has previously selected "Sorcerer" as role and either "left" or "right" as the path before them

    if role == "Sorcerer":
        if road_choice == "left":
            print("You choose the left trail and continue down.  You find the gang of thieves, but not the Princess. The thieves take your pants and leave you on the side of the path. 'Not my day', you think to yourself.  Night falls and you soon lose consciousness from a severe case of hypothermia.")
            print("")
            wake_up_groggy()
        elif road_choice == "right":
            print("You choose the right trail and continue on.  There is no sign of the Princess, and you are running low on supplies.  You pass an abandoned caravan with skeletal remains.  You contract a severe case of dysentery, and lose consciousness from lack of fluids.")
            print("")
            wake_up_groggy()
        else:
            print("You choose the middle trail. Your clairvoyance is more profound than usual, and you sense that the Princess is near.  The gang of thieves appears, with the Princess in stow as a hostage.  A wicked firefight ensues, and you summon all your skills as a "+role+" to win the battle.  You have saved the Princess!")
            print("")
            congratulations()

#This section of the function features three different questline story endings for the "Save the Princess" questline
#This section of the function wins the game if the user has previously selected "Brawler" as role and "right" as the path before them
#This section of the function loses and restarts the game if the user has previously selected "Brawler" as role and either "left" or "middle" as path before them

    elif role == "Brawler":
        if road_choice == "left":
            print("You amble down the left trail, unsure of what you'll find.  You hear the low growl of an animal and turn behind you to see a large black bear charging at you.  You turn to run, but it's too late.  With a single swipe the large beast mauls you down.  You feign death as you begin to lose consciousness, in hopes the bear forgets you and goes on his way.")
            wake_up_groggy()
        elif road_choice == "right":
            print("You choose the trail on the right.  After a short while, your keen senses tell you that the King's daughter is just ahead.  Lo and behold, as you come around a bend in the path you see the flaxen-haired beauty.  As you rush to intercept her, she is surrounded by a group of Dark Elves.  There are 5 of them against only you, but your "+weapon+" and "+role+" training prove to be no match.  You have saved the Princess!")
            print("")
            congratulations()
        else:
            print("You walk slowly down the middle trail.  As afternoon turns to dusk and dusk turns to night, you begin to grow weary.  You stop to set a small fire to keep warm for the night, but neglect to notice how arid and dry the underbrush surrounding you is.  A gust of wind picks up after you've built your fire, and spreads the flames in a small semi-circle around you.  As the bone-dry tinder on the ground begins to ignite, you frantically stomp on the ground, attempting to extinguish it in vain.  The flames slowly lick at your appendages as you begin to lose consciousness from the searing pain.")
            wake_up_groggy()

#This section of the function features three different questline story endings for the "Save the Princess" questline
#This section of the function wins the game if the user has previously selected "Priest" as role and "left" as the path before them
#This section of the function loses and restarts if the user has previously selected "Priest" as role and either "right" or "middle" as the path before them

    else:
        if road_choice == "left":
            print("You choose the trail on the left.  As you walk along the woods, you notice a small songbird hopping on one foot, seemingly unable to fly.  You summon your training as a "+role+" and lay a single hand on the breast of the songbird.  A flash of light appears as the songbird transforms into the raven-haired princess, 'I had to test your true powers,' she exclaims, 'to see if you were the one who was worthy of saving me!'  You have saved the Princess!")
            print("")
            congratulations()
        elif road_choice == "right":
            print("You choose the trail on the right.  You walk for miles and miles, and as the shadows grow longer you begin to run low on water.  After another hour passes with no sign of more, you become giddy at the sound of running water just off the trail.  You excitedly trample through the brush towards the sound of running water, ducking branches and following your ears.  You are so excited and moving so quickly that you trip and fall into the river, which is icy cold and quickly deposits you over a waterfall and into a rocky ravine.  You begin to lose consciousness from a head injury.")
            print("")
            wake_up_groggy()
        else:
            print("You choose the trail in the middle.  There is no sign of the Princess, nor of any other life.  The landscape becomes more and more barren.  A dust devil begins to swirl around you, and soon has developed into a mini-tornado.  You are picked up off the ground against your will and whipped around with enough centrifugal force to make your head spin.  The wind finally releases you, slamming you on your back on the ground.  You begin to lose consciousness from lack of oxygen.")
            print("")
            wake_up_groggy()

#This function congratulates the user after winning the game

def congratulations():
    print("Congratulations, "+name+", you are a hero amongst heroes and your name shall be forever storied.  Arcana is eternally indebted to you.")

main()
