
Scene 2: Witch Map

Instructions:
1. run .py in terminal
wget https://raw.githubusercontent.com/lineality/teaching_NLP_basics_1/master/ReadMe_Adventures/test_demo_1/Windows_OS/scene_2/scene_2.py


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
