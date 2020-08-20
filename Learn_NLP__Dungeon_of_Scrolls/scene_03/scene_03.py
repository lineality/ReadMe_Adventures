# version 001
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
    random_times = [0.005]
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
Content Map
For scene_01, dungeon of scolls, ReadMe Adventures.

Coding is about communication.

The first goal
(in this first lesson of the course)
is to open and "print" a file in python
so that you can read it
either in a terminal
or in a notebook.

There are a few 'computer science' parts to this, such as 'variables.'
And there are a few python-specific parts to this, the steps.

Step 1: Find the name of the file you want to open
in this case: inn_guest_log.txt

One thing you will deal with every day is 'folders' or 'directories'
as they are often called in tech-speak.

For this course, your files will be
automatically put into a system of folders
when they are created on your computer

game_folder -> adventure_folder -> scene_folder

in this case:
ReadMe_Adventures -> Learn_NLP__Dungeon_of_Scrolls -> scene_01

If you look at the .py file (which is a good idea)
you will see these same items listed out.

scene = "scene_01"
blurb = "  Find Your Friends "
adventure = "Learn_NLP__Dungeon_of_Scrolls"
game = "ReadMe_Adventures"

using standards names for things makes everything easier
to find and deal with.

In these folders (game_folder -> adventure_folder -> scene_folder)
you will find the file you need: inn_guest_log.txt

(Note:
You can view the text of the inn_guest_log.txt in a text editor
or by looking at the .py (scene_01.py) file itself in a text editor,
or maybe in a word processor (depending on your computer),
and you should try and be able to do all of those in case you need to,
(to open a file in atom: atom inn_guest_log.txt )
(to open the whole folder in atom: atom . )
but other method described here will be using python to disply the text.)

Step 1: Get to the right file location...Where are you now?

Here are some handy python directory functions:

# python directory functions
os.getcwd()  # pwd pathway to working directory (where you are) (same as python cwd "current" working directory)
os.chdir("..")  # go back only one directory
os.listdir()  # lists all files in that directory same as "ls" in posix or "DIR" in windows
os.mkdir("target")  # mkdir, create a new folder/directory
os.chdir("../target")  # "change" move into exsting directory / folder
os.path.exists("../target")  # checks if folder or file exists
os.path.isdir("../target")  # checks if x is the directory (not whole path) or are in...

You can do this either in your computer's terminal, or in python
you may want to practice both. The notation for each is a bit different
(and windows is differnt from the 'posix' standard that just about
every other OS uses)

Notation:
The terminal sign is (usually) "$", so this means type "pwd" in the terminal
The python sign is ">>>" so

These commands below will show you where you are (two steps in python)
in the file-system of the computer, what 'directory' you are 'in'
in terminal: $ pwd
in python:  >>> import os
and then    >>> os.getcwd()

If you don't see any of the folders you need, then either:
1. you need to find them (using your OS file explorer may be best)
2. or make them if they do not exist (running the .py will make them for you)

To get into a directory, stepping through each step is often long and boring.
When possible, go to that folder in your OS file explorer and open a terminal
in that directory (windowsOS makes this strange but the idea is the same).

In the future we will first make a custom python environment,
usually using pipenv or anaconda (there are many other options too,
and you should explore as many as you can, eventually).

Step 2: double check
When you are in the right directory, it is always good to check to see
where you are. Checking is very fast,
and doing something in the wrong directory makes a mess which wastes time
to clean up. Kind of a "measure twice, cut once" approach.

posix:    $ ls
windows:  > dir

(Note: there are many websites and videos on topics like this,
and usually a good resource is just a quick search away.)

(Note: this whole process is also part of using github, which hopefully
we will practice later in this course)


Step 3: open the file
When you see the file you want listed amongst all the other files in
that directory...there are 2(?) ways to read the file (in this context):
1: use a text editor: good to know and you will usually do this:
    to open a file in atom: atom inn_guest_log.txt
    to open the whole folder in atom: atom .
    to open a file in vsCode: code inn_guest_log.txt
    to open the whole folder in vsCode: code .

2: use python: you won't do this as often, but very often you will need to
do this at least once the beginning of a project to get your data loaded:

# to open, read, & print the file
intermediate_file_variable = open("file_you_pick.txt", "r")
print(intermediate_file_variable.read())

While clicking on an icon, or typing: $ atom .
are just one step
in python we use 2 steps. Why?
This is a good example of how coding is about communication and readability.
You can do this in just one step, but it maybe harder to read:
>>> print((open("advanced_instructions.txt", "r")).read())

In two steps we save the item as a variable before putting into the print
function(or 'method'). This is also an important step because sometimes you
MUST put a variable into a function (where you cannot cram a lot of other code in)
1. create an intermediate variable from the file
2. read and print that intermediate variable

We could have done 3 steps with another item to print variable...
maybe that would be more clear? is 2 steps clear enough?
Do whatever you think is clear enough and works.

# 3 step example:
# to open, read, & print the file

# Step 1: make an intermediate file in python
intermediate_file_variable = open("advanced_instructions.txt", "r")
# Step 2: make an item_to_print by reading the intermediate file
item_to_print = intermediate_file_variable.read()
# Step 3: Print the item you want to print
print(item_to_print)


You can do this in just one step, where everything is being done
all together. Some people say they like "one-liners,"
but do you think it's a good idea to be unclear? We all make choices.

>>> print((open("advanced_instructions.txt", "r")).read())

Which of the above methods do you like best?
1 step
2 steps?
3 steps?

Experiment:

The default instructions are:
    >>> name_you_choose = open("inn_guest_log.txt", "r").read()
    >>> print(name_you_choose)

