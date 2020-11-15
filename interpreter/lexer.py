from logger import get_logger
from tokens import Token
from tokens import TokenTypes

logger = get_logger("lexer")


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos]

    def error(self):
        raise Exception("Error Parsing input")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return int(result)

    def get_next_token(self):
        """
        Lexical analyser aka. lexer, scanner or tokenizer
        """

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                integer = self.integer()
                logger.debug(f"Returning {Token(TokenTypes.INTEGER, integer)}")
                return Token(TokenTypes.INTEGER, integer)

            if self.current_char == "+":
                self.advance()
                logger.debug(f'Returning {Token(TokenTypes.PLUS, "+")}')
                return Token(TokenTypes.PLUS, "+")

            if self.current_char == "-":
                self.advance()
                logger.debug(f'Returning {Token(TokenTypes.MINUS, "-")}')
                return Token(TokenTypes.MINUS, "-")

            if self.current_char == "*":
                self.advance()
                logger.debug(f'Returning {Token(TokenTypes.MULTIPLY, "*")}')
                return Token(TokenTypes.MULTIPLY, "*")

            if self.current_char == "/":
                self.advance()
                logger.debug(f'Returning {Token(TokenTypes.DIVIDE, "/")}')
                return Token(TokenTypes.DIVIDE, "/")

            if self.current_char == "(":
                self.advance()
                logger.debug(f'Returning {Token(TokenTypes.LPAR, "(")}')
                return Token(TokenTypes.LPAR, "(")

            if self.current_char == ")":
                self.advance()
                logger.debug(f'Returning {Token(TokenTypes.RPAR, ")")}')
                return Token(TokenTypes.RPAR, ")")

            self.error()

        return Token(TokenTypes.EOF, None)
