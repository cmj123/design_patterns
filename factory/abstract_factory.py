from abc import ABC 

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass 

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount} ml, enjoy!')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount} ml, enjoy!')
        return Coffee()

def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None

if __name__ == '__main__':
    entry =  input(f'What kind of drink would you like?')
    drink = make_drink(entry)
    drink.consume