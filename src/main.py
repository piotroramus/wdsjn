from __future__ import print_function

import pickle
from operator import itemgetter

from preprocessing import load_preprocessed_documents
from associations import compute_associations

input_file = 'resources/pap.txt'

docs = load_preprocessed_documents()

alpha = 0.66
beta = 0.00002
gamma = 0.00002
window_size = 12

# TODO: deogonkify corpus and see the results
stimuli = ['obiad', 'jedzenie', 'dom', 'smaczny']

all_associations = compute_associations(docs, stimuli, alpha, beta, gamma, window_size)

for stimulus, associations in all_associations.items():
    associations_sorted = sorted([(word, strength) for word, strength in associations.items()],
                                 key=itemgetter(1), reverse=True)
    print("======================================")
    print("{}".format(stimulus))
    for word, association in associations_sorted:
        print(u"\t{:16} {:.6f}".format(word, association))
