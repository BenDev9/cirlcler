from args_parser import parser, WantedArgs
from maths_funcs import get_point
from tts import speak

import pyautogui
from pprint import pprint

import time

# Stop pyautogui interfering with our fun
pyautogui.PAUSE = 0.01

# Load and check arguments
args: WantedArgs = parser.parse_args()
pprint(args.__dict__, indent=4)

# Calculate degrees
step_degree = 360 / args.fidelity
curr_degree = step_degree

print("step_degree", step_degree)

if not args.manual:
    # Establish the circle origin
    speak("Place your cursor on the center of the circle!")
    time.sleep(3)
    origin = pyautogui.position()
    print("\nOrigin:", tuple(origin))

    # Establish the circle origin
    speak("Pull your mouse out to get the radius!")
    time.sleep(3)
    new_pos = pyautogui.position()
    radius = abs(origin.x - new_pos.x)
    print("Radius:", radius, "\n")

    speak("Drawing now...")

    for i in range(args.tries):
        # Work out the initial offset and add it to the origin
        abstract_pos = get_point(0, radius)
        pos = (origin.x + abstract_pos[0], origin.y + abstract_pos[1])
        pyautogui.moveTo(*pos, 0.3)

        # Click down
        pyautogui.mouseDown()

        for i in range(args.fidelity + 1):
            # Work out the offset and add it to the origin
            abstract_pos = get_point(curr_degree, radius)
            pos = (origin.x + abstract_pos[0], origin.y + abstract_pos[1])

            # Some debug prints
            print("Angle: " + str(int(curr_degree)) + "°")
            print("Coordinate: " + str(pos))
            print()

            # Move to the new position and increment the angle
            pyautogui.moveTo(*pos, 0.5 / args.fidelity)
            curr_degree += step_degree

        # Let go of the mouse
        pyautogui.mouseUp()
else:
    speak("Manual mode not implemented yet")
