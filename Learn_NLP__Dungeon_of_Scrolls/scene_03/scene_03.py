# version 003
# Scene_3
# Remember All
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


scene = "scene_03"
blurb = "  Remember All "
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
    # requests not available on termux, wget requires pip...
    # # check .py file
    # py_path = f"https://raw.githubusercontent.com/lineality/{game}/master/{adventure}/{scene}/{scene}.py"
    # if not os.path.exists(f"{scene}.py"):
    #     myfile = requests.get(py_path, allow_redirects=True)
    #     open(f"{scene}.py", 'wb').write(myfile.content)


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
    wait_time = 0.015
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
#manage_file_pathways()

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

# default to 'she'
if len(pronoun) == 0:
    pronoun = "she"

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

# pronoun_phrase_1
if pronoun == "he":
    pronoun_phrase_1 = "he doesn't"

elif pronoun == "she":
    pronoun_phrase_1 = "she doesn't"

elif pronoun == "they":
    pronoun_phrase_1 = "they don't"


# make sure file structure is correct
manage_file_pathways()


#################
### Create Files extra files for this tutorial scene
#################

# create file: readme_text
readme_text = """
ReadMe: Scene_03, Dungeon of Scrolls 
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
          (macOS / Linux / etc ->) curl -O https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_03/scene_03.py ; python3 scene_03.py 
          (windows ->) curl -O scene_03.py https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_03/scene_03.py ; python3 scene_03.py

    Step 3. Hit Enter
          (No python? -> https://www.python.org/downloads/ )

    ( For Windows_OS, see: https://docs.google.com/document/d/1p6R2LpBZtgs9IO349W1Zrx8u_Zy_5kgCxbJ64toOJXI/edit?usp=sharing )
    ( For MAC_OS, see: https:... )

2. Journal & Buddy
    Journal about what you are learning. Study with a study-buddy.

3. Lost or Curious
    Content_Map.txt !

4. User Manual
    https://docs.google.com/document/d/1q2AiDPM0BpQal7ltm3sWk0suxLJSS7uX6S9yH44F_ZA/edit?usp=sharing


"""
# create, write-to, & save .txt file
file_to_create1 = open("ReadMe.txt", "w")
file_to_create1.write(readme_text)
file_to_create1.close()

# #open, read, & print the file
# file_to_read1 = open("ReadMe.txt", "r")
# print(file_to_read1.read())


# create file: content map
content_map_text = """

Goal 1: Understanding "current working directory"
Goal 2: Understanding "changing directories"
Goal 3: skill/ability: Opening a Terminal directly in a folder (directory) 
Goal 4: skill/ability: Checking the pathway in the terminal
Goal 6: skill/ability: checking the contents of a folder (directory)
Goal 5: skill/ability: Being able to use the terminal in different operating systems (change, check, open)


In previous lessons, to make things easier at the beginning,
the game used temporary files make and removed wherever the terminal
happened to be. But since an important skill is using a terminal
in specific folders, and being able to navigate folders and files,
this lesson introduces just that set of skills.

Most likely, opening a terminal in a folder will be the newest
and potentially most challenging step. 


"""
# create, write-to, & save .txt file
file_to_create2 = open("Content_Map.txt", "w")
file_to_create2.write(content_map_text)
file_to_create2.close()

# #open, read, & print the file
# file_to_read2 = open("Content_Map.txt", "r")
# print(file_to_read2.read())


# create file:
advanced_instructions = """
 ...
"""

# create, write-to, & save .txt file
file_to_create3 = open("advanced_instructions.txt", "w")
file_to_create3.write(readme_text)
file_to_create3.close()

# #open, read, & print the file
# file_to_read3 = open("advanced_instructions.txt", "r")
# print(file_to_read3.read())


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
- Friend 1: Jane Adams
- Friend 2: Franklin Merln
- Friend 3: Lavender McCavity
- Friend 4: Gullover Hitch
Items Purchased:
- three pizzas
- 1 gallon of ginger-brew
- 1 cup of tea
- 1 book of dubious trail maps for tourists

(regulars)
- Four men in Kendal Green (difficult to see)
Items Purchased:
- fish'n chips x 4
- coffee x 8
- 2 books of crossword puzzles
- a dish towel
"""
# create, write-to, & save .txt file
file_to_create4 = open("inn_guest_log.txt", "w")
file_to_create4.write(inn_guest_log_text)
file_to_create4.close()

# # open, read, & print the file
# file_to_read4 = open("inn_guest_log.txt", "r")
# print(file_to_read4.read())



#########################
# Scene 2 Materials Files
#########################

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
Directions: Go to the base of Blossom Ridge Mountain.
"""
# create, write-to, & save .txt file
file_to_create6 = open("map_2.txt", "w")
file_to_create6.write(map_2)
file_to_create6.close()




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

# Main Story
typed_print(
    """
\nThe door closes behind you,
as you all stand on the creaking boards
outside of the inn.

"I have another question for you," says the girl in the green hat
as she turns towards you. "...Can you remember... EVERYTHING?
For example, can you recall what was on those maps, and
everything you read in the inn? Just curious...but, 
can you do that?"

"Can you remember what...
...can you remember what Old McSally was eating?"

"And what mountain was at the end of Map Two?"

"And..."

"""
)

typed_print(f'"Ok, ok, don\'t crowd {pronoun2}. Give {pronoun2} some air.')
typed_print(f' Let {pronoun2} answer..."\n')

