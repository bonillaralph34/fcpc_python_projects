ListChords = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

input_chords = input('Chords: ')
input_step = int(input('step: '))

user_chords = [word for word in input_chords]
print(user_chords[0])

new = ''
for chord in user_chords:
    if chord in ListChords:
        index = ListChords.index(chord)
        if index + input_step > len(ListChords):
            x = (index + input_step) - len(ListChords)
            new += ListChords[x]

        else:
            new += ListChords[index+input_step]

print(new)


