import argparse

# Create parser instance
parser = argparse.ArgumentParser(
    prog="circle",
    description="Draws a (hopefully) perfect circle on https://neal.fun/perfect-circle/",
    epilog="Have fun cheating! ;)",
)

# Define parameters
parser.add_argument("fidelity", help="the number of vertices of the circle", type=int)

parser.add_argument("-a", "--audio", help="use audio or not", action="store_true")

parser.add_argument(
    "-r", "--radius", help="the radius of the circle", type=float, required=False
)

parser.add_argument(
    "-t", "--tries", help="the number of tries to do", type=int, required=False
)

parser.add_argument(
    "-m", "--manual", help="use manual mode or not", action="store_true"
)


# Create an inheritable class (for IntelliSense ease of use)
class WantedArgs(argparse.Namespace):
    fidelity: int
    radius: float
    manual: bool
    tries: int = 1
