import time
import sys

def get_anagrams_b(file_dir, input_word):
    input_word_b = input_word.lower().encode('utf-8')
    input_word_len = len(input_word) + 2
    input_word_sorted = sorted(input_word_b.lower())
    with open(file_dir, 'rb') as f:
        for word in f:
            if len(word) == input_word_len and sorted(word[:-2].lower()) == input_word_sorted:
                yield word.decode('utf-8').rstrip()


if __name__ == '__main__':
    start_time = time.time()

    result = ','.join(get_anagrams_b(sys.argv[1], sys.argv[2]))

    end_time = time.time()       
    print('{},{}'.format((end_time - start_time)*10**6, result))