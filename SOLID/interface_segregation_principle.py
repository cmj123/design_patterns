# Nachine base class
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass 

    def scan(self, document):
        pass 

# What happens when you want to create a class that does not have all the functions of the base class?
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass # noop 

    def scan(self, document):
        raise NotImplementedError('Printer cannot scan!') # problem in a large application. Can break the program
        # use not supported comment 
        '''Not supported'''

######## List SOLIDify the code
# Create a printer interface
class Printer:
    @abstractmethod
    def print(self, document):
        pass 

# Create a scanner interface 
class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

# Create a my printer class 
class MyPrinter(Printer):
    def print(self, document):
        print(document)

# Create my photocopier class 
class Photocopier(Printer, Scanner):
    def print(self, document):
        pass 

    def scan(self, document):
        pass 


### What if I want an abstract class to do it both - print and scan?
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass 

    @abstractmethod
    def scan(self, document):
        pass 


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.printer = printer 
        self.scanner = scanner 

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

myPrinter = MyPrinter()
# myPrinter.print('123')


