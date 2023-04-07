import re
from tokens import Tokens
from Regex_Postfix import convertExpression
from Postfix_AFN import PostifixToAFN

# variable del archivo
archivo = 'ya.lex'

# creacion de la variable que almacena afns con su nombre
afns = []

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

                # instancia de clase para convertir a AFN
                afn = PostifixToAFN(postfix)

                # llamada a metodo para convertir afn
                afn.conversion(token[0])

                afns.append((token, afn))

        except:
            print('\nNo podemos generar ese afn aun')

new_tokens = []

for i, token in enumerate(tokenizer.tokens):
    if token[2]:
        new_tokens.append((token[0], token[1], token[2]))
    if not token[2]:
        operands_operators = []
        regex_splitted = re.findall('\w+|[+*?()|.]', token[1])
        operands_operators.extend(regex_splitted)

        for i, element in enumerate(operands_operators):
            for afn in afns:
                if element == afn[0][0]:
                    operands_operators[i] = "("+afn[0][1]+")"
        new_regex = ''.join(operands_operators)

        new_tokens.append((token[0], new_regex, token[2]))

# por cada token compuesto en tokens creamos un afn
for i, token in enumerate(new_tokens):
    print('\n', i+1, token)
    if token[2] == False:
        try:
            # Creamos el automata a partir de la expresión regular
            conversion = convertExpression(len(token[1]))

            # llamada de funcion para convertir a postfix
            conversion.RegexToPostfix(token[1])
            if conversion.ver == True:
                postfix = conversion.res

                # instancia de clase para convertir a AFN
                afn = PostifixToAFN(postfix)

                # llamada a metodo para convertir afn
                afn.conversion(token[0])

                afns.append((token, afn))

        except:
            print('\nNo podemos generar ese afn aun')

print(tokenizer.tokens)
print(new_tokens)
print(afns)
