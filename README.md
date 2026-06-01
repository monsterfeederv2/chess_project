# Projet d'echecs Python

Projet I1 realise en Python avec une approche orientee objet.

## Lancer le jeu

```bash
python3 main.py
```

Une variante d'affichage avec symboles Unicode est disponible :

```bash
python3 mainAffichage.py
```

## Format des coups

Le format principal suit le sujet : identifiant de piece + position de depart, puis identifiant de piece + position d'arrivee.

Exemples :

```text
Nb1 Nc3
Pe2 Pe4
Ng1 Nf3
```

Le programme accepte aussi le format simplifie `e2 e4`, mais le format avec la lettre de piece est celui a presenter.

Commandes disponibles pendant une partie :

```text
save
load
quit
```

`save` enregistre la partie dans `savegame.json`. `load` restaure ce fichier.

## Tests

```bash
python3 -m unittest -v
```

## Dependances

Le projet utilise uniquement la bibliotheque standard de Python :

- `abc` : creation de la classe abstraite `Piece`.
- `json` : sauvegarde et restauration d'une partie.
- `random` : generation de coups simples pour `AIPlayer`.
- `unittest`, `tempfile`, `os` : tests unitaires.

Aucune dependance externe n'est necessaire. Il n'y a donc rien a installer avec `pip`.

## Architecture

- `Position.py` : represente une case de l'echiquier, par exemple `e4`.
- `piece.py` : classe abstraite commune aux pieces.
- `king.py`, `queen.py`, `bishop.py`, `knight.py`, `rook.py`, `pawn.py` : regles de deplacement de chaque piece.
- `board.py` : etat du plateau, recherche de piece, deplacement, sauvegarde des pieces.
- `player.py` : joueur humain.
- `aiplayer.py` : joueur automatique simple.
- `chess.py` : boucle de jeu, validation des coups, changement de joueur, echec et mat, sauvegarde/restauration.
- `main.py` : point d'entree principal.
- `mainAffichage.py` : point d'entree avec affichage plus visuel.
- `test_position.py`, `test_chess_rules.py` : tests unitaires.

Le plateau stocke les pieces dans une liste. Un dictionnaire `PIECE_TYPES` dans `Board` associe les lettres des pieces aux classes Python, ce qui sert a restaurer une sauvegarde.

## Fonctionnalites implementees

- Initialisation complete de l'echiquier.
- Deplacements standards du roi, de la reine, du fou, du cavalier, de la tour et du pion.
- Verification des obstacles pour les pieces lineaires.
- Capture des pieces adverses.
- Interdiction de capturer une piece de meme couleur.
- Interdiction de jouer une piece adverse.
- Detection d'echec et d'echec et mat basique.
- Sauvegarde et restauration dans un fichier JSON.
- Joueur IA simple.
- Tests unitaires des regles principales.

## Limites

Comme demande dans le sujet, les coups speciaux ne sont pas implementes :

- roque ;
- prise en passant ;
- promotion des pions.

L'IA reste volontairement simple : elle choisit un coup possible sans strategie avancee.
