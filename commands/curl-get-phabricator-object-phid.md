---
id: cmd-uuid-3
data: >-
  curl -X GET 'https://phabricator.example.com/T123' -H 'Cookie:
  session=authenticated' | grep -o 'PHID-[A-Z]*-[a-z0-9]*'
tags:
  - phid-extract
  - html-parse
  - phabricator
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.053Z'
verified: false
validated: true
submitted: true
---
# curl-get-phabricator-object-phid

## Command

```bash
curl -X GET 'https://phabricator.example.com/T123' \
  -H 'Cookie: session=authenticated' | grep -o 'PHID-[A-Z]*-[a-z0-9]*'
```

## Description

Fetches a Phabricator task page and greps for PHID patterns in HTML to extract object references.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `-H 'Cookie: ...'` | Authentication cookie | Yes |
| `| grep ...` | Pattern match for PHIDs | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://phabricator.example.com/T123' -H 'Cookie: session=authenticated' | grep -o 'PHID-[A-Z]*-[a-z0-9]*'
```

### Advanced Usage

```bash
curl -X GET 'https://phabricator.example.com/T123' -H 'Cookie: session=authenticated' | grep -o 'PHID-PROJ-[a-z0-9]*'
```

## Expected Output

PHID-PROJ-def456
PHID-TASK-ghi789

## Related

- [[Related Procedure]]
