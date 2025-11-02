---
id: 47ef6c68-ea61-45c3-9db9-fe92730bb0e7
name: Neo4j
type: tool
verified: true
created_at: '2020-03-12T21:04:39.211694+00:00'
updated_at: '2023-05-30T01:07:27.396827+00:00'
commands:
- '[[Launch a Neo4j Instance]]'
platforms:
- Linux
- Windows
tags:
- '[[database]]'
---

# Neo4j

**Status**: ✓ Verified

## Overview

High performance graph store with all of the features expected of a mature and robust database. Neo4j works with a flexible network structure of nodes and relationships rather than static tables, but maintains the benefits of enterprise-quality databases. 

## Description

# Description

High performance graph store with all of the features expected of a mature and robust database. Neo4j works with a flexible network structure of nodes and relationships rather than static tables, but maintains the benefits of enterprise-quality databases.



# Installation

## Install on Windows

1. Neo4j requires Java SE 11. [Downlaod Java SE 11 here](https://www.oracle.com/java/technologies/javase-downloads.html)



Note: Oracle requires users sign-up before downloading the Java installer. Alternatively users can avoid the sign-up requirement by downloading and extracting Java 11.0.2 manually. [Download the Java 11.0.2 archive here](https://jdk.java.net/archive/). When manually installing Java, users must add the "JAVA_HOME" System Variable to their Windows Environment Variables, with the Value set to the base directory where Java was copied.





![e0839cab-d485-4bcb-8efc-2227ede2059e.png](_assets/images/data.redstack.io/Mark/e0839cab-d485-4bcb-8efc-2227ede2059e.png)



2. After preparing Java, download Neo4j: [Download Neo4j Community Edition here](https://neo4j.com/download-center/#community)
3. Neo4j can be run by executing either neo4j.bat or neo4j.ps1, both found in "<Neo4j Extracted Dir>/bin", with the "console" argument.



{{EMBEDDED_COMMAND_175bfe2e-780f-4071-abe5-df3af65c86a8}}



4. After launching Neo4j, use a web browser to navigate to: http://localhost:7474 



![51f9c858-e4dd-420c-9f23-d14937468fd5.png](_assets/images/data.redstack.io/Mark/51f9c858-e4dd-420c-9f23-d14937468fd5.png)



5. Use the default credentials of  "neo4j:neo4j" to log in, then change the password to complete the setup.



## Platforms

- Linux
- Windows

## Commands (2)

- [[Launch a Neo4j Instance]]
- [[Launch a Neo4j Instance]]

## Tags

- [[database]]


