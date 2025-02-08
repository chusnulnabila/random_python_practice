# buat fungsi untuk mengecek apakah input word sama dengan original word

def check_word(current_word):
    word = current_word.lower().replace(' ', '')
    return ''.join(sorted(word))

input_word = input('Input: ')
original_word = input('Original: ')

if (check_word(input_word) == check_word(original_word)):
    print(f"the original word from '{input_word}' is '{original_word}'")
else:
    print(f"'{input_word}' is not anagram with '{original_word}'")



# OTHER VERSIONrandom_word = 'CHATMDEMA'
# random_word = 'CHATMDEMA'
# original_word = 'Matchmade'

# def normalize(current_word):
#     word = current_word.lower().replace(' ', '')
#     return ''.join(sorted(word))

# def checking(word1, word2):
#     return normalize(word1) == normalize(word2)

# if (checking(random_word, original_word)):
#     print(f"'{original_word}' is the original from '{random_word}'")
# else:
#     print(f"'{random_word}' is different from '{original_word}'")

