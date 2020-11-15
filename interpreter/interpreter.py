from lexer import Lexer
from tokens import TokenTypes
from tokens import Token
from logger import get_logger

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
            return token.value

        if token.type == TokenTypes.LPAR:
            self.eat(TokenTypes.LPAR)
            result = self.expr()
            self.eat(TokenTypes.RPAR)
            return result

    def term(self):
        result = self.factor()
        logger.debug(f"Term {result}")

        while (token_type := self.current_token.type) in (
            TokenTypes.MULTIPLY,
            TokenTypes.DIVIDE,
        ):
            if token_type == TokenTypes.MULTIPLY:
                self.eat(TokenTypes.MULTIPLY)
                result *= self.factor()
            elif token_type == TokenTypes.DIVIDE:
                self.eat(TokenTypes.DIVIDE)
                result /= self.factor()

        return result

    def expr(self):
        result = self.term()
        logger.debug(f"Expr {result}")

        while (token_type := self.current_token.type) in (
            TokenTypes.PLUS,
            TokenTypes.MINUS,
        ):
            if token_type == TokenTypes.PLUS:
                self.eat(TokenTypes.PLUS)
                result += self.term()
            if token_type == TokenTypes.MINUS:
                self.eat(TokenTypes.MINUS)
                result -= self.term()

        return result


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
        print(result)


if __name__ == "__main__":
    main()
