# Ascii Converter
###### par Yasmine Margueron et Gabriel Fasano

## Installation

Pour créer l'environnement virtuel et pour installer les dépendances, lancer le script `init.sh` du projet. En cas de problème les commandes suivantes peuvent être effectuées manuellement :
`python3 -m venv .venv` puis pour activer l'environnement virtuel : `source .venv/bin/activate`. Finalement pour installer les dépendances lancer `pip install -r requirements.txt`.
Dans le script, les dossiers nécessaire (détaillés ci-dessous) sont également crées.
Il est également nécessaire d'ajouter le chemin de la bibliothèque `ffmpeg` à la variable d'environnement `PATH`. La bibliothèque est disponible dans le projet en fichier compressé `ffmpeg.7z`

## Usage

Le lancement des programmes nécessite d'avoir activé l'environnement virtuel.
### GUI

Le programme avec interface graphique peut être lancé en ligne de commande. Le script se nomme `gui.py` et est accessible via le chemin `./gui.py`.

### Image

Le programme traitant l'image peut être lancé en ligne de commande. Le script se nomme `image.py` et est accessible via le chemin `./image.py`.

### Vidéo

Le programme traitant la vidéo peut être lancé en ligne de commande. Le script se nomme `video.py` et est accessible via le chemin `./video.py`.

## Arborescence

Les dossiers `images` et `video` contient les images de test du projet mais n'importe quelle image, respectivement vidéos, peut être utilisée.

Le dossier `temp` contient les fichiers temporaires du projet. Si le dossier est absent il doit être créé pour que le programme puisse fonctionner correctement. Les dossiers et fichiers à l'intérieur sont supprimés à la fin de la conversion d'une image ou d'une vidéo si tout s'est déroulé correctement et sans erreur.

Le dossier `result` contient les résultats de la conversion. Il doit contenir un dossier nommé `images` et un dossier nommé `videos` pour que le programme fonctionne correctement.