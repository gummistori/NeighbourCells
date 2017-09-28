# NeighbourCells checker

## About this system
Checks for redundancy errors in adjacent sites.

In a trunking radio system, neighbouring cells must be configured correctly in that way that Cell A has Cell B as configured neighbour but if Cell B does not have Cell A as a neighbour, there is a misconfiguration.

## Languages and requirements
### About this project
This program reads in the exported HTML file from UCS's "Source site ACC" and imports the information to a installed Neo4j database.

### Prerequisite
* You should have Python 3 (I used version 3.5.4)
* You should have Python packet called beautifulsoup4 installed
* You should have Python packet called neo4j-driver installed
* You should have Neo4j installed and running with an empty database.

## Usage

First reads a HTML file containing all the site adjacency list.
