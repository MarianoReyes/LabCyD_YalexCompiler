from Regex_Postfix import convertExpression
from Postfix_AFN import PostifixToAFN
import re


# Concatenamos los patrones en una única expresión regular
regex = "0|1|2|3|4|5|6|7|8|9"

# Creamos el automata a partir de la expresión regular
conversion = convertExpression(len(regex))

# llamada de funcion para convertir a postfix
conversion.RegexToPostfix(regex)

if conversion.ver == True:
    postfix = conversion.res
    print(regex)
    print(postfix)

    # instancia de clase para convertir a AFN
    conversionAFN = PostifixToAFN(postfix)

    # llamada a metodo para convertir afn
    conversionAFN.conversion()

    # Ejemplo de uso
    cadena = 'if (a > b) { print("a es mayor"); }'
    tokens = re.findall(regex, cadena)
    print(tokens)
