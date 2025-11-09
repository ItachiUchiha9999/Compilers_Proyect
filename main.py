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

route = 'test/error-lexico.txt'
#route = 'test/error-sintactico.txt'
#route = 'test/sin-errores.txt'

def file_analyzer(route):
    try:
        with open(route) as file:
            data = file.read().strip()
            if not data:
                print("El archivo está vacío")
                return

            lexer.input(data)

            print("\n Análisis Léxico:")
            for tok in iter(lexer.token, None):
                print(f"-> {tok.type}: '{tok.value}' (Línea {tok.lineno})")

            print("\n Análisis Sintáctico:")
            result = parser.parse(data, lexer=lexer)
            print("\n Análisis completado sin errores")
            print(" Resultado del parser:", result)

    except SystemExit:
        pass
    except (FileNotFoundError, SyntaxError) as e:
        print(f"\n {e}")
    except Exception as e:
        print(f"\n Error inesperado: {e}")

if __name__ == "__main__":
    file_analyzer(route)

#Aclaracion 

#Solamente trabajar con los tokens dados en el pdf tema no agregar mas tokens porque me invalidan en tp