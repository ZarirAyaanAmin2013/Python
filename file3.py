class Engine:
    def start(self):
        return "Engine started"


class NoEngine:
    def start(self):
        return "No engine available"  # safe fallback


class Vehicle:
    def __init__(self, engine):
        self.engine = engine  # inject behavior

    def start(self):
        return self.engine.start()  # delegation


# Different vehicle configurations
car = Vehicle(Engine())
scooter = Vehicle(NoEngine())
bicycle = Vehicle(NoEngine())

print(car.start())       # Engine started
print(scooter.start())  # No engine available
print(bicycle.start())  # No engine available 