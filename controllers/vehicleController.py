import random
from views.display import ViewVehicle
from models.vehicles import Vehicle

class VehicleController:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, brand, model, color, rates, glass, price):    
        vehicle = Vehicle(brand, model, color, rates, glass, price)
        self.vehicles.append(vehicle)

    def get_vehicles(self):
        return self.vehicles

    def execute(self):
        while True:
            ViewVehicle.show_menu()
            option = input("Ingrese una opción: ")
            if option == '1':
                brand = input("Ingrese la marca: ")
                model = input("Ingrese el modelo: ")
                color = input("Ingrese el color: ")
                rates = input("Ingrese el tipo: ")
                glass = input("Ingrese el vidrio: ")
                price = input("Ingrese el precio: ")
                self.add_vehicle(brand, model, color, rates, glass, price)
            elif option == '2':
                vehicles = self.get_vehicles()
                ViewVehicle.show_vehicles(vehicles)
            elif option == '3':
                break
            else:
                ViewVehicle.show_error("Opción inválida")
