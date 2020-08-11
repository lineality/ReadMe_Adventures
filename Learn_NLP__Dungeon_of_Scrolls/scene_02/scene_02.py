# version 008
# Scene_02
# Witch Map

import os  # for terminal functions etc.
import random  # for randomized replies etc
import sys  # for realistic printing
import time  # for pauses
import requests

scene = "scene_02"
adventure = "Learn_NLP__Dungeon_of_Scrolls"
game = "ReadMe_Adventures"

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
    # check .py file
    py_path = f"https://raw.githubusercontent.com/lineality/{game}/master/{adventure}/{scene}/{scene}.py"
    if not os.path.exists(f"{scene}.py"):
        myfile = requests.get(py_path, allow_redirects=True)
        open(f"{scene}.py", 'wb').write(myfile.content)


# in case easier to remember
def pause_seconds(seconds):
    time.sleep(seconds)
    pass


# making text print-out look like it is being typed
def slow_print(input_text):
    # staggered times
    random_times = [
        0.5,
        0.5,
        0.6,
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
    "What?",
    "You're pulling my leg!",
    "I'm sorry, my mind was wondering. What was that again?",
    "Ha ha hah ahahahhahahhh, that's a good one.",
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
Scene 2: Witch Map

Instructions:
1. Open Terminal
2. Get file       wget https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_02/scene_02.py
3. Run file       Command: python3 scene_1.py


(Optional)
Tips:
Steps to check the length of two files in python:
1. open python:
    python3
2. import both files (as different variables)
3. check the lenth with len()

e.g.
You could use a word processor to check the length,
but it is worthwhile to learn in python.
The easy part is getting the lenth of anything:
len(x)
It takes more steps to open the file and copy the contents to a variable,
but still just a few steps. ( lines that start with # are a comment)

# import the files as separate variables
map1_intermediary_file = open("map_1.txt", "r")
map2_intermediary_file = open("map_2.txt", "r")

# file_to_read = open("map_1.txt", "r")
map1_text = map1_intermediary_file.read()
map2_text = map2_intermediary_file.read()

# print out the lengths, using len(x)
print(len(map1_text))
print(len(map2_text))
"""

# create, write-to, & save .txt file
file_to_create = open("ReadMe.txt", "w")
file_to_create.write(readme_text)
file_to_create.close()

# #open, read, & print the file
# file_to_read = open("ReadMe.txt", "r")
# print(file_to_read.read())

# create file:
advanced_instructions = """

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
file_to_create = open("advanced_instructions.txt", "w")
file_to_create.write(readme_text)
file_to_create.close()

# #open, read, & print the file
# file_to_read = open("advanced_instructions.txt", "r")
# print(file_to_read.read())

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
file_to_create = open("map_1.txt", "w")
file_to_create.write(map_1)
file_to_create.close()

# # #open, read, & print the file
# map1_file_to_read = open("map_1.txt", "r")
# print(map1_file_to_read.read())

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
file_to_create = open("map_2.txt", "w")
file_to_create.write(map_2)
file_to_create.close()

# # #open, read, & print the file
# map2_file_to_read = open("map_2.txt", "r")
# print(map2_file_to_read.read())

# # #count length
# map2_file_to_read = open("map_2.txt", "r")
# map2_text = map2_file_to_read.read()
# print(len(map2_text))


##############
# The Action!
##############

# clear screen (for windows or...everything else)
os.system("cls" if os.name == "nt" else "clear")

slow_print(scene)

# Main Story
typed_print(
    """
\n
You walk to the back,
carying the hot pizza,
over creaking wooden floor boards.
\nThe rooms get quieter as you get further from the bar.
You walk up to a round table in the back up against the wall
with a small round dusty window overhead.\n
Something splashes against the window.
\n"Hey," someone at the table says as they look up.
"Is that our pizza? I'm starving."\n\n
"""
)

answer = input("Your Answer: Is this their pizza? (yes/no)\n")

# clear screen (for windows or...everything else)
os.system("cls" if os.name == "nt" else "clear")

answer = answer.lower()
if answer == "yes":
    typed_print(
        """
    \n"Yayy!!!!"

    \nYou put the pizza on the table
    and they start to grab slices and eat.
    """
    )
else:
    typed_print('"...but it smells so good..."\n')

# Tip
typed_print(
    """
"Ok, everyone, let's focus. What are we going to do
about these maps?"

"I think THAT one looks longer."

"But it could be off by just one character.
We need the one with the shorter text."

"I know, I tried counting the letters last night but
I kept coming up with slightly different numbers."

"Can we just try both maps?"\n
"""
)

# press
input("  ...Press enter to continue...  \n")

clear_terminal()

typed_print(
    """
"They lead in opposite directions, it takes days to get there,
one of them is probably a trap, and we have classes on Monday."

"And I have to walk my Dog."

"And Q has to walk her dog."

"My Aunt's dog."

"Her Aunt's dog. It's your Aunt's dog?
Anyway, we shouldn't try them both."\n
"""
)

typed_print(f'"Hang on...I bet {pronoun} can count...Can you count?"\n')


typed_print("\nAll voices go silent as everyone turns their gaze to you.\n")

answer_check = False
# keep asking until answer is correct
while answer_check is False:
    answer = input('\n"...Can you count?" (yes/no)\n')
    answer = answer.lower()
    if answer == "yes":
        answer_check = True
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

# clear screen (for windows or...everything else)
os.system("cls" if os.name == "nt" else "clear")

typed_print(
    """
"You can? Oh my gosh, ok, which of these is longer?"

"...I was thinking,
they're almost more like pamphlets than maps, really."

"We could call them...Folded-Publications?"

"We got them from witches, are witches 'publishers'?
I always wondered about that."

"Whatever, map-pamphlets, leaflets,
can you count how long they are? Like,
how many characters are printed on each one?
Like, letters and numbers and spaces and everything?"
"""
)

typed_print("\n(Compare the length of the two files.)")

# lengths
map1_file_to_read = open("map_1.txt", "r")
map1_text = map1_file_to_read.read()
map1_length = len(map1_text)

map2_file_to_read = open("map_2.txt", "r")
map2_text = map2_file_to_read.read()
map2_length = len(map2_text)

map_length_dict = {"map_1": map1_length, "map_2": map2_length}

# typed_print(map1_length, map2_length)

answer_check = False
# keep asking until answer is correct
while answer_check is False:
    answer = input('\n"...How long is the first map?"\n')
    answer = float(answer)
    answer = int(answer)
    answer_check = answer == map_length_dict["map_1"]
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

answer_check = False
# keep asking until answer is correct
while answer_check is False:
    answer = input('"...How about the second one?"\n')
    answer = float(answer)
    answer = int(answer)
    answer_check = answer == map_length_dict["map_2"]
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

# clear screen (for windows or...everything else)
os.system("cls" if os.name == "nt" else "clear")

typed_print('\n"That was awsome. Ok, quick vote: Should we bring the android?"\n')

typed_print(
    f"\n\"You can't just bring {pronoun2} if {pronoun} doesn't want to come?\"\n"
)

typed_print(f'\n"That\'s not what I meant but, whatever. Do we invite {pronoun2}?"\n')

typed_print(f'\n"{pronoun.title()} can hear us...{pronoun4} standing right there."\n')

typed_print(
    """
"Yes, awkward, sorry, bad planning here. But, what's the vote?
Who says yes?"
"""
)

time.sleep(2)

typed_print(
    """
Everyone immidiately raises their hand.

"Do you want to come find a dungeon?
We'll tell you all about it on the way.
Well, we don't know all about it,
but, do you want to come?"\n
"""
)

answer = input("(yes/no)\n")

# clear screen (for windows or...everything else)
os.system("cls" if os.name == "nt" else "clear")

if answer == "yes":
    slow_print("\nEnd of Scene 2\n\n")

