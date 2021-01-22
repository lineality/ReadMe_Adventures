# version 003
# Scene_06
# Unscrambled Eggs
#  _____           _ _____
# | __  |___ ___ _| |     |___
# |    -| -_| .'| . | | | | -_|
# |__|__|___|__,|___|_|_|_|___|
#  _____   _             _
# |  _  |_| |_ _ ___ ___| |_ _ _ ___ ___ ___    ___ _ _
# |     | . | | | -_|   |  _| | |  _| -_|_ -|  | . | | |
# |__|__|___|\_/|___|_|_|_| |___|_| |___|___|()|  _|_  |
#                                              |_| |___|

import os  # for terminal functions etc.
import random  # for randomized replies etc
import sys  # for realistic printing
import time  # for pauses

scene = "scene_06"
blurb = " Unscrambled Eggs "
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
    random_times = [0.4]
    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()
    # end
    pass


# making text print-out look like it is being typed
def medium_print(input_text):
    # staggered times
    random_times = [0.08]
    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()
    # end
    pass


# making text print-out look like it is being typed
def fast_print(input_text):
    # staggered times
    random_times = [0.002]
    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()
    # end
    pass


# making text print-out look like it is being typed
def steady_print(input_text):
    # staggered times
    wait_time = 0.016
    # stagger each character
    for i in input_text:
        time.sleep(wait_time)
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
    "What did you say?",
    "Is that what you meant to say?",
    "What was that?",
    "Really?",
    "I didn't catch that...",
    "Are you entirely sure that that was what you wanted to say?",
    "Come again?",
    "...You want to maybe try that one more time?",
    "Are you sure about that?",
    "That just doesn't sound right..." "What?",
    "You're pulling my leg!",
    "I'm sorry, my mind was wondering. What was that again?",
    "Ha ha hah ahahahhahahhh, that's a good one.",
    "...Seriously?", 
    "You have to be joking.",
]

# general_wrong_answer_responces
urgent_responses = [
    "Huh?",
    "What? Can you hurry that up?",
    "Oh, we don't have time for this...",
    "Come again? Quick! Quick!",
    "That doesn't sound right...",
    "What? Give it another quick look.",
]

clear_terminal()

# ############
# # pronouns #

# # Note: for uppercase, use: pronoun.title()

# # setting up question:
# pronoun = input("What is your character's pronoun?\n")
# clear_terminal()

# # making user input lower case
# pronoun = pronoun.lower()

# # default to 'she'
# if len(pronoun) == 0:
#     pronoun = "she"

# # fix (he vs. him etc.)
# # pronoun(1)
# if pronoun == "him" or pronoun == "he":
#     pronoun = "he"

# elif pronoun == "her" or pronoun == "she":
#     pronoun = "she"

# else:
#     pronoun = "they"

# # pronoun2
# if pronoun == "he":
#     pronoun2 = "him"

# elif pronoun == "she":
#     pronoun2 = "her"

# elif pronoun == "they":
#     pronoun2 = "them"

# # pronoun3
# if pronoun == "he":
#     pronoun3 = "his"

# elif pronoun == "she":
#     pronoun3 = "hers"

# elif pronoun == "they":
#     pronoun3 = "theirs"

# # pronoun4
# if pronoun == "he":
#     pronoun4 = "he's"

# elif pronoun == "she":
#     pronoun4 = "she's"

# elif pronoun == "they":
#     pronoun4 = "they're"

###############
# Create Files
###############

