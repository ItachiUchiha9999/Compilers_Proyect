from lexer import lexer
from parser import parser


'''
1. Estructura General 

Programa -> Instruccion Programa | Instruccion

Instruccion -> Asignacion | Condicional | Funcion
'''


'''
2. Asignaciones 

Asignacion -> ID ASSIGMENT (EXPRESION)
'''

'''
3. Sentencia de Control

Condicional -> IF (EXPRESION): Bloque ELIF_PART ELSE_PART
ELIF_PART -> ELIF (EXPRESION): Bloque | 
ELSE_PART -> ELSE: Bloque |
Bloque -> Intruccion | Intruccion Bloque
'''

'''
4. Funciones 

Funcion -> PRINT (EXPRESION)
           | LEN (ID)
           | MAX (ID,ID)
'''

'''
5. Expresiones o Tipos de Datos

Expresion -> Expresion Operador Expresion
            | (EXPRESION)
            | ID
            | INT
            | FLOAT
            | STRING
'''

'''
6. Operadores

Operador -> ASSIGMENT | PLUS | MINUS
            | MULTIPLY | DIVIDE | AND
            | OR | NOT | EQUALS | NOT EQUALS
            | LESS THAN | GREATHER THAN
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