def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        num = len(num_words(file_contents))
        l = letter_count(file_contents)
    print(f'number of words: {num}')
    print(f'Number of each letter used: \n{l}')
    

def num_words(contents):
    words = contents.split()
    return words

def letter_count(contents):
    letters = contents.lower()
    word_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 
                 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
                 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
                 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
                 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 
                 'z': 0}
    for l in letters:
        if l.isalpha():
            word_dict[l] = word_dict[l] + 1
    return word_dict

if __name__ == '__main__':
    main()