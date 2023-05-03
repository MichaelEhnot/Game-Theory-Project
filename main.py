import numpy as np
import pprint

#create participants and preferences
num_participants = 10
num_rooms = num_participants

uniform_prefs = {}
correlated_prefs = {}

for i in range(num_participants):
    uniform_prefs[i] = np.random.permutation(np.arange(10))
    correlated_prefs[i] = np.append(np.random.permutation(np.arange(5)), np.random.permutation(np.arange(5,10)))

# pprint.pprint(uniform_prefs)
# print()
# pprint.pprint(correlated_prefs)

#begin serial dictatorship
selection_order = np.random.permutation(np.arange(num_participants))

available_items_correlated = np.arange(num_participants)
available_items_uniform = np.arange(num_participants)

uniform_serial_pairs = {}
correrlated_serial_pairs = {}

for i in selection_order:   
    for j in uniform_prefs[i]:
        if j in available_items_uniform:
            available_items_uniform = np.delete(available_items_uniform, np.where(available_items_uniform == j))
            uniform_serial_pairs[i] = j
            break
    
    for j in correlated_prefs[i]:
        if j in available_items_correlated:
            available_items_correlated = np.delete(available_items_correlated, np.where(available_items_correlated == j))
            correrlated_serial_pairs[i] = j
            break

print("Uniform serial:")
pprint.pprint(uniform_serial_pairs)
print("Correlated serial:")
pprint.pprint(correrlated_serial_pairs)