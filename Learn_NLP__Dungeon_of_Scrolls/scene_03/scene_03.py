# version 002
# Scene_03
# Any Way You Slice It

import os  # for terminal functions etc.
import random  # for randomized replies etc
import sys  # for realistic printing
import time  # for pauses

scene = "scene_03"
blurb = " Any Way You Slice It "
adventure = "Learn_NLP__Dungeon_of_Scrolls"
game = "ReadMe_Adventures"

# TODO add Bonus challenges

friends_dict = {
    "first": "jane baldwin",
    "second": "franklin merln",
    "third": "lavender mccavity",
    "fourth": "gullover hitch",
    "fifth": "ada babbage",
}


#########################
# Story Display Funtions
#########################


def check_cd_or_make_cd(folder_name):
    # check
    if os.path.exists(folder_name):  # checks if folder or file exists
        # CD (change directory - move into that folder)
        os.chdir(folder_name)
    else:
        # mkdir (Make a new directory / folder)
        os.mkdir(folder_name)
        # CD (change directory - move into that folder)
        os.chdir(folder_name)


def manage_file_pathways():
    # if adventurea geames is not in the pathway: make all
    if game not in os.getcwd():
        check_cd_or_make_cd(game)
        check_cd_or_make_cd(adventure)
        check_cd_or_make_cd(scene)
    else:  # it is...
        # change director to game, check/make other files
        while not os.path.isdir(f"../{game}"):
            # go back a directory
            os.chdir("..")
        # then check and make adventure and scene
        check_cd_or_make_cd(adventure)
        check_cd_or_make_cd(scene)


# in case easier to remember
def pause_seconds(seconds):
    time.sleep(seconds)
    pass


# making text print-out look like it is being typed
def slow_print(input_text):
    # staggered times
    random_times = [
        0.4,
    ]

    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()

    # end
    pass


# making text print-out look like it is being typed
def typed_print(input_text):
    # staggered times
    random_times = [
        0.03,
        0.03,
        0.03,
        0.04,
        0.04,
        0.04,
        0.05,
        0.05,
        0.05,
        0.08,
        0.08,
        0.3,
    ]
    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()
    # end
    pass


# clear screen (for windows or...everything else)
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    pass


#############
# Setting Up
#############

# make sure file structure is correct
manage_file_pathways()

# general_wrong_answer_responces
responses = [
    "Huh?",
    "What was that?",
    "Really?",
    "I didn't catch that...",
    "Come again?",
    "Are you sure about that?",
    "That just doesn't sound right..."
    "What?",
    "You're pulling my leg!",
    "I'm sorry, my mind was wondering. What was that again?",
    "Ha ha hah ahahahhahahhh, that's a good one.",
    "...Seriously?"
    "You have to be joking.",
]

clear_terminal()

############
# pronouns #

# Note: for uppercase, use: pronoun.title()

# setting up question:
pronoun = input("What is your character's pronoun?\n")
clear_terminal()

# making user input lower case
pronoun = pronoun.lower()

# fix (he vs. him etc.)
# pronoun(1)
if pronoun == "him" or pronoun == "he":
    pronoun = "he"

elif pronoun == "her" or pronoun == "she":
    pronoun = "she"

else:
    pronoun = "they"

# pronoun2
if pronoun == "he":
    pronoun2 = "him"

elif pronoun == "she":
    pronoun2 = "her"

elif pronoun == "they":
    pronoun2 = "them"

# pronoun3
if pronoun == "he":
    pronoun3 = "his"

elif pronoun == "she":
    pronoun3 = "hers"

elif pronoun == "they":
    pronoun3 = "theirs"

# pronoun4
if pronoun == "he":
    pronoun4 = "he's"

elif pronoun == "she":
    pronoun4 = "she's"

elif pronoun == "they":
    pronoun4 = "they're"

###############
# Create Files
###############

