from dataclasses import dataclass

@dataclass
class Dish:
    name: str
    price: float
    available: bool

    def describe(self) -> str:
        return f"{self.name} ({round(self.price, 1)} €) - {"disponible" if self.available else "Indisponible" }"
