"""
clase Sujeto - Sujeto (Tema) - es la entidad que mantiene una lista de sus observadores 
y los notifica sobre los cambios de estado. 
Cualquier número de objetos observadores puede observar 
un sujeto para mantenerse actualizado sobre su estado.

"""

class Sujeto:
    
    observadores=[]

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)
            # Se actualiza el observador cada vez que se llame "notificar()"


""" 

Observer (Observador): Es una interfaz que define el método update(), 
el cual es llamado por el Sujeto cuando su estado cambia.

"""
class Observador:
    def update(self, ):
        raise NotImplementedError("delegación de actualización")


"""
ConcreteObserver (ObservadorConcreto): 
Implementaciones específicas de la interfaz Observer 
que realizan acciones cuando el Sujeto les notifica un cambio.

"""

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        # aquí se agrega el tema al observador que está vinculado a Sujeto y a sus actualizaciones 
        self.observado_a.agregar(self)
        # acá se llama al métodp "agregar()" de la clase Sujeto para agregar al observador

    def update(self, *args):
        # acá se llama y sobreescribe directamente al método de la clase madre "Observador.update()"
        # en donde se informará sobre el estado y su actualización
        print("actualizado dentro de Observador ConcreteObserverA")
        print("Estado = ", args)

