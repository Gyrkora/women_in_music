"""

Módulo que se encarga de hacer funcionar la aplicación directamente con el uso del módulo Vista como argumento.

"""

from tkinter import Tk 

from vista import Vista
import observador


class Controlador:
    def __init__(self, root):
        self.root = root
        self.view = Vista(self.root)
        self.el_observador = observador.ConcreteObserverA(self.view.model_class)


if __name__ == "__main__":
    try:
        root = Tk()
        app = Controlador(root)
        root.mainloop()

    except TypeError as e:
        print(f"el typerror es: {e}")
    except Exception as e:
        print(f"otro tipo de error:", e)

