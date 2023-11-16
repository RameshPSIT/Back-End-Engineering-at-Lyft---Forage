from engine.Engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000


if __name__ == "__main__":
    ce = CapuletEngine(0, 30001)
    print(ce.needs_service())
