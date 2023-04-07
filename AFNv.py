from AFN import *


class PostifixToAFN:

    @staticmethod
    def infix_to_postfix(infix_regex):
        """
        Convierte una expresión regular en notación infija a notación posfija.
        """
        prec = {'*': 100, '+': 100, '?': 100,
                '.': 90, '|': 80, '(': 70, ')': 60}
        stack = []
        postfix_list = []
        for char in infix_regex:
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    postfix_list.append(stack.pop())
                stack.pop()
            elif char in prec:
                while stack and prec[char] <= prec.get(stack[-1], 0):
                    postfix_list.append(stack.pop())
                stack.append(char)
            else:
                postfix_list.append(char)
        while stack:
            postfix_list.append(stack.pop())
        return ''.join(postfix_list)

    @staticmethod
    def postfix_to_afn(postfix_regex):
        """
        Convierte una expresión regular en notación posfija a un Autómata Finito No Determinista (AFN).
        """
        stack = []
        for char in postfix_regex:
            if char == '*':
                afn = stack.pop()
                afn.cerradura_kleene()
                stack.append(afn)
            elif char == '+':
                afn = stack.pop()
                afn.cerradura_positiva()
                stack.append(afn)
            elif char == '?':
                afn = stack.pop()
                afn.cerradura_opcional()
                stack.append(afn)
            elif char == '.':
                afn2 = stack.pop()
                afn1 = stack.pop()
                afn1.concatenacion(afn2)
                stack.append(afn1)
            elif char == '|':
                afn2 = stack.pop()
                afn1 = stack.pop()
                afn1.union(afn2)
                stack.append(afn1)
            else:
                afn = AFN(char)
                stack.append(afn)
        return stack.pop()
