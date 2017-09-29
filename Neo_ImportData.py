# Neo4j Source site acc data importer
# Gudmundur F Jonsson
# gummi@climbing.is

#Edit the following lines to match the Neo4j username/password
neo_username = 'neo4j'
neo_password = 'neo4j'




# Program data is here below
from neo4j.v1 import GraphDatabase, basic_auth

def insertData(site1, site2, session):
    session.run("MERGE (site:Site {alias: \""+site1+"\"})")
    session.run("MERGE (site2:Site {alias: \""+site2+"\"})")
    session.run("MATCH (site:Site {alias: \""+site1+"\"}), (site2:Site {alias: \""+site2+"\"}) MERGE (site)-[:ACC{Enabled: true}]->(site2)")


driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth(neo_username, neo_password))
session = driver.session()

with open('accList.csv', 'r') as file:
    data = file.read().splitlines()
    for i in data:
        if i == 'Site1,Site2':
            continue
        item = i.split(',')
        insertData(item[0], item[1], session)
        print("Inserting: ["+item[0]+"]->["+item[1]+"]")

session.close()

print("Importing data is done. Check your Neo4j for adjacency list")
