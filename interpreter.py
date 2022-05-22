from enum import Enum, auto
import sys

class OpType(Enum):
    INT = auto()
    BOOL = auto()
    STR = auto()

assert len(OpType) == 3, "You have to handle all the OpTypes"
OpTypeMap = {
    int: OpType.INT,
    bool: OpType.BOOL,
    str: OpType.STR
}

class OpOperation(Enum):
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    OP_EQ = auto()
    OP_NE = auto()
    OP_GT = auto()
    OP_LT = auto()
    OP_GET = auto()
    OP_LET = auto()
    OP_MOD = auto()

    OP_PRINT = auto()
    OP_OVER = auto()
    OP_DUP = auto()
    OP_DROP = auto()
    OP_SWAP = auto()
    OP_2DUP = auto()
    OP_BAND = auto()
    OP_BOR = auto()
    OP_BXOR = auto()

    OP_IF = auto()
    OP_ELSE = auto()
    OP_END = auto()
    OP_WHILE = auto()
    OP_DO = auto()

assert len(OpOperation) == 25, "You have to handle all the OpOperations"
OpOperationMap = {
    '+': OpOperation.OP_PLUS,
    '-': OpOperation.OP_MINUS,
    '*': OpOperation.OP_MUL,
    '/': OpOperation.OP_DIV,
    '=': OpOperation.OP_EQ,
    '!=': OpOperation.OP_NE,
    '>': OpOperation.OP_GT,
    '<': OpOperation.OP_LT,
    '>=': OpOperation.OP_GET,
    '<=': OpOperation.OP_LET,
    'mod': OpOperation.OP_MOD,

    'print': OpOperation.OP_PRINT,
    'over': OpOperation.OP_OVER,
    'dup': OpOperation.OP_DUP,
    'drop': OpOperation.OP_DROP,
    'swap': OpOperation.OP_SWAP,
    '2dup': OpOperation.OP_2DUP,
    'band': OpOperation.OP_BAND,
    'bor': OpOperation.OP_BOR,
    'bxor': OpOperation.OP_BXOR,

    'if': OpOperation.OP_IF,
    'else': OpOperation.OP_ELSE,
    'end': OpOperation.OP_END,
    'while': OpOperation.OP_WHILE,
    'do': OpOperation.OP_DO,
}

if_while_end = [OpOperation.OP_IF, OpOperation.OP_WHILE, OpOperation.OP_END, OpOperation.OP_ELSE, OpOperation.OP_DO]

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

program = []

def check_types(program):

    assert len(OpType) == 3, "You have to handle all the OpTypes"
    for op in program:
        value = op[0]
        row = op[0]
        col = op[0]

        try:
            value = int(value)
        except:
            try:
                value = bool(value)
            except:
                try:
                    value = str(value)
                except:
                    print(colors.FAIL + "ERROR" + colors.ENDC + ": undefined token type " + colors.WARNING + "'%s'" % value + colors.ENDC + " at %d:%d" % (row, col))
                    exit(1)

        program.append((value, row, col))
    
    return program


"""
def check_types(word):
    assert len(OpType) == 2, "You have to handle all the OpTypes"
    try:
        word = int(word)
    except:
        if word == 'True':
            word = True
        elif word == 'False':
            word = False

    return word
"""

def check_token(program):
    tokens = []

    for token in program:
        value = token[0]

        if value in if_while_end:
            tokens.append(token)
        elif value in OpOperationMap.values() or type(value) in OpTypeMap:
            tokens.append(value)
        else:
            print(colors.FAIL + "ERROR" + colors.ENDC + ": undefined token " + colors.WARNING + "'%s'" % value + colors.ENDC + " at %d:%d" % (token[1], token[2]))
            exit(1)

    return tokens

paired_elements = []

