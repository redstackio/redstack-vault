---
id: fc06df80-d482-4e7b-9d97-0d0ad735630a
name: start-neo4j-console
type: command
executor: bash
data: neo4j console
output: null
created_at: '2023-04-06T03:56:02.119749+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - setup
  - db
verified: true
validated: true
---

# start-neo4j-console

## Command

```bash
neo4j console
```

## Description

Starts Neo4j database in console mode for BloodHound backend.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| neo4j | Database executable | Built-in |
| console | Run in foreground | Yes |

## Examples

### Basic Usage

```bash
neo4j console
```

## Expected Output

Logs showing "Neo4j 5.x.x is running" and ports 7474/7687 listening.

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/Neo4j]]
