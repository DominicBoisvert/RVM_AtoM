# RVM vers AtoM
 
Script en Python pour préparer les termes "sujets" du RVM pour l'importation dans AtoM.

## Utilisation

```
usage: rvm2atom.py [-h]
                   source destination subject

positional arguments:
  source                Path to source file, must be XML
  destination           Path to destination file, must be XML
  subject               Subject heading to insert in the prefLabel XML tag of the destination file.

```

rvm2atom accepte les chemins absolus et relatifs pour la source et la destination.

Example commands:
rvm2atom.py "/home/bcadmin/Desktop/File from rvm.xml" /home/bcadmin/Desktop/File for atom.xml "congrès et conférence": le résultat sera un fichier XML presque prêt pour l'importation dans AtoM.

### Avant l'importation dans AtoM

Vous devez valider les `altLabel` du fichier de destination. Le RVM utilise cette balise pour identifier des sources.

Vous pourrez ensuite importer le fichier XML dans AtoM.