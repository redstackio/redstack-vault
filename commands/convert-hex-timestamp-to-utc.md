---
data: >-
  print(datetime.datetime.fromtimestamp(int('0x614daecb',16),
  tz=datetime.timezone.utc))
tags:
  - timestamp-conversion
  - bruteforce-aid
type: command
executor: python
platforms:
  - Linux
id: cbc9e8bd-473f-4828-b9b9-018b415c1d2b
created_at: '2025-12-14T17:23:27.972Z'
updated_at: '2025-12-14T17:23:27.972Z'
verified: false
validated: true
submitted: true
---
# convert-hex-timestamp-to-utc

## Command

```python
import datetime
print(datetime.datetime.fromtimestamp(int('0x614daecb',16), tz=datetime.timezone.utc))
```

## Description

Converts the hexadecimal UTC timestamp prefix from uniqid() back to a readable datetime, aiding in predicting temporary directory names for bruteforcing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hex_timestamp` | 8-char hex string (e.g., '0x614daecb') | Yes |

## Examples

### Basic Usage

```python
import datetime
print(datetime.datetime.fromtimestamp(int('0x614daecb',16), tz=datetime.timezone.utc))
```

### Advanced Usage

```python
import datetime
hex_val = '0x' + input('Enter hex: ')
print(datetime.datetime.fromtimestamp(int(hex_val,16), tz=datetime.timezone.utc))
```

## Expected Output

UTC timestamp, e.g., 2021-09-24 10:56:11+00:00.

## Related

- [[Related Procedure: Bruteforce-Temporary-Directory-Location]]
