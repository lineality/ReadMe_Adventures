# version 004
# Scene_07
# Here Is A Notebook
#  _____           _ _____
# | __  |___ ___ _| |     |___
# |    -| -_| .'| . | | | | -_|
# |__|__|___|__,|___|_|_|_|___|
#  _____   _             _
# |  _  |_| |_ _ ___ ___| |_ _ _ ___ ___ ___    ___ _ _
# |     | . | | | -_|   |  _| | |  _| -_|_ -|  | . | | |
# |__|__|___|\_/|___|_|_|_| |___|_| |___|___|()|  _|_  |
#                                              |_| |___|

import json
import os  # for terminal functions etc.
import random  # for randomized replies etc
import sys  # for realistic printing
import time  # for pauses


scene = "scene_07"
blurb = " Here Is A Notebook "
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
ReadMe: Scene_07, Dungeon of Scrolls 
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
          (macOS / Linux / etc ->) curl -O https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_07/scene_07.py ; python3 scene_07.py 
          (windows ->) curl -O scene_07.py https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_07/scene_07.py ; python3 scene_07.py

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
For scene_07, Dungeon of Scolls, ReadMe Adventures.

The Skills/Abilities in scene_06 are: 
1. virtual environments
2. notebooks

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


# This creates a working notebook file, which is a json file
# that has a ".ipynb" suffix
# so the file must be created as a json file.

# this cludge stops 'null' in notebook json from messing up python
null = 0

