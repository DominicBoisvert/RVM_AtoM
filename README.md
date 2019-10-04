# RVM_AtoM
 
Script en Python pour préparer les termes du RVM pour l'importation dans AtoM.

## Utilisation

```usage: rvm2atom.py [-h]
                     source destination

positional arguments:
  source                Path to source file, must be XML
  destination           Path to destination file, must be XML```

rvm2atom accepte les chemins absolus et relatifs pour la source et la destination.

Example commands:
brunnhilde.py -z "/home/bcadmin/Desktop/Folder to Scan" /home/bcadmin/Desktop brunnhilde-test-0 : will result in a new directory "brunnhilde-test-0" on the BitCurator desktop containing various reports on input source "Folder to Scan".