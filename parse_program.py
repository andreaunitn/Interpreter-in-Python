from types_keywords import *
from colors import *

#CHECK KEYWORD
def check_keyword(word, row, col, tp):
    assert len(OpKeywords) == 5, "You have to handle all the OpKeywords"
    if tp == OpType.WORD:
        if not (word in OpKeywordsMap.keys()):
            print(colors.FAIL + "ERROR" + colors.ENDC + ": undefined token " + colors.WARNING + "'%s'" % word + colors.ENDC + " at %d:%d" % (row, col))
            exit(1)

#CHECK TYPE
def check_type(word):
    assert len(OpType) == 3, "You have to handle all the OpTypes"
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

#PARSE FILE INTO TOKENS
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

            for col in range(1, length+1):
                if not line[col-1].isspace():
                    if line[col-1] == '#':
                        break
                    else:
                        word += line[col-1]

                        if word in words:

                            tp = check_type(word)
                            check_keyword(word, row, col - len(str(word)) + 1, tp)
                            token = (word, row, col - len(str(word)) + 1, tp)
                            program.append(token)
                            word = ''
        
            row = row + 1
    
    return program
