# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:27:38 2017

@author: User
"""

from graphviz import Digraph

dot = Digraph(comment = 'Проезд ПВП МСК-> РнД')

dot.node('A', 'ПВП1')
dot.node('B', 'ПВП2')
dot.node('C', 'ПВП3')
dot.node('D', 'ПВП4')

dot.edges(['AB', 'BC', 'CD'])
dot.edge('A', 'C', color='Red', label='135 КМ')
dot.edge('A', 'D', color='Red')
dot.attr(color='Green')

print (dot.source)

dot.render('C:\\py_tests\\round-table.gv.pdf', view=True)
#dot.render('C:\\py_tests\\round-table.gv', view=True)  # doctest: +SKIP 'C:\\py_tests\\round-table.gv.pdf' 