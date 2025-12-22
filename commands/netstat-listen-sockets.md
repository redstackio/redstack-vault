---
data: 'netstat -an | egrep ''LISTEN[^I]'''
tags:
  - recon
  - network
type: command
output: |-
  tcp 0 0 0.0.0.0:5000 0.0.0.0:* LISTEN
  tcp 0 0 :::5000 :::* LISTEN
executor: bash
platforms:
  - Linux
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.458Z'
id: 7d53e98a-871a-4a2e-9082-ad1f638f0601
verified: false
validated: true
submitted: true
---
# netstat-listen-sockets

## Command

```bash
netstat -an | egrep 'LISTEN[^I]'
```

## Description

Lists all listening TCP/UDP sockets on the system, filtering for those in LISTEN state and excluding lines with 'I' (to avoid irrelevant outputs like ICMP), useful for identifying exposed services like the Shopify PoS WebSocket on port 5000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-an` | Displays all sockets numerically without name resolution | Yes |
| `| egrep 'LISTEN[^I]'` | Pipes to grep for listening sockets not containing 'I' | Yes |

## Examples

### Basic Usage

```bash
netstat -an | egrep 'LISTEN[^I]'
```

### Advanced Usage

```bash
netstat -an | egrep 'LISTEN[^I]' | grep :5000
```

## Expected Output

Lines like: tcp 0 0 0.0.0.0:5000 0.0.0.0:* LISTEN, tcp 0 0 :::5000 :::* LISTEN, confirming binding to all interfaces on port 5000.

## Related

- [[Related Command: ss-listen]]
- [[Related Procedure: Analyze-PoS-App-WebSocket-Server-Configuration]]