# create ReadMe.txt file
readme_text = """
ReadMe Scene__03  Any Way You Slice It

Instructions:

1. Run The Game
    1. Open Terminal
    2. Get file      Command: wget https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_03/scene_03.py
    3. Run file      Command: python3 scene_03.py

    ( For Windows_OS, see: https://docs.google.com/document/d/1p6R2LpBZtgs9IO349W1Zrx8u_Zy_5kgCxbJ64toOJXI/edit?usp=sharing )

2. Journal
    Keep a Journal about what you are learning.

3. Lost or Curious
    Check out the Content_Map.txt for this scene.
    ( Content_Map.txt will be generated when .py is run )

4. User Manual
    Advanced Instructions: https://docs.google.com/document/d/1q2AiDPM0BpQal7ltm3sWk0suxLJSS7uX6S9yH44F_ZA/edit?usp=sharing

"""

# create, write-to, & save .txt file
file_to_create1 = open("ReadMe.txt", "w")
file_to_create1.write(readme_text)
file_to_create1.close()

# # #open, read, & print the file
# # Step 1: make an intermediate file in python
# intermediate_file_variable = open("ReadMe.txt", "r")
# # Step 2: make an item_to_print by reading the intermediate file
# item_to_print = intermediate_file_variable.read()
# # Step 3: Print the item you want to print
# print(item_to_print)
# # You can do this in just one step, but it maybe harder to read:
# print((open("ReadMe.txt", "r")).read())

# create file:
advanced_instructions_text = """

"ReadMe Adventures" is a minimal game-system that requires just two files
to play, and just one of those files to get started, a ReadMe.txt

This ReadMe.txt & Scene.py system is flexible and should be workable
on many operating systems including mobile devices. This make
'complete instructions' difficult as set-up may be a bit different on
the huge possible combinations of tools, software, and hardware.
but in general, you can get by with:
1. a terminal (any OS) and a text editor (like notepad)
or
2. just a python notebook (like colab)

(You could also maybe use an online Repl (e.g. https://repl.it)
and a word processor or office suite (open office, google, ms, etc.)
It is flexible and minimal so many creative possibilities exist.)

You could do it all in VIM.(an editor that runs in a terminal)

You can do it all online, or do it all off-line (once you have
the files downloaded and the python environments set up).


Using a terminal is recommended, but using a "colab notebook"
see: https://colab.research.google.com/notebooks/welcome.ipynb
(or see AWS sagemaker notebooks)
is also work-able and this can be done on just about any platform that runs
any up-to-date browser (safari, firefox, chrome/chromium, etc.)

As the course progresses, using a notebook and or a terminal may be
a part of some scenes.

Using pip environments and or conda environments or notebook environments
will probably come up also.

To view the a .txt file you can open it in any 'text editor,'
probably clicking on it will open it in a default application.
(note: in some systems, the .txt suffix is not needed and may be absent)
To open it in python put next 3 commands in a terminal:
  - python3
  - file_to_read = open("the_file_name_in_quotes.txt", "r")
  - print(file_to_read.read())

Note: running the .py file in any python3 version 3.7 or higher should work.
running just: python scene.py (and not python3 scene.py) will usually
not work because many operating systems have two different versions
of python installed: python (which is python version 2)
and python3 (python version 3)
Even older versionof python 3 (3.1 to 3.5) will not work.

Advanced Instructions for How to Start:

First time set-up:
  - install python
  - check your version of python (terminal: python3 --version)
  if below 3.7, upgrade to a higher version of python
  - windows OS: install wget
  - install pipenv
  - install up-to-date code editor: atom / vsCode

To do a scene (each time):
  - make a new folder/dirctory for the adventure
  - make a new folder/dirctory for the scene
  - go into that folder
  - create a pip-environment to use python in
  - open a text editor / IDE (developement environment)
    in that area showing all files
  - download the scene_x.py file
  - run the .py file

Run in a terminal:
  mkdir adventure_name
  mkdir scene_x
  cd scene_x
  pipenv install -d --pre black pylint pytest flake8
  atom . / code .
  wget https://raw.githubusercontent.com/...etc
  python3 scene_x.py
"""

# create, write-to, & save .txt file
file_to_create2 = open("advanced_instructions.txt", "w")
file_to_create2.write(advanced_instructions_text)
file_to_create2.close()

# # #open, read, & print the file
# # Step 1: make an intermediate file in python
# intermediate_file_variable = open("advanced_instructions.txt", "r")
# # Step 2: make an item_to_print by reading the intermediate file
# item_to_print = intermediate_file_variable.read()
# # Step 3: Print the item you want to print
# print(item_to_print)
# # You can do this in just one step, but it maybe harder to read:
# print((open("advanced_instructions.txt", "r")).read())


