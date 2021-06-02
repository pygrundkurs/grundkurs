import mod.mod1
import math
import mod.helper.db.testmod as testmod

import mod.mod1

# Holt get_sinn in den aktuellen Namensraum
from mod.mod1 import get_sinn
from math import pi

from mod.mod1 import get_sinn as wichtig

SINN = 42


print('Welt')

print(mod.mod1.zahl)
print(math.pi)
print(pi)

print(mod.mod1.get_sinn())
print(get_sinn())
print(wichtig())

print(mod.helper.db.testmod.tag)
print(testmod.tag)
