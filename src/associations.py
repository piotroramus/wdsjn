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
