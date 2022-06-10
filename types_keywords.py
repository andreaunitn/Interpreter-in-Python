from enum import Enum, auto

class OpKeywords(Enum):
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    OP_PRINT = auto()

class OpType(Enum):
    INT = auto()
    STR = auto()
    WORD = auto()

assert len(OpKeywords) == 5, "You have to handle all the OpKeywords"
OpKeywordsMap = {
    '+': OpKeywords.OP_PLUS,
    '-': OpKeywords.OP_MINUS,
    '*': OpKeywords.OP_MUL,
    '/': OpKeywords.OP_DIV,
    'print': OpKeywords.OP_PRINT
}

assert len(OpType) == 3, "You have to handle all the OpTypes"
OpTypeMap = {
    'int': OpType.INT,
    'str': OpType.STR,
    'WORD': OpType.WORD
}