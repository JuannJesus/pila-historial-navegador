class Nodo:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node


class PilaHistorial:
    def __init__(self):
        self.arriba = None

    def push(self, url):
        print("\n")
        print("Navegando en:", url)
        nuevo_nodo = Nodo(url)
        nuevo_nodo.setNext(self.arriba)
        self.arriba = nuevo_nodo
        self.mostrar_historial()

    def pop(self):
        if self.arriba is None:
            print("\n No hay paginas en el historial")
            return None

        print("\n")
        print("\nSI SE PRESIONA EL BOTON ATRAS O RETROCEDER")
        url_actual = self.arriba.getData()
        self.arriba = self.arriba.getNext()
        self.mostrar_historial()
        return url_actual

    def mostrar_historial(self):
        if self.arriba is None:
            print("Historial vacio")
            return

        print("Como se ve el historial:")

        print("Arriba:", self.arriba.getData())
        actual = self.arriba.getNext()

        # esto muesta la palabra de abajo y la url que tiene guardada en la pagina actual,
        # y se hace llamando a la funcion getData y lo imprime en la consola
        while actual is not None:
            print("Abajo:", actual.getData())
            actual = actual.getNext()


mi_navegador = PilaHistorial()
mi_navegador.push("google.com")
mi_navegador.push("youtube.com")
mi_navegador.push("facebook.com")
mi_navegador.pop()
mi_navegador.pop()
