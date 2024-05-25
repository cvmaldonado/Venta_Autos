class ViewVehicle:
    @staticmethod
    def show_vehicle(vehicle):
        print(vehicle)

    @staticmethod
    def show_vehicles(vehicles):
        for vehicle in vehicles:
            print(vehicle)

    @staticmethod
    def show_error(error):
        print(error)

    @staticmethod
    def show_menu():
        print("1. Agregar vehículo")
        print("2. Mostrar vehículos")
        print("3. Salir")
