from types_keywords import *

def parse_file_to_tokens(program_path, program):
    with open(program_path, 'r') as source:
        
        lines = source.readlines()
        row = 1

        words = []

        for line in lines:
            word = ''
            length = len(line)

            for col in range(length):
                if not line[col].isspace():
                    if line[col] == '#':
                        break
                    else:
                        word += line[col]
                else:
                    program.append(word)
        
        row = row + 1
    
    return program

                        
