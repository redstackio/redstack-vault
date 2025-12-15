---
id: cmd-sudo-tail-logs
data: sudo tail -f /var/log/messages
tags:
  - monitoring
  - logs
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.584Z'
verified: false
validated: true
submitted: true
---
# sudo-tail-log-messages

## Command

```bash
sudo tail -f /var/log/messages
```

## Description

Monitors the system log file in real-time to capture DNS queries or other events on a Linux-based DNS server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Run with elevated privileges | Yes (for log access) |
| -f | Follow the file continuously | Yes |
| /var/log/messages | Path to system log | Yes |

## Examples

### Basic Usage

```bash
sudo tail -f /var/log/messages
```

## Expected Output

Real-time log lines, e.g., 'Jul 22 00:10:00 server named[7356]: client 180.179.199.50: query: mealstest.demonsec.us IN A -EDC (10.0.5.200)'.

## Related

- [[Related Procedure: Demonstrate Network Interaction with Nslookup Payload]]
