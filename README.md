# RVM vers AtoM
 
Script en Python pour préparer les termes "sujets" du RVM pour l'importation dans AtoM.

## Utilisation

```
usage: rvm2atom.py [-h]
                   source destination

positional arguments:
  source                Path to source file, must be XML
  destination           Path to destination file, must be XML

```

rvm2atom accepte les chemins absolus et relatifs pour la source et la destination.

Example commands:
rvm2atom.py "/home/bcadmin/Desktop/File from rvm.xml" /home/bcadmin/Desktop/File for atom.xml : le résultat sera un fichier XML presque prêt pour importation dans AtoM.

### Avant l'importation dans AtoM

Le script `rvm2atom.py` va créer une ligne `<skos:prefLabel xml:lang="fr">AJOUTER LE TERME ICI</skos:prefLabel>` dans le fichier de destination.

Vous devrez remplacer le texte `AJOUTER LE TERME ICI` par le terme sujet que vous souhaitez importer dans AtoM.

Vous pourrez ensuite importer le fichier XML dans AtoM.