import ast
import inspect
import json
import os
import collections


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_functions(source):
    functions = []

    def visit_Call(node):
        path = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id
        if len(node.args) != 0:
            path += ':' + ':'.join([str(val) for arg in node.args for val in build_dict(arg).values()])

        if len(node.keywords) != 0:
            path += ':' + ':'.join([str(val) for keyword in node.keywords for val in build_dict(keyword).values()])

        functions.append(path)

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return functions

def get_functions_returns(source):
    returns = []

    def visit_Return(node):
        returns.append(build_dict(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Return = visit_Return
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return returns

def get_statements(source):
    statements = []

    def visit_If(node):
        statements.append(build_dict(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_If = visit_If
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return statements

def build_dict(node):
    result = {}
    if node.__class__.__name__ == 'Is' or node.__class__.__name__ == 'Eq':
        result['node_type'] = node.__class__.__name__
    for attr in dir(node):
        if not attr.startswith("_") and attr != 'ctx' and attr != 'lineno' and attr != 'col_offset':
            value = getattr(node, attr)
            if isinstance(value, ast.AST):
                value = build_dict(value)
            elif isinstance(value, list):
                final = [build_dict(n) for n in value]
                value = final[0] if len(final) == 1 else final
            if value != []:
                result[attr] = value
    return flatten(result, sep='/')
