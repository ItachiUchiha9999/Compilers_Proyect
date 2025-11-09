import ply.lex as lex


# ==============================
# LISTA DE TOKENS
# ==============================

Reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'print': 'PRINT',
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
    'MAYQ',
    'MENQ',
    'DIST',
    'EQ',
    'ASSIGN',
]

tokens = [
    'ID',
    'INT',
    'FLOAT',
    'STRING',
] + list(Reserved.values()) + Operators

# ==============================
# EXPRESIONES REGULARES
# ==============================

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_DIST      = r'!='
t_EQ        = r'=='
t_ASSIGN    = r'='
t_MAYQ      = r'>'
t_MENQ      = r'<'


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
    r'\#\#.*'
    t.lexer.lineno += 1
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"⛔ Error léxico en línea {t.lineno}: carácter inválido '{t.value[0]}'")
    t.lexer.skip(1)
    raise SystemExit  # 🔥 Esto hace que se detenga completamente al primer error

# ==============================
# CONSTRUCCIÓN
# ==============================

lexer = lex.lex()


if __name__ == '__main__':
    # When this module is run directly, print a short confirmation.
    # When imported (e.g. `from lexer import lexer`) these prints won't run.
    print("Lexer cargado correctamente con tokens:")
    print(tokens)