but what is you didn't say print? Not saying print before a number
is usually fine, but what happens here?
    >>> name_you_choose = open("inn_guest_log.txt", "r").read()
    >>> name_you_choose

or just
    >>> open("inn_guest_log.txt", "r").read()

Note:
in posix (linux, ios, bsd, unix, etc) you may need to use
control shift C/V to cut and paste.

Misc:

"Coding is about communication."

Remember, like in real life, there is no such thing as 'cheating' when you are
fully understanding code. You want to see and understand everything.

Study the .py file. Will it 'give you the answers'? It should.
You are trying to understand how it works, so look at it.
If studying what you want to understand works, you succeeded.

There is no single way to solve these or nearly any programing problem,
so try to understand as many ways as you can.

Look at everyting. Read everything. Try everything.
Internet-search questions on everything.

You want your code to be readable, which means it should NOT
look completely alien strange and unique to only that one project for you.
There is no "plagerism" in writing clean code.
2+2=4 SHOULD look similar when different people write it.
There is no such thing as code 'not being unique enough' to work properly.
Your goal is to write code the works very very well and will keep working very
very well for as many users and realistic situations as possible.

Your file names and program should not be 100% unique just for the sake of
being absolutely unique.

In this lesson you will learn to open a file. You do not need an absolutely
unique way of opening a file that is unique to you and unique every time you
open a file. That would be a hard to read and understand,
and being hard to understand would be a catastrophy.

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
Advanced Instructions for Installing and Setup For ReadMe Adventures

"ReadMe Adventures" is a minimal game-system that requires just two files
to play, and just one of those files to get started, a ReadMe.txt

For Windows_OS configuration: https://docs.google.com/document/d/1p6R2LpBZtgs9IO349W1Zrx8u_Zy_5kgCxbJ64toOJXI/edit?usp=sharing

3. Running the .py file will
run the interactive story in the terminal
and will create new files
that you can use during the scene.
Look for these folders and files
in the directory (folder) that your command terminal is open in.
(This file may be updated as well.)

3. (quasi spoiler)
Since it is lying on the bar-counter in front of you,
you can 'access' the inn's guest-register.
Check your file directory again.
(This will help you to answer
the red-nosed innkeeper's question.)

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


in windows powershell
wget -OutFile filename url
e.g.
wget -Outfile scene_01.py https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_01/scene_01.py

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
    .....................................
""")

pause_seconds(1)

clear_terminal()


slow_print(scene + blurb)

# Main Story
typed_print(
    """
\nThe front door to the inn closes behind you,
and the wind gusts up, showering you all with bits 
of tree bark
and crushed rock, 
as you huddle outside.

"I've got one more question for you. ...Can you remember everything?
Like, can you recall what was on those maps, and
everything you read in the inn? Just curious...but, can you do that?"

"For example...can you remember what...
...can you remember what Old McSally was eating?"

"And what mountain was at the end of Map Two?"

"""
)

typed_print(f'"Ok, ok, don\'t crowd {pronoun2}. Give {pronoun2} some air.')
typed_print(f' Let {pronoun2} answer..."\n')

# Press Enter to Continue
input("\n\n  ...Press enter to continue...  \n")
clear_terminal()

steady_print(
    """
(Instructions)


The only NEW part of this challenge is:  Opening a Terminal in a folder

This .py file created folders and files that look like this:

   ReadMe_Adventures ->  Learn_NLP__Dungeon_of_Scrolls ->
   -> scene_03 -> "map2.txt" & "inn_guest_log.txt"

To find the folder, probably your computer's 'file Exporer' or 'file Finder'
is easiest: Find a folder called "scene_03"

""")

# Press Enter to Continue
input("\n  ...Press enter to continue...  ")

clear_terminal()

steady_print(
    """
Goal: Open a Terminal In a Folder ("Directory" = "Folder")

A Terminal can only see in one folder at a time.
If you ask the terminal to read a file outside of the one folder
it can see, then Terminal will say: That file doesn't exit!
The one folder the terminal can see is called the "working directory."

You can always use the 'cd' command ('Change Directory' command) 
to move the Teriminal from one folder to the next.
For example: cd ReadMe_Adventures (to go into that folder)
but it's annoying to do that many times. 
It is easier and faster to open the Terminal in that folder directly. 


""")

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")


steady_print(
    """

Instructions: 
  Linux:   Right click in folder: "Open in Terminal"
  MacOS:   Right click in folder: Services -> "New Terminal at Folder"
  Windows: SHIFT Right click in folder: "Open Power Shell here"

Mac Note: for Mac0S, you may need to configure your settings:
( See short guide here: https://www.youtube.com/watch?v=IAmsq1ULvSk )

  System Preferences > Keyboard > Shortcuts > Services
   -->  turn on "Enable New Terminal at Folder"

Additional way: On mac you MAY be able to drag that folder to the Terminal icon.



""")

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")

steady_print(
    """
(Scroll up to see instructions again.)

You can do it! 3 Steps:

1. Open new Terminal in scene_03 folder (right click ~'open terminal')
   (folders) ReadMe_Adventures ->  Learn_NLP__Dungeon_of_Scrolls ->
   -> scene_03 -> "map2.txt" & "inn_guest_log.txt"

2. Check you are in the correct directory with these commands:
    $ ls
    $ pwd

3. Type: (Don't type '$' or '>' signs.  Press Enter after each line.)
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

    So, what was Old McSally was eating?"
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

"Well...the winds sure are picking up. 
Let's get going."

"""
)

slow_print("\nEnd of Scene 3\n\n")


