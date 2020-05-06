from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("baking pizza for 12min in 400 degrees..")

    def cut(self):
        print("cutting pizza in pieces")

    def box(self):
        print("putting pizza in box")


class USStyleCheesePizza(Pizza):
    def prepare(self):
        print("preparing a New York style cheese pizza..")


class ItaliaStyleCheesePizza(Pizza):
    def prepare(self):
        print("preparing a Chicago style cheese pizza..")


class USStyleGreekPizza(Pizza):
    def prepare(self):
        print("preparing a New York style greek pizza..")


class ItaliaStyleGreekPizza(Pizza):
    def prepare(self):
        print("preparing a Chicago style greek pizza..")


# This time, PizzaStore is abstract
class PizzaStore(ABC):

    # We brought createPizza back into the PizzaStore (instead of the SimpleFactory)
    # However, it is declared as abstract. This time, instead of having
    # a factory class, we have a factory method:
    @abstractmethod
    def _createPizza(self, pizzaType: str) -> Pizza:
        pass

    def orderPizza(self, pizzaType):
        pizza: Pizza

        pizza = self._createPizza(pizzaType)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


class USPizzaStore(PizzaStore):

    def _createPizza(self, pizzaType: str) -> Pizza:
        pizza: Pizza = None

        if pizzaType == 'Greek':
            pizza = USStyleGreekPizza()
        elif pizzaType == 'Cheese':
            pizza = USStyleCheesePizza()
        else:
            print("No matching pizza found in the NY pizza store...")

        return pizza


class ItaliaPizzaStore(PizzaStore):

    def _createPizza(self, pizzaType: str) -> Pizza:
        pizza: Pizza = None

        if pizzaType == 'Greek':
            pizza = ItaliaStyleGreekPizza()
        elif pizzaType == 'Cheese':
            pizza = ItaliaStyleCheesePizza()
        else:
            print("No matching pizza found in the Chicago pizza store...")

        return pizza


usPizzaStore = USPizzaStore()
itPizzaStore = ItaliaPizzaStore()

usPizzaStore.orderPizza('Greek')
print("\n")
itPizzaStore.orderPizza('Cheese')