# create file: content map
content_map_text = """
Content Map
For scene_03, Dungeon of Scolls, ReadMe Adventures.

The Skill-Ability in scene_03 is: slicing with []

...examples pending
maybe point to notebook...

1. what it can be used on (lists, strings, etc)
2. using around :

"""
# create, write-to, & save .txt file
file_to_create3 = open("Content_Map.txt", "w")
file_to_create3.write(content_map_text)
file_to_create3.close()

# # #open, read, & print the file
# # Step 1: make an intermediate file in python
# intermediate_file_variable = open("Content_Map.txt", "r")
# # Step 2: make an item_to_print by reading the intermediate file
# item_to_print = intermediate_file_variable.read()
# # Step 3: Print the item you want to print
# print(item_to_print)
# # You can do this in just one step, but it maybe harder to read:
# print((open("Content_Map.txt", "r")).read())



#################
# Materials Files
#################

# create map_1 file
map_1 = """
Welcome to the historic dungeons of
Spring Falls Imperial Forest Reserves,
home to the most highly reviewed dungeon restaurants
and a family friendly enchanted forest retreat center.
From the impasses of blister bay to the seasonal favorite
'house of blood' that delight family travelers,
you can also stop by our xylophone emporium for an acoustic mystery
the family will never forget. (All instruments are made by humans
on the premises accorded to Imperial law.)
Fasting, loitering, and pets are prohibited.
Directions: Head east past the Axis Mountains then follow
the South Ridge mountains continuing south until you
get to the third old growth pine forest
and turn west at the base of the mountain.
"""

# create, write-to, & save .txt file
file_to_create4 = open("map_1.txt", "w")
file_to_create4.write(map_1)
file_to_create4.close()

# # #open, read, & print the file
# # Step 1: make an intermediate file in python
# intermediate_file_variable = open("map_1.txt", "r")
# # Step 2: make an item_to_print by reading the intermediate file
# item_to_print = intermediate_file_variable.read()
# # Step 3: Print the item you want to print
# print(item_to_print)
# # You can do this in just one step, but it maybe harder to read:
# print((open("map_1.txt", "r")).read())

# # #count length
# map1_file_to_read = open("map_1.txt", "r")
# map1_text = map1_file_to_read.read()
# print(len(map1_text))


# create map_2 file
map_2 = """
Here at the Murkland Designated Sites,
we are proud to have received recognition
for our 100% magic-free locally grown produce.
Tours are temporarily behind schedule
due to a wagon guild strike.
Information about the fence around the park
may be obtained with a freedom of information request
submitted before the next full moon
to the Bureau of Parks and Sacrifices. May the
the great empire prevailed over threats of technology.
Seasonal passes will resume availability
during the livestock relation season.
Due to a decrease in demand, trumpet filters will no longer be
available even with a judicial order on park grounds. All hail the humans.
Directions: Go to the base of Blossom ridge mountain.
"""

# create, write-to, & save .txt file
file_to_create5 = open("map_2.txt", "w")
file_to_create5.write(map_2)
file_to_create5.close()

# # #open, read, & print the file
# # Step 1: make an intermediate file in python
# intermediate_file_variable = open("map_2.txt", "r")
# # Step 2: make an item_to_print by reading the intermediate file
# item_to_print = intermediate_file_variable.read()
# # Step 3: Print the item you want to print
# print(item_to_print)
# # You can do this in just one step, but it maybe harder to read:
# print((open("map_2.txt", "r")).read())

# # #count length
# map2_file_to_read = open("map_2.txt", "r")
# map2_text = map2_file_to_read.read()
# print(len(map2_text))


##############
# The Action!
##############

slow_print(f"{scene} {blurb} ")
 
typed_print(
"""
\nFive pairs of feet crunch the snow in the wood,
over the tinkling of ice showering frozen leaves,
and the more periodic popping sounds of frozen birds
falling and shattering like lightbulbs on marble.
 
"Nice time for a walk, this is. Scenic."
 
"Don't mind Hitch."
 
"Yes, don't mind me. Imagination gets the better of me sometimes.
It's probably a warm summer day."
 
"It is the month for that. Odd."
""")
 
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()
 
 
 
