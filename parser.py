import ply.yacc as yacc
from lexer import tokens

start = 'expression'

# === GRAMÁTICA DE EXPRESIONES ARITMÉTICAS ===
variable = {}
def p_assignment(p):
    'expression : ID ASSIGN expression'
    variable[p[1]] = p[3]
    print(f"{p[1]} = {p[3]}")

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : INT
              | FLOAT'''
    p[0] = p[1]

def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]

"""
-> Recomendado por optimizacion / pero no para distinguir cada sentencia
def p_coondition(p):
    '''if_statement : IF condition block
                  | ELIF condition block
                  | ELSE block'''
    if p[0] == 'IF':
        print('Conditional IF')
    elif p[0] == 'ELIF':
        print('Conditional ELIF')
    elif p[0] == 'ELSE':
        print('Conditional ELSE')
    else:
        print('Error in conditional')
"""

def p_if_statement(p):
    'expression : IF condition block'
    p[0] = ('IF', p[2], p[4])

def p_elif_statement(p):
    'expression : ELIF expression block'
    p[0] = ('ELIF', p[2], p[4])

def p_else_statement(p):
    'expression : ELSE block'
    p[0] = ('ELSE', p[3])

def p_boolean_expression(p):
    '''condition : expression AND expression
                 | expression OR expression'''
    if p[2] == 'and' or p[2] == 'AND':
        p[0] = p[1] and p[3]
    elif p[2] == 'or' or p[2] == 'OR':
        p[0] = p[1] or p[3]

def p_boolean_not(p):
    'condition : NOT condition'
    p[0] = not p[2] 

def p_print(p):
    'expression : PRINT expression'
    print(p[2])
    p[0] = None

def p_len(p):
    'expression : LEN ID'
    p[0] = len(variable.get(p[2], []))

def p_max(p):
    'expression : ID MAX ID'
    val1 = variable.get(p[1], 0)
    val2 = variable.get(p[3], 0)
    p[0] = max(val1, val2)

def p_condition(p):
    '''condition : expression EQ expression
                 | expression DIST expression
                 | expression MAYQ expression
                 | expression MENQ expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]

def p_block(p):
    '''block : expression
             | block expression'''
    p[0] = p[1]
    
def p_error(p):
    if p:
        print(f"Error sintáctico: token inesperado '{p.value}' en la línea {p.lineno}")
    else:
        print("Error sintáctico: fin de archivo inesperado")
    raise SyntaxError("Se detuvo el análisis por error sintáctico")

parser = yacc.yacc()

