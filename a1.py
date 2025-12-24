class vehicle:
    def __init__(self, name, speed, mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

class bus(vehicle):
    pass

bus1=bus("SCHOOL VOLVO", 180, 12)
print("VEHICLE NAME:", bus1.name, "SPEED:", bus1.speed, "MILEAGE:", bus1.mileage)

bus2=bus("BENZ BUS", 150, 15)
print("VEHICLE NAME:", bus2.name, "SPEED:", bus2.speed, "MILEAGE:", bus2.mileage)