# -*- coding: utf-8 -*-
###############################################################################
# Name: vistor.py
# Purpose: Filter results using visitor semantic class
# Author: Yash <yash AT speedovation D.O.T. com>
# Copyright: (c) 2014 Yash <yash AT speedovation D.O.T. com> 
# License: Apache License
#
# Traverse nodes and produce result based on semantic class
#  
#  Vistor Example
#
#    class Visitor():
#
#        def __init__(self):
#            Optional pass 
#            self.second_pass = False
#    
#        def sem_rulename(self, parser, node, children):
#            pass
#
#    Use:
#        parser = ParserPEG(calc_grammar, "calc", True)
#
#        analyseASG( parser, input, Visitor(), True, False )
#
#
###############################################################################

from __future__ import print_function, unicode_literals

import sys
if sys.version < '3':
    text = unicode
else:
    text = str

import codecs
import re
import bisect
from arpeggio import SemanticAction, SemanticActionResults, NonTerminal
import types




class analyseASG(object):
    
    """
    Creates Abstract Semantic Graph (ASG) from the parse tree.

    Args:
        parser  : Parser object
        input   : User provided input text
        visitor : Semantic Visitor Class 
        defaults (bool): If True a default semantic action will be
            applied in case no action is defined for the node.
        debug : Print Debug messages if True    
    """
    def __init__(self, parser, input, visitor, defaults=True, debug=False):
    
        self.debug = debug | parser.debug
        self.defaults = defaults
        self.visitor = visitor
        self.parser = parser
        
        try:
            self.parse_tree = parser.parse(input)
        except:
            raise Exception("Parsing failed")    
    
        if not self.parse_tree:
            raise Exception("Parse tree is empty. You did call parse(), didn't you?")
    
        if self.visitor is None:
            raise Exception("Semantic Vistor class not defined.")
  
        self.for_second_pass = []

        def tree_walk(node):
            """
            Walking the parse tree and calling first_pass for every registered
            semantic actions and creating list of object that needs to be
            called in the second pass.
            """
    
            if self.debug:
                print("Walking down ", node.name, "  type:",
                      type(node).__name__, "str:", text(node))
    
            children = SemanticActionResults()
            if isinstance(node, NonTerminal):
                for n in node:
                    child = tree_walk(n)
                    if child is not None:
                        children.append_result(n.rule_name, child)
    
            if self.debug:
                print("Processing ", node.name, "= '", text(node),
                      "'  type:", type(node).__name__,
                      "len:", len(node) if isinstance(node, list) else "")
                for i, a in enumerate(children):
                    print("\t%d:" % (i + 1), text(a), "type:", type(a).__name__)
    

            if hasattr(self.visitor, 'sem_'+node.rule_name) and callable(getattr(self.visitor, 'sem_'+node.rule_name)) :
            
                sem_action = getattr(self.visitor, 'sem_'+node.rule_name)
                retval = sem_action(self, node, children)
    
                if (self.visitor.second_pass):
                    self.for_second_pass.append((node.rule_name, retval))
    
                if self.debug:
                    action_name = sem_action.__name__ \
                        if hasattr(sem_action, '__name__') \
                        else sem_action.__class__.__name__
                    print("\tApplying semantic action ", action_name)
    
            else:
                if defaults:
                    # If no rule is present use some sane defaults
                    if self.debug:
                        print("\tApplying default semantic action.")
    
                    retval = SemanticAction().first_pass(parser, node, children)
    
                else:
                    retval = node
    
            if self.debug:
                if retval is None:
                    print("\tSuppressed.")
                else:
                    print("\tResolved to = ", text(retval),
                          "  type:", type(retval).__name__)
            return retval
    
        if self.debug:
            print("ASG: First pass")
            
        asg = tree_walk(self.parse_tree)
    
        # Second pass
        if self.debug:
            print("ASG: Second pass")
        
        #TODO : I don't know why it's required and what's second pass 
        for sa_name, asg_node in self.for_second_pass:
            print (sa_name )
            print (asg_node)
            #getattr(self.visitor,sa_name ).second_pass(self, asg_node)
    
        return 
    
        