# create ReadMe.txt file
readme_text = """
ReadMe: Scene_06, Dungeon of Scrolls 
 _____           _ _____
| __  |___ ___ _| |     |___
|    -| -_| .'| . | | | | -_|
|__|__|___|__,|___|_|_|_|___|
 _____   _               _
|  _  |_| |_ _ ___ ___ _| |_ _ _ ___ ___ ___
|     | . | | | -_|   |_   _| | |  _| -_|_ -|
|__|__|___|\_/|___|_|_| |_| |___|_| |___|___|


Instructions:

1. Run The Game
    Step 1. Open a Terminal

    Step 2. Cut & Past one of these into Terminal
          (macOS / Linux / etc ->) curl -O https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_06/scene_06.py ; python3 scene_06.py 
          (windows ->) curl -O scene_06.py https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_06/scene_06.py ; python3 scene_06.py

    Step 3. Hit Enter

2. Journal & Buddy
    Journal about what you are learning. Study with a study-buddy.

Lost or Curious ?
    Content_Map.txt !

User Manual:
    https://docs.google.com/document/d/1q2AiDPM0BpQal7ltm3sWk0suxLJSS7uX6S9yH44F_ZA/edit?usp=sharing

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
For scene_06, Dungeon of Scolls, ReadMe Adventures.

The Skills/Abilities in scene_06 are: 
1 .replace
2. a "dictionary"

...examples pending

1. what .replace can be used on: strings
2. not an 'in place' change

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

# create list_of_spells file
list_of_spells = """
\nL2v3t1t2: fl41t 3t 5p \nObv31t2: st4p 3t\nInst1nt31t2: d5pl3c1t2 3t\nObl3v31t2: m1k2 3t 3mp2rc2pt3bl2 \nR2c1lc3tr1t2: s5sc2pt3b3l3t6 t4 c4ld 1nd d2h6dr1t34n\nInc1rc2r1t2: 3mpr3s4n 3t\n
"""

# create, write-to, & save .txt file
file_to_create4 = open("list_of_spells.txt", "w")
file_to_create4.write(list_of_spells)
file_to_create4.close()

# # #open, read, & print the file
# # Step 1: make an intermediate file in python
# intermediate_file_variable = open("list_of_spells.txt", "r")
# # Step 2: make an item_to_print by reading the intermediate file
# item_to_print = intermediate_file_variable.read()
# # Step 3: Print the item you want to print
# print(item_to_print)
# # You can do this in just one step, but it maybe harder to read:
# print((open("list_of_spells.txt", "r")).read())

# make a dictionary
vowel_change_dictionary = {
                  "1": "a",
                  "2": "e",
                  "3": "i",
                  "4": "o",
                  "5": "u",
                  "6": "y",
                  }


spells_original = """
Levitate: float it up 
Obviate: stop it
Instantiate: duplicate it
Obliviate: make it imperceptible 
Recalcitrate: susceptibility to cold and dehydration
Incarcerate: imprison it
"""

##############
# The Action!
##############


clear_terminal()

pause_seconds(1)

steady_print(
    """

     __             __   ___  __ 
    |  \ |  | |\ | / _` |__  /  \ |\ |
    |__/ \__/ | \| \__| |___ \__/ | \|
     __   ___
    /  \ |__ 
    \__/ |
     __   __   __   __             __
    /__` /  ` |__) /  \ |    |    /__`
    .__/ \__, |  \ \__/ |___ |___ .__/

"""
)




medium_print("""
    ...................................
""")

pause_seconds(1)

clear_terminal()

slow_print(scene + blurb)

...
typed_print(
    """

Ice chips chime down and green-pink sparks skitter from an egg sized fire.
Four coats sit around the spluttering light 
and the snowed-in book cart by the foot of the piney mountains.

Franklin reaches up and takes down a dust and ice crusted book. 
He frowns into the first few pages. 

"Morning tea, anyone? Jane asks.

"Uh, the...five...or...the three? Maybe?" babbles Franklin.

"Franklin."

"Oh, ...What did you ask?"

"Tea?"

"It's lovely, yes..."
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
Jane rolls her eyes and turns to Hitch. "Tea?"

"I'll have, uh...How long does it take to fly here from the tavern?"

Jane puts a cup of hot tea into Hitch's gloved hand 
and pats him on the shoulder. "She'll be back soon."

Franklin, with eyes still buried in his book, puts a hand in the air, 
where it wanders around. 
"Babbage, can you lend a hand with this?" he asks. 
"I think," Franklin goes on, 
"...I think I might see the issue...yes...uh no...yes..."

Hitch holds his hands palm up and squints at Franklin, 
shaking his head slightly.

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"See this?" Franklin says, turning the book about and pointing at the page. 
"This is supposed to be a list of spells. But it doesn't look like a list of 
spells. The words don't make any sense. 
It's a jumble of letters and numbers. See?"  

At the top of the page it says:

\nL2v3t1t2: fl41t 
3t 5p \nObv31t2: st4p 3t\nInst1nt31t2: 
d5pl3c1t2 3t\nObl3v31t2: m1k2 3t 
3mp2rc2pt3bl2 \nR2c1lc3tr1t2: s5sc2pt3b3l3t6 
t4 c4ld 1nd d2h6dr1t34n\nInc1rc2r1t2: 3mpr3s4n 3t\n
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"But what if...maybe because numbers are part of this kind of spellcasting... 
what if those numbers are the vowels? 
Babbage, can you test out that idea? 
Can you print this, switching the numbers for vowels?"

