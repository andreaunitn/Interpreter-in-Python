from parse_program  import *
from types_keywords import *
import sys

program = []

def simulate_program(program):
    stack = []
    ip = 0

    op = [operation[0] for operation in program]
    row_col = [(operation[1], operation[2]) for operation in program]
    types = [operation[3] for operation in program]

    assert len(OpKeywords) == 20, "You have to handle all the OpOperations"
    while ip < len(program):
        if op[ip] == '+':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(a + b))
            ip = ip + 1

        elif op[ip] == '-':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b - a))
            ip = ip + 1

        elif op[ip] == '*':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b * a))
            ip = ip + 1

        elif op[ip] == '/':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b / a))
            ip = ip + 1

        elif op[ip] == '=':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b == a))
            ip = ip + 1

        elif op[ip] == '!=':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b != a))
            ip = ip + 1

        elif op[ip] == '>':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b > a))
            ip = ip + 1

        elif op[ip] == '<':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b < a))
            ip = ip + 1

        elif op[ip] == '>=':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b >= a))
            ip = ip + 1
        
        elif op[ip] == '<=':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b <= a))
            ip = ip + 1

        elif op[ip] == 'mod':
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b % a))
            ip = ip + 1

        elif op[ip] == 'print':
            a = stack.pop()
            print(a)

            ip = ip + 1

        elif op[ip] == 'over':
            a = stack.pop()
            b = stack.pop()

            stack.append(b)
            stack.append(a)
            stack.append(b)
            ip = ip + 1

        elif op[ip] == 'dup':
            a = stack.pop()

            stack.append(a)
            stack.append(a)
            ip = ip + 1

        elif op[ip] == 'drop':
            stack.pop()
            ip = ip + 1

        elif op[ip] == 'swap':
            a = stack.pop()
            b = stack.pop()

            stack.append(a)
            stack.append(b)
            ip = ip + 1
        
        elif op[ip] == '2dup':
            a = stack.pop()
            b = stack.pop()

            stack.append(a)
            stack.append(b)
            stack.append(a)
            stack.append(b)
            ip = ip + 1

        elif op[ip] == 'band':
            a = stack.pop()
            b = stack.pop()

            stack.append(b & a)
            ip = ip + 1

        elif op[ip] == 'bor':
            a = stack.pop()
            b = stack.pop()

            stack.append(b | a)
            ip = ip + 1

        elif op[ip] == 'bxor':
            a = stack.pop()
            b = stack.pop()

            stack.append(b ^ a)
            ip = ip + 1

        elif op[ip] == 'if':
            print("sus")

        else:
            if types[ip] in OpType:
                stack.append(op[ip])
                ip = ip + 1
            else:
                assert False, "unreachable"

if __name__ == '__main__':
    
    argv = sys.argv
    if len(argv) != 2:
        assert False, "The interpreter requires a file to interpret"
    program_path = argv[1]

    #Parsing
    program = parse_file_to_tokens(program_path, program)

    #Simulate
    simulate_program(program)