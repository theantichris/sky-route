from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{} - {}\n".format(letter, landmark)

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

# Sets the selected origin and destination points
def set_start_and_end(start_point, end_point):
    pass

# Request an origin from the user
def get_start():
    pass

# Request the destinaton from the user
def get_end():
    pass

def skyroute():
    greet()

skyroute()