# Author : Dominic Boisvert
# Email : db@dominicboisvert.ca
# Scope : Python script to prepare a RVM term for importation in AtoM as a subject.
# Use : python rvm2atom.py argument1 argument2
# Use : argument1 is the name of the file imported from RVM.
# Use : argument2 is the name of the output file, must be xml, example : congres.xml
# Use : add the name of the term in place of AJOUTER LE TERME ICI

import re, sys

rvm_altLabel = []
linenum = 0
pattern = re.compile('<skos:altLabel xml:lang="fr">' "[^RVM]" "[^CHS]" "[^RAMEAU]", re.IGNORECASE)

# We create or open atom_file to add some XML stuff at the beginning.
with open(sys.argv[2], "w+") as atom_file:
    atom_file.write('<?xml version="1.0" encoding="utf-8" ?>' + '\n' + '<rdf:RDF' + '\n' + 'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"' + '\n' + 'xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"' + '\n' + 'xmlns:skos="http://www.w3.org/2004/02/skos/core#"' + '\n' + 'xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n' + '<skos:prefLabel xml:lang="fr">AJOUTER LE TERME ICI</skos:prefLabel>'  + '\n')
atom_file.close()

with open(sys.argv[1], 'rt') as rvm_file, \
     open(sys.argv[2], mode='a+') as atom_file:
    for line in rvm_file:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            rvm_altLabel.append((linenum, line.rstrip('\n')))
    for altLabel in rvm_altLabel:
        atom_file.write(altLabel[1])
# We close or files.
atom_file.close()
rvm_file.close()

# We reopen atom_file to add some XML stuff at the end.
with open(sys.argv[2], "a") as atom_file2:
    atom_file2.write('</rdf:RDF>')
atom_file2.close()