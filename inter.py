from parse_program  import *
import sys

program = []

if __name__ == '__main__':
    
    argv = sys.argv
    if len(argv) != 2:
        assert False, "The interpreter requires a file to interpret"
    program_path = argv[1]

    #Parsing
    program = parse_file_to_tokens(program_path, program)
    print(program)