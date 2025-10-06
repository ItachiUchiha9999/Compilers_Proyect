import ply.lex as lex

# ==============================
# LISTA DE TOKENS
# ==============================

Reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'print': 'PRINT',
    'while': 'WHILE',
    'len': 'LEN',
    'max': 'MAX',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
}

Operators = [
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'PTCOMA',
    'MAYQ',
    'MENQ',
    'DIST',
    'EQ',
]

tokens = [
    'ID',
    'COMMENT',
    'INT',
    'FLOAT',
    'STRING',
    'LPAREN',
    'RPAREN',
] + list(Reserved.values()) + Operators

# ==============================
# EXPRESIONES REGULARES
# ==============================

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_PTCOMA    = r';'
t_MAYQ      = r'>'
t_MENQ      = r'<'
t_DIST      = r'!='
t_EQ        = r'=='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'

t_ignore = ' \t'

# ==============================
# TOKENS COMPLEJOS
# ==============================

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9_]*'
    t.type = Reserved.get(t.value, 'ID')
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error: carácter inválido '{t.value[0]}'")
    t.lexer.skip(1)

# ==============================
# CONSTRUCCIÓN
# ==============================

lexer = lex.lex(optimize=1)
