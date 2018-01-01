from collections import Counter, defaultdict


def adjacent_words(document, index, window_size):
    if not document:
        return list()

    # don't take the first element
    if index == 0:
        return document[1:window_size + 1]

    max_index = len(document) - 1

    # don't take the last element
    if index == max_index:
        return document[-window_size - 1:-1]

    left_start = max(0, index - window_size)
    left_end = max(0, index - 1)
    preceding_words = document[left_start:left_end + 1]

    right_start = min(max_index, index + 1)
    right_end = min(max_index, index + window_size)

    following_words = document[right_start:right_end + 1]

    return preceding_words + following_words


def calculate_stimuli_stats(documents, stimuli, window_size):
    result = dict()
    for stimulus in stimuli:
        result[stimulus] = Counter()

    for doc in documents:
        for i, word in enumerate(doc):
            for stimulus in stimuli:
                if word == stimulus:
                    adjacent = adjacent_words(doc, i, window_size)
                    for w in adjacent:
                        if w == stimulus:
                            continue
                        result[stimulus][w] += 1

    return result


def words_occurences(documents):
    result = Counter()
    for doc in documents:
        for word in doc:
            result[word] += 1
    return result


def compute_associations(documents, stimuli, alpha, beta, gamma, window_size):
    stimuli_stats = calculate_stimuli_stats(documents, stimuli, window_size)

    words_stats = words_occurences(documents)
    total_words = len(words_stats.items())

    associations = dict()

    beta_q = beta * total_words
    gamma_q = gamma * total_words

    for stimulus in stimuli:
        associations[stimulus] = defaultdict(float)
        for word, word_count in stimuli_stats[stimulus].items():
            if words_stats[word] > beta_q:
                associations[stimulus][word] = word_count / (words_stats[word] ** alpha)
            else:
                associations[stimulus][word] = word_count / gamma_q

    return associations
