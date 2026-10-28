# P1C5 — Feedback et Solution Idéale

## 📋 Contexte

**Exercice :** Lire un fichier CSV, manipuler des données et gérer des erreurs simples

Lire un fichier `menu.csv` contenant des plats, afficher chaque plat avec son prix, et gérer le cas où le fichier est absent.

**Objectifs pédagogiques :**
- Ouvrir et lire un fichier avec `open()` et le context manager `with`
- Utiliser `.strip()` pour nettoyer les lignes (retirer le `\n`)
- Découper une chaîne avec `.split(",")`
- Gérer une erreur avec `try/except FileNotFoundError`
- Utiliser `pathlib.Path` pour construire des chemins robustes

**Corrigé de référence :** [python-p1c5-corrige-clean.pdf](https://course.oc-static.com/courses/9137941/python-p1c5-corrige-clean.pdf)

---

## 📝 Énoncé actuel (avant correction)

```python
from pathlib import Path

RESOURCE_CSV_MENU = Path(__file__).parent / "resources/menu.csv"

def main():
    print(RESOURCE_CSV_MENU)  # ← ligne de debug, pas dans le corrigé

    try:
        with open(RESOURCE_CSV_MENU, encoding="utf-8") as file:
            for line in file:
                line_exploded = line.strip().split(',')  # ← guillemets simples, nom peu explicite
                print(f"{line_exploded[0]} - {line_exploded[1]} €")  # ← tiret simple, pas d'espace avant €
    except FileNotFoundError:
        print("Menu introuvable")

if __name__ == "__main__":
    main()
```

**Fichier `resources/menu.csv` :**
```csv
Pizza,12
Salade,8
Burger,10
Tiramisu,6
```

**Ce qui est demandé :**
1. Lire le fichier `menu.csv` ligne par ligne
2. Pour chaque ligne, extraire le nom et le prix
3. Afficher : `Nom — prix €`
4. Si le fichier n'existe pas, afficher `Menu introuvable`

**Sortie attendue (corrigé) :**
```
Pizza — 12 €
Salade — 8 €
Burger — 10 €
Tiramisu — 6 €
```

**Sortie si fichier absent :** `Menu introuvable`

---

## ✅ Analyse de la solution de base

### Points positifs
- ✅ Utilisation de `pathlib.Path` — robuste, fonctionne depuis n'importe quel répertoire
- ✅ `encoding="utf-8"` explicite — évite les problèmes d'encodage
- ✅ `with open(...) as file:` — le fichier se ferme automatiquement
- ✅ `.strip()` présent — nettoie les sauts de ligne
- ✅ `try/except FileNotFoundError` — gestion d'erreur propre
- ✅ Structure `main()` + `if __name__ == "__main__"` — bonne pratique
- ✅ Message d'erreur en français — cohérent avec l'UI

### Points à améliorer

| Aspect | Problème | Solution |
|--------|----------|----------|
| Ligne de debug | `print(RESOURCE_CSV_MENU)` affiche le chemin absolu | Supprimer — pas dans le corrigé |
| Séparateur | `-` (tiret simple) au lieu de `—` (em dash) | Utiliser `—` (U+2014) comme le corrigé |
| Nommage | `line_exploded[0]`, `line_exploded[1]` — peu explicite | `parts`, `name`, `price` — auto-documenté |
| Guillemets | `split(',')` — guillemets simples | `split(",")` — guillemets doubles (PEP 8) |
| Robustesse | Pas de vérification si une ligne est vide | Ajouter `if not line.strip(): continue` |
| Flexibilité | Chemin en dur dans le code | ✅ Déjà bien avec `pathlib` — garder |

---

## 💎 Solution Idéale avec Bonnes Pratiques

### Version 1 : Corrigée (celle retenue)

```python
# src/foodexpress/p1c5.py
"""
Exercice P1C5 — Lecture d'un fichier CSV et gestion d'erreurs.

Lit le fichier resources/menu.csv, affiche chaque plat
avec son prix, et gère le cas où le fichier est absent.
"""

from pathlib import Path

# Chemin robuste : fonctionne quel que soit le répertoire de lancement
RESOURCE_CSV_MENU = Path(__file__).parent / "resources/menu.csv"


def main() -> None:
    """Lit le menu CSV et affiche chaque plat, ou un message d'erreur."""
    try:
        with open(RESOURCE_CSV_MENU, encoding="utf-8") as file:
            for line in file:
                # Nettoie la ligne (retire \n) et découpe sur la virgule
                parts = line.strip().split(",")
                name = parts[0]
                price = parts[1]
                print(f"{name} — {price} €")
    except FileNotFoundError:
        print("Menu introuvable")


if __name__ == "__main__":
    main()
```

### Version 2 : Avec validation (au-delà du cours)

```python
"""
Version avancée avec validation des lignes et gestion d'erreurs complète.
"""

from pathlib import Path

RESOURCE_CSV_MENU = Path(__file__).parent / "resources/menu.csv"


def lire_menu(chemin: Path) -> list[tuple[str, str]]:
    """
    Lit le fichier CSV et retourne une liste de (nom, prix).

    Args:
        chemin: Chemin vers le fichier CSV

    Returns:
        Liste de tuples (nom, prix)

    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si une ligne est mal formatée
    """
    plats = []
    with open(chemin, encoding="utf-8") as file:
        for numero_ligne, line in enumerate(file, start=1):
            line = line.strip()
            if not line:  # Ignore les lignes vides
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError(
                    f"Ligne {numero_ligne} mal formatée : {line!r}"
                )
            plats.append((parts[0], parts[1]))
    return plats


def main() -> None:
    """Point d'entrée : lit et affiche le menu."""
    try:
        plats = lire_menu(RESOURCE_CSV_MENU)
        for name, price in plats:
            print(f"{name} — {price} €")
    except FileNotFoundError:
        print("Menu introuvable")
    except ValueError as erreur:
        print(f"Erreur dans le fichier menu : {erreur}")


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. `pathlib.Path` pour des chemins robustes

```python
# ❌ Chemin relatif (dépend du répertoire de lancement)
open("menu.csv", encoding="utf-8")
# → plante si lancé depuis un autre dossier

# ✅ Chemin absolu construit depuis __file__
from pathlib import Path
RESOURCE_CSV_MENU = Path(__file__).parent / "resources/menu.csv"
open(RESOURCE_CSV_MENU, encoding="utf-8")
# → fonctionne depuis n'importe où
```

**Pourquoi ?**
- `Path(__file__).parent` donne le dossier du script actuel
- `/` est l'opérateur de concaténation de chemins (portable Windows/Linux/Mac)
- Plus robuste que les chemins relatifs ou les `os.path.join`

### 2. `.strip()` est essentiel

```python
# Sans strip : la ligne contient un \n final
line = "Pizza,12\n"
parts = line.split(",")  # ["Pizza", "12\n"]
print(parts[1])  # "12\n" → saut de ligne parasite

# Avec strip : la ligne est nettoyée
line = "Pizza,12\n".strip()  # "Pizza,12"
parts = line.split(",")      # ["Pizza", "12"]
print(parts[1])              # "12" ✅
```

**Pourquoi ?**
- Chaque ligne d'un fichier texte se termine par `\n` (sauf éventuellement la dernière)
- Sans `.strip()`, le prix contiendrait `\n` et l'affichage serait cassé
- `.strip()` retire aussi les espaces en début/fin de ligne

### 3. `with open(...)` — le context manager

```python
# ❌ Sans with (risque de fuite si erreur)
file = open("menu.csv", encoding="utf-8")
for line in file:
    print(line)
file.close()  # peut être oublié si exception !

# ✅ Avec with (fermeture garantie)
with open("menu.csv", encoding="utf-8") as file:
    for line in file:
        print(line)
# fichier fermé automatiquement, même en cas d'erreur
```

**Pourquoi ?**
- Garantit la fermeture du fichier, même si une exception survient
- Libère les ressources système (descripteur de fichier)
- C'est LE geste Python pour travailler avec des fichiers

### 4. `try/except FileNotFoundError`

```python
# ❌ Sans gestion d'erreur
with open("menu.csv") as file:  # → crash si fichier absent
    ...

# ✅ Avec gestion d'erreur
try:
    with open("menu.csv") as file:
        ...
except FileNotFoundError:
    print("Menu introuvable")  # message clair pour l'utilisateur
```

**Pourquoi ?**
- Si le fichier n'existe pas, Python lève `FileNotFoundError`
- Sans `try/except`, le programme plante avec une traceback technique
- Le `except` affiche un message utilisateur compréhensible
- **Le `try` englobe le `with`** : l'ouverture ET la lecture sont protégées

### 5. Nommage explicite vs index brut

```python
# ❌ Accès par index (peu lisible)
line_exploded = line.strip().split(",")
print(f"{line_exploded[0]} - {line_exploded[1]} €")
# line_exploded[0], c'est quoi ? On doit remonter au split pour savoir

# ✅ Nommage explicite (auto-documenté)
parts = line.strip().split(",")
name = parts[0]
price = parts[1]
print(f"{name} — {price} €")
# name et price parlent d'eux-mêmes
```

**Pourquoi ?**
- Le code se lit comme une phrase
- Pas besoin de commentaire pour comprendre
- Plus facile à modifier (si l'ordre des colonnes change)

### 6. La sortie exacte compte

```python
# ❌ Avant
print(f"{name} - {price} €")   # tiret simple -

# ✅ Après (conforme au corrigé)
print(f"{name} — {price} €")   # em dash — (U+2014)
```

**Pourquoi ?**
- Le corrigé utilise `—` (tiret cadratin), pas `-` (tiret simple)
- C'est la typographie française correcte (espace insécable + tiret cadratin)
- Un test de sortie exacte échoue au moindre écart de caractère

---

## 📊 Tableau récapitulatif — Lecture de fichiers

| Concept | Syntaxe | Rôle |
|---------|---------|------|
| `open()` | `open(path, encoding="utf-8")` | Ouvre un fichier |
| `with` | `with open(...) as file:` | Context manager, ferme auto |
| `encoding` | `encoding="utf-8"` | Définit l'encodage (évite les surprises) |
| `.strip()` | `line.strip()` | Retire espaces et `\n` en début/fin |
| `.split()` | `line.split(",")` | Découpe une chaîne en liste |
| `Path` | `Path(__file__).parent / "fichier"` | Construit un chemin robuste |
| `FileNotFoundError` | `except FileNotFoundError:` | Capture l'erreur fichier absent |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] `pathlib.Path` pour les chemins (robuste, portable)
- [x] `with open(...) as file:` (fermeture garantie)
- [x] `encoding="utf-8"` explicite
- [x] `.strip()` sur chaque ligne (nettoie `\n`)
- [x] `.split(",")` avec guillemets doubles (PEP 8)
- [x] Nommage explicite (`name`, `price`) plutôt que `parts[0]`
- [x] `try/except FileNotFoundError` autour du `with`
- [x] Message d'erreur en français (cohérent UI)
- [x] Structure `main()` + `if __name__ == "__main__"`
- [x] Docstring module + fonction
- [x] Pas de ligne de debug dans la sortie
- [x] Format de sortie conforme au corrigé (`—`, espace avant `€`)

---

## 💬 Pour aller plus loin

1. **Validation des lignes** : vérifier que chaque ligne a exactement 2 colonnes (`len(parts) == 2`)
2. **Conversion du prix** : `price = float(parts[1])` pour calculer un total
3. **Classe `Dish`** : créer un objet `Dish` par ligne et les stocker dans une liste
4. **CSV module** : utiliser `import csv` et `csv.DictReader` pour plus de robustesse
5. **Gestion d'encodage** : ajouter `errors="replace"` pour les fichiers mal encodés
6. **Fichier JSON** : remplacer le CSV par du JSON avec `json.load()`

```python
# Exemple avancé : avec csv.DictReader et classe Dish
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Dish:
    name: str
    price: float
    available: bool = True

    def describe(self) -> str:
        statut = "disponible" if self.available else "indisponible"
        return f"{self.name} ({self.price} €) - {statut}"


def lire_menu_csv(chemin: Path) -> list[Dish]:
    """Lit un CSV et retourne une liste de Dish."""
    plats = []
    with open(chemin, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)  # Lit l'en-tête automatiquement
        for row in reader:
            plat = Dish(
                name=row["nom"],
                price=float(row["prix"]),
                available=row.get("disponible", "true").lower() == "true"
            )
            plats.append(plat)
    return plats


# Utilisation
chemin = Path(__file__).parent / "resources/menu.csv"
try:
    for plat in lire_menu_csv(chemin):
        print(plat.describe())
except FileNotFoundError:
    print("Menu introuvable")
```

---

*Rapport généré le 28 octobre 2026 — Format aligné sur `oc-python-basics`.*
