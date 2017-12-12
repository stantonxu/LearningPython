def getword(path):
    fin = open(path, 'r')
    line_number =0
    for line in fin:
        line_number += 1
        for word in line.split():
            control = yield (line_number, word)
            if control == 'next': 
                break

a = getword("/Users/xus12/git/LearningPython/AdvancedPython/lines.txt")

for line_word in a:
    if line_word[1] == 'six':
        line_word = a.send('next')
    print(line_word[0], line_word[1])

print("That's all folks!")