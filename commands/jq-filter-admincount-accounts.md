---
type: command
executor: bash
data: >-
  jq -r '.[] | select(.attributes.adminCount == 1) | .sAMAccountName'
  $_JSON_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - json
  - parsing
  - enumeration
verified: true
validated: true
---

# jq-filter-admincount-accounts

## Command

```bash
jq -r '.[] | select(.attributes.adminCount == 1) | .sAMAccountName' $_JSON_FILE
```

## Description

Parses JSON output from ldapdomaindump to extract sAMAccountNames of objects with adminCount=1.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JSON_FILE | Path to the JSON dump file (e.g., domain_users.json) | Yes |
| .[] | Iterates over array of objects | Built-in |
| select(.attributes.adminCount == 1) | Filters for adminCount=1 | Built-in |
| .sAMAccountName | Extracts the account name | Built-in |

## Examples

### Basic Usage

```bash
jq -r '.[] | select(.attributes.adminCount == 1) | .sAMAccountName' domain_users.json
```

### Advanced Usage

```bash
jq -r '.[] | select(.attributes.adminCount == 1) | ["name", .sAMAccountName] | @csv' domain_users.json
```

## Expected Output

```
adminuser
protectedaccount
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/python-ldapdomaindump-domain-dump]]