def pair_if_while_end(program):
    tmp1 = []
    tmp2 = []
    tmp3 = []

    assert len(if_while_end) == 5, "length of if_while_end"
    for op in program:
        if op[0] == OpOperation.OP_IF or op[0] == OpOperation.OP_WHILE:
            tmp1.append(op)
        elif op[0] == OpOperation.OP_ELSE:
            tmp2.append(op)
        elif op[0] == OpOperation.OP_DO:
            tmp3.append(op)
        elif op[0] == OpOperation.OP_END:
            op_end = op
            op_if_while = tmp1.pop()
            
            if len(tmp2) > 0 and op_if_while[0] == OpOperation.OP_IF:
                op_else = tmp2.pop()
                paired_elements.append((op_if_while, op_else, op_end))
            elif len(tmp3) > 0 and op_if_while[0] == OpOperation.OP_WHILE:
                op_do = tmp3.pop()
                paired_elements.append((op_if_while, op_do, op_end))
            else:
                paired_elements.append((op_if_while, op_end))

def parse_file_to_tokens(program_path):
    with open(program_path, "r") as source:

        lines = source.readlines()
        row = 1

        words = []
        for line in lines:
            words.append(line.split())

        for line in lines:
            word = ''
            length = len(line)

            for col in range(length):
                if not line[col].isspace() and line[col] != '\n':
                    if line[col] == '#':
                        break
                    else:
                        word += line[col]
                else:
                    if word in words[row - 1]:
                        word_len = len(word)
                        #word = check_types(word)
                        
                        if word in OpOperationMap.keys():
                            token = (OpOperationMap[word], row, col - word_len + 1)
                        else:
                            token = (word, row, col - word_len + 1)

                        program.append(token)
                   
                    word = ''
                
                if col == length - 1:
                    if word in words[row - 1]:
                        word_len = len(word)
                        #word = check_types(word)
                        
                        if word in OpOperationMap.keys():
                            token = (OpOperationMap[word], row, col - word_len + 2)
                        else:
                            token = (word, row, col - word_len + 2)

                        program.append(token)
            row = row + 1 

