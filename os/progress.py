# Python Standard Library
import sys
import time

# Third-Party Libraries
from tqdm import tqdm

args = sys.argv
try:
    num_steps = int(args[1])
except IndexError: # no argument
    num_steps = 10

for i in tqdm(range(num_steps)):
    time.sleep(1.0)