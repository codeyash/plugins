#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
 
class EntryParser(NodeVisitor):
    
    def __init__(self, grammar, text):
        self.entry = {}
        ast = Grammar(grammar).parse(text)
        self.visit(ast)
    
    def visit_name(self, n, vc):
        self.entry['name'] = n.text
    
    def visit_gender(self, n, vc):
        self.entry['gender'] = n.text
    
    def visit_age(self, n, vc):
        self.entry['age'] = n.text
    
    def generic_visit(self, n, vc):
        pass
 
grammar = """\
entry = name sep gender? (sep age)?
sep = ws "," ws
ws = " "*
name = ~"[A-z]*"
gender = "male" / "female"
age = ~"[0-9]*"
"""

calc_grammar = """

calc = expression+ anyword
factor = ("+" / "-")? ( number / ("(" expression ")") )
expression = term (("+" / "-") term)*
term = factor (( "*" / "/") factor)*
number = ~"\d*\.\d*|\d+"

anyword = ~"[\w\W]*"

"""

text = """\
Bob,
Kim,female,30
Joe,male
"""

calc_text = """\
4+5
4+6+(4*7)h hh b
"""


class EntryVisitor(NodeVisitor):
    
    def __init__(self, grammar, text):
        self.entry = {}
        ast = Grammar(grammar).parse(text)
        self.visit(ast)
    
    def visit_number(self, n, vc):
        self.entry['number'] = n.text
    
    def visit_expression(self, n, vc):
        self.entry['expression'] = n.text
    
    def generic_visit(self, n, vc):
        pass
        
        
grammar = Grammar(calc_grammar)
#print( grammar.parse("4+6+(4*7)") )

for line in calc_text.splitlines():
    print( EntryVisitor(calc_grammar, line).entry )

#for line in text.splitlines():
#    print( EntryParser(grammar, line).entry )