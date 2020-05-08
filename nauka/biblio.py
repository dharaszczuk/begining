#nauka importowania dodatkowych bibliotek
import random
from time import sleep
sleep (1)
print (random.randint(1,20))

from funkcje import *

from collections import defaultdict
d = defaultdict(int)
print (d["x"])
napis = "aaabbccooooossasdk"
for litera in napis:
    d[litera] +=1
print (d)
