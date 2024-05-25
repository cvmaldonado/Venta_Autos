class Vehicle:
    def __init__(self, brand, model, color, rates, glass, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.rates = rates
        self.glass = glass
        self.price = price

    def __str__(self):
        return f"Marca: {self.brand}, Modelo: {self.model}, Color: {self.color}, Tipo: {self.rates}, Vidrios: {self.glass}, Precio: {self.price}"
