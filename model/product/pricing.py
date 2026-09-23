#abc - abstract base class 
#https://docs.python.org/3/library/abc.htmlfrom abc import ABC, abstractmethod
 
class PricingPolicy(ABC):
    @abstractmethod
    def factor(self) -> float:
        pass
    
class Normal(PricingPolicy):
    def factor(self):
        return 1.0

class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        percentage = percentage / 100
        self._factor = 1.0 - percentage
    
    def factor(self):
        return self._factor