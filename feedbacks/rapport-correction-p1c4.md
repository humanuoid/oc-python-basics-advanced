# P1C4 — Feedback et Solution Idéale

## 📋 Contexte

**Exercice :** Programmation Orientée Objet — Créer une classe `Dish`

Modéliser un plat de restaurant avec ses caractéristiques (nom, prix, disponibilité) et une méthode pour l'afficher.

**Objectifs pédagogiques :**
- Comprendre le trio fondateur de la POO : attributs + `__init__` + méthode avec `self`
- Créer une classe avec `@dataclass` (raccourci moderne) ou `__init__` manuel
- Instancier des objets et appeler leurs méthodes
- Formater une sortie lisible avec les f-strings

**Corrigé de référence :** [python-p1c4-corrige-clean.pdf](https://course.oc-static.com/courses/9137941/python-p1c4-corrige-clean.pdf)

---

## 📝 Énoncé actuel (avant correction)

```python
# src/foodexpress/Entities/Dish.py (avant)
from dataclasses import dataclass

@dataclass
class Dish:
    name: str
    price: float
    available: bool

    def describe(self) -> str:
        return f"{self.name} ({round(self.price, 2)}€) - {"Disponible" if self.available else "Indisponible" }"

# src/foodexpress/__init__.py (avant — logique dans le mauvais fichier)
from Entities.Dish import Dish

products = [
    Dish("Pizza", 12.0, True),
    Dish("Tiramisu", 6.0, False)
]

for product in products:
    print(product.describe())
```

**Ce qui est demandé :**
1. Créer une classe `Dish` avec 3 attributs : `name`, `price`, `available`
2. Ajouter une méthode `describe()` qui retourne une chaîne descriptive
3. Instancier 2 plats et afficher leur description

**Sortie attendue (corrigé) :**
```
Pizza (12.0 €) - disponible
Tiramisu (6.0 €) - indisponible
```

---

## ✅ Analyse de la solution de base

### Points positifs
- ✅ Utilisation correcte de `@dataclass` (Python moderne)
- ✅ Annotations de type présentes (`str`, `float`, `bool`)
- ✅ Méthode `describe()` avec retour de type `-> str`
- ✅ Boucle `for` pour afficher tous les produits (propre)
- ✅ Structure en packages (`entities/`) — bonne organisation

### Points à améliorer

| Aspect | Problème | Solution |
|--------|----------|----------|
| Majuscules fichiers/dossiers | `Entities/Dish.py` (style PHP/PSR-4) | `entities/dish.py` (snake_case PEP 8) |
| Logique dans `__init__.py` | Code exécutable dans `__init__.py` | Déplacer dans `main.py` ou `p1c4.py` |
| Import fragile | `from Entities.Dish import Dish` (dépend du CWD) | `from foodexpress.entities.dish import Dish` |
| Format de sortie | `12.0€` (pas d'espace), `Disponible` (majuscule) | `12.0 €` (espace), `disponible` (minuscule) |
| Ternaire inline | `{"disponible" if ... else "Indisponible"}` | `if/else` explicite (plus lisible pour débutant) |
| `round(self.price, 1)` | Inutile ici (`12.0` n'a pas de décimale) | Supprimer, utiliser `self.price` directement |
| Casse « Indisponible » | Majuscule alors que le corrigé veut minuscule | `indisponible` |

---

## 💎 Solution Idéale avec Bonnes Pratiques

### Version 1 : Avec `@dataclass` (moderne, celle retenue)

```python
# src/foodexpress/entities/dish.py
"""
Module représentant un plat du restaurant FoodExpress.

La classe Dish modélise un plat avec son nom, son prix
et sa disponibilité.
"""

from dataclasses import dataclass


@dataclass
class Dish:
    """
    Représente un plat du menu.

    Attributes:
        name: Nom du plat (ex: "Pizza")
        price: Prix en euros (ex: 12.0)
        available: Disponibilité (True/False)
    """
    name: str
    price: float
    available: bool

    def describe(self) -> str:
        """
        Retourne une description formatée du plat.

        Returns:
            Chaîne formatée : "Nom (prix €) - disponible/indisponible"
        """
        if self.available:
            statut = "disponible"
        else:
            statut = "indisponible"
        return f"{self.name} ({self.price} €) - {statut}"
```

```python
# src/foodexpress/p1c4.py (point d'entrée)
"""
Point d'entrée de l'exercice P1C4.

Instancie des plats et affiche leur description.
"""

from foodexpress.entities.dish import Dish


def main() -> None:
    """Fonction principale : crée les plats et les affiche."""
    products = [
        Dish("Pizza", 12.0, True),
        Dish("Tiramisu", 6.0, False),
    ]

    for product in products:
        print(product.describe())


if __name__ == "__main__":
    main()
```

### Version 2 : Avec `__init__` manuel (celle du corrigé, pédagogique)

```python
# Version du corrigé officiel — pour comprendre la mécanique
class Dish:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

    def describe(self):
        if self.available:
            return f"{self.name} ({self.price} €) - disponible"
        else:
            return f"{self.name} ({self.price} €) - indisponible"


pizza = Dish("Pizza", 12.0, True)
tiramisu = Dish("Tiramisu", 6.0, False)
print(pizza.describe())
print(tiramisu.describe())
```

> **Note pédagogique** : `@dataclass` génère automatiquement `__init__`, `__repr__`, `__eq__`. C'est un raccourci puissant, mais il faut d'abord comprendre ce qu'il génère. Le corrigé part de `__init__` manuel pour que tu voies la mécanique.

---

## 🔍 Explications des améliorations

### 1. Convention de nommage PEP 8

```python
# ❌ Style PHP/PSR-4 (majuscules)
Entities/Dish.py

# ✅ Style Python (snake_case)
entities/dish.py
```

**Pourquoi ?**
- **PEP 8** : les modules (fichiers) et packages (dossiers) en `snake_case`
- Les classes seules en `PascalCase` (`class Dish:`)
- Évite la confusion et respecte l'écosystème Python

### 2. Séparation des responsabilités

```python
# ❌ Logique dans __init__.py
# src/foodexpress/__init__.py
products = [Dish("Pizza", 12.0, True)]
for product in products:
    print(product.describe())

# ✅ Logique dans un fichier dédié
# src/foodexpress/p1c4.py
def main():
    products = [Dish("Pizza", 12.0, True)]
    for product in products:
        print(product.describe())
```

**Pourquoi ?**
- `__init__.py` marque un dossier comme package Python — il ne doit pas contenir de logique exécutable
- Un point d'entrée clair (`main.py` ou `p1c4.py`) facilite les tests et la réutilisation

### 3. Import robuste

```python
# ❌ Import fragile (dépend du répertoire de lancement)
from Entities.Dish import Dish

# ✅ Import absolu avec le package complet
from foodexpress.entities.dish import Dish
```

**Pourquoi ?**
- Fonctionne quel que soit le répertoire courant
- Nécessite `PYTHONPATH=src` ou installation du package (`pip install -e .`)
- Évite les erreurs `ModuleNotFoundError`

### 4. `if/else` explicite vs ternaire

```python
# ❌ Ternaire inline (compact mais moins lisible)
return f"{self.name} ({self.price} €) - {"disponible" if self.available else "indisponible"}"

# ✅ if/else explicite (pédagogique, plus lisible)
if self.available:
    statut = "disponible"
else:
    statut = "indisponible"
return f"{self.name} ({self.price} €) - {statut}"
```

**Pourquoi ?**
- La ternaire est puissante mais masque la logique pour un débutant
- Le `if/else` montre clairement les deux branches
- Plus facile à modifier (ajouter un troisième statut, par exemple)

### 5. Format de sortie exact

```python
# ❌ Avant
f"{self.name} ({round(self.price, 1)}€) - ..."     # pas d'espace, round inutile
f"... - {"Disponible" if ... else "Indisponible"}" # majuscules

# ✅ Après
f"{self.name} ({self.price} €) - disponible"        # espace avant €, minuscule
f"{self.name} ({self.price} €) - indisponible"
```

**Pourquoi ?**
- Le corrigé attend `12.0 €` (avec espace) et `disponible` (minuscule)
- `round(self.price, 1)` ne change rien pour `12.0` ou `6.0` — c'est du bruit
- Un test de sortie exacte échoue au moindre écart

---

## 📊 Tableau récapitulatif POO

| Concept | Syntaxe | Rôle |
|---------|---------|------|
| Classe | `class Dish:` | Modèle/plan de fabrication |
| Attributs | `name: str`, `price: float` | Caractéristiques de l'objet |
| `@dataclass` | `@dataclass` | Génère `__init__`, `__repr__`, `__eq__` automatiquement |
| `__init__` manuel | `def __init__(self, name, price):` | Initialise les attributs (version corrigé) |
| `self` | `self.name` | Référence à l'instance courante |
| Méthode | `def describe(self) -> str:` | Action que l'objet peut faire |
| Instance | `Dish("Pizza", 12.0, True)` | Objet concret créé depuis la classe |
| Appel méthode | `product.describe()` | Exécute la méthode sur l'instance |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Nommage PEP 8 : `entities/dish.py` (snake_case), `class Dish:` (PascalCase)
- [x] `@dataclass` avec annotations de type
- [x] Docstrings module + classe + méthode (PEP 257)
- [x] Séparation logique (`p1c4.py`) / modèle (`entities/dish.py`)
- [x] `__init__.py` vide (marque le package, pas de code)
- [x] Import absolu robuste (`from foodexpress.entities.dish import Dish`)
- [x] Structure `main()` + `if __name__ == "__main__"`
- [x] Format de sortie conforme au corrigé
- [x] `if/else` explicite (pédagogique)
- [x] Pas de `round` inutile

---

## 💬 Pour aller plus loin

1. **Version sans `@dataclass`** : réécrire `Dish` avec `__init__` manuel pour comprendre ce que génère le décorateur
2. **Ajouter `__str__`** : pour que `print(dish)` fonctionne sans appeler `.describe()`
3. **Validation des données** : prix positif, nom non vide (`raise ValueError`)
4. **Héritage** : créer `class Boisson(Dish)` avec un attribut `volume` supplémentaire
5. **Sérialisation** : sauvegarder les plats dans un fichier JSON avec `dataclasses.asdict()`

```python
# Exemple avancé : __str__ + validation
from dataclasses import dataclass

@dataclass
class Dish:
    name: str
    price: float
    available: bool = True

    def __post_init__(self):
        """Validation exécutée automatiquement après __init__."""
        if self.price < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        if not self.name:
            raise ValueError("Le nom ne peut pas être vide")

    def __str__(self) -> str:
        return self.describe()

    def describe(self) -> str:
        statut = "disponible" if self.available else "indisponible"
        return f"{self.name} ({self.price} €) - {statut}"
```

---

*Rapport généré le 28 octobre 2026 — Format aligné sur `oc-python-basics`.*
