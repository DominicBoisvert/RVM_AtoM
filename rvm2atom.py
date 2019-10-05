#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
rvm2atom
---
A Python tool to transform RVM XML into something AtoM understands.

For information on usage and dependencies, see:
https://github.com/DominicBoisvert/RVM_AtoM

Python 2.7+

The MIT License (MIT)
Copyright (c) 2019 Dominic Boisvert
http://dominicboisvert.ca

"""

import argparse
import os
import re
import sys
import textwrap

rvm_altLabel = []
rvm_prefLabel = []

# Search pattern to find altlabel in RVM XML file. The pattern excludes some altLabels that are unwanted, mainly institutions names it might not catch them all. Should be in a config file.
pattern = re.compile('<skos:altLabel xml:lang="fr">' "[^AAT]" "[^RVM]" "[^CHS]" "[^MeSH]" "[^RAMEAU]", re.IGNORECASE)

# Search for the last prefLabel in RVM XML file. But doesn't work because the prefLabel we want isn't always the last one.
# re.findall(r"\w+ <skos:prefLabel xml:lang="fr"> \w+$", s)
# patternPrefLabel = re.compile('<skos:prefLabel xml:lang="fr">', re.IGNORECASE)

# Add help
def _make_parser(version):
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="path to source file, must be xml") # This is our input file from RVM
    parser.add_argument("destination", help="path to destination file, must be xml") # This is our output file for AtoM
    parser.add_argument("subject", help="subject heading to insert in the prefLabel tag.") # This is the name of the subject heading
    parser.add_argument("-V", "--version", help="display rvm2atom version", action="version", version="%s" % version)

    return parser

def main():
    # system info
    rvm2atom_version = 'rvm2atom 0.0.2'

    parser = _make_parser(rvm2atom_version)
    args = parser.parse_args()

    # global variables
    global source, destination, subject
    source = os.path.abspath(args.source) 
    destination = os.path.abspath(args.destination)
    subject = args.subject

    # We need this for line 67. 
    linenum = 0

    # We create or open destination file to add some XML stuff at the beginning.
    with open(args.destination, "w+") as destination:
        destination.write('<?xml version="1.0" encoding="utf-8" ?>' + '\n' \
        + '<rdf:RDF' + '\n' \
        +'    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"' + '\n' \
        +'    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"' + '\n' \
        +'    xmlns:skos="http://www.w3.org/2004/02/skos/core#"' + '\n' \
        +'    xmlns:dc="http://purl.org/dc/elements/1.1/">' + '\n' + '\n' \
        + '    <skos:ConceptS>' + '\n' 
        + '\n' \
        + '        <skos:prefLabel xml:lang="fr">' + subject + '</skos:prefLabel>'  + '\n' + '\n')
    destination.close()

    # Open both files to find the altLabels in the source file and copy them in the destination file. We could have better wrapping.
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
   
    # We reopen destination file to add some XML stuff at the end.
    with open(args.destination, "a") as destination:
        destination.write('    </skos:Concept>' + '\n' + '</rdf:RDF>')
    destination.close()

main()