
def get_sentence_count(rows, cols, sentence, attempt, start_from, row_count):

    for word in sentence:
        reaming_space = cols - start_from
        required_space = len(word) if reaming_space == cols else len(word) +1
        if required_space <= reaming_space:
            # pass the word
            start_from += required_space
        else:
            if row_count < rows-1:
                row_count += 1
                start_from = 0
                start_from = len(word)
            else:
                return attempt
    attempt += 1
    return get_sentence_count(rows, cols, sentence, attempt, start_from, row_count)

if __name__ == '__main__':
    print(get_sentence_count(rows=4, cols=5, sentence=["i","had","apple","pie"],
                             attempt=0, start_from=0, row_count=0))
    print(get_sentence_count(rows=2, cols=8, sentence=["hello","world"],
                             attempt=0, start_from=0, row_count=0))
    print(get_sentence_count(rows=3, cols=6, sentence=["a", "bcd", "e"],
                             attempt=0, start_from=0, row_count=0))