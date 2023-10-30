################################################################
#                         FACTORY A                            #
################################################################

### FactoryA Sample Code
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self

class FactoryA:
    "The FactoryA Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception('Class Not Found')
        except Exception as _e:
            print(_e)
        return None

################################################################
#                         FACTORY B                            #
################################################################
    
### FactoryB Sample Code
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self

class FactoryB:
    "The FactoryB Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception('Class Not Found')
        except Exception as _e:
            print(_e)
        return None

################################################################
#                    ABSTRACT FACTORY                          #
################################################################

### Abstract Factory Concept Sample Code
from abc import ABCMeta, abstractmethod

class IAbstractFactory(metaclass=ABCMeta):
    "Abstract Factory Interface"

    @staticmethod
    @abstractmethod
    def create_object(factory):
        "The static Abstract factory interface method"

class AbstractFactory(IAbstractFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def create_object(factory):
        "Static get_factory method"
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA.create_object(factory[1])
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB.create_object(factory[1])
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None

# The Client
PRODUCT = AbstractFactory.create_object('ab')
print(f"{PRODUCT.__class__}")

PRODUCT = AbstractFactory.create_object('bc')
print(f"{PRODUCT.__class__}")
