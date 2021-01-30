# version 006
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

# .ipynb cludge notes
# this cludge stops 'null' in notebook json from messing up python
null = 0
# items like                  "toc_visible": true 
# may need to be changed to   "toc_visible": True
# which appears to run fine

# create ReadMe.txt file
A_Notebook = {
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "A_Notebook.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
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
      "cell_type": "markdown",
      "metadata": {
        "id": "ucdw01Bb9s0V"
      },
      "source": [
        "## About python Notebooks:\n",
        "These text \"cells\" use formatting called \"markdown\"\n",
        "\n",
        "Double click on one to *see* the formatting.\n",
        "\n",
        "e.g.\n",
        "\n",
        "```\n",
        "## About python Notebooks:\n",
        "These text \"cells\" use formatting called \"markdown\"\n",
        "\n",
        "Double click on one to *see* the formatting.\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ptb-BoiIca2u"
      },
      "source": [
        "A python notebook file has the suffix .ipynb"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qOtnmROk99x_"
      },
      "source": [
        "### Those code cells below are python code. Each cell can be \"run\" as a separate cell.\n",
        "\n",
        "Tip: Rerun your cells in-order often with a restarted/refreshed kernal/runtime."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dX_fcxCX-K-H"
      },
      "source": [
        "#### Or you can run all the cells in the whole Notebook\n",
        "(See controls at the top of the page: ~\"Run all\")"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JxN_Zn-7-JFp"
      },
      "source": [
        "# Text in a code cell starting with a '#' sign is not run. It's just text."
      ],
      "execution_count": 51,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zoF6P_7E-pqi",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "d1add304-0a5d-40ab-e878-d563c1fb0746"
      },
      "source": [
        "\"\"\"\n",
        "Same for text-blocks in triple quotes, but these can be harder to use.\n",
        "\"\"\""
      ],
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'\\nSame for text-blocks in triple quotes, but these can be harder to use.\\n'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 52
        }
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
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D-_5d9Z06kr8",
        "outputId": "901a36ac-a7ac-4480-d405-af90cb2ae74b"
      },
      "source": [
        "2+2"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uBC5Mkhq6oH3",
        "outputId": "7a81590c-5ff8-4783-8136-2eb7391718d0"
      },
      "source": [
        "print(\"Hello_World\")"
      ],
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello_World\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "babE4j2F67Ro"
      },
      "source": [
        "message = \"\"\"hello world\"\"\""
      ],
      "execution_count": 55,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C-sgVxqZ7Bvd",
        "outputId": "33fc1c13-4159-4834-f53f-08adb48feeac"
      },
      "source": [
        "print(message)"
      ],
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "hello world\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "hAKFfnki7EAv",
        "outputId": "62a0972d-7fe5-4064-a4f9-f04a37085a09"
      },
      "source": [
        "message"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'hello world'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "45Bv8_qf6r70"
      },
      "source": [
        "message = \"\"\"hello \n",
        "world\"\"\""
      ],
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tbJzKN1V6vNl",
        "outputId": "8851351b-2af4-4db0-f8b7-f8305c92250e"
      },
      "source": [
        "print(message)"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "hello \n",
            "world\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "PN2F8BHR-4Kl",
        "outputId": "aab35b15-22a1-4fdf-c7e4-c3408fad090a"
      },
      "source": [
        "animal = \"wolf\"\n",
        "\n",
        "plant = \"tree\"\n",
        "\n",
        "animal + plant + \"!\""
      ],
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'wolftree!'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 60
        }
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
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "dAyg44Fu7FlQ",
        "outputId": "ae5dc1e0-ab83-40e3-99ef-839d28de2eba"
      },
      "source": [
        "message"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'hello \\nworld'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kjsZbbEp_U8F"
      },
      "source": [
        "# Review Past Scenes"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kE5S0T7O6k6c"
      },
      "source": [
        "## Scene_01\r\n",
        "## opening files\r\n",
        "## printing files"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gZhu-KCY7hNr",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4c965b9f-6a17-4e9e-f689-92f02ad84ad1"
      },
      "source": [
        "# create file: readme_text\r\n",
        "text_to_add_to_file = \"\"\"\r\n",
        "Sample \r\n",
        "Text\r\n",
        "\"\"\"\r\n",
        "\r\n",
        "# create, write-to, & save .txt file\r\n",
        "file_to_create1 = open(\"example.txt\", \"w\")\r\n",
        "file_to_create1.write(text_to_add_to_file)\r\n",
        "file_to_create1.close()\r\n",
        "\r\n",
        "# #open, read, & print the file\r\n",
        "\r\n",
        "file_to_read1 = open(\"example.txt\", \"r\")\r\n",
        "print(file_to_read1.read())\r\n",
        "file_to_read1.close()\r\n",
        "\r\n"
      ],
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "Sample \n",
            "Text\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AqRio51Sd-an",
        "outputId": "857307a6-73f3-43c7-e4df-48e49b36ae88"
      },
      "source": [
        "# Another quick way to print a file in a terminal\n",
        "!cat example.txt"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "Sample \n",
            "Text\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vyloYNxA1OK1"
      },
      "source": [
        "## \"with\" method\r\n",
        "### This is the recommended best practice for opening and closing files...at least according to some people. The idea is to ensure that files are closed properly...I think.\r\n",
        "\r\n",
        "https://www.python.org/dev/peps/pep-0343/"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A6qnxTrm2qP9",
        "outputId": "480571a8-3eef-4e4c-912d-34a398497207"
      },
      "source": [
        "with open('example.txt') as f:\r\n",
        "    print(f.read())"
      ],
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "Sample \n",
            "Text\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9pSTIz9Jyv-A"
      },
      "source": [
        "## note: a notebooks is *like* a terminal but they are not exactly the same. \r\n",
        "\r\n",
        "### e.g.\r\n",
        "### some terminal commands need a \"!\" in front in order to work."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hddmi-zQzEGq",
        "outputId": "990df3ad-427d-4c0d-ab14-a3fa7803173e"
      },
      "source": [
        "# pathway to current working directory\r\n",
        "!pwd\r\n",
        "\r\n",
        "# list files in directory\r\n",
        "!ls\r\n",
        "\r\n",
        "# list files including hidden files\r\n",
        "!ls -a\r\n",
        "\r\n",
        "# show file 'ownership'\r\n",
        "!du\r\n",
        "\r\n",
        "# print file\r\n",
        "!cat example.txt"
      ],
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content\n",
            "example.txt  sample_data  testing\n",
            ".  ..  .config\texample.txt  sample_data  testing\n",
            "8\t./.config/configurations\n",
            "60\t./.config/logs/2021.01.20\n",
            "64\t./.config/logs\n",
            "100\t./.config\n",
            "4\t./testing\n",
            "55508\t./sample_data\n",
            "55620\t.\n",
            "\n",
            "Sample \n",
            "Text\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6kSnXbLp7hNp"
      },
      "source": [
        "## Scene_02\r\n",
        "### len()\r\n",
        "#### How long is a string, list, dictionary, etc.?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CiKL9X-T_WaF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "be4a5076-1285-4316-ee56-89e8f84cd4c2"
      },
      "source": [
        "example_string = \"abcd\"\r\n",
        "\r\n",
        "len(example_string)"
      ],
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IhaPuvmSbU_K",
        "outputId": "b70c5ae4-aeb6-4cb6-eeba-b89454c7f40f"
      },
      "source": [
        "number_list = [1,'2','3']\n",
        "len(number_list)"
      ],
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eMah_PX4bpN1",
        "outputId": "79b2132f-c783-4de8-e15a-81031a1e8a65"
      },
      "source": [
        "number_dictionary = {1:'a','2':'b','3':'c'}\n",
        "len(number_dictionary)"
      ],
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ybjtToi47nky"
      },
      "source": [
        "## Scene_03\r\n",
        "### Navigating Folders (Directories)\r\n",
        "### Note: real terminals and notebooks work differently here..."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A_hQEE3m9iIG",
        "outputId": "6629ecb8-f287-4d30-fcaa-c6b50d92a2be"
      },
      "source": [
        "# where are we?\r\n",
        "!pwd"
      ],
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DtKzHVod6YG7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5c5a90b6-adb0-4a95-8075-cef6fd71d457"
      },
      "source": [
        "# make a new place\r\n",
        "!mkdir testing"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "mkdir: cannot create directory ‘testing’: File exists\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U4CqKoI_7bfP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "07de2557-06c0-4996-e571-548c99790abf"
      },
      "source": [
        "# check all the places\r\n",
        "!ls"
      ],
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "example.txt  sample_data  testing\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iMu4yKxC9qPG"
      },
      "source": [
        "# moving to a new directory\r\n",
        "!cd testing"
      ],
      "execution_count": 72,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Tv0b0La6-M-M"
      },
      "source": [
        "# go back on space\r\n",
        "! cd ..\r\n"
      ],
      "execution_count": 73,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FcFyew7o9vfu",
        "outputId": "d42e55f7-7fa4-45b2-e007-b3e287317a83"
      },
      "source": [
        "# check were you are agian\r\n",
        "!pwd"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-wT4a2Yt7vGM"
      },
      "source": [
        "## Scene_04\r\n",
        "## Slicing"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TmWxliI57vGt",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "f4d6c8ec-151a-42b9-cb48-23d8f34dd3cb"
      },
      "source": [
        "# slice a string\r\n",
        "sample_string = \"abc\"\r\n",
        "sample_string[0]"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'a'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 75
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "tBdnPPq-_Pf2",
        "outputId": "90853cda-0933-41d6-8430-c63109750ae7"
      },
      "source": [
        "# slice a list/array\r\n",
        "sample_array = [\"a\", \"b\", \"c\", \"d\", \"e\"]\r\n",
        "\r\n",
        "sample_array[0]"
      ],
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'a'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 76
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BLs_wvrW_h7K",
        "outputId": "94d60aff-5269-4e1a-8762-475cb1e7ea56"
      },
      "source": [
        "# reverse slice!\r\n",
        "sample_array[::-1]"
      ],
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['e', 'd', 'c', 'b', 'a']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 77
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NjrSy7Xx7vGu"
      },
      "source": [
        "## Scene_05\r\n",
        "## Slice From Here & To There\r\n",
        "## [here,there]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lqreknb9ASwg",
        "outputId": "e13ec0c3-15a1-4922-fb27-ac6055ab5af3"
      },
      "source": [
        "# slice from and to\r\n",
        "sample_array[1:3]"
      ],
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['b', 'c']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 78
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "27u9lnvSAiNo"
      },
      "source": [
        "# count backwards"
      ],
      "execution_count": 79,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "D-B5YZ3yAfPW",
        "outputId": "dfcae988-0773-4682-c81b-1f09f8b15f48"
      },
      "source": [
        "sample_array[-2]"
      ],
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'d'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 80
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rEWMwGjp7vGv"
      },
      "source": [
        "## Scene_06\r\n",
        "## .replace()\r\n",
        "## Make a Dictionary\r\n",
        "## Dictionary + For Loop"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Njw_1w-B7vGv"
      },
      "source": [
        "spells = \"Pr4p2rt6 4f P3n6 H3lls Un3v2rs3t6\"\r\n",
        "\r\n",
        "# make a dictionary\r\n",
        "vowel_change_dict = {\"1\": \"a\", \"2\": \"e\", \"3\": \"i\", \"4\": \"o\", \"5\": \"u\", \"6\": \"y\"} \r\n",
        "\r\n",
        "# user a for loop\r\n",
        "for number in vowel_change_dict:\r\n",
        "           # safe the changes each time\r\n",
        "           spells = spells.replace(number, str(vowel_change_dict[number]))\r\n",
        "\r\n",
        "print(spells)\r\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
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
Hitch stands back up and glances over at the fire.

"All right, up on the rug then," he says,
and when the bird steps into the middle of the wool
he tosses his other blanket over the goose.

The blanket floats down 
over the shape moving beneath the surface,
and then pulls back around Lavender's head 
as she shakes out her hair in the blowing snow.

"You should put some boots on, it's cold out," Hitch says,  
"What's happened to your hair?"

"Hey, Babbage", Lavender calls out.
"Look in that bag. Present from Old John."

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

# Dialogue
typed_print("""
Turning back to Hitch she says, "Thanks for the blanket. 
Do you have my snow boots? I'm starving. Did you make tea?"

As you reach down into the snow and pick up the bundle 
that had been tied around the gooses leg and you reach inside,
Franklin somes over to look.
"What is it?" he asks, "Wo! A Notebook? Where did they find that?
Those have been banned for years."

Jane comes over too as Hitch curries McCavities boots and other clothes.

"It's a what?" asks Jane.

"It's a notebook," says Franklin. 

"Are you sure? That doesn't look like any sort of book I've ever seen."
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

# Dialogue
typed_print("""

"It's a Code Notebook!" says Franklin, gesturing generously with both hand. 
"I can't believe this. Try and opening it!
Let's run it and see what it says at the end. Maybe we can find out
where it came from. Open it up and let's see!"

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()


# Challenge
steady_print("""

Goal: Open a Jupyter Notebook File in a Virtual Environment

Virtual environments can be tricky to set up at first, 
(or they may be already set up and ready to use easily)
but virtual environments are very important and useful.

Rules of thumb: 
1. Do NOT pip install anything outside of a virtual environment.
2. Always make a new folder(directory) and use a virtual environment inside.
(Of course you may need to pip install the virtual environment package
in your home directory to start with.) 

What do you have installed?
Start by seeing what your current setup is:
- Do you have pip?
- Do you have pipenv?
- Do you have venv / virtualenv?

Ideally you should be able to use both/either, 
pipenv and/or venv depending on the task
(e.g. AWS projects may require venv).
""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
# ...Challenge
steady_print("""

Once you are set up, using a virtual environment can be as simple as running 
these two commands in your terminal:
    $ pipenv install jupyterlab
    $ pipenv run jupyter lab

Step 1. Check to see if you have pipenv or venv installed already:
    $ pipenv --version
    $ virtualenv --version

and/or:
   $ pip list
   (Then look to see if pipenv and or virtualenv are listed.)

""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
# ...Challenge
steady_print("""

Step 2: Install (if you do not already have pipenv or venv)

If you do have either, you can move ahead. If you do not, then you will 
need to install one. 

For pipenv:  
  $ pip install pipenv

Read more here:
https://pypi.org/project/pipenv/

""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
# ...Challenge
steady_print("""

For venv (or virtualenv):

If you have pip (maybe called pip3)
this ~may work on any system:
  $ pip install virtualenv

If you don't have pip:
To installvenv on debian etc.
	$ sudo apt install python3 python3-venv

Read more here:
https://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html

""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
# ...Challenge
steady_print("""
 
Step 3. Make/Enter/Use a Virtual Environment

In terminal, in scene_07 folder:
$ pipenv shell
or
$ python3 -m venv this_environment; source this_environment/bin/activate

""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
# ...Challenge
steady_print("""

Step 4. Install & Run Jupyterlab or Jupyter Notebook

Then for pipenv:
$ pipenv install jupyter
$ pipenv run jupyter notebook
or
$ pipenv install jupyterlab
$ pipenv run jupyter lab

Then for venv: (Make sure you see the name of 
your virtual environment in the command line)
e.g. (env_name) [user_name@localhost scene_07]$ 

$ pip install jupyter
$ pip run jupyter notebook
or
$ pip install jupyterlab
$ pip run jupyter lab

""")
# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
# ...Challenge
steady_print("""

Step 5. Open the jupyter notebook & run all code cells

For Jupyter Lab:
Under the "Run" menu tab at the top, select: "Run All Cells"

For Jupyter Notebook:
Under the "Cell" menu tab at the top, select: "Run All"

(Note: This notebook should contain the code you studied 
in each of the past scenes. Notebooks are a useful way to record, share,
run, experiment with, and use code. Some people use python directly
in the command line (as you have been doing), but often people use python 
inside a notebook. It is useful to be able to use python both ways.)

Back to the story:
Now you can read what your notebook file says at the very bottom.

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

# https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

# Second Dialogue
typed_print(
    """


Jane turns to Lavender and asks, "You are not usually followed 
by other birds like that are you?"

"Setting asside that reference to me as 'a bird,'" Lavender says, 
sweeping her hand to the side, "I think that was something I did by accident. 
Something new. Maybe useful?
That is a very weird fire you have there. What are you burning?"

"Those bits of frozen...birds."

"You're burning frozen birds?"

"What else are we supposed to burn out here, ice?"

"Um...wood?"

"Oh...right."

"By the way," says Lavender, "Old John sends his thanks." 
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

# Save the change:
# $ source ~/. bash_profile

# """
# )


slow_print(f"\n\n End of {scene} {blurb} \n\n")
pause_seconds(5)
clear_terminal()
