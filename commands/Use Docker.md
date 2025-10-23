---
id: 5216b440-8c3d-43b6-8485-bfbb98e49771
name: Use Docker
type: command
executor: bash
data: docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j
output: null
created_at: '2023-04-06T03:56:02.119821+00:00'
updated_at: '2023-04-10T20:26:14.196507+00:00'
---

# Use Docker

```bash
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j
```


