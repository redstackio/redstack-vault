---
id: cmd-uuid-17
data: echo -n "mrgrinch463127.0.0.1" | md5sum
tags:
  - hashing
type: command
output: 3e3f8df1658372edf0214e202acb460b
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.595Z'
verified: false
validated: true
submitted: true
---
# Echo Md5 Payload Hash

## Command

```bash
echo -n "mrgrinch463127.0.0.1" | md5sum
```

## Description

Generates MD5 hash for salt + target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No newline | No |
| Input | Salt+target | Yes |

## Examples

### Basic Usage

```bash
echo -n 'input' | md5sum
```

## Expected Output

Hex hash.

## Related

- [[procedures/Brute-Force-Salt-and-DNS-Rebinding-for-DDoS-Bypass]]
