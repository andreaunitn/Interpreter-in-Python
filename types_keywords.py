from enum import Enum, auto

class OpKeywords(Enum):
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

class OpType(Enum):
    INT = auto()
    STR = auto()
    WORD = auto()

assert len(OpKeywords) == 25, "You have to handle all the OpKeywords"
OpKeywordsMap = {
    '+': OpKeywords.OP_PLUS,
    '-': OpKeywords.OP_MINUS,
    '*': OpKeywords.OP_MUL,
    '/': OpKeywords.OP_DIV,
    '=': OpKeywords.OP_EQ,
    '!=': OpKeywords.OP_NE,
    '>': OpKeywords.OP_GT,
    '<': OpKeywords.OP_LT,
    '>=': OpKeywords.OP_GET,
    '<=': OpKeywords.OP_LET,
    'mod': OpKeywords.OP_MOD,

    'print': OpKeywords.OP_PRINT,
    'over': OpKeywords.OP_OVER,
    'dup': OpKeywords.OP_DUP,
    'drop': OpKeywords.OP_DROP,
    'swap': OpKeywords.OP_SWAP,
    '2dup': OpKeywords.OP_2DUP,
    'band': OpKeywords.OP_BAND,
    'bor': OpKeywords.OP_BOR,
    'bxor': OpKeywords.OP_BXOR,

    'if': OpKeywords.OP_IF,
    'else': OpKeywords.OP_ELSE,
    'end': OpKeywords.OP_END,
    'while': OpKeywords.OP_WHILE,
    'do': OpKeywords.OP_DO,
}

assert len(OpType) == 3, "You have to handle all the OpTypes"
OpTypeMap = {
    'int': OpType.INT,
    'str': OpType.STR,
    'WORD': OpType.WORD
}