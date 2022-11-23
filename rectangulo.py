class Punto:
    def __init__(self, _param_abscisa, _param_ordenada):
        self.abscisa = _param_abscisa
        self.ordenada = _param_ordenada

    def son_puntos_diferentes(self, _param_punto):
        if ((self.abscisa != _param_punto.abscisa) or (self.ordenada != _param_punto.ordenada)):
            return True
        else:
            return False

    def distancia_otro_punto(self, _param_punto):
        _distancia = (((_param_punto.ordenada - self.ordenada)**2) +
                      ((_param_punto.abscisa - self.abscisa)**2))**(1/2)
        return _distancia

    def mostrar_punto(self):
        _cadena_punto = "("+str(self.abscisa)+" "+str(self.ordenada)+")" + " "
        return _cadena_punto


class Linea:
    def __init__(self, _primer_punto, _segundo_punto):
        self.primer_punto = _primer_punto
        self.segundo_punto = _segundo_punto

    def vector_principal(self):
        _abscisa = self.segundo_punto.abscisa - self.primer_punto.abscisa
        _ordenada = self.segundo_punto.ordenada - self.primer_punto.ordenada
        return Punto(_abscisa, _ordenada)

    def segundo_vector(self, _param_punto):
        _abscisa = _param_punto.abscisa - self.primer_punto.abscisa
        _ordenada = _param_punto.ordenada - self.primer_punto.ordenada
        return Punto(_abscisa, _ordenada)

    def tercer_vector(self, _param_punto):
        _abscisa = _param_punto.abscisa - self.segundo_punto.abscisa
        _ordenada = _param_punto.ordenada - self.segundo_punto.ordenada
        return Punto(_abscisa, _ordenada)

    def invertir_vector_principal(self):
        _abscisa = self.primer_punto.abscisa - self.segundo_punto.abscisa
        _ordenada = self.primer_punto.ordenada - self.segundo_punto.ordenada
        return Punto(_abscisa, _ordenada)

    def punto_fuera_de_linea():

        print()

    def es_perpendicular(self, _param_punto):
        _vector_principal = self.vector_principal()
        _segundo_vector = self.segundo_vector(_param_punto)
        _tercer_vector = self.tercer_vector(_param_punto)
        if ((_vector_principal.abscisa * _segundo_vector.abscisa) + (_vector_principal.ordenada * _segundo_vector.ordenada) == 0):
            return True
        elif ((_vector_principal.abscisa * _tercer_vector.abscisa) + (_vector_principal.ordenada * _tercer_vector.ordenada) == 0):
            return True
        else:
            return False

    def linea_incluye_punto(self, _param_punto):

        if (((_param_punto.ordenada - self.primer_punto.ordenada) * (self.segundo_punto.abscisa - self.primer_punto.abscisa)) - ((self.segundo_punto.ordenada - self.primer_punto.ordenada) * (_param_punto.abscisa - self.primer_punto.abscisa)) == 0):
            return True
        else:
            return False

    def calcular_ultimo_punto(self, _param_punto):
        _vector_principal = self.vector_principal()
        _segundo_vector = self.segundo_vector(_param_punto)
        _tercer_vector = self.tercer_vector(_param_punto)
        if ((_vector_principal.abscisa * _segundo_vector.abscisa) + (_vector_principal.ordenada * _segundo_vector.ordenada) == 0):
            return Punto(_vector_principal.abscisa + _param_punto.abscisa, _vector_principal.ordenada + _param_punto.ordenada)
        elif ((_vector_principal.abscisa * _tercer_vector.abscisa) + (_vector_principal.ordenada * _tercer_vector.ordenada) == 0):
            _vector_principal = self.invertir_vector_principal()
            return Punto(_vector_principal.abscisa + _param_punto.abscisa, _vector_principal.ordenada + _param_punto.ordenada)


class Rectangulo:
    def __init__(self, _param_linea, _param_punto_explicito, _param_punto_implicito):
        self.linea = _param_linea
        self.punto_explicito = _param_punto_explicito
        self.punto_implicito = _param_punto_implicito
    def vertices_en_lista(self):
        lista_vertices = []
        _punto1 = self.linea.primer_punto
        lista_vertices.append(_punto1)
        _punto2 = self.linea.primer_punto
        lista_vertices.append(_punto2)
        _punto3 = self.punto_explicito
        lista_vertices.append(_punto3)
        _punto4 = self.linea.primer_punto
        lista_vertices.append(_punto4)
        return lista_vertices

    def mostrar_rectangulo(self):
        _cadena_rectangulo = self.linea.primer_punto.mostrar_punto() + self.linea.segundo_punto.mostrar_punto() + \
            self.punto_explicito.mostrar_punto() + self.punto_implicito.mostrar_punto()
        print(_cadena_rectangulo)


