from token import TokenTypes, Token
from ast import Num, BinOp

class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == TokenTypes.INTEGER:
            self.eat(TokenTypes.INTEGER):
            return Num(token)
        elif token.type == TokenTypes.LPAR:
            self.eat(TokenTypes.LPAR)
            node = self.expr()
            self.eat(TokenTypes.RPAR)
            return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (TokenTypes.MULTIPLY, TokenTypes.DIVIDE):
            token = self.current_token
            if token.type == TokenTypes.MULTIPLY:
                self.eat(TokenTypes.MULTIPLY)
            elif token.type == TokenTypes.DIVIDE:
                self.eat(TokenTypes.DIVIDE)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (TokenTypes.PLUS, TokenTypes.MINUS):
            token = self.current_token
            if token.type == TokenTypes.PLUS:
                self.eat(TokenTypes.PLUS)
            elif token.type == TokenTypes.MINUS:
                self.eat(TokenTypes.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()

