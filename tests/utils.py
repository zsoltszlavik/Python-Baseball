import ast
import inspect
import json
import os
import collections

def convert_ast(node, return_type='string', sep=':'):
    count = 1
    def _flatten(d, parent_key='', sep=':'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(_flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def _format(node):
        nonlocal count
        if isinstance(node, ast.AST):
            result = {}
            for key, value in ast.iter_fields(node):
                if key != 'ctx':
                    result[key] = _format(value)

            return _flatten(result)

        elif isinstance(node, list):
            return [_format(node_list) for node_list in node]

        return str(node)

    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    if return_type == 'string':
        return sep.join(_format(node).values())
    elif return_type == 'list':
        return list(_format(node).values())
    else:
        return _format(node)

def get_functions(source):
    function_calls = []

    def visit_Call(node):
        function_calls.append(convert_ast(node, 'dict'))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return function_calls

def get_functions_returns(source):
    returns = []

    def visit_Return(node):
        returns.append(convert_ast(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Return = visit_Return
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return returns

def get_statements(source):
    statements = []

    def visit_If(node):
        statements.append(convert_ast(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_If = visit_If
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return statements