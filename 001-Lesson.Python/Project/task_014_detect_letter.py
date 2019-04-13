vowel_letters = ['a', 'e', 'i', 'o', 'u', 'y']
consonant_letter = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


def detect_letter(a):
    if a in vowel_letters:
        print("VOWEL!")
    elif a in consonant_letter:
        print("CONSONANT!")


letter = input("Input a letter: ")
detect_letter(letter)
