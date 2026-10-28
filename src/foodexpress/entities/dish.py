from dataclasses import dataclass

@dataclass
class Dish:
    name: str
    price: float
    available: bool

    def describe(self) -> str:
        if self.available:
            statut = "disponible"
        else:
            statut = "indisponible"
        return f"{self.name} ({self.price} €) - {statut}"
