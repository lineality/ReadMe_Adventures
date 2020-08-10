# version 007 - no special typing
# Scene_1
# Find Your Friends

import os  # for terminal functions etc.
import random  # for randomized replies etc
import sys  # for realistic printing
import time  # for pauses

scene = "Scene_1"  # scene 1: where you begin


#########################
# Story Display Funtions
#########################


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


#################
### Create Files
#################

# create file:
readme_text = """
Scene 1: Find Your Friends


Instructions:
1. Open Terminal
2. Get file       wget https://raw.githubusercontent.com/lineality/teaching_NLP_basics_1/master/ReadMe_Adventures/test_demo_1/Windows_OS/scene_1/scene_1.py
3. Run file       Command: python3 scene_1.py


(Optional)
Tips:
1. When given a choice or a question,
type in your answer and hit return.

2. Running the .py file will
run the interactive story in the terminal
and will create new files
that you can use during the scene.
Look for these files
in the directory (folder) that your command terminal is open in.
(This file may be updated as well.)

3. Since it is lying on the bar-counter in front of you,
you can 'access' the inn's guest-register.
Check your file directory again.
(This will help you to answer
the red-nosed innkeeper's question.)

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


# create file
# .txt file of inn's guest log for user:
inn_guest_log_text = """
(*loyal customer)
- Old Martha McSally
Items Purchased:
- capon (stuffed rooster)
- sauce
- fortified wine, two gallons
- one crouton of Bread

(seasonal traveler)
- Captn. Wilda Wooster
Items Purchased:
- bag of potatoes
- 1 *live rooster

(Those Meddlesome Kids)
- Friend 1: Baldwin
- Friend 2: Merln
- Friend 3: McCavity
- Friend 4: Q
Items Purchased:
- three pizzas
- 1 gallon of ginger-brew
- 1 cup of tea
- 1 book of dubious maps for tourists

(regulars)
- Four men in Kendal Green (difficult to see)
Items Purchased:
- fish'n chips x 4
- coffee x 8
- 2 books of crossword puzzles
- a dish towel
"""
# create, write-to, & save .txt file
file_to_create = open("inn_guest_log.txt", "w")
file_to_create.write(inn_guest_log_text)
file_to_create.close()

# # open, read, & print the file
# file_to_read = open("inn_guest_log.txt", "r")
# print(file_to_read.read())


##############
# The Action!
##############

clear_terminal()

slow_print(scene)

# Main Story
typed_print(
    """
\nYou are in The Mos Inn.
You are standing at the bar.
The bartender looks down at your arm
and eyes you suspiciously.

"We don't allow droids in here...", the barman says.
"Not usually...but...who are you with?
Who are your friends?"
"""
)

# Tip
print(
    """
\n(Tip: Since the inn's guest-register is lying on the bar-counter
in front of you, you can 'access'it.
Check your file directory again.)
"""
)

friends_dict = {
    "first": "Baldwin",
    "second": "Merln",
    "third": "McCavity",
    "fourth": "Q",
}

tip = """\n\n(Tip: Check the ReadMe file if you are out of ideas.)\n"""

responses = [
    "Who?",
    "Hmm...not sure I know anyone by that name..." "What was that?",
    "I didn't catch that...",
    "Come again?",
    "Are you sure about that?",
    "What?",
    "I'm sorry, my mind was wondering. What was that again?",
    "How would you spell that...doesn't sound familiar...",
    "Ha ha hah ahahahhahahhh, that's a good one.",
    "Ok, who are your friends, really?",
]


# function to check if the person's name is correct
def correct_name(person, name):
    return friends_dict[person] == name


# loop through and ask about each person:
for person_number in friends_dict:
    # reset flag
    friend_name_check = False

    # keep asking until the friends' names are given
    while friend_name_check is False:
        friend_name = input(f'\n"What was your {person_number} friend\'s name?"\n')
        friend_name_check = correct_name(person_number, friend_name)
        if friend_name_check is False:
            typed_print(f'"{random.choice(responses)}"', tip)

typed_print(
    """\n
"Oh, those crazy kids.
They're in the back at table eight.
Here, their pizza just came out of the oven
you might as well bring it with you.
Their tables' just back there."
"""
)

slow_print("\nEnd of Scene 1\n\n")
