import ast
import inspect
import json
import os
import collections

def convert_ast(node, return_type='string', sep=':'):
    count = 1
    def _flatten_dict(d, parent_key='', sep=':'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(_flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def _flatten_list(lst):
        return sum(([x] if not isinstance(x, list) else _flatten_list(x) for x in lst), [])

    def _format(node):
        nonlocal count
        if isinstance(node, ast.AST):
            return _flatten_dict({ key: _format(value) for key, value in ast.iter_fields(node) if key != 'ctx'})

        elif isinstance(node, list):
            return sep.join(_flatten_list([value for list_node in node for value in _format(list_node).values() if value]))

        return str(node)

    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    if return_type == 'string':
        return sep.join([value for value in _format(node).values() if value])

    elif return_type == 'list':
        return list(_format(node).values())
    else:
        return _format(node)

def get_calls(source, return_type='string'):
    calls = []

    def visit_Call(node):
        calls.append(convert_ast(node, return_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return calls

def get_assignments(source, return_type='string'):
    assignments = []

    def visit_Assign(node):
        assignments.append(convert_ast(node, return_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Assign = visit_Assign
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return assignments

def get_for_loops(source, return_type='string'):
    assignments = []

    def visit_For(node):
        assignments.append(convert_ast(node, return_type))

    node_iter = ast.NodeVisitor()
    node_iter.visit_For = visit_For
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return assignments