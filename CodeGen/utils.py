import html


def indent(string: str, no_indents=1, indent_spaces=4):
    """Indents an entie block of text by a fixed amount.

    Parameters
    ----------
    string : str
        The text to indent.
    time : int
        The number of times the text should be indented.
    indent_spaces : int
        The number of spaces (" ") each indent consists of.
    """
    spaces = " " * no_indents * indent_spaces
    return "\n".join([spaces + i for i in string.split("\n")])


def escape(x):
    return html.escape(x, quote=False)


class InitError(Exception):
    pass
