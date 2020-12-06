
class AST(object):
    pass

class BinOp(object):
    """
    Represents operator in the abstract syntax tree.
    BinOp handles binary operations (operates on two operands).
    """
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(AST):
    """
    Represents integer in the abstract syntax tree.
    """
    def __init__(self, token):
        self.token = token
        self.value = token.value