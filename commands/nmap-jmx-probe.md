---
data: nmap -p 555 --script=jmx-info $target
tags:
  - recon
  - scan
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.522Z'
id: 23f0ee9a-98b6-4d9b-a602-00e6c35ee88e
verified: false
validated: true
submitted: true
---
# nmap-jmx-probe

## Command

```bash
nmap -p 555 --script=jmx-info $target
```

## Description

Scans a specific target for an open JMX port 555 and extracts service information using nmap's jmx-info script, useful for detecting exposed Java management interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 555` | Specifies port 555 to scan | Yes |
| `--script=jmx-info` | Runs the JMX info NSE script | Yes |
| `$target` | Domain or IP to probe (e.g., jabber.37signals.com) | Yes |

## Examples

### Basic Usage

```bash
nmap -p 555 --script=jmx-info jabber.37signals.com
```

### Advanced Usage

```bash
nmap -p 555 --script=jmx-info -sV jabber.37signals.com
```

## Expected Output

PORT    STATE SERVICE
555/tcp open  unknown
| jmx-info: 
|   JMX service detected
|   Java Version: 1.8.0
|_  Authentication: None

## Related

- [[Related Procedure: Probe-Exposed-JMX-Server]]
