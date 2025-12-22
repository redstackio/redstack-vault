---
id: 3537d03c-00fe-4a35-a234-29c4bf6116e4
name: BloodHound-Setup-and-Launch-Sequence
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:02.119593+00:00'
updated_at: '2023-10-10T20:26:14.194807+00:00'
platforms:
  - Linux
tags:
  - setup
  - ad
validated: true
---

# BloodHound-Setup-and-Launch-Sequence

## Code

```bash
root@payload$ apt install bloodhound 

# start BloodHound and the database
root@payload$ neo4j console
# or use docker
root@payload$ docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j

root@payload$ ./bloodhound --no-sandbox
Go to http://127.0.0.1:7474, use db:bolt://localhost:7687, user:neo4J, pass:neo4j
```

## Description

Step-by-step commands to install, start Neo4j backend, and launch BloodHound for AD data analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| root@payload$ | Shell prompt | root@kali# |
| neo4j/bloodhound | Default auth | neo4j/bloodhound |
| bolt://localhost:7687 | DB connection | bolt://localhost:7687 |

## Usage

Run on assessment machine to set up BloodHound environment before importing recon data.

## Detection

- Neo4j service startup on non-standard hosts
- Docker containers with neo4j image
- BloodHound process with --no-sandbox flag

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/BloodHound]]