def simulate_program(program):
    #program = [(OpOperationMap[i[0]], i[1], i[2]) if i[0] in OpOperationMap else i for i in program]
    #program = [OpOperationMap[i] if i in OpOperationMap else i for i in program]
    """
    for op in program:
        if type(op) == tuple:
            val = op[0]
            ind = program.index(op)

            if val in if_while_end:
                program.remove(op)
                op = list(op)
                op[0] = OpOperationMap[val]
                op = tuple(op)
                program.insert(ind, op)
    """
    stack = []
    ip = 0

    assert len(OpOperation) == 25, "You have to handle all the OpOperations"
    while ip < len(program):
        if program[ip] == OpOperation.OP_PLUS:
            a = stack.pop()
            b = stack.pop()

            stack.append(int(a + b))
            ip = ip + 1
        
        elif program[ip] == OpOperation.OP_MINUS:
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b - a))
            ip = ip + 1
        
        elif program[ip] == OpOperation.OP_MUL:
            a = stack.pop()
            b = stack.pop()

            stack.append(int(a * b))
            ip = ip + 1

        elif program[ip] == OpOperation.OP_DIV:
            a = stack.pop()
            b = stack.pop()

            stack.append(int(b / a))
            ip = ip + 1

        elif program[ip] == OpOperation.OP_EQ:
            a = stack.pop()
            b = stack.pop()

            if a == b:
                stack.append(True)
            else:
                stack.append(False)
            ip = ip + 1
        
        elif program[ip] == OpOperation.OP_NE:
            a = stack.pop()
            b = stack.pop()

            if a != b:
                stack.append(True)
            else:
                stack.append(False)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_GT:
            a = stack.pop()
            b = stack.pop()

            if b > a:
                stack.append(True)
            else:
                stack.append(False)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_LT:
            a = stack.pop()
            b = stack.pop()

            if b < a:
                stack.append(True)
            else:
                stack.append(False)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_GET:
            a = stack.pop()
            b = stack.pop()

            if b >= a:
                stack.append(True)
            else:
                stack.append(False)
            ip = ip + 1
        
        elif program[ip] == OpOperation.OP_LET:
            a = stack.pop()
            b = stack.pop()

            if b <= a:
                stack.append(True)
            else:
                stack.append(False)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_MOD:
            a = stack.pop()
            b = stack.pop()

            stack.append(b % a)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_PRINT:
            a = stack.pop()
            print(a)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_OVER:
            a = stack.pop()
            b = stack.pop()

            stack.append(b)
            stack.append(a)
            stack.append(b)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_DUP:
            a = stack.pop()

            stack.append(a)
            stack.append(a)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_DROP:
            stack.pop()
            ip = ip + 1

        elif program[ip] == OpOperation.OP_SWAP:
            a = stack.pop()
            b = stack.pop()

            stack.append(a)
            stack.append(b)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_2DUP:
            a = stack.pop()
            b = stack.pop()

            stack.append(a)
            stack.append(b)
            stack.append(a)
            stack.append(b)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_BAND:
            a = stack.pop()
            b = stack.pop()

            stack.append(b & a)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_BOR:
            a = stack.pop()
            b = stack.pop()

            stack.append(b | a)
            ip = ip + 1

        elif program[ip] == OpOperation.OP_BXOR:
            a = stack.pop()
            b = stack.pop()

            stack.append(b ^ a)
            ip = ip + 1

        elif type(program[ip]) == tuple and program[ip][0] == OpOperation.OP_IF:
            condition = stack.pop()

            if type(condition) != bool:
                print(colors.FAIL + "ERROR" + colors.ENDC + ": 'if' accept only True/False conditions")
                exit(1)

            pos_end = ip
            pos_else = ip

            for elem in paired_elements:
                if elem[0] == program[ip]:
                    op = elem[1]
                    if len(elem) == 2:
                        pos_end = program.index(op)
                    elif len(elem) == 3:
                        pos_else = program.index(op)
                    break

            if condition == True:
                ip = ip + 1
            else:
                if pos_else != ip:
                    ip = pos_else + 1
                else:
                    ip = pos_end

        elif type(program[ip]) == tuple and program[ip][0] == OpOperation.OP_ELSE:
            pos_end = ip

            for elem in paired_elements:
                for sub_elem in elem:
                    if sub_elem == program[ip]:
                        pos_end = program.index(elem[2])
                        break
            
            if pos_end != ip:
                ip = pos_end
            else:
                assert False, "unreachable"

        elif type(program[ip]) == tuple and program[ip][0] == OpOperation.OP_END:

            for elem in paired_elements:
                if program[ip] in elem:
                    if elem[0][0] == OpOperation.OP_IF:
                        ip = ip + 1
                        break
                    elif elem[0][0] == OpOperation.OP_WHILE:
                        pos_while = program.index(elem[0])
                        ip = pos_while
                        break
                    else:
                        assert False, "unreachable"

        elif type(program[ip]) == tuple and program[ip][0] == OpOperation.OP_WHILE:
            ip = ip + 1

        elif type(program[ip]) == tuple and program[ip][0] == OpOperation.OP_DO:
            condition = stack.pop()

            if type(condition) != bool:
                print(colors.FAIL + "ERROR" + colors.ENDC + ": 'while-do' accept only True/False conditions")
                exit(1)

            for elem in paired_elements:
                if program[ip] in elem:
                    op_end = program.index(elem[-1])
                    break

            if condition == True:
                ip = ip + 1
            else:
                ip = op_end + 1


        else:
            if program[ip] in OpOperationMap.values() or type(program[ip]) in OpTypeMap:
                stack.append(program[ip])
                ip = ip + 1
            else:
                assert False, "unreachable"
 
if __name__ == '__main__':
   
    argv = sys.argv
    if len(argv) != 2:
        assert False, "The interpreter requires a file to interpret"

    program_path = argv[1]
    #Parsing
    parse_file_to_tokens(program_path)

    #Rearrange tokens
    pair_if_while_end(program)
    program = check_types(program)
    program = check_token(program)

    #Simulate program
    simulate_program(program)