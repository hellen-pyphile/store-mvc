from model.identity.person import Person, Address, Contact

class Customer(Person):
    def __init__(self, customer_id: str, name: str, address: Address, contact: Contact):
        if not costumer_id.strip():
            raise ValueError("O ID nao pode estar vazio")
        #https://www.w3schools.com/python/ref_func_super.asp
        super().__init__(name, address, contact) # Usa a inicializacao do pai (Person)
        self._customer_id = customer_id
        self._loyalty_points = 0

    @property
    def customer_id(self):
        return self._customer_id

    # Vou apresentar essa ideia pro Rodrigo amanhã
    def add_points(self, n: int) -> None:
        if n > 0:
            self._loyalty_points += n
        else:
            raise ValueError("Nao pode ser negativo")
    
    def __repr__(self):
        # o que será que esse !r faz aqui?
        # !r retorna uma string raw/crua - le e imprime exatamente o que e lido, incluindo comandos de texto
        return (f"Customer(id={self._customer_id!r}, "
                f"name={self._name!r}, "
                f"address={self._address!r}, "
                f"contact={self._contact!r})")

    def __str__(self):
        return (f"[{self._customer_id}] {self._name}\n"
                f"  {self._address}\n"
                f"  {self._contact}")