# AGENTS.md — FoodExpress

Instructions pour tout agent IA (Claude Code, Copilot, Cursor, Vibe…) intervenant sur ce dépôt.
Ce fichier fait foi sur les règles de collaboration. En cas de conflit avec une habitude de l'agent, ce fichier gagne.

## Contexte

**FoodExpress** est une mini-application de livraison de repas, en ligne de commande : le fil rouge du cours OpenClassrooms « Maîtrisez les bases de Python ».

Le propriétaire du dépôt (Emmanuel) est **développeur back-end senior (PHP, 15 ans)** en montée en compétence Python dans le cadre d'une formation Data Engineer. Le projet est **pédagogique** : sa valeur est dans ce qu'il m'apprend, pas dans ses fonctionnalités.

Conséquences pour l'agent :

- écrire du **Python idiomatique**, jamais du PHP transposé ;
- rester au niveau du cours : structures de données, fonctions, classes, fichiers, exceptions. Toute idée au-delà de ce périmètre est bienvenue, mais **marquée « au-delà du cours »** dans la réponse — jamais glissée en silence dans le code ;
- privilégier la lisibilité aux ruses de sioux : un code que je relis sans effort vaut mieux qu'un code clever.

## Environnement

- **Python 3.14**, environnement virtuel `.venv/` à la racine du projet.
- Activation : `source .venv/bin/activate`, lancement : `python main.py`.
- **Stdlib uniquement** tant que le cours n'introduit pas de dépendance.
- Indentation : **4 espaces**, jamais de tabulation.

## Conventions de code

- Identifiants **en anglais** : `snake_case` pour variables et fonctions, `PascalCase` pour les classes, `UPPER_SNAKE` pour les constantes.
- **Commentaires de code en français**, messages affichés à l'utilisateur **en français**.
- PEP 8 de référence ; **f-strings** pour l'interpolation.
- `@dataclass` pour les objets de données ; classe classique avec `__init__` quand la logique et les méthodes l'emportent.
- Annotations de type sur les signatures publiques dès qu'elles aident à la lecture ; docstrings (PEP 257) sur les fonctions et classes publiques.
- Nommer au plus juste : `stock`, `order_total`, pas `current_order_total_amount`.

## Les trois modes de travail

Chaque demande commence par un mode explicite : « Je code », « Délègue », « Corrige ».
Si le mode est ambigu, **demander avant d'agir**.

### Mode 1 — « Je code » (implémentation manuelle)

Emmanuel écrit lui-même. L'agent :

- ne modifie **aucun fichier** ;
- répond aux questions factuelles (syntaxe, comportement d'un builtin) **sans fournir la solution** de l'exercice en cours : indices et documentation, pas de code final ;
- ne propose pas de refactor non sollicité.

### Mode 2 — « Délègue » (l'agent implémente)

Ce mode ne s'active **que** sur une demande structurée. Une délégation doit contenir ces six champs :

1. **Objectif** : une phrase, le besoin métier.
2. **Fichiers** : ceux à créer ou modifier — et rien d'autre.
3. **Comportement attendu** : les critères d'acceptation, avec les sorties console attendues si possible.
4. **Contraintes** : le périmètre négatif, ce qu'il ne faut **pas** faire.
5. **Données** : exemples en entrée, format attendu en sortie.
6. **Validation** : la commande qui prouve que ça marche.

Si un champ manque : **demander le champ manquant, ne pas improviser.**
C'est une règle absolue — une délégation floue produit du code que je ne comprends pas, donc de l'apprentissage perdu.

Règles d'exécution en mode délégation :

- respecter le périmètre **exactement** : pas de fonctionnalité bonus, pas de refactor des zones non concernées ;
- le code suit les conventions ci-dessus sans exception ;
- livrer avec un **court résumé des choix** (3 à 5 puces) : pourquoi cette structure, cet idiome.

### Mode 3 — « Corrige » (revue avec rapport)

Déclenché par « Corrige » ou « Rapport de correction ». L'agent **ne modifie aucun fichier** dans ce mode : il produit un rapport. Il peut ensuite, sur demande explicite, appliquer les suggestions retenues.

Format du rapport :

1. **Conformité** — la solution fait-elle ce qui était demandé, point par point ?
2. **Erreurs** — bugs réels et comportements incorrects, chacun avec le scénario qui le provoque.
3. **Suggestions d'amélioration** — classées par nature : idiome Python, lisibilité, PEP 8, robustesse, performance. Une suggestion = le geste actuel, la proposition, et le **pourquoi en une phrase**.
4. **Tics PHP** — les endroits où le code est du PHP transposé. Montrer le **même geste dans les deux langages** (jamais un idiome PHP contre un idiome Python), en deux blocs de code séparés, chacun avec ses propres commentaires.
5. **Ce que j'apprends** — 2 à 3 puces : les notions Python que ce travail mobilise ou révèle.

Règles de la revue :

- **Ton senior** : direct, factuel, ancré dans le code. Pas de conseils pour débutants, pas de félicitations de complaisance.
- Ne pas réécrire le code d'un bloc dans le rapport : suggérer, laisser Emmanuel décider.
- Ce qui est bien est nommé aussi — en une ligne, pas un paragraphe.

## Interdits transversaux (tous modes)

- **Jamais** de nouvelle dépendance sans accord explicite.
- **Jamais** de refactor ou de suppression en dehors du périmètre demandé.
- **Jamais** de code non demandé en mode correction.
- **Jamais** résoudre l'exercice en mode « Je code ».

## État du projet

- `main.py` : point d'entrée, affiche l'écran d'accueil (menu du jour).
- Pas de persistance, pas de base, pas de tests à ce stade : ça vient avec les chapitres du cours.

> Cette section se met à jour à mesure que le projet avance ; elle décrit l'état réel, pas l'état final.

---

*Dernière mise à jour : 27 octobre 2026.*
