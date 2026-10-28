# Rapport de correction — P1C4 FoodExpress

Exercice : implémenter la classe `Dish` en POO Python.
Corrigé de référence : [python-p1c4-corrige-clean.pdf](https://course.oc-static.com/courses/9137941/python-p1c4-corrige-clean.pdf)

> **Mise à jour** : rapport révisé après corrections d'Emmanuel (v2).

---

## 1. Conformité

| Critère | Attendu (corrigé) | Réalisé | Statut |
|---|---|---|---|
| Classe `Dish` avec 3 attributs | `name`, `price`, `available` via `__init__` | Identique via `@dataclass` | ✅ (équivalent, *au-delà du cours*) |
| Méthode `describe()` | Retourne une chaîne descriptive | ✅ | ✅ |
| Instanciation de 2 objets | `pizza`, `tiramisu` | `products` (liste) | ✅ (équivalent) |
| Affichage des descriptions | `print(pizza.describe())` | `print(product.describe())` dans une boucle | ✅ (équivalent) |
| Point d'entrée `main.py` | — | `src/foodexpress/main.py` | ✅ |
| `__init__.py` sans logique | — | Vide | ✅ |
| **Format de sortie exact** | `Tiramisu (6.0 €) - indisponible` | `Tiramisu (6.0 €) - Indisponible` | ❌ |

**Sortie réelle vs attendue :**

```
# Réalisé                          # Attendu (corrigé)
Pizza (12.0 €) - disponible         Pizza (12.0 €) - disponible
Tiramisu (6.0 €) - Indisponible     Tiramisu (6.0 €) - indisponible
```

Un seul écart restant : `Indisponible` avec une majuscule au lieu de `indisponible`.

---

## 2. Erreurs

### 2.1 Casse incorrecte sur « indisponible » — **CORRIGÉ PARTIELLEMENT**

**Où** : `src/foodexpress/Entities/Dish.py`, ligne 10.

**Quoi** : `"disponible"` est maintenant en minuscule ✅, mais `"Indisponible"` garde sa majuscule ❌.

**Pourquoi** : Si un test automatisé compare la sortie caractère par caractère, l'exercice échoue sur la deuxième ligne.

**Correction** : ligne 10, remplacer `"Indisponible"` par `"indisponible"`.

```python
# Actuel
return f"{self.name} ({round(self.price, 1)} €) - {"disponible" if self.available else "Indisponible" }"
# Corrigé
return f"{self.name} ({round(self.price, 1)} €) - {"disponible" if self.available else "indisponible" }"
```

### 2.2 Import absolu — **RÉSOLU**

L'import `from Entities.Dish import Dish` (qui plantait selon le CWD) a été remplacé par `from foodexpress.Entities.Dish import Dish` dans `main.py`. Fonctionne avec `PYTHONPATH=src python -m foodexpress.main`.

### 2.3 Logique dans `__init__.py` — **RÉSOLU**

`src/foodexpress/__init__.py` est maintenant vide. La logique a été déplacée dans `src/foodexpress/main.py`, conformément aux conventions Python.

### 2.4 `Entities` sans `__init__.py` — **RÉSOLU**

`src/foodexpress/Entities/__init__.py` créé (vide), `Entities` est maintenant un package Python propre.

---

## 3. Suggestions d'amélioration

### Idiome Python

| Actuel | Proposé | Pourquoi |
|---|---|---|
| `@dataclass` + annotations de type | `__init__` manuel comme dans le corrigé | ⚠️ **Au-delà du cours** — le cours enseigne le trio `attributs + __init__ + self` comme geste fondateur. `@dataclass` masque cette mécanique. À réserver pour plus tard. |
| Ternaire inline `{"disponible" if self.available else "indisponible"}` | `if self.available: return ... else: return ...` | ⚠️ **Au-delà du cours** — la ternaire est compacte mais le `if/else` du corrigé est plus lisible pour un débutant. |
| `round(self.price, 1)` | `self.price` directement | Le `round` est inutile ici (`12.0` et `6.0` n'ont pas de décimale à arrondir). Le corrigé n'en met pas. |

### Lisibilité / PEP 8

| Actuel | Proposé | Pourquoi |
|---|---|---|
| `round(self.price, 1)` | Supprimer le `round` | Moins de code, sortie identique pour ces valeurs. |
| `products` (liste) + boucle `for` | OK, garde ça | La boucle est propre et Pythonique — mieux que deux `print` séparés. |

### Structure du projet

| Actuel | Statut |
|---|---|
| `src/foodexpress/main.py` comme point d'entrée | ✅ Conforme |
| `src/foodexpress/__init__.py` vide | ✅ Conforme |
| `src/foodexpress/Entities/__init__.py` + `Dish.py` | ✅ Package propre |

> La structure `src/` + packages reste « au-delà du cours » pour ce chapitre, mais elle est propre et bien organisée. À garder si tu veux anticiper les chapitres suivants.

---

## 4. Tics PHP

Aucun tic PHP détecté. Le code est du Python idiomatique :
- `snake_case` pour les variables (`products`, `product`)
- Pas de `array()` à la PHP, utilisation correcte des listes `[]`
- Pas de `echo`, utilisation de `print()`
- Pas de `->` pour l'accès aux membres, utilisation correcte du `.`
- `@dataclass` est un idiome Python pur (même si avancé pour ce chapitre)

**Ce qui est bien** : la structure en packages est propre, les imports sont corrects, les conventions de nommage sont respectées, les f-strings sont utilisées correctement, les annotations de type sont présentes.

**Progrès** : la séparation `main.py` / `__init__.py` / package `Entities` est un vrai pas en avant par rapport à la v1.

---

## 5. Ce que j'apprends

- **`@dataclass` vs `__init__`** : `@dataclass` génère automatiquement `__init__`, `__repr__`, `__eq__`… C'est un raccourci puissant, mais il faut d'abord comprendre ce qu'il génère. Le corrigé part de `__init__` manuel pour que tu voies la mécanique.
- **La sortie compte** : Un exercice peut être « fonctionnellement correct » mais échouer si le format de sortie ne colle pas exactement. Toujours comparer avec la sortie attendue du corrigé, caractère par caractère.
- **Structure en packages** : `__init__.py` marque un dossier comme package Python. La logique va dans `main.py`, pas dans `__init__.py`. C'est la convention qui rend les imports robustes.

---

*Rapport v2 — mis à jour le 28 octobre 2026 après corrections d'Emmanuel.*
