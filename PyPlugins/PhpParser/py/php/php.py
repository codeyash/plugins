#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

from arpeggio.cleanpeg import ParserPEG
from arpeggio import visit_parse_tree
from visitor import Visitor
import sys

#Used finder.py module to recursively finding php tokens    
def parse(filename, debug=False):

    
    with open(filename) as file:
        contents = file.read()
        
    parser = ParserPEG(calc_grammar, "start", True)
    
    parse_tree = parser.parse(contents)

    visitor = Visitor(debug=debug)
    
    
    result = visit_parse_tree(parse_tree, visitor )
    
    #Try to get if we found anything or not
    
    if ( visitor.functions or visitor.classes):
        print (visitor.namespace )
    
        return visitor
        
    print ("Empty")
    
    return None
    
#Below code just to dev used and testing    

def main(debug=False):

        
    filename = sys.argv[1]
    #debug = bool(sys.argv[2])
    
    with open(filename) as file:
        contents = file.read()
    #print (contents)
#    # An expression we want to evaluate
    input_expr = """class Application extends Container implements HttpKernelInterface, TerminableInterface, ResponsePreparerInterface {
        """
     
     
#    input_expr = input
    input_expr = contents
    
    if not input_expr:
        return None
    
    # First we will make a parser - an instance of the calc parser model.
    # Parser model is given in the form of PEG notation therefore we
    # are using ParserPEG class. Root rule name (parsing expression) is "calc".
    parser = ParserPEG(calc_grammar, "start", True)


    # Then parse tree is created out of the input_expr expression.
    parse_tree = parser.parse(input_expr)

    visitor = Visitor(debug=debug)
    result = visit_parse_tree(parse_tree, visitor )
    
    print (visitor.namespace )
    #print (visitor.classes )
    #print (visitor.functions )

#    analyseASG( parser, input, Visitor(), True, False )


    # Then parse tree is created out of the input_expr expression.
    #parse_tree = parser.parse(input_expr)
    #result = parser.getASG(sem_actions)

    #print( parse_tree )
    #print( result )
    if debug:
        # getASG will start semantic analysis.
        # In this case semantic analysis will evaluate expression and
        # returned value will be evaluated result of the input_expr expression.
        # Semantic actions are supplied to the getASG function.
        print("{} = {}".format(input_expr, result))

if __name__ == "__main__":
    # In debug mode dot (graphviz) files for parser model
    # and parse tree will be created for visualization.
    # Checkout current folder for .dot files.
    main(debug=False)

