from types_keywords import *
from colors import *

def check_keyword(word, row, col, tp):
    if tp == OpType.WORD:
        if not (word in OpKeywordsMap.keys()):
            print(colors.FAIL + "ERROR" + colors.ENDC + ": undefined token " + colors.WARNING + "'%s'" % word + colors.ENDC + " at %d:%d" % (row, col))

def check_type(word):
    if word.isnumeric():
        return OpTypeMap['int']
    elif word[0] == '"':
        l = len(word)

        if word[l-1] == '"':
            return OpTypeMap['str']
        else:
            return OpTypeMap['WORD']
    else:
        return OpTypeMap['WORD']

def parse_file_to_tokens(program_path, program):
    with open(program_path, 'r') as source:
        
        lines = source.readlines()
        row = 1

        words = []
        for line in lines:
            words.append(line.split())

        words = [x for xs in words for x in xs]

        for line in lines:
            word = ''
            length = len(line)

            for col in range(0, length):
                if not line[col].isspace():
                    if line[col] == '#':
                        break
                    else:
                        word += line[col]

                        if word in words:

                            tp = check_type(word)
                            check_keyword(word, row, col, tp)
                            token = (word, row, col, tp)
                            program.append(token)
                            word = ''
        
        row = row + 1
    
    return program
