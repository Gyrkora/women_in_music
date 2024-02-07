"""
clase Sujeto: es la entidad que mantiene una lista de sus observadores 
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


""" 

Observador: Es una interfaz que define el método update(), 
el cual es llamado por el Sujeto cuando su estado cambia.

"""
class Observador:
    def update(self, ):
        raise NotImplementedError("delegación de actualización")


"""
ConcreteObserverA: 
Implementaciones específicas de la interfaz Observer 
que realizan acciones cuando el Sujeto les notifica un cambio.

"""

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("actualizado el observador =  ConcreteObserverA")
        ((nombre, descripcion),) = args

        with open('log.txt', 'a') as file:  
            file.write(f"nuevo registro con nombre =  {nombre.upper()}  ")

