import io
import random


def generate_random_text(input_book, num_of_sentences, words_in_sentence):
    """Generate random text from input book and return it in list format"""

    with io.open(input_book, encoding='utf-8') as file:
        file = file.read().split()

    """Removal punctuation"""
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '?"', '-', '…', '"']
    res_text = []

    for word in file:
        if word in punctuation:
            continue
        
        while(word) and (word[-1] in punctuation):
            word = word[:-1]

        while (word) and (word[0] in punctuation):
            word = word[1:]

        res_text.append(word.lower())

    """text generation"""
    count_sentences = random.randint(num_of_sentences - 4, num_of_sentences)
    list_sentences = []
    for i in range(1, count_sentences):
        word_count = random.randint(words_in_sentence - 4, words_in_sentence)
        for j in range(0, word_count):
            list_sentences.append(res_text.pop(random.randint(1, len(res_text)-1)))
        temp = list_sentences.pop(-j)
        chars = list(temp)
        chars.insert(0, (''.join(chars.pop(0))).upper())
        temp = ''.join(chars)
        list_sentences.insert(-j, temp)
        temp = list_sentences.pop(len(list_sentences)-1)
        temp = temp + '.'
        list_sentences.insert(len(list_sentences), temp)

    text = ' '.join(list_sentences)

    return text


def random_sentence(input_book, num_of_sentences=1):
    """Generate random text from input book and return it in list format"""

    with io.open(input_book, encoding='utf-8') as file:
        file = file.read().split('\n')

    """text generation"""
    list_sentences = []
    for i in range(0, num_of_sentences):
        list_sentences.append(file.pop(random.randint(0, len(file) - 1)))

    text = ' '.join(list_sentences)

    return text


"""Example of using generate_random_text function"""
# path = 'rand_sent.txt'
# # print(generate_random_text(path, 20, 10))
# print(random_sentence(path, 15))
