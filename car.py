class Car:
    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine_on = False
        self.current_speed = 0
        self.parts_needing_maintenance = []

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            return f"Motorn på {self.brand} {self.model} har startat."
        return "Motorn är redan igång."

    def accelerate(self, amount):
        if not self.engine_on:
            return "Motorn är inte igång."
        self.current_speed += amount
        return f"Hastighet: {self.current_speed} km/h"

    def brake(self, amount):
        self.current_speed = max(0, self.current_speed - amount)
        return f"Ny hastighet: {self.current_speed} km/h"

    def get_status(self):
        engine = "På" if self.engine_on else "Av"
        return (f"{self.brand} {self.model} ({self.year}) | "
                f"Motor: {engine} | Hastighet: {self.current_speed} km/h | "
                f"Miltal: {self.mileage} km")

    def add_part_for_maintenance(self, part_name):
        self.parts_needing_maintenance.append(part_name)
        return f"Del '{part_name}' har lagts till i underhållslistan."

    def perform_maintenance_on_part_by_index(self, index):
        if not isinstance(index, int):
            return "Index måste vara ett heltal."
        if 1 <= index <= len(self.parts_needing_maintenance):
            part = self.parts_needing_maintenance.pop(index - 1)
            return f"Underhåll utfört på '{part}'."
        return f"Ogiltigt index. Välj 1–{len(self.parts_needing_maintenance)}."
