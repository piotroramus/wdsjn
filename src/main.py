from __future__ import print_function

import pickle
from operator import itemgetter

from preprocessing import load_preprocessed_documents, preprocess_documents
from associations import compute_associations

input_file = 'resources/pap.txt'

docs = load_preprocessed_documents()

alpha = 0.66
beta = 0.00002
gamma = 0.00002
window_size = 12

# TODO: deogonkify corpus and see the results
stimuli = ['obiad', 'jedzenie', 'dom', 'smaczny']

raw_corpus_file = 'resources/pap.txt'
preprocessed_corpus_file = 'resources/preprocessed.txt'
computed_associations_file = 'resources/associations.dat'

preprocess_input = False
compute_assocs = True

best_n_to_print = 10

if __name__ == '__main__':
    if preprocess_input:
        preprocess_documents(raw_corpus_file, output=preprocessed_corpus_file)

    if compute_assocs:
        all_associations = compute_associations(docs, stimuli, alpha, beta, gamma, window_size)
        with open(computed_associations_file, 'wb') as f:
            f.write(pickle.dumps(all_associations))

    else:
        with open(computed_associations_file, 'rb') as f:
            all_associations = pickle.loads(f.read())

    for stimulus, associations in all_associations.items():
        associations_sorted = sorted([(word, strength) for word, strength in associations.items()],
                                     key=itemgetter(1), reverse=True)
        print("======================================")
        print("{}".format(stimulus))
        for word, association in associations_sorted[:best_n_to_print]:
            print(u"\t{:16} {:.6f}".format(word, association))
