---
id: cmd-uuid-5
data: 'netstat -an | grep :3000 | wc -l'
tags:
  - monitor
  - connections
type: command
output: '100'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.652Z'
verified: false
validated: true
submitted: true
---
# netstat-connections

## Command

```bash
netstat -an | grep :3000 | wc -l
```

## Description

Counts active connections to a port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-an` | Numeric, all connections | Yes |
| `grep :3000` | Filter for port | Yes |
| `wc -l` | Line count | Yes |

## Examples

### Basic Usage

```bash
netstat -an | grep :3000 | wc -l
```

## Expected Output

Integer count of connections.

## Related

- [[procedures/Establish-Multiple-HTTP2-Connections]]
