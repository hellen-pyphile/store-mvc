from model.product.product import Product
from model.identity.customer import Customer

class LineItem:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("A quantidade nao pode ser menor que 0")
        self._product = product
        self._quantity = quantity

    @property
    def product(self):
        return self._product
    
    @property
    def quantity(self):
        return self._quantity

    def subtotal(self) -> float:
        return self._product.final_price * self._quantity
 
    def add_quantity(self, quantity: int) -> None:
        self._quantity += quantity
        
    def __str__(self):
        return f"{self._product.name} x {self._quantity} = R$ {self._product.final_price():.2f}"
       
    def __repr__(self):
        return f"LineItem(sku={self._product.sku!r}, qty={self._quantity})"

class Cart:
    def __init__(self, customer: Customer):
        self._customer = customer
        self._items: list[LineItem] = []

    @property
    def customer(self):
        return self._customer
    
    @property
    def items(self):
        return list(self._items)

    def add(self, product: Product, qty: int) -> None:
        for item in self._items:
            if item.product.sku == product.sku:
                item.add_quantity(qty)
                return
        self._items.append(LineItem(product, qty))

    def remove(self, sku: str) -> None:
        self._items = [i for i in self._items if str(i.product.sku) != sku]

    def total(self) -> float:
        return sum(i.subtotal() for i in self._items)

    def __str__(self):
        lines = "\n".join(f"  {i}" for i in self._items)
        return f"Cart [{self._customer.name}]\n{lines}\n  Total: R$ {self.total():.2f}"