typed_print(
"""
Jane crunches her way up next to you 
and holds something out in front of you.

"There's another piece of this map that needs figuring...
that witch who gave this to us, she penciled in a code
for what directions to go in."
 
"Yeah, I was looking at that. 
Really annoying trying to figure that out."
 
"Tedious, I'd say."
 
"You would say that."

"What's that supposed to mean?"
 
You feel a tugging on your sleeve.
"""
)
 
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()
 
 
typed_print(
"""
"Can you help us figure this part out too? 
The map has this number." 

She points with an unsteady finger at a number scrawled in the top corner.

"The number is how many characters to count along, 
and that points to the directions we should go in. 
Each should point to a cardinal-direction-letter, 
like "w" for West or "e" for East...or at least I hope they do."
 
"Yeah, but you see those arrows going forwards and backwards? 
We need to count twice: Once forwards and THEN once backwards,
to get two direction-letters. I nearly went blind last night 
at the inn trying to count that. And that tea didn't help at all,
thank you very much, whoever suggested that. Every time I tried 
counting it by hand I got a different letter. Useless."
 
"I wouldn't say you're completely useless, Hitch.
Don't be so hard on yourself."
""")
 

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()
 

typed_print(
"""
"...so can you give us a hand then? 
Should be easy for you, you know."
 
"Don't be rude, Hitch."
 
"What did I say?"
 
Jane hands you the crinkled page 
with the penciled in number and arrows:
"""
)
 
print("""
_______________
|
|	-> 
|	699
|	<-
""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

print("""
 _______________
|
|	-> 
|	699
|	<-

Slice[] the Text[]: Find the 699th letter and -699th Letter
 
Read in the map text like before, but this time "Slice" it. 
"Slice" out the +699th & -699th character, 
by putting square brackets after what you want to slice. 
 
(Note: The forward count starts from ZERO 
BUT counting backward starts from 1.)
IMPORTANT: Make sure you are clear on this before you go on:
e.g.  "abc"[0] is "a" / "abc"[1]  is "b" / "abc"[2]  is c
     "abc"[-1] is "c" / "abc"[-2] is "b" / "abc"[-3] is "a"
 
This is an example of how you would print the 'slice' of a variable:
    >>> print( map1[-699] )
Or it might work to leave out the 'print()' and just say >>> map1[-699]
"""
)

# Press Enter to Continue
input("  ...Press enter to continue...  \n")

print(""" 
To Start Python: Open another Terminal in the scene_03 folder. 
(Check you are in the correct directory with $ ls & $ pwd, and type:
  $ python3

This 'slicing' task is similiar to what you did before.

More Sample Code: (Review scene 1) Open, Read, & Print file
Step 1: make an intermediate file in python
    >>> file_to_read = open("map_2.txt", "r")
 
Step 2: make item_to_print by reading the intermediate file
    >>> item_to_print = file_to_read.read()
 
# Step 3: Print the item you want to print
    >>> print(item_to_print)
 
# (Review Scene 2) Count Length
    >>> file_to_read = open("map_2.txt", "r")
    >>> map2_text = file_to_read.read()
    >>> print(len(map2_text))
"""
)

# Press Enter to Continue
input("  ...Press enter to continue...  \n")
 
answer1 = 0
while answer1 != "n":
    answer1 = input('\n"What is the first letter or cardinal direction from the map?"\n (Scroll Up to see examples.)\n')
    answer1 = answer1.lower()
    if answer1 == "i":
        typed_print('\n"You sure you\'re counting up from 0, and not from 1?"')
    if answer1 != "n":
        typed_print(f'"{random.choice(responses)}"')

answer2 = 0
while answer2 != "e":
    answer2 = input('\n"What is the second letter or cardinal direction from the map?"\n (Scroll Up to see examples.)\n')
    answer2 = answer2.lower()
    if answer2 != "e":
        typed_print(f'"{random.choice(responses)}"')


typed_print(
"""
"Excellent... North and East...off we go! 
That was so much faster than counting letters, 
"""
)
typed_print(f'\nI\'m telling you, {pronoun4} amazing."\n') 


slow_print(f"\n\n End of {scene} {blurb} \n\n")



