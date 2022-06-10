from enum import Enum, auto

class OpKeywords(Enum):
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_MUL = auto()
    OP_DIV = auto()

class OpType(Enum):
    INT = auto()
    BOOL = auto()
    STR = auto()

assert len(OpKeywords) == 4, "You have to handle all the OpKeywords"
OpKeywordsMap = {
    '+': OpKeywords.OP_PLUS,
    '-': OpKeywords.OP_MINUS,
    '*': OpKeywords.OP_MUL,
    '/': OpKeywords.OP_DIV
}

assert len(OpType) == 3, "You have to handle all the OpTypes"
OpTypeMap = {
    int: OpType.INT,
    bool: OpType.BOOL,
    str: OpType.STR
}