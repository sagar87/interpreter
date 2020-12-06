from lexer import Lexer
from tokens import TokenTypes
from tokens import Token
from logger import get_logger
from ast import AST, BinOp, Num

logger = get_logger("Interpreter")


class Interpreter(object):
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid Syntax")

    def eat(self, token_type: Token):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == TokenTypes.INTEGER:
            self.eat(TokenTypes.INTEGER)
            return Num(token)

        if token.type == TokenTypes.LPAR:
            self.eat(TokenTypes.LPAR)
            result = self.expr()
            self.eat(TokenTypes.RPAR)
            return result

    def term(self):
        node = self.factor()
        logger.debug(f"Term {node}")

        while (token := self.current_token) in (
            TokenTypes.MULTIPLY,
            TokenTypes.DIVIDE,
        ):
            if token.type == TokenTypes.MULTIPLY:
                self.eat(TokenTypes.MULTIPLY)
            elif token.type == TokenTypes.DIVIDE:
                self.eat(TokenTypes.DIVIDE)
        
            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()
        logger.debug(f"Expr {node}")

        while (token := self.current_token) in (
            TokenTypes.PLUS,
            TokenTypes.MINUS,
        ):
            if token.type == TokenTypes.PLUS:
                self.eat(TokenTypes.PLUS)
            if token.type == TokenTypes.MINUS:
                self.eat(TokenTypes.MINUS)
            
            node = BinOp(left=node, op=token, right=self.term())
                

        return node

    def parse(self):
        return self.expr()

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result.value)


if __name__ == "__main__":
    main()