def registrar_punto(contador, mensaje):
    print("")
    print("Registro del punto "+str(contador)+" "+mensaje)
    _abscisa = int(input("Ingrese abscisa del punto: "))
    _ordenada = int(input("Ingrese abscisa del punto: "))
    return Punto(_abscisa, _ordenada)


def menu():
    print("===============REGISTRO DEL PRIMER RECTANGULO================")
    _var_punto1 = registrar_punto(1, "")
    _var_punto2 = registrar_punto(2, "")
    while (_var_punto1.son_puntos_diferentes(_var_punto2) == False):
        _var_punto2 = registrar_punto(
            2, "; NO ES VALIDO REGISTRAR EL MISMO PUNTO!")
    _var_linea1 = Linea(_var_punto1, _var_punto2)
    _var_punto_explicito = registrar_punto(3, "")
    while (_var_linea1.es_perpendicular(_var_punto_explicito) == False or _var_linea1.linea_incluye_punto(_var_punto_explicito) == True):
        _var_punto_explicito = registrar_punto(
            3, "; NO ES VALIDO REGISTRAR UN PUNTO QUE PERTENECE A LA LINEA o no ayuda a formar un rectangulo (no es perpendicular a ninguno de los puntos anteriores)!")
    _var_punto_implicito = _var_linea1.calcular_ultimo_punto(
        _var_punto_explicito)
    _var_rectangulo1 = Rectangulo(
        _var_linea1, _var_punto_explicito, _var_punto_implicito)
    _var_rectangulo1.mostrar_rectangulo()

    print("===============REGISTRO DEL SEGUNDO RECTANGULO================")
    _var_punto1 = registrar_punto(1, "")
    _var_punto2 = registrar_punto(2, "")
    while (_var_punto1.son_puntos_diferentes(_var_punto2) == False):
        _var_punto2 = registrar_punto(
            2, "; NO ES VALIDO REGISTRAR EL MISMO PUNTO!")
    _var_linea1 = Linea(_var_punto1, _var_punto2)
    _var_punto_explicito = registrar_punto(3, "")
    while (_var_linea1.es_perpendicular(_var_punto_explicito) == False or _var_linea1.linea_incluye_punto(_var_punto_explicito) == True):
        _var_punto_explicito = registrar_punto(
            3, "; NO ES VALIDO REGISTRAR UN PUNTO QUE PERTENECE A LA LINEA o no ayuda a formar un rectangulo (no es perpendicular a ninguno de los puntos anteriores)!")
    _var_punto_implicito = _var_linea1.calcular_ultimo_punto(
        _var_punto_explicito)
    _var_rectangulo2 = Rectangulo(
        _var_linea1, _var_punto_explicito, _var_punto_implicito)
    _var_rectangulo2.mostrar_rectangulo()

    #Calculo del entrechoque de rectangulos
    _lista_vertices_rectangulo1 = _var_rectangulo1.vertices_en_lista()
    _lista_vertices_rectangulo2 = _var_rectangulo2.vertices_en_lista()
    print(_lista_vertices_rectangulo1[0].abscisa)
    print(_lista_vertices_rectangulo2[1].ordenada)

    _bandera_entrechoque = False
    for i in range(len(_lista_vertices_rectangulo1)-1):
        _linea = Linea(_lista_vertices_rectangulo1[i],_lista_vertices_rectangulo1[i+1])
        for j in range(len(_lista_vertices_rectangulo2)):
            _bandera_entrechoque = _bandera_entrechoque or _linea.linea_incluye_punto(_lista_vertices_rectangulo2[j])
    
    for i in range(len(_lista_vertices_rectangulo2)-1):
        _linea = Linea(_lista_vertices_rectangulo2[i],_lista_vertices_rectangulo2[i+1])
        for j in range(len(_lista_vertices_rectangulo1)):
            _bandera_entrechoque = _bandera_entrechoque or _linea.linea_incluye_punto(_lista_vertices_rectangulo1[j])

    if(_bandera_entrechoque == True):
        print("Los rectangulos se entrechocan por lo menos en un punto!")
    else:
        print("Los rectangulos no se entrechocan.")

menu()
