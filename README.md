# NeighbourCells checker

## About this project
Checks for redundancy errors in adjacent sites.

In a trunking radio system, neighbouring cells must be configured correctly in that way that Cell A has Cell B as configured neighbour but if Cell B does not have Cell A as a neighbour, there is a misconfiguration.

## Languages and requirements
Written in Python and uses Neo4j Graph database to work out the results.


### Prerequisite
* You should have Python 3 (I used version 3.5.4)
* You should have Python packet called beautifulsoup4 installed
* You should have Python packet called neo4j-driver installed
* You should have Neo4j installed and running with an empty database.

## Usage

To use this program you will need to follow these steps:

1. Fetch the adjacent site list to UCS and place in the same folder as the scripts. This file should be called "SSiteAcc.html" which is UCS default filename.
2. Run the script "parseListToCSV.py". This should result in a new file called "accList.csv" in the folder containing comma seperated list of all adjacent settings.
3. Now edit the script "Neo_ImportData.py" and make sure the Neo4j username and password are correct. They are palced in the top of the file.
4. Run the script described in step 3.
5. Open browser to Neo4j web interface and run the following query:
```
MATCH (s1:Site)-[r:ACC]->(s2:Site)
WHERE (s1)-[:ACC]->(s2)
AND NOT (s2)-[:ACC]->(s1)
RETURN s1, r, s2
```
