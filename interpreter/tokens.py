from typing import Union


class TokenTypes:
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    EOF = "EOF"
    LPAR = "LPAR"
    RPAR = "RPAR"


class Token(object):
    def __init__(self, type: str, value: Union[str, int]):
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type}, {self.value})"

    def __repr__(self) -> str:
        return self.__str__()
