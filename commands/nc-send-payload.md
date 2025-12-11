---
data: nc $PS4IP 1337 < payload.bin
tags:
  - network
  - payload-delivery
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 675c0b8c-7198-41f4-84a8-af9618b2961a
created_at: '2025-12-11T03:47:57.253Z'
updated_at: '2025-12-11T03:47:57.253Z'
verified: false
validated: true
submitted: true
---
# nc-send-payload

## Command

```bash
nc $PS4IP 1337 < payload.bin
```

## Description

This command uses netcat to send a binary payload file to a PS4 or PS5 over the network on port 1337, triggering the exploit chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$PS4IP` | IP address of the PS4/PS5 | Yes |
| `1337` | Port to connect to | Yes |
| `< payload.bin` | Redirect payload file as input | Yes |

## Examples

### Basic Usage

```bash
nc 192.168.1.100 1337 < payload.bin
```

### Advanced Usage

```bash
nc -v $PS4IP 1337 < payload.bin
```

## Expected Output

Connection established, payload sent, resulting in exploit execution and potential kernel panic on the target.

## Related

- [[procedures/Trigger-Buffer-Overflow-in-UDF-Driver]]
- [[procedures/Burn-and-Load-Exploit-ISO]]
