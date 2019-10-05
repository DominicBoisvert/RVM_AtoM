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

rvm2atom accepte les chemins absolus et relatifs pour la source et la destination. Le sujet doit être entre guillemets lorsqu'il est composé de plus d'un mot.

Exemple d'une commande avec des espaces dans le chemin et plus d'un mot pour former le sujet :
`rvm2atom.py "/home/bcadmin/Desktop/File from rvm.xml" "/home/bcadmin/Desktop/File for atom.xml" "congrès et conférence"`

Exemple d'une comande dans le répertoire de travail et pour un sujet formé d'un seul mot : 
`rvm2atom.py rvm.xml atom.xml restaurants`

Le résultat est un fichier XML presque prêt pour l'importation dans AtoM.

### Avant l'importation dans AtoM

Vous devez valider les `altLabel` du fichier de destination. Le RVM utilise aussi cette balise pour identifier des sources.

Vous pourrez ensuite importer le fichier XML dans AtoM.