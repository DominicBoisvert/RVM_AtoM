#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
rvm2atom
---
A Python tool to transform RVM XML into something AtoM understands.

For information on usage and dependencies, see:
https://github.com/DominicBoisvert/RVM_AtoM

Python 3.4+

The MIT License (MIT)
Copyright (c) 2019 Dominic Boisvert
http://dominicboisvert.ca

"""

import argparse
import os
import re
import sys

rvm_altLabel = []

# Search pattern to find altlabel in RVM XML file. The pattern excludes some altLabels that are unwanted, mainly institutions names. Should be in a config file.
pattern = re.compile('<skos:altLabel xml:lang="fr">' "[^AAT]" "[^RVM]" "[^CHS]" "[^MeSH]" "[^RAMEAU]", re.IGNORECASE)

# Add help
def _make_parser(version):
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to source file, must be xml")
    parser.add_argument("destination", help="Path to destination file, must be xml")

    return parser

def main():
    # system info
    rvm2atom_version = 'rvm2atom 0.0.1'
    linenum = 0

    parser = _make_parser(rvm2atom_version)
    args = parser.parse_args()

    # global variables
    global source, destination
    source = os.path.abspath(args.source)
    destination = os.path.abspath(args.destination)

    # We create or open atom_file to add some XML stuff at the beginning.

    with open(args.destination, "w+") as destination:
        destination.write('<?xml version="1.0" encoding="utf-8" ?>' + '\n' + '<rdf:RDF' + '\n' + 'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"' + '\n' + 'xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"' + '\n' + 'xmlns:skos="http://www.w3.org/2004/02/skos/core#"' + '\n' + 'xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n' '<skos:ConceptS>' + '\n' + '<skos:prefLabel xml:lang="fr">AJOUTER LE TERME ICI</skos:prefLabel>'  + '\n')
    destination.close()


    # Open both files to find the altLabels in the input file and copy them in the output file.
    with open(args.source, 'rt') as source, \
        open(args.destination, mode='a+') as destination:
        for line in source:
            linenum += 1
            if pattern.search(line) != None:      # If a match is found 
                rvm_altLabel.append((linenum, line.rstrip('\n')))
        for altLabel in rvm_altLabel:
            destination.write(altLabel[1])
    # We close our files.
    source.close()
    destination.close()
   
    # We reopen atom_file to add some XML stuff at the end.
    with open(args.destination, "a") as destination:
        destination.write('</skos:Concept>' + '\n' + '</rdf:RDF>')
    destination.close()

main()