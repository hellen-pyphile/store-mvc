from model.checkout import Order, Cart
from model.identity import Customer
from model.product import Product
from view.checkout.checkout_view import CheckoutView

class CheckoutController:
    def __init__(self, view: CheckoutView):
        self._cart: Cart | None = None
        self._orders: list[Order] = []
        self._view = view

    def open_cart(self, customer: Customer) -> None:
        self._cart = Cart(customer)

    def add_item(self, product: Product, qty: int) -> None:
        if not self._cart:
            raise ValueError("No open cart")
        self._cart.add(product, qty)
        self._view.show_cart(self._cart)

    def confirm(self) -> Order | None:
        self._view.show_cart(self._cart)
        if self._view.confirm_prompt():
            print("Obrigado por comprar conosco!") # Deixando minha marca no projeto!
            order = Order(self._cart)
            self._orders.append(order)
            self._view.show_order(order)
            return order
        return None

    def advance(self) -> None:
        # TODO: Vou pra casa agora
        pass