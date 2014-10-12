#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from __future__ import absolute_import, unicode_literals, print_function

from arpeggio.cleanpeg import ParserPEG
import sys

# Semantic actions
from calc import to_floatSA, factorSA, termSA, exprSA

from visitor import analyseASG

input = """\
<?php 
class Man extends Person {
    protected $self = array();
    public function __construct( $fun ) {
        $args = func_get_args();
        for( $i=0, $n=count($args); $i<$n; $i++ )
            $this->add($args[$i]);
    }
   
    public function __get(  $name = null ) {
        return $this->self[$name];
    }
   
    public function add(  $name = null,  $enum = null ) {
        if( isset($enum) )
            $this->self[$name] = $enum;
        else
            $this->self[$name] = end($this->self) + 1;
    }

class Man1  {
    
}

class Man2 extends Person {
    
}

class Man3 extends Person,Common {
    
}


    
    
    

"""


# Grammar is defined using textual specification based on PEG language.
calc_grammar = """


calc =  (class/ function / variable / symbol / word  )*
class = "class" word ( "extend" ","  ( word ","* )+  )*
function = visibility "function" word arguments* block
block = "{" r'[^}]*' "}"
arguments = "(" argument* ")"

#$types = array("cappuccino")
#arguments end with optional comma
argument = ( byvalue / byreference ) ("=" value )* ","*
byreference = "&" variable
byvalue = variable

#value may be variable or array or string or any php type 
#Need to add more like array
value = variable / word / string 

visibility = "public" / "protected" / "private"

variable = r'\$[a-zA-z]+[a-zA-Z0-9_]*'

string = ('"' word '"' ) / ( "'" word "'" )
word = r'[a-zA-Z0-9_]+'
literal = r'[a-zA-Z]+'

comment = r'("//.*")|("/\*.*\*/")'
symbol = r'[\W]+'

anyword = r'[\w]*'
ws = r'[\s]+'


"""

class Visitor():

    def __init__(self):
        #Optional pass 
        self.second_pass = False

    def sem_function(self, parser, node, children):
        """
            Removes parenthesis if exists and returns what was contained inside.
        """
        print ("Function name")
        print(children[1])
        
        if len(children) == 1:
            print(children[0]) 
            return children[0]
        
        sign = -1 if children[0] == '-' else 1
        
        return sign * children[-1]
    
    def sem_class(self, parser, node, children):
        print (" class name" )
        print (children)


# Rules are mapped to semantic actions
#sem_actions = {
#    "function" : function,
#    "class" : sem_class,
#}
#

def main(debug=False):

    # First we will make a parser - an instance of the calc parser model.
    # Parser model is given in the form of PEG notation therefore we
    # are using ParserPEG class. Root rule name (parsing expression) is "calc".
    parser = ParserPEG(calc_grammar, "calc", True)

    analyseASG( parser, input, Visitor(), True, False )

#    filename = sys.argv[1]
#    with open(filename) as file:
#        contents = file.read()
#    
#    # An expression we want to evaluate
    input_expr = """public function __construct( $rtt = hh ) { }"""
#    input_expr = contents
    input_expr = input

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

