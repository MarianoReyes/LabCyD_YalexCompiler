class AFN:
    def __init__(self, simbolo):
        self.transiciones = {}
        self.estado_inicial = 0
        self.estados_finales = [1]
        self.num_estados = 2
        self.agregar_transicion(self.estado_inicial,
                                simbolo, self.estados_finales[0])

    def agregar_estado(self):
        nuevo_estado = self.num_estados
        self.num_estados += 1
        self.transiciones[nuevo_estado] = {}
        return nuevo_estado

    def agregar_transicion(self, estado_origen, simbolo, estado_destino):
        if (estado_origen, simbolo) not in self.transiciones:
            self.transiciones[(estado_origen, simbolo)] = [estado_destino]
        else:
            self.transiciones[(estado_origen, simbolo)].append(estado_destino)

    def cerradura_epsilon(self, estados):
        visitados = set()
        pila = list(estados)
        while pila:
            estado = pila.pop()
            if estado not in visitados:
                visitados.add(estado)
                if (estado, '') in self.transiciones:
                    for estado_destino in self.transiciones[(estado, '')]:
                        pila.append(estado_destino)
        return visitados

    def cerradura_kleene(self):
        nuevo_estado_inicial = self.num_estados
        nuevo_estado_final = nuevo_estado_inicial + 1
        self.estados_finales = [nuevo_estado_final]
        self.num_estados += 2
        self.agregar_transicion(nuevo_estado_inicial, '', self.estado_inicial)
        self.agregar_transicion(nuevo_estado_inicial, '', nuevo_estado_final)
        self.agregar_transicion(
            self.estados_finales[0], '', self.estado_inicial)
        self.agregar_transicion(
            self.estados_finales[0], '', nuevo_estado_final)
        self.estado_inicial = nuevo_estado_inicial

    def cerradura_positiva(self):
        nuevo_estado_inicial = self.num_estados
        nuevo_estado_final = nuevo_estado_inicial + 1
        self.estados_finales = [nuevo_estado_final]
        self.num_estados += 2
        self.agregar_transicion(nuevo_estado_inicial, '', self.estado_inicial)
        self.agregar_transicion(
            self.estados_finales[0], '', nuevo_estado_final)
        self.agregar_transicion(
            self.estados_finales[0], '', self.estado_inicial)
        self.estado_inicial = nuevo_estado_inicial

    def cerradura_opcional(self):
        nuevo_estado_inicial = self.num_estados
        nuevo_estado_final = nuevo_estado_inicial + 1
        self.estados_finales = [nuevo_estado_final]
        self.num_estados += 2
        self.agregar_transicion(nuevo_estado_inicial, '', self.estado_inicial)
        self.agregar_transicion(nuevo_estado_inicial, '', nuevo_estado_final)
        self.estado_inicial = nuevo_estado_inicial

    def concatenacion(self, afn2):
        for estado in self.estados_finales:
            self.agregar_transicion(estado, '', afn2.estado_inicial)
        self.estados_finales = afn2.estados_finales
        self.num_estados += afn2.num_estados - 2
        for transicion, destinos in afn2.transiciones.items():
            for destino in destinos:
                self.agregar_transicion(transicion[0] + self.num_estados - afn2.num_estados + 2,
                                        transicion[1], destino + self.num_estados - afn2.num_estados + 2)

    def union(self, afn2):
        self.agregar_estado('')
        self.agregar_transicion('', '', self.estado_inicial)
        self.agregar_transicion('', '', afn2.estado_inicial)
        self.num_estados += afn2.num_estados + 1
        self.estados_finales.extend(afn2.estados_finales)
        for transicion, destinos in afn2.transiciones.items():
            for destino in destinos:
                self.agregar_transicion(
                    transicion[0] + 1, transicion[1], destino + 1)

    def cerradura_positiva(self):
        self.agregar_estado('')
        self.agregar_transicion('', '', self.estado_inicial)
        self.agregar_transicion('', '', '')
        self.agregar_transicion(
            self.estados_finales[0], '', self.estado_inicial)
        self.agregar_transicion(self.estados_finales[0], '', '')
        self.estados_finales = [self.num_estados]
        self.num_estados += 1

    def cerradura_estrella(self):
        self.agregar_estado('')
        self.agregar_transicion('', '', self.estado_inicial)
        self.agregar_transicion('', '', '')
        self.agregar_transicion(
            self.estados_finales[0], '', self.estado_inicial)
        self.agregar_transicion(self.estados_finales[0], '', '')
        self.estados_finales = [self.num_estados]
        self.num_estados += 1
