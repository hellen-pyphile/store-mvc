from enum import Enum, auto
from uuid import uuid4
from model.checkout.cart import Cart

class OrderStatus(Enum):
    PENDING = 1
    PAID = 2
    FULFILLED = 3
    
class Order:
    _TRANSITIONS = {
        OrderStatus.PENDING:   OrderStatus.PAID,
        OrderStatus.PAID:      OrderStatus.FULFILLED,
    }

    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("O carrinho nao pode estar vazio")
        self._order_id = str(uuid4())[:8]
        self._customer = cart.customer
        self._items = list(cart.items)
        self._status = OrderStatus.PENDING

    @property
    def order_id(self):
        return self._order_id
    
    @property
    def status(self):
        return self._status
    
    @property
    def items(self):
        return list(self._items)

    def total(self) -> float:
        return sum(i.subtotal() for i in self._items)

    def advance_status(self) -> None:
        if self._status == OrderStatus.FULFILLED:
            raise ValueError("Pedido ja finalizado")
        next_status = self._TRANSITIONS[self._status]
        self._status = next_status

    def __str__(self):
        lines = "\n".join(f"  {i}" for i in self._items)
        return (f"Order #{self._order_id} [{self._status.name}]\n"
                f"  Customer: {self._customer.name}\n"
                f"{lines}\n"
                f"  Total: R$ {self.total():.2f}")

    def __repr__(self):
        return f"Order(id={self._order_id!r}, status={self._status.name})"
