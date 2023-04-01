import re
from tokens import Tokens
from Regex_Postfix import convertExpression
from Postfix_AFN import PostifixToAFN

# variable del archivo
archivo = 'YALex.txt'

# a los tokens del archivo los covertimos en arreglo
tokenizer = Tokens()
tokenizer.getTokens(archivo)

for i in range(len(tokenizer.tokens)):
    for j in range(len(tokenizer.tokens)):
        if i != j and tokenizer.tokens[i][0] in tokenizer.tokens[j][1]:
            tokenizer.tokens[i] = (
                tokenizer.tokens[i][0], tokenizer.tokens[i][1], True)
            break
        else:
            tokenizer.tokens[i] = (
                tokenizer.tokens[i][0], tokenizer.tokens[i][1], False)

# por cada token en tokens creamos un afn
for i, token in enumerate(tokenizer.tokens):
    print('\n', i+1, token)
    if token[2] == True:
        try:
            # Creamos el automata a partir de la expresión regular
            conversion = convertExpression(len(token[1]))

            # llamada de funcion para convertir a postfix
            conversion.RegexToPostfix(token[1])
            if conversion.ver == True:
                postfix = conversion.res
                print(token[1])
                print(postfix)

                # instancia de clase para convertir a AFN
                conversionAFN = PostifixToAFN(postfix)

                # llamada a metodo para convertir afn
                conversionAFN.conversion(i+1)
        except:
            print('no podemos generar ese afn aun')
