from parse_program  import *
from types_keywords import *
import sys

program = []

def simulate_program(program):
    stack = []
    ip = 0

    """
    assert len(OpKeywords) == 5, "You have to handle all the OpOperations"
    while ip < len(program):
        if program[ip] == OpKeywords.OP_PLUS:
            a = stack.pop()
            b = stack.pop()

            stack.append(int(a + b))
            ip = ip + 1
        
        else:
            if program[ip] in OpKeywordsMap.values() or type(program[ip]) in OpTypeMap:
                stack.append(program[ip])
                ip = ip + 1
            else:
                assert False, "unreachable"
        """

if __name__ == '__main__':
    
    argv = sys.argv
    if len(argv) != 2:
        assert False, "The interpreter requires a file to interpret"
    program_path = argv[1]

    #Parsing
    program = parse_file_to_tokens(program_path, program)
    print(program)

    #Simulate
    simulate_program(program)
