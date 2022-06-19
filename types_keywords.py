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

class OpType(Enum):
    INT = auto()
    STR = auto()
    WORD = auto()

assert len(OpKeywords) == 12, "You have to handle all the OpKeywords"
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

    'print': OpKeywords.OP_PRINT
}

assert len(OpType) == 3, "You have to handle all the OpTypes"
OpTypeMap = {
    'int': OpType.INT,
    'str': OpType.STR,
    'WORD': OpType.WORD
}