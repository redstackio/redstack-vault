---
data: aapt dump badging zomato.apk | grep -A 10 "activity"
tags:
  - aapt
  - manifest-analysis
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.214Z'
id: 7e8a8323-ce45-4fc4-aef3-11cfefa7c23a
verified: false
validated: true
submitted: true
---
# aapt-dump-badging

## Command

```bash
aapt dump badging zomato.apk | grep -A 10 "activity"
```

## Description

Dumps the badging info (manifest) from an APK and filters for activity declarations to identify exported components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `dump badging` | Extracts manifest data | Yes |
| `zomato.apk` | Input APK file | Yes |
| `grep -A 10 "activity"` | Filters activities with context | Yes |

## Examples

### Basic Usage

```bash
aapt dump badging zomato.apk | grep -A 10 "activity"
```

### Advanced Usage

```bash
aapt dump badging zomato.apk > manifest.txt && grep exported manifest.txt
```

## Expected Output

Activity lines with attributes like exported='true' for vulnerable components.

## Related

- [[Related Procedure]]
