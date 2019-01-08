import ast
import inspect
import json
import os
import collections

def ast_to_dict(node):
    def _flatten(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(_flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def _format(node):
        if isinstance(node, ast.AST):
            result = {} 
            for key, value in ast.iter_fields(node):
                if key != 'ctx':
                    result[key] = _format(value)
            return _flatten(result)

        elif isinstance(node, list):
            return [_flatten(_format(node_list)) for node_list in node]

        return repr(node)
    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)
    return _format(node)

def get_functions(source):
    functions = []

    def visit_Call(node):
        functions.append(ast_to_dict(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return functions

def get_functions_returns(source):
    returns = []

    def visit_Return(node):
        returns.append(ast_to_dict(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Return = visit_Return
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return returns

def get_statements(source):
    statements = []

    def visit_If(node):
        statements.append(ast_to_dict(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_If = visit_If
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return statements