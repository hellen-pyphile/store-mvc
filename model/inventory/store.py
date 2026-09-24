from model.inventory.stock import StockItem

class Shelf:
    def __init__(self, code: str):
        if not code.strip():
            raise ValueError("Preencha um valor valido")
        self._code = code
        self._items: list[StockItem] = []

    @property
    def code(self):
        return self._code
    
    @property
    def items(self):
        return list(self._items)

    def add_item(self, item: StockItem) -> None:
        self._items.append(item)

    def find(self, sku: str) -> StockItem | None:
        for item in self._items:
            if str(item.product.sku) == sku:
                return item
        return None

    def __str__(self):
        return f"Shelf({self._code})"
    
    def __repr__(self):
        return f"Shelf(code={self._code!r}, items={len(self._items)})"


class Aisle:
    def __init__(self, number: int):
        if number <= 0:
            raise ValueError("Preencha com um numero maior que 0")
        self._number  = number
        self._shelves: list[Shelf] = []

    @property
    def number(self):
        return self._number
    
    @property
    def shelves(self):
        return list(self._shelves)

    def add_shelf(self, shelf: Shelf) -> None:
        self._shelves.append(shelf)

    def find(self, sku: str) -> StockItem | None:
        for shelf in self._shelves:
            item = shelf.find(sku)
            if item:
                return item
        return None

    def __str__(self):
        return f"Aisle {self._number}"
    
    def __repr__(self):
        return f"Aisle(number={self._number}, shelves={len(self._shelves)})"