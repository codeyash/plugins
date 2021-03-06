#######################################################################
# Name: calc.py
# Purpose: Simple expression evaluator example
# Author: Igor R. Dejanovic <igor DOT dejanovic AT gmail DOT com>
# Copyright: (c) 2009-2014 Igor R. Dejanovic <igor DOT dejanovic AT gmail DOT com>
# License: MIT License
#
# This example demonstrates grammar definition using python constructs as
# well as using semantic actions to evaluate simple expression in infix
# notation.
#######################################################################

from __future__ import unicode_literals, print_function
try:
    text=unicode
except:
    text=str

from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF, SemanticAction,ParserPython, RegExMatch


def number():     return RegExMatch(r'\d*\.\d*|\d+')
def factor():     return Optional(["+","-"]), [number,
                          ("(", expression, ")")]
def term():       return factor, ZeroOrMore(["*","/"], factor)
def expression(): return term, ZeroOrMore(["+", "-"], term)
def calc():       return OneOrMore(expression), EOF


# Semantic actions
def to_floatSA(parser, node, children):
    """
    Converts node value to float.
    """
    if parser.debug:
        print("Converting {}.".format(node.value))
    return float(node.value)

def factorSA(parser, node, children):
    """
    Removes parenthesis if exists and returns what was contained inside.
    """
    if parser.debug:
        print("Factor {}".format(children))
    if len(children) == 1:
        return children[0]
    sign = -1 if children[0] == '-' else 1
    return sign * children[-1]

def termSA(parser, node, children):
    """
    Divides or multiplies factors.
    Factor nodes will be already evaluated.
    """
    if parser.debug:
        print("Term {}".format(children))
    term = children[0]
    for i in range(2, len(children), 2):
        if children[i-1] == "*":
            term *= children[i]
        else:
            term /= children[i]
    if parser.debug:
        print("Term = {}".format(term))
    return term


def exprSA(parser, node, children):
    """
    Adds or substracts terms.
    Term nodes will be already evaluated.
    """
    if parser.debug:
        print("Expression {}".format(children))
    expr = 0
    start = 0
    # Check for unary + or - operator
    if text(children[0]) in "+-":
        start = 1

    for i in range(start, len(children), 2):
        if i and children[i - 1] == "-":
            expr -= children[i]
        else:
            expr += children[i]

    if parser.debug:
        print("Expression = {}".format(expr))

    return expr


# Connecting rules with semantic actions
number.sem = to_floatSA
factor.sem = factorSA
term.sem = termSA
expression.sem = exprSA

def main(debug=False):
    # First we will make a parser - an instance of the calc parser model.
    # Parser model is given in the form of python constructs therefore we
    # are using ParserPython class.
    parser = ParserPython(calc, debug=debug)

    # An expression we want to evaluate
    input_expr = "-(4-1)*5+(2+4.67)+5.89/(.2+7)"

    # We create a parse tree out of textual input_expr
    parse_tree = parser.parse(input_expr)

    result = parser.getASG()

    if debug:
        # getASG will start semantic analysis.
        # In this case semantic analysis will evaluate expression and
        # returned value will be the result of the input_expr expression.
        print("{} = {}".format(input_expr, result))

if __name__ == "__main__":
    # In debug mode dot (graphviz) files for parser model
    # and parse tree will be created for visualization.
    # Checkout current folder for .dot files.
    main(debug=True)