# Press Enter to Continue
input("\n\n  ...Press enter to continue...  ")
clear_terminal()

fast_print(
    """
(Instructions)

Skill Goal: You can find and use all files and folders using a terminal.
The only NEW skill in this scene is:  Opening a terminal in a folder

Step 1: Find The Folder
This .py (python) game file created folders and files that look like this:

   ReadMe_Adventures ->  Learn_NLP__Dungeon_of_Scrolls ->
   -> scene_03 -> "map2.txt" & "inn_guest_log.txt"

First we need to find that folder for this scene: the "scene_03" folder.

To find the scene_03 folder, probably using your computer's 'file Exporer' 
or 'file Finder' is easiest. 

Task: Now, find the folder called "scene_03"

""")

# Press Enter to Continue
input('\n ...If you have found the "scene_3" folder , press enter to continue...')

clear_terminal()

fast_print(
    """
"Where" is the Terminal now?  

Skill/Ability Goal: Open a terminal in a Folder ("Folder" = "Directory")

(Understanding terminals)
A terminal can only see in one folder at a time. When a terminal is 
open in a folder, that is the only folder where the terminal can see and act.
(Type: "ls" and enter to see what is inside that folder. 
"ls" shows everything the terminal can see.)

If you ask the terminal to read a file outside of that one folder
it can see (without saying the target is outside), 
then the terminal will say: ...That file doesn't exit!
The one folder the terminal can see inside (at the moment)
is called the "working directory."

Where is your terminal now? 
Type "pwd" and enter in your terminal to see what folder you are in.
This shows you the Pathway of folders to your "current Working Directory"!

It is a good idea to check "ls" and "pwd" often to see where you are.
""")
# Press Enter to Continue
input("  ...Press enter to continue...  ")
fast_print(
    """
Moving the Terminal!

You can always use the 'cd' command (the 'Change Directory' command) 
to move the Terminal from one folder to the next.
For example: 
  $ cd ReadMe_Adventures" (moves into the ReadMe_Adventures folder)

Or you can move ahead more than one folder at at time:
  $ cd ReadMe_Adventures/Learn_NLP__Dungeon_of_Scrolls/scene_03

This moves you ahead three folders in one go.
But you can only move into a folder starting where the terminal can see.

You can also go backwards: (use this to go back one directory)
 $ cd .. 

But it is annoying to use 'cd' many times. 
It is easier and faster to open the Terminal in a folder directly. 


""")

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")

#clear_terminal()

fast_print(
    """

Mac Note: for Mac0S, you may need to configure your settings first:
( See this short guide here: https://www.youtube.com/watch?v=IAmsq1ULvSk )

  System Preferences > Keyboard > Shortcuts > Services
   -->  turn on "Enable New Terminal at Folder"


Now try it! Open a terminal in the scene_03 folder!!

Instructions for opening a Terminal in a folder: 
  Linux:   Right click in folder: "Open in Terminal"
  MacOS:   Right click in folder: Services -> "New Terminal at Folder"
  Windows: SHIFT Right click in folder: "Open Power Shell here"




""")

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n\n")

fast_print(
    """
(Scroll up to see instructions again.)

Now you can answer your friends' questions, 
all on your own, in just 3 steps:


1. Open new Terminal in scene_03 folder (right click ~'open terminal')
   (folders) ReadMe_Adventures ->  Learn_NLP__Dungeon_of_Scrolls ->
   -> scene_03 -> "map2.txt" & "inn_guest_log.txt"

2. Check you are in the correct directory with these commands:
    $ ls
    $ pwd

3. Type:   (Don't type '$' or '>' signs.  Press Enter after each line.)
      $ python3
    >>> name_you_choose = open("inn_guest_log.txt", "r").read()
    >>> print(name_you_choose)
    >>> name_you_choose = open("map2.txt", "r").read()
    >>> print(name_you_choose)
"""
)



answer_flag = False
while answer_flag is False:
    typed_print ("""

    "So, what was Old McSally was eating?"
    """
    )
    answer = input()
    answer = answer.lower()

    if ("capon" in answer) or ("rooster" in answer) or ("chicken" in answer):
        answer_flag = True

    if ("sauce" in answer) or ("wine" in answer) or ("sack" in answer):
        answer_flag = True

    if ("crouton" in answer) or ("bread" in answer):
        answer_flag = True

    if answer_flag is False:
        typed_print(f'"{random.choice(responses)}"')



typed_print (f'\n"That\'s amazing. I can\'t believe {pronoun} remembered that."\n')

typed_print ("""
"Ok, next question.
What mountain... 
Are you ready?"
"""
)

#typed_print (f'\n"Let\'s see if {pronoun} can answer that one..."')




answer_flag = False
while answer_flag is False:
    typed_print ("""

    "What mountain...did the second map talk about at the very end?"
    """
    )
    answer = input()
    answer = answer.lower()

    if ("blossom" in answer) or ("flower" in answer) or ("bloom" in answer):
        answer_flag = True

    if ("peaks" in answer):
        answer_flag = True

    if answer_flag is False:
        typed_print(f'"{random.choice(responses)}"')

clear_terminal()

typed_print(
    """\n
"That's just incredible. Spot on. Look at that." One of them says, 
as he holds out a map 
and jabs his finger pointedly
at the page's bottom.

"Ok...everyone has their stuff?
Are we all ready?"


"""
)

slow_print("\nEnd of Scene 3\n\n")


