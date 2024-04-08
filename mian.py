from code import morse_roles
import winsound
from time import sleep


frequency = 700
duration_long = 500
duration_short = 100

def to_morse(sentence):
    morse= ''
    for i in sentence:
        morse += f'{morse_roles[i]}  ' 
    return (morse)

def to_sound(code_morse): 
    code_morse = code_morse.replace(' ', '')
    for i in code_morse:
        if i == '•':
            winsound.Beep(frequency=frequency, duration=duration_short)
        else:
            winsound.Beep(frequency=frequency, duration=duration_long)

game_over = False

while game_over == False:
    sentence = input('Enter your string to converto into a Morse Code: \n').upper().replace(' ', '')

    code_morse = to_morse(sentence=sentence)
    print(code_morse)

    sound = input('Would you like to play this sound? (yes/no)').upper()
    if sound == 'YES':
        to_sound(code_morse=code_morse)
        again = input('Would you like to convert another string?(yes/no)').upper()
        if again == 'Yes':
            continue
        else :
            game_over = True
    elif sound =='NO':
        sentence = input('Would you like to convert another string?(yes/no)').upper()
        if sentence == 'YES':
            continue
        else:
            game_over =True


