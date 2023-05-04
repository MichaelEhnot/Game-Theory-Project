import numpy as np
import pprint
import itertools

num_participants = 10
num_rooms = num_participants

def normalizeColumns(matrix):
    for j in range(num_rooms):
        if np.sum(matrix[:,j]) != 0:
            # matrix[:,j] =  matrix[:,j] / np.sum(matrix[:,j])
            #return matrix / np.linalg.norm(matrix, ord=1)
            matrix[:,j] =  matrix[:,j] / np.linalg.norm(matrix[:,j], ord=1)
        #else:
            #matrix[:,j] = np.zeros(10)
    return matrix

#create participants and preferences

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

#begin probabalistic serial mechanism
available_items_correlated = []
available_items_uniform = []

probability_matrix_uniform = np.zeros((num_participants, num_rooms))
probability_matrix_correlated = np.zeros((num_participants, num_rooms))

#allocate array of availible shares
num_shares = 100
for i in range(num_participants):
    available_items_correlated = np.append(available_items_correlated, np.full(num_shares, i))
    available_items_uniform = np.append(available_items_uniform, np.full(num_shares, i))

# select shares for uniform prefs
for i in itertools.cycle(selection_order):
    for j in uniform_prefs[i]:
        if j in available_items_uniform:
            available_items_uniform = np.delete(available_items_uniform, np.where(available_items_uniform == j)[0][0])
            probability_matrix_uniform[i][j]+=1
            break
    if available_items_uniform.size == 0:
        break

# select shares for correlated prefs
for i in itertools.cycle(selection_order):
    for j in correlated_prefs[i]:
        if j in available_items_correlated:
            available_items_correlated = np.delete(available_items_correlated, np.where(available_items_correlated == j)[0][0])
            probability_matrix_correlated[i][j]+=1
            break
    if available_items_correlated.size == 0:
        break

print(probability_matrix_uniform)
print()
print(probability_matrix_correlated)
print()

#convert shares to probablilites
# probability_matrix_correlated/=num_shares
# probability_matrix_uniform/=num_shares

# for j in range(num_rooms):
#         if np.sum(probability_matrix_correlated[:,j]) != 0:
#             probability_matrix_correlated[:,j] /= np.sum(probability_matrix_correlated[:,j])
#         else:
#              probability_matrix_correlated[:,j] = np.zeros(10)

# for j in range(num_rooms):
#     if np.sum(probability_matrix_uniform[:,j]) != 0:
#         probability_matrix_uniform[:,j] /= np.sum(probability_matrix_uniform[:,j])
#     else:
#             probability_matrix_uniform[:,j] = np.zeros(10)
probability_matrix_correlated = normalizeColumns(probability_matrix_correlated)
probability_matrix_uniform = normalizeColumns(probability_matrix_uniform)

#assign items using matrix

uniform_prob_pairs = {}
correrlated_prob_pairs = {}

for i in range(num_rooms):
    #select uniform pairings
    print(np.sum(probability_matrix_uniform[:,i]))
    if np.sum(probability_matrix_uniform[:,i]) == 0:
        # case where no one has shares in current item, allocate to first unassigned person
        for j in range(num_participants):
            if np.sum(probability_matrix_uniform[j]) != 0:
                uniform_prob_pairs[j] = i
                probability_matrix_uniform[j] = np.zeros(10)
    else:
        winner = np.random.choice(np.arange(num_participants), p=probability_matrix_uniform[:,i])
        uniform_prob_pairs[winner] = i
        probability_matrix_uniform[winner] = np.zeros(10)
    #recompute probabilites by dividing each column by its sum
    # for j in range(num_rooms):
    #     if np.sum(probability_matrix_uniform[:,j]) != 0:
    #         probability_matrix_uniform[:,j] /= np.sum(probability_matrix_uniform[:,j])
    #     else:
    #          probability_matrix_uniform[:,j] = np.zeros(10)
    probability_matrix_uniform = normalizeColumns(probability_matrix_uniform)
    
    #select correleated pairings
    print(np.sum(probability_matrix_correlated[:,i]))
    print()
    if np.sum(probability_matrix_correlated[:,i]) == 0:
        # case where no one has shares in current item, allocate to first unassigned person
        for j in range(num_participants):
            if np.sum(probability_matrix_correlated[j]) != 0:
                correrlated_prob_pairs[j] = i
                probability_matrix_correlated[j] = np.zeros(10)
    else:
        winner = np.random.choice(np.arange(num_participants), p=probability_matrix_correlated[:,i])
        correrlated_prob_pairs[winner] = i
        probability_matrix_correlated[winner] = np.zeros(10)
    #recompute probabilites by dividing each column by its sum
    # for j in range(num_rooms):
    #     if np.sum(probability_matrix_correlated[:,j]) != 0:
    #         probability_matrix_correlated[:,j] /= np.sum(probability_matrix_correlated[:,j])
    #     else:
    #          probability_matrix_correlated[:,j] = np.zeros(10)
    probability_matrix_correlated = normalizeColumns(probability_matrix_correlated)

print(uniform_prob_pairs)
print(correrlated_prob_pairs)
    
