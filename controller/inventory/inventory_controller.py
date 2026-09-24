from model.inventory import *
from model.product import Product
from view.inventory.inventory_view import InventoryView
 
class InventoryController:
    def __init__(self, view: InventoryView):
        self._aisles: list[Aisle] = []
        self._view = view
 
    def add_aisle(self, number: int) -> Aisle:
        aisle = Aisle(number)
        self._aisles.append(aisle)
        return aisle
 
    def stock_item(self, shelf: Shelf, product: Product, qty: int, min_stock: int = 3) -> None:
        item = StockItem(product, qty, min_stock)
        shelf.add_item(item)
        self._view.show(item)
 
    def restock(self, sku: str, n: int) -> None:
        item = self._find(sku)
        if item:
            item.add(n)
            self._view.show(item)
 
    def low_stock_report(self) -> None:
        for aisle in self._aisles:
            for shelf in aisle.shelves:
                if shelf.low_stock():
                    self._view.show_alert()
 
    def _find(self, sku: str) -> StockItem | None:
        for aisle in self._aisles:
            item = aisle.find(sku)
            if item:
                return item
        return None
 