"Let's try," Franklin continues, "just one word and just one letter-change 
to start with,
so you can see what I mean."

"Can you rewrite 's' 'l' '2' '2' 'p' 
by replacing the number with the letter 'e'?
Can you try that out? 
's' 'l' '2' '2' 'p' "

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()


# Activity 1

steady_print(
    """
(Task!) Learn how to replace characters in a string.

You can use .replace to replace all of one thing for something else.
For example, replace all "a"s to "p"s, or every "1" to an "H", 
or "abc" to "xyz", or "e" to "123", 
you can replace anything with anything else. 

.replace will also print the results, but it does not save the changes in-place.

Example: 
  >>> any_text.replace("replace this", "replace it with this")


1. Open new Terminal
2. $ python
3. Use .replace to replace "2" with "e"
   >>> "sl22p".replace("number_here","letter_here")

"""
)


answer_check = False

while answer_check is False:
    answer = input('\n"Ok", says Franklin, "What word does that make?"\n')
    answer = answer.lower()
    # boolean check
    answer_check = "sleep" in answer
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

clear_terminal()


typed_print(
    """

"Great! Now let's try all the different vowels in one word...ready?"

"""
)


# Activity 2

steady_print(
    """
(Task!) Make a dictionary

A dictionary holds a very fast 'look-up' for a one-way relationship.

The standard terms are "key" and "value"
Using a normal word-dictionary as an example, the 'key' is the word, 
and the 'value' is the definition.

You "look up" a word, and you get the definition.
You "look up" the "key" and you get the "value."

When you make the dictionary a "dictionary" 
use curly brackets "{}" and a colon ":"
and then a comma "," between items. 
 
When you use the dictionary you use square brackets. 

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")

steady_print(
    """
For Example:

You can make a dictionary like this:
    >>> your_dictionary = {"one word" : "one definition",
                           "another word" : "another definition"}

(You can put all key:value pairs all on one line, but sometimes using new
lines are easier to read, which is important.)

To use your dictionary, you do something like this:
    >>> your_dictionary["one word"]

Result:
  "one definition"

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")

steady_print(
    """

Try making your number-to-vowels dictionary,
and then change all vowels in a word,
using a "for loop"
to move through every item in the dictionary:

1. Open new Terminal
2. $ python
3. >>> number_to_vowel_dict = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u", "6": "y"}
4. >>> word = "n3c2"
5. >>> for number in number_to_vowel_dict:
           word = word.replace(number, str(number_to_vowel_dict[number]))
5. >>> print(word)
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")

answer_check = False

while answer_check is False:
    answer = input('\n"What is that next word, "n3c2"?"\n')
    answer = answer.lower()
    # boolean check
    answer_check = "nice" in answer
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

clear_terminal()

typed_print(
    """
"Now you can do the same thing with the list of spells,
and we can see if it makes any sense," says Franklin. 

"""
)
# Activity 4

steady_print(
    """

use .replace to change all the vowels back to letters 
in Franklin's list of spells:

1. Open new Terminal in scene_06 folder (right click: 'open in terminal')
  (folders) ReadMe_Adventures ->  Learn_NLP__Dungeon_of_Scrolls ->
  -> scene_06 
  (You should see "list_of_spells.txt" in that folder.)
2. Check you are in the correct directory with $ ls & $ pwd then type:
    $ python3
3. >>> vowel_change_dict = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u", "6": "y"} 
4. >>> spells = open("list_of_spells.txt", "r").read()
5. >>> for number in vowel_change_dict:
           spells = spells.replace(number, str(vowel_change_dict[number]))
6. >>> print(spells)

"""
)


# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")

typed_print(
    """

"Ok, let's look at this spell list," says Franklin. "This looks a lot better."

"""
)


# Check the first spell
answer_check = False

while answer_check is False:
    answer = input('\n"What is the name of the last spell?"\n')
    answer = answer.lower()
    # boolean check
    answer_check = "incarcerate" in answer
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')


# Check the second spell
answer_check = False

while answer_check is False:
    answer = input('\n"What does the second spell do?"\n')
    answer = answer.lower()
    # boolean check
    answer_check = "stop" in answer
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')


clear_terminal()

typed_print(
    """

"Amazing!" says Franklin, "We've got our spell list now! 
Thank you, Babbage. Thank you kindly." 

"""
)



slow_print(f"\n\n End of {scene} {blurb} \n\n")
clear_terminal()
