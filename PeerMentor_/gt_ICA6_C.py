#gt_ICA6_C.py

# Translate english to piglatin
# Input: english text
# Output: piglatin text

# by. Gentry Trimble


def reformat_english():
    txt = input("English: ")
    txt = txt.lower()
    for i in txt:
        if i == '!':
            txt = txt.replace('!', ' ')
        if i == '.':
            txt = txt.replace('.', ' ')
        if  i == '?':
            txt = txt.replace('?',' ')
        if i == ',':
            txt = txt.replace(',',' ')
    return txt

def english_to_piglatin(txt):
    word_list = txt.split(' ')
    pig_latin_words = []
    for word in word_list:
        if len(word) == 0:
            continue
        if word[0] in 'aeiou':
            pig_latin_words.append(word + 'way')
        else:
            if word[0] == 'y':
                pig_latin_words.append(word[1:] + word[0] + 'ay' )
            else:
                consonant = ''
                i = 0
                while i < len(word) and word[i] not in 'aeiouy':
                    consonant += word[i]
                    i +=1
                pig_latin_words.append(word[i:] + consonant + 'ay')
    translated = ' '.join(pig_latin_words)
    return translated

def main():
    choice = 'y'
    while choice == 'y':
        txt = reformat_english()
        if txt == '' or txt == ' ':
            print("You didn't enter any text.")
        else:
            line = '{:10} {:>5}'
            print(line.format('English:',txt))
            pig_latin = english_to_piglatin(txt)
            print(line.format("Pig Latin:",pig_latin))
        choice = input('Translate another one? (y/n): ')
    print("Thank you, Bye!!")
main()