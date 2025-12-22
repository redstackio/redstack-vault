---
id: 5216b440-8c3d-43b6-8485-bfbb98e49771
name: start-neo4j-with-docker
type: command
executor: bash
data: 'docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j'
output: null
created_at: '2023-04-06T03:56:02.119821+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - setup
  - db
  - docker
verified: true
validated: true
---

# start-neo4j-with-docker

## Command

```bash
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j
```

## Description

Runs Neo4j container for BloodHound with exposed ports and default auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p7474:7474 | Map HTTP port | Yes |
| -p7687:7687 | Map Bolt port | Yes |
| -e NEO4J_AUTH | Set username/password | Yes |
| neo4j | Image name | Yes |

## Examples

### Basic Usage

```bash
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j
```

## Expected Output

Container logs: "Started neo4j (bolt://0.0.0.0:7687, http://0.0.0.0:7474)".

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/Neo4j]]
