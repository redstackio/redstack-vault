---
data: python3 payload.py | nc localhost 8080
tags:
  - python
  - nc
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: 26a7f031-291a-45e9-8940-79a860ee7faf
created_at: '2025-12-13T09:01:17.086Z'
updated_at: '2025-12-13T09:01:17.086Z'
verified: false
validated: true
submitted: true
---
# python3-payload-nc

## Command

```bash
python3 payload.py | nc localhost 8080
```

## Description

Runs a Python script to generate a smuggling payload and pipes it to netcat for sending to the ATS proxy on port 8080.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `payload.py` | Script generating the smuggled request | Yes |
| `localhost 8080` | Target host and port | Yes |

## Examples

### Basic Usage

```bash
python3 payload.py | nc localhost 8080
```

## Expected Output

Prints '/admin was reached!' in terminal, indicating successful smuggling.

## Related

- [[procedures/Execute-HTTP-Request-Smuggling-Attack-via-Chunk-Extension]]
- [[tools/python3]]
- [[tools/nc]]