# create ReadMe.txt file
A_Notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ljc8eY5cAGVe"
   },
   "source": [
    "set to no dupe"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hu1K53Je6gBd"
   },
   "source": [
    "# This is a \"Notebook\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "9RWKFekBAMIk"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ucdw01Bb9s0V"
   },
   "source": [
    "## About python Notebooks:\n",
    "These text \"cells\" use formatting called \"markdown\"\n",
    "\n",
    "Double click on one to *see* the formatting."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qOtnmROk99x_"
   },
   "source": [
    "### Those code cells below are python code. Each cell can be \"run\" as a separate cell."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dX_fcxCX-K-H"
   },
   "source": [
    "#### Or all the cells in the whole Notebook can be run together.\n",
    "(See controls at the top of the page.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "JxN_Zn-7-JFp"
   },
   "outputs": [],
   "source": [
    "# Text in a code cell starting with a '#' sign is not run. It's just text."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "zoF6P_7E-pqi"
   },
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Same for text-blocks in triple quotes, but these can be harder to use.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "F-4zZAIi-zKS"
   },
   "source": [
    "# Some Python Basics:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "D-_5d9Z06kr8",
    "outputId": "e092f04c-71c7-4500-af73-0a7b6286bb7a"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 1,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2+2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "uBC5Mkhq6oH3",
    "outputId": "d748aa85-6779-4474-e9f3-705b217003ca"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello_World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello_World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "obI95ZcF-159"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "babE4j2F67Ro"
   },
   "outputs": [],
   "source": [
    "message = \"\"\"hello world\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "C-sgVxqZ7Bvd",
    "outputId": "aad597fc-3a71-4bad-a572-fabea47b24a3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "hAKFfnki7EAv",
    "outputId": "c21d83ca-6b32-4d19-e641-5388cae90c83"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "'hello world'"
      ]
     },
     "execution_count": 12,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "45Bv8_qf6r70"
   },
   "outputs": [],
   "source": [
    "message = \"\"\"hello \n",
    "world\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "tbJzKN1V6vNl",
    "outputId": "f52cb788-9daa-44f2-b61c-cc5d9f14a125"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello \n",
      "world\n"
     ]
    }
   ],
   "source": [
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "PN2F8BHR-4Kl",
    "outputId": "668f6c85-0065-423e-fbf0-cd77446a9105"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "'wolftree!'"
      ]
     },
     "execution_count": 20,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "animal = \"wolf\"\n",
    "\n",
    "plant = \"tree\"\n",
    "\n",
    "animal + plant + \"!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "alpC6H277Sgp"
   },
   "source": [
    "## Note the \\n new line 'escape character' in the raw print."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "dAyg44Fu7FlQ",
    "outputId": "688674f2-d75c-4c48-828c-3c86d6cf4906"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "'hello \\nworld'"
      ]
     },
     "execution_count": 17,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "message"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "kjsZbbEp_U8F"
   },
   "source": [
    "# Review"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "kE5S0T7O6k6c"
   },
   "source": [
    "## Scene_01\n",
    "## opening files\n",
    "## printing files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gZhu-KCY7hNr",
    "outputId": "896cd6b1-eecf-44d2-c7f8-e2287f072fe8"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sample \n",
      "Text\n",
      "\n",
      "\n",
      "Sample \n",
      "Text\n"
     ]
    }
   ],
   "source": [
    "# create file: readme_text\n",
    "text_to_add_to_file = \"\"\"\n",
    "Sample \n",
    "Text\n",
    "\"\"\"\n",
    "\n",
    "# create, write-to, & save .txt file\n",
    "file_to_create1 = open(\"example.txt\", \"w\")\n",
    "file_to_create1.write(text_to_add_to_file)\n",
    "file_to_create1.close()\n",
    "\n",
    "# #open, read, & print the file\n",
    "\n",
    "file_to_read1 = open(\"example.txt\", \"r\")\n",
    "print(file_to_read1.read())\n",
    "file_to_read1.close()\n",
    "\n",
    "# Another way to print a file in a terminal\n",
    "!cat example.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vyloYNxA1OK1"
   },
   "source": [
    "## \"with\" method\n",
    "### This is the recommended best practice for opening and closing files...at least according to some people. The idea is to ensure that files are closed properly...I think.\n",
    "\n",
    "https://www.python.org/dev/peps/pep-0343/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "A6qnxTrm2qP9",
    "outputId": "e75e6c91-b808-4c03-c4bc-6d53d0bcd64d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sample \n",
      "Text\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open('example.txt') as f:\n",
    "    print(f.read())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "9pSTIz9Jyv-A"
   },
   "source": [
    "## note: a notebooks is *like* a terminal but they are not exactly the same. \n",
    "\n",
    "### e.g.\n",
    "### some terminal commands need a \"!\" in front in order to work."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Hddmi-zQzEGq",
    "outputId": "0ceb6bb1-4a07-4bd5-e1a7-e07dbea44e71"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/content\n",
      "example.txt  ReadMe.txt  sample_data\n",
      ".  ..  .config\texample.txt  ReadMe.txt  sample_data\n",
      "60\t./.config/logs/2021.01.20\n",
      "64\t./.config/logs\n",
      "8\t./.config/configurations\n",
      "100\t./.config\n",
      "55508\t./sample_data\n",
      "55620\t.\n",
      "\n",
      "Sample \n",
      "Text\n"
     ]
    }
   ],
   "source": [
    "# pathway to current working directory\n",
    "!pwd\n",
    "\n",
    "# list files in directory\n",
    "!ls\n",
    "\n",
    "# list files including hidden files\n",
    "!ls -a\n",
    "\n",
    "# show file 'ownership'\n",
    "!du\n",
    "\n",
    "# print file\n",
    "!cat example.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6kSnXbLp7hNp"
   },
   "source": [
    "## Scene_02\n",
    "## len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "CiKL9X-T_WaF",
    "outputId": "7b6399f3-9151-4c91-eba9-34e1a213c7ff"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 12,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "example = \"abcd\"\n",
    "\n",
    "len(example)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ybjtToi47nky"
   },
   "source": [
    "## Scene_03\n",
    "### Navigating Folders (Directories)\n",
    "### Note: real terminals and notebooks work differently here..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "A_hQEE3m9iIG",
    "outputId": "0091a523-b926-47c2-f9b6-32e7e95ea95a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/content\n"
     ]
    }
   ],
   "source": [
    "# where are we?\n",
    "!pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "DtKzHVod6YG7"
   },
   "outputs": [],
   "source": [
    "# make a new place\n",
    "!mkdir testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "U4CqKoI_7bfP",
    "outputId": "723395b9-62e2-48dc-fe34-2e677fbff699"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "example.txt  ReadMe.txt  sample_data  testing\n"
     ]
    }
   ],
   "source": [
    "# check all the places\n",
    "!ls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "iMu4yKxC9qPG"
   },
   "outputs": [],
   "source": [
    "# moving to a new directory\n",
    "!cd testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "Tv0b0La6-M-M"
   },
   "outputs": [],
   "source": [
    "# go back on space\n",
    "! cd ..\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "FcFyew7o9vfu",
    "outputId": "8d9a349c-6866-4dd4-c73e-519a0d9530f7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/content\n"
     ]
    }
   ],
   "source": [
    "# check were you are agian\n",
    "!pwd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "-wT4a2Yt7vGM"
   },
   "source": [
    "## Scene_04\n",
    "## Slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "TmWxliI57vGt",
    "outputId": "1e660d93-86c8-42a5-842d-5618182fb2ff"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 25,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# slice a string\n",
    "sample_string = \"abc\"\n",
    "sample_string[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "tBdnPPq-_Pf2",
    "outputId": "b91f7877-c62e-4220-bef3-02ff55995054"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 29,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# slice a list/array\n",
    "sample_array = [\"a\", \"b\", \"c\", \"d\", \"e\"]\n",
    "\n",
    "sample_array[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "BLs_wvrW_h7K",
    "outputId": "8be0dcb5-78fe-47a8-e195-7efb95330d50"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['e', 'd', 'c', 'b', 'a']"
      ]
     },
     "execution_count": 30,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# reverse slice!\n",
    "sample_array[::-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "NjrSy7Xx7vGu"
   },
   "source": [
    "## Scene_05\n",
    "## Slice From Here & To There\n",
    "## [here,there]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Lqreknb9ASwg",
    "outputId": "5d511f21-d20e-4bf9-839f-c827b70f102d"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['b', 'c']"
      ]
     },
     "execution_count": 32,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# slice from and to\n",
    "sample_array[1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "27u9lnvSAiNo"
   },
   "outputs": [],
   "source": [
    "# count backwards"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 35
    },
    "id": "D-B5YZ3yAfPW",
    "outputId": "76eb1523-e7b1-4209-ae39-a3e82b22fd02"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 33,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sample_array[-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "CvmlOp4B7vGu"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "rEWMwGjp7vGv"
   },
   "source": [
    "## Scene_06\n",
    "## .replace()\n",
    "## Make a Dictionary\n",
    "## Dictionary + For Loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "Njw_1w-B7vGv"
   },
   "outputs": [],
   "source": [
    "spells = \"Pr4p2rt6 4f P3n6 H3lls Un3v2rs3t6\"\n",
    "\n",
    "# make a dictionary\n",
    "vowel_change_dict = {\"1\": \"a\", \"2\": \"e\", \"3\": \"i\", \"4\": \"o\", \"5\": \"u\", \"6\": \"y\"} \n",
    "\n",
    "# user a for loop\n",
    "for number in vowel_change_dict:\n",
    "           # safe the changes each time\n",
    "           spells = spells.replace(number, str(vowel_change_dict[number]))\n",
    "\n",
    "print(spells)\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [
    "vyloYNxA1OK1",
    "9pSTIz9Jyv-A",
    "6kSnXbLp7hNp",
    "ybjtToi47nky"
   ],
   "name": "A_Notebook.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0b5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

