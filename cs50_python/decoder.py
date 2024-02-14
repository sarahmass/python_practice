
def decode(message_file):
    # read message_file into a list of lines
    with open(message_file, "r") as f:
        lines = f.readlines()
    
    # initiate a dictionary key = number, value = word
    number_word = {}
    
    # processes each line
    for line in lines:
        # make sure line is not empty
        if len(line.strip()) == 0:
            continue
        # strip white space and split into [number, word]
        line = line.strip().split(' ')

        # store keys as ints so math can be applied
        number_word[int(line[0])] = line[1]
    
    # collect the words stored at keys 
    # 1 for first word, 1+2=3 for second, 1+2+3=6 for third, etc
    num = 1
    idx = 1
    msg = []
    while idx <= max(number_word.keys()):
        msg.append(number_word[idx])
        num += 1
        idx = idx + num
    # return the words as a single string separated with a space 
    return ' '.join(msg)

import pandas
input = pandas.read_csv()
game = pandas.DataFrame()
game.re