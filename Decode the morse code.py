'''

While the Morse code is now mostly superseded by voice and digital data communication
channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes".
For example, the letter A is coded as ·−, letter Q is coded as −−·−,
and digit 1 is coded as ·−−−−.
The Morse code is case-insensitive, traditionally capital letters are used.
When the message is written in Morse code, a single space is used to separate the
character codes and 3 spaces are used to separate words.
For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes,
the most notorious of those is the international distress signal SOS (that was first issued by Titanic,
that is coded as ···−−−···. These special codes are treated as single special characters,
and usually are transmitted as separate words.

Your task is to implement a function that would take
the morse code as input and return a decoded human-readable string.
'''
#Nuaiman's Solution
def decodeMorse(morse_code):
    while morse_code[0] == '   ':
        morse_code = morse_code[0:]
    while morse_code[len(morse_code)-1:] == ' ':
        morse_code = morse_code[:len(morse_code)-1]
    morse_code += ' '
    Ctext = ''
    Decode = ''
    i = 0
    for c in morse_code:
        if c != ' ':
            i = 0
            Ctext += c
        else:
            i += 1
            if i == 3:
                Decode += ' '
            elif i == 1 and Ctext != '':
                Decode += MORSE_CODE[Ctext]
                Ctext = ''


    return Decode

#Solution 1
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

#Solution 2
def decodeMorse(morse_sequence):
    words = []
    for morse_word in morse_sequence.split('   '):
        word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
        if word:
            words.append(word)
    return ' '.join(words)

#Solution 3
CHAR_SEP = ' '
WORD_SEP = ' ' * 3


def decodeMorse(morseCode):
    return ' '.join(
        ''.join(MORSE_CODE[c] for c in word.split(CHAR_SEP))
        for word in morseCode.strip().split(WORD_SEP))