# Save notebook as json file:
with open('A_Notebook.ipynb', 'w') as outfile:
    json.dump(A_Notebook, outfile)

# # create, write-to, & save .txt file
# file_to_create1 = open("A_Notebook.ipynb", "w")
# file_to_create1.write(A_Notebook)
# file_to_create1.close()



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

# First Dialogue
typed_print("""

Starting out as light grey dots in a light grey snowy sky,
a flock of snow geese flap and glide. 

As they grow from little dots to bigger dots
one goose looks to have something tied to one of its legs. 

Gliding down between frosted pine trees 
into a clearing nearby,
one by one a few of the big white birds 
begin to waddle towards the book cart. 

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

# Dialogue
typed_print("""

"Finally," says Hitch as he grabs up some woolen blankets and stands up. 
"Made some new friends, did you? 
Always the life of the party. 
...Or am I talking to a flock of migrating birds..."

A goose walks out of the gaggle and over to Hitch,
dragging a pouch tied around an ankle. 
Hitch runs over to it and throws a blanket
over the snow next to it. "Come on," he says,
"You won't want your feet in the snow."

The goose stands where it is and shakes its leg,
tugging around the tethered bundle.
Hitch squints and then says "Oh, right,"
and he kneels down and works through the knot.

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

# Dialogue
typed_print("""

After the bundle's tether is undone
Hitch stands back up, and glances over at the fire.

"All right, up on the rug then," he says,
and when the bird steps into the middle of the wool
he tosses his other blanket over the goose.

The blanket floats down 
over the shape moving beneath the surface,
and then pulls back around Lavender's head 
as she shakes out her hair in the blowing show.

"You should put some boots on, it's cold out," he says,  
"What's happened to your hair?"

"Babbage", Lavender calls out.
"Look in that bag. Present from Old John."

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

# Dialogue
typed_print("""

Turning back to Hitch she asks, "Thanks for the blanket. 
Do you have my snow boots? I'm starving. Did you make tea?"

As you pick up the bundle and reach inside
Franklin somes over to look
"What is it?"
"Wo! A Notebook? Where did they find that?
Those have been banned for years."

Jane comes over as Hitch curries McCavities boots and 
other clothes back over to her.

"It's a what?" asks Jane

"It's a notebook," says Franklin. 

"Are you sure? It doesn't look like a book."

"""
)



# Dialogue
typed_print("""

"It's a Code Notebook," says Franklin. "Try and opening it.
Let's run it and see what it says at the end. Maybe we can see
where it came from."

In terminal, in scene_07 folder:
$ python3 -m venv this_environment; source this_environment/bin/activate
$ jupyter notebook

Under the "Run" menu tab at the top, select: "Run All Cells"

"""
)


# Question Code 

answer_check = False

while answer_check is False:
    answer = input('\n"What does that last line say?"\n')
    answer = answer.lower()
    # boolean check
    answer_check = ("property" in answer) or ("hill" in answer) or ("piny" in answer)
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()


# https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

# # Dialogue
# typed_print("""



# See files listed in jupyter notbook

# """
# )



# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()


# Second Dialogue
typed_print(
    """
"That's a weird fire. What are you burning."

"Those bits of frozen birds."

"You're burning frozen birds?"

"What else are we supposed to burn out here, ice?"

"Um...wood?"

"Oh...right."

"Old John sends his thanks." 
"""
)


# answer_check = False

# while answer_check is False:
#     answer = input('\n"Ok", says Franklin, "What word does that make?"\n')
#     answer = answer.lower()
#     # boolean check
#     answer_check = "sleep" in answer
#     if answer_check is False:
#         typed_print(f'"{random.choice(responses)}"')

# clear_terminal()


# typed_print(
#     """

# If no pip on debian/ubuntu etc:
# $ sudo apt install python3-pip

# If no pip on RPM (fedora, redhat, centos, etc.)
# $ sudo install python3-pip

# Install pipenv:
# $ pip install --user pipenv

# Add "pipenv" to paths (so that it works in the command line)
# $ export PATH="$PATH:$HOME/.local/bin"



# """
# )


slow_print(f"\n\n End of {scene} {blurb} \n\n")
clear_terminal()
