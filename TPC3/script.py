import json

with open("mapa_virtual.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise

ttl = f"""@prefix : <http://rpcw.di.uminho.pt/2024/mapaVirtual/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/mapaVirtual/> .

<http://rpcw.di.uminho.pt/2024/mapaVirtual> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .


#################################################################
#    Object Properties
#################################################################

###  http://www.rpcw.di.uminho.pt/2024/mapaVirtual#origem
:origem rdf:type owl:ObjectProperty ;
        rdfs:domain :Ligacao ;
        rdfs:range :Cidade ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .

###  http://www.rpcw.di.uminho.pt/2024/mapaVirtual#destino
:destino rdf:type owl:ObjectProperty ;
        rdfs:domain :Ligacao ;
        rdfs:range :Cidade ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .


#################################################################
#    Data properties
#################################################################

### http://www.rpcw.di.uminho.pt/2024/mapaVirtual#id
:id rdf:type owl:DatatypeProperty ;
        rdfs:domain :Cidade ,
                :Ligacao ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .

### http://www.rpcw.di.uminho.pt/2024/mapaVirtual#nome
:nome rdf:type owl:DatatypeProperty ;
        rdfs:domain :Cidade ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .

###  http://rpcw.di.uminho.pt/2024/mapa-virtual#populacao
:populacao rdf:type owl:DatatypeProperty ;
        rdfs:domain :Cidade ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .

###  http://www.rpcw.di.uminho.pt/2024/mapaVirtual#descricao
:descricao rdf:type owl:DatatypeProperty ;
        rdfs:domain :Cidade ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .

###  http://rpcw.di.uminho.pt/2024/mapa-virtual#distancia
:distancia rdf:type owl:DatatypeProperty ;
        rdfs:domain :ligacao ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .


#################################################################
#    Classes
#################################################################

###  http://www.rpcw.di.uminho.pt/2024/mapaVirtual#Cidade
:Cidade rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .

###  http://www.rpcw.di.uminho.pt/2024/mapaVirtual#Ligacao
:Ligacao rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "JoanaP02" .


#################################################################
#    Individuals
#################################################################

"""

for Cidade in bd["cidades"]:
        ttl += f"""
###  http://rpcw.di.uminho.pt/2024/mapa-virtual#{Cidade["id"]}
:{Cidade["id"]} rdf:type owl:NamedIndividual ,
        :Cidade ;
        :descricao "{Cidade["descrição"]}" ;
        :distrito "{Cidade["distrito"]}" ;
        :id "{Cidade["id"]}" ;
        :nome "{Cidade["nome"]}" ;
        :populacao {Cidade["população"]} .
"""

for Ligacao in bd["ligacoes"]:
        ttl+=f"""
###  http://rpcw.di.uminho.pt/2024/mapa-virtual#{Ligacao["id"]}
:{Ligacao["id"]} rdf:type owl:NamedIndividual ,
        :ligacao ;
        :destino :{Ligacao["destino"]} ;
        :origem :{Ligacao["origem"]} ;
        :distancia {Ligacao["distância"]} ;
        :id "{Ligacao["id"]}" .

"""

# Salve o conteúdo TTL em um arquivo
with open("mapaVirtual.ttl", "w", encoding="utf-8") as output_file:
        output_file.write(ttl)

print("Conteúdo guardado.")

