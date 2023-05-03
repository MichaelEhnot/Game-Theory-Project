import numpy as np
import pprint

num_participants = 10
num_rooms = num_participants

uniform_prefs = {}
correlated_prefs = {}

for i in range(num_participants):
    uniform_prefs[i] = np.random.permutation(np.arange(10))
    correlated_prefs[i] = np.append(np.random.permutation(np.arange(5)), np.random.permutation(np.arange(5,10)))

pprint.pprint(uniform_prefs)
print()
pprint.pprint(correlated_prefs)