from model.product import *
from view.product.product_view import ProductView
 
class ProductController:
    def __init__(self, view: ProductView):
        self._products: list[Product] = []
        self._view = view
 
    def add(self) -> Product:
        data = self._view.prompt_data()
        product = Product(
            sku = SKU(data["sku"]),
            name = data["name"],
            price = Price(data["price"]),
            category = ProductType[data["category"].upper()],
        )
        self._products.append(product)
        self._view.show(product)
        return product
 
    def find(self, sku: str) -> Product | None:
        for p in self._products:
            if str(p.sku) == sku:
                self._view.show(p)
                return p
        return None
 
    def apply_policy(self, sku: str, policy: PricingPolicy) -> None:
        product = self.find(sku)
        if product:
            product.policy = policy
 
    def prompt_choice(self) -> Product | None:
        pass
 