# Rapport de correction — P1C5 FoodExpress

Exercice : lire un fichier CSV, manipuler des données et gérer des erreurs simples.
Corrigé de référence : [python-p1c5-corrige-clean.pdf](https://course.oc-static.com/courses/9137941/python-p1c5-corrige-clean.pdf)

---

## 1. Conformité

| Critère | Attendu (corrigé) | Réalisé (avant) | Réalisé (après) | Statut |
|---|---|---|---|---|
| Lecture du fichier CSV | `open("menu.csv", encoding="utf-8")` | `open(RESOURCE_CSV_MENU, ...)` avec `pathlib` | Idem | ✅ (équivalent, plus robuste) |
| Gestion `FileNotFoundError` | `try/except` autour du `with` | ✅ Correct | ✅ Correct | ✅ |
| `.strip()` pour nettoyer les lignes | ✅ Présent | ✅ Présent | ✅ Présent | ✅ |
| `.split(",")` pour découper | ✅ Présent | `split(',')` (guillemets simples) | `split(",")` (guillemets doubles) | ✅ corrigé |
| Nommage des variables | `parts`, `name`, `price` | `line_exploded[0]`, `line_exploded[1]` | `parts`, `name`, `price` | ✅ corrigé |
| **Format de sortie exact** | `Pizza — 12 €` (em dash `—`) | `Pizza - 12 €` (tiret `-`) | `Pizza — 12 €` | ✅ corrigé |
| Pas de sortie parasite | Aucune ligne avant les plats | `print(RESOURCE_CSV_MENU)` affiche le chemin | Supprimé | ✅ corrigé |
| Structure `main()` | Pas de fonction (code plat) | `def main()` + `if __name__` | Conservé | ✅ (bonne pratique) |

**Sortie avant correction :**
```
/Users/.../resources/menu.csv      ← ligne parasite (debug)
Pizza - 12 €                       ← tiret simple au lieu de —
Salade - 8 €
Burger - 10 €
Tiramisu - 6 €
```

**Sortie après correction (conforme au corrigé) :**
```
Pizza — 12 €
Salade — 8 €
Burger — 10 €
Tiramisu — 6 €
```

**Test fichier absent :** `Menu introuvable` ✅

---

## 2. Erreurs

### 2.1 Sortie parasite — **CORRIGÉ**

**Où** : `p1c5.py`, ligne 6 (avant correction).

**Quoi** : `print(RESOURCE_CSV_MENU)` affichait le chemin absolu du fichier avant le contenu du menu.

**Pourquoi c'est un problème** : La sortie ne correspondait pas au corrigé. Si un test automatisé compare la sortie, la première ligne (`/Users/.../menu.csv`) fait échouer le test.

**Correction** : ligne supprimée.

### 2.2 Mauvais séparateur — **CORRIGÉ**

**Où** : `p1c5.py`, ligne 12 (avant correction).

**Quoi** : `f"{line_exploded[0]} - {line_exploded[1]} €"` utilisait un tiret simple `-` au lieu du tiret cadratin `—` (em dash, U+2014).

**Pourquoi c'est un problème** : Le corrigé utilise `—`. C'est une différence subtile mais visible — et un test de sortie exacte la détecte.

**Correction** : `—` au lieu de `-`.

### 2.3 Nommage des variables — **CORRIGÉ**

**Où** : `p1c5.py`, ligne 11 (avant correction).

**Quoi** : `line_exploded[0]` et `line_exploded[1]` — accès direct par index, peu lisible.

**Pourquoi c'est un problème** : `line_exploded[0]`, c'est quoi ? On ne sait pas sans remonter au `split`. Le corrigé nomme explicitement `name` et `price`, ce qui rend le code auto-documenté.

**Correction** :
```python
parts = line.strip().split(",")
name = parts[0]
price = parts[1]
```

### 2.4 Guillemets simples — **CORRIGÉ**

**Où** : `p1c5.py`, ligne 11 (avant correction).

**Quoi** : `split(',')` avec des guillemets simples.

**Pourquoi** : PEP 8 recommande les guillemets doubles `"` par défaut (les simples servent quand la chaîne contient des doubles). Ce n'est pas une erreur fonctionnelle, mais une convention à prendre.

**Correction** : `split(",")`.

---

## 3. Suggestions d'amélioration

### Idiome Python

| Actuel | Proposé | Pourquoi |
|---|---|---|
| `line_exploded[0]` / `line_exploded[1]` | `name = parts[0]` / `price = parts[1]` | ✅ Appliqué — le nommage explicite rend le code lisible sans commentaire. |
| Accès par index | Déstructuration `name, price = line.strip().split(",")` | ⚠️ **Au-delà du cours** — plus élégant, mais le corrigé reste sur `parts[0]`/`parts[1]` pour la pédagogie. |

### Lisibilité / PEP 8

| Actuel | Proposé | Pourquoi |
|---|---|---|
| Tiret `-` dans la sortie | Tiret cadratin `—` | ✅ Appliqué — colle au corrigé et c'est la typographie correcte en français. |
| `split(',')` | `split(",")` | ✅ Appliqué — PEP 8 recommande les guillemets doubles. |
| `print(RESOURCE_CSV_MENU)` | Supprimé | ✅ Appliqué — sortie parasite, pas dans le corrigé. |

### Robustesse

| Actuel | Proposé | Pourquoi |
|---|---|---|
| `Path(__file__).parent / "resources/menu.csv"` | Chemin relatif `"menu.csv"` (comme le corrigé) | Ton approche avec `pathlib` est **plus robuste** — elle fonctionne quel que soit le répertoire de lancement. Garde-la, c'est mieux que le corrigé. |
| `except FileNotFoundError` | Ajouter `except Exception` en dernier recours ? | ⚠️ **Au-delà du cours** — pour l'instant, `FileNotFoundError` suffit. Ne masque pas les vraies erreurs. |

### Structure

| Actuel | Statut |
|---|---|
| `def main()` + `if __name__ == "__main__"` | ✅ Bonne pratique — le corrigé est en code plat, mais ta structure est prête pour un vrai projet. |
| `pathlib.Path` | ✅ Moderne et robuste — le corrigé utilise un chemin relatif simple, mais `pathlib` est la voie royale en Python 3. |

---

## 4. Tics PHP

Aucun tic PHP détecté. Le code est du Python idiomatique :
- `pathlib.Path` pour les chemins — l'équivalent PHP serait `__DIR__ . '/resources/menu.csv'`, mais `Path` est plus propre
- `with open(...) as file:` — le context manager Python, pas de `fclose()` à la PHP
- `try/except FileNotFoundError` — gestion d'exceptions Python, pas de `@file_exists()` ou `is_file()` à la PHP
- `.strip()` et `.split()` — méthodes de chaîne Python, chaînage propre
- `f-strings` — interpolation moderne, pas de `echo $name . " - " . $price`

**Ce qui est bien** :
- Le `with` garantit la fermeture du fichier (pas de `fclose` oublié)
- `encoding="utf-8"` explicite — évite les problèmes d'encodage
- Gestion d'erreur propre avec message utilisateur en français

---

## 5. Ce que j'apprends

- **`pathlib.Path` vs chemin relatif** : `Path(__file__).parent / "resources/menu.csv"` fonctionne depuis n'importe quel répertoire de lancement. C'est plus robuste que `"menu.csv"` qui dépend du CWD. Bonne pratique à garder.
- **`.strip()` est essentiel** : Sans `.strip()`, chaque ligne du CSV garderait son `\n` final, et `"12\n"` ne s'afficherait pas comme `12`. Toujours nettoyer les lignes lues dans un fichier.
- **La sortie exacte compte** : Un tiret `-` vs `—`, une ligne de debug en trop — ces détails cassent un test de sortie. Toujours comparer caractère par caractère avec le corrigé.
- **`with open(...)`** : Le context manager ferme le fichier automatiquement, même en cas d'erreur. C'est le geste Python pour travailler avec des fichiers.

---

*Rapport généré le 28 octobre 2026.*
