# version 006
# Scene_05
# Heads Down, Heads Up
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

scene = "scene_04"
blurb = " Heads Down, Heads Up "
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
    "What was that?",
    "Really?",
    "I didn't catch that...",
    "Come again?",
    "Are you sure about that?",
    "That just doesn't sound right..." "What?",
    "You're pulling my leg!",
    "I'm sorry, my mind was wondering. What was that again?",
    "Ha ha hah ahahahhahahhh, that's a good one.",
    "...Seriously?" "You have to be joking.",
]

# general_wrong_answer_responces
urgent_responses = [
    "Huh?",
    "What? Can you hurry that up?",
    "Oh, we don't have time for this...",
    "Come again? Quick! Quick!",
    "That doesn't sound right..." "What? Give it another quick look.",
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
ReadMe: Scene_05, Dungeon of Scrolls 
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
          (macOS / Linux / etc ->) curl -O https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_05/scene_05.py ; python3 scene_05.py 
          (windows ->) curl -O scene_05.py https://raw.githubusercontent.com/lineality/ReadMe_Adventures/master/Learn_NLP__Dungeon_of_Scrolls/scene_05/scene_05.py ; python3 scene_05.py

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


# create papers_in_cart_tracks.txt file
papers_in_cart_tracks_text = """
According to the proceedings of the bureau for the documentation and certifications of actions and correspondences herewith and forthwith in great solemnity and for the purposes of future accord, right actions, and cetera, it is hereby published with full permissions from, and in the furtherance of the purposes and prosperances of, the aforementioned governing bodies or bodies that the contents of this document be held in regards consistent with expected standards. This frontmatter certifies not only the authenticity of the date, contents, and seal of notice, but also the sanctity of the paper on which this decree was published, namely that this paper was produced entirely with subjugated labor, using no contact or input from base service creatures or unholy machines and dangerous numerical comparisons of unsanctified symbols. Furthermore the reclaimed labor from hostile foreign lands work indefinitely without food. By virtue of the declarations of this administration there will be an Imperial Temple Guard action consistent with "restraint by conflagration" for all Universities, and those guilty by however indirect an association, found not to be in compliance with his Most Supreme and Highest Pinnacle of Absolute Top Utmostness, the Universal Eternal Emperor.
"""
# create, write-to, & save .txt file
file_to_create4 = open("papers_in_cart_tracks.txt", "w")
file_to_create4.write(papers_in_cart_tracks_text)
file_to_create4.close()

# # open, read, & print the file
# file_to_read4 = open("papers_in_cart_tracks.txt", "r")
# print(papers_in_cart_tracks_text.read())


##############
# The Action!
##############

slow_print(f"{scene} {blurb} ")

...
typed_print(
    """
"\n\nOk. We're off. We know where we're going...
and so, about time for introductions then?"

"Yes, that's hitch. We call him hitch, he is Gullover Hitch.
Or something like that."

"Or something like that? Or something like that?"

"Isn't your real name Hitchcock?"

"...maybe it is..."

"So we call him Hitch."

"At your services." Hitch takes his hat off and bows deeply,
plowing a slice through the snow with his hat.

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"I'm Jane Adams."

"Is it proper to do your own introduction?"

"Don't mind him. And that is Lavender over there. Lavender McCavity."

"We'll all be turning lavender if we don't find a windbreak. Oh good,
there's something up there. I think...I can't really make it out..."

"And that's Franklin back there."

"Hello! Franklin Merln. Pleased to make your acquaintance."
The smallest of them, under a huge racoon skin cap, waves and bounces.

"But what should we call you? ...Hang on,
I think we're coming up on...is that a cart...?"
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"And what's this?" Jane reaches down
and pulls up a pile of pages out of the cart tracks in the snow.
"Official papers? Oh no..."

She runs up to you, eyes wide. "Ok,
can you check this really quickly
for what it says about 1000 characters in?
The first 1000 characters are always...just fluff.
This may be important and we don't have time to read it all.
Just skip ahead 1000 characters
and then read me the next 30 or so characters,
the next few words, right...
Can you do that? Quickly?"

She keeps looking back and forth between you and the cart.
"""
)

answer_check = False

while answer_check is False:
    answer0 = input('\n"Can you check?" (yes/no)')
    answer0 = answer0.lower()
    # boolean check
    answer_check = "yes" in answer0
    if answer_check is False:
        typed_print(f'"{random.choice(urgent_responses)}"')

clear_terminal()

# Activity:

steady_print(
    """
(Task!) Learn a new way to slice from index 1000 to index ~1030

Previously, you sliced one item >>> file[number]
Now, slice out a RANGE of items >>> file[start_here : end_BEFORE_here]
IMPORTANT: Remember positive numbers count from ZERO,
AND the end-point goes UP TO but does NOT include that end-point.

Example: "abc" has indexes 0,1,2, start at index [0], stop BEFORE index [2]
This range-slice produces "ab"
  >>> file = "abc"
  >>> file[0:2]

1. Open new Terminal in scene_04 folder (right click: 'open in terminal')
   (folders) ReadMe_Adventures ->  Learn_NLP__Dungeon_of_Scrolls ->
   -> scene_04 ->  "papers_in_cart_tracks.txt"
2. Check you are in the correct directory with $ ls & $ pwd then type:
     $ python3
   >>> name_you_choose = open("papers_in_cart_tracks.txt", "r").read()
   >>> print(name_you_choose[###:####])
"""
)


answer_check = False

while answer_check is False:
    answer = input("\n(What is AFTER 1000 characters in papers_in_cart_tracks.txt?)\n")
    answer = answer.lower()
    # boolean check
    answer_check = "temple guard" in answer
    if answer_check is False:
        typed_print(f'"{random.choice(responses)}"')

clear_terminal()

typed_print(
    """
"Oh, dear. This is...this is bad. That a Temple Guard."

"A TG? Out here? What's going on?"

"Keep it down. Ok...first, take off that arm band.
Yes, I know, just take it off. McCavity, get this off her. Fast."

You feel a slight brushing against the back of your arm,
and the once band falls onto the snow in four pieces.
What used to be the circular cog symbol now a scatter
of arches and bars on clean cut strips of canvas.

"Grab that all up, we can burn it properly later."

"Take this," you hear Jane say, as you feel something warm placed
on top of your head. "And keep your head down."

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """

"You! What you doing out here?" Comes the loud bark of the cartman's voice.

No one moves.

"Oh, you're just a bunch of kids. You scared the daylights out of me.
Say, you are just kids right? Blasted snow, I can't see anything straight."

The round misty figure by the cart raises his hand to his forehead.

"Yes, yes we are. We are just a bunch of kids, heading...to school."

"In the snow. Towards a mountain. On the weekend."

"Shut up, Hitch."

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """

"Thank goodness for that. You're not, you're not...working for anyone, right?"

"Nope, we are just students. Yes we are." And as Jane says this
she preemptively sticks her gloved hand
into Hitch's mouth.

"Well in that case...well in THAT case I was wondering, I was wondering
if you'd like to buy...if YOU would like...to buy..."
he was looking carefully all around as he spoke,
"some books?"

"You're not going to say that part twice as well?" says hitch,
spitting out glove-lint.

"Shut up, Hitch."

"What kind of books?"

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """

"Well...you know they're, uh...
oh all right, I'll just tell you. The Emperor,
Save His Royalness, the Emperor's Guard just, uh, Reclaimed two
Universities, that weren't, you know, following commands right.
And we was told to burn it all properly.
But, I MEAN, some of those books,
I says to myself, they must be worth something to someone, right?
But I've got to get rid of the lot, fast."

"How about 10 Pyrians?"

"Ten?...Just Ten?"

"Eleven. Eleven Pyrians, we take them all right now, and you're clean."

"Uh...uh..." The cartman frowns, looking around on all sides.
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
After a moment of only the sound of ice crystals singing down,
another bird explodes with a pop just behind the cartman,
and he jumps.

"Oh all right." He says, "You have that with you now, do you?"

A small cloth sack arcs through the air and lands in the cartman's hands.

"Done." Comes Lavender's voice.

"Yes, nice doing business with you. May the Humans Prevail.
Save His Royalness." As the cartman's arm shoots up in a solute,
you see for the first time his uniform. And with that he runs off
into the snow towards the inn. "Keep your head's up! Enjoy the books!
I hope..." he calls out but his voice and his visage
both melt away into the glittering clouds of ice.
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"McCavity, where did you get eleven Pyrians?"

"WHAT are we supposed to do with this cart?
We are walking to a mountain,
in a freak storm,
with a, now, fugitive,
why exactly did we just buy a cart of stolen books?"

"The Pyrians", says Lavender as she crunches slowly
through the snow up to the cart, "are from The Mos."

"You stole from the inn?"

"Sort of. Long Story. But that same fat rogue is running to the inn now
to spend it all back again. And probably tell some fabulous lies..."
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"And why did we buy that cart?"

"We bought silence."

"We bought what?"

"Lavender's right...Even if he isn't a true believer there's still the bounty,
and I'm not sure there's anything that one wouldn't do
for a few pyrians."

"Who'd have thought we'd run into an Imperial.
Out here...in the nowheres,
I haven't seen one in months."
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"And if he saw our new friend here,
he'd probably leave us ALL hanging
from tree branches...probably in pieces just to make sure, like they do.
Like strange frozen fruits. But we know he's a theif,
and now he owes us for getting him out of trouble.
And most importantly he was completely distracted from our friend.
And...speaking of you,
we still need to give you a name."

"I know!", says Franklin. "I was just reading
about these wonderful old machines.
"""
)
typed_print(f'"We can call {pronoun2} Babbage!"')

typed_print(
    """
\n"....Well...sounds kind of like Cabbage...doesn't it..."

"No objections? Anyone? Ok, welcome to the gatherings, Babbage!"
"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """
"You know..." Frankin says. "We should at least tell
Old John that rascal is a TG, you think?.

Jane turns to Lavender. "McCavity, sorry to ask twice
in one day. Could you fly back and warn him?"

"I probably can't do a third and come back any time today.
Ok if I find you all in the morning?"

"Yeah that works."

"Worth a try," she says, and McCavity seemed to
explode in a billow of snow, or like two bursting
pillows in a pillow fight. And you see a large snow goose
fly out of the churning cloud and back
in the direction of the inn.

"""
)

# Press Enter to Continue
input("\n  ...Press enter to continue...  \n")
clear_terminal()

typed_print(
    """

"Dead useful she is."

"Yeah, well she shouldn't change so many times in one day,
you know that, Hitch."

"Yeah I know. It's not far to fly though."

"You're probably right. Grab her clothes, will you.
We'll dry them out for when she gets back."

"Just hope there's no off season hunters wandering around..."

"""
)

slow_print(f"\n\n End of {scene} {blurb} \n\n")
clear_terminal()
