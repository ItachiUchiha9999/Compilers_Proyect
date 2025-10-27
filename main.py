from lexer import lexer
from parser import parser


'''
1.Estructura General
Programa             → ListaInstrucciones

ListaInstrucciones   → Instruccion
                     | Instruccion ListaInstrucciones

Instruccion          → Asignacion
                     | Condicional
                     | Funcion

2.Asignaciones
Asignacion           → ID ASSIGNMENT Expresion

3.Sentencia de Control
Condicional          → IF Expresion COLON Bloque Elif_Part Else_Part

Elif_Part            → ELIF Expresion COLON Bloque
                     | ε

Else_Part            → ELSE COLON Bloque
                     | ε

Bloque               → INDENT ListaInstrucciones DEDENT

4.Funciones
Funcion              → PRINT LPAREN Expresion RPAREN
                     | LEN LPAREN ID RPAREN
                     | MAX LPAREN ID COMMA ID RPAREN

5.Expresiones o Tipos de Datos
Expresion            → ExprOr

ExprOr               → ExprOr OR ExprAnd
                     | ExprAnd

ExprAnd              → ExprAnd AND ExprNot
                     | ExprNot

ExprNot              → NOT ExprNot
                     | ExprComp

ExprComp             → ExprSuma (EQUALS | NOT_EQUALS | LESS_THAN | GREATER_THAN) ExprSuma
                     | ExprSuma

ExprSuma             → ExprSuma (PLUS | LESS) Termino
                     | Termino

Termino              → Termino (MULTIPLY | DIVIDE) Factor
                     | Factor

Factor               → LPAREN Expresion RPAREN
                     | ID
                     | INT
                     | FLOAT
                     | STRING
         
'''

route = 'test/text.txt'

def file_anayzer(route):
    try:   
        with open(route, 'r') as file:
            data = file.read()
    
        print('-> Analisis Lexico y Sintactico <-')
        result = parser.parse(data, lexer=lexer)
        print('\nAnalisis completed successfully')
    except FileNotFoundError:
        print(f'Error, no found file in route: "{route}"')
    except Exception as e:
        print(f'Error during parsing {e}')

if __name__ == '__main__':
    file_anayzer(route)