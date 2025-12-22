---
data: telnet $target 555
tags:
  - recon
  - connect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.512Z'
id: 96652a54-850a-4c50-b156-8e18267304dc
verified: false
validated: true
submitted: true
---
# telnet-port-check

## Command

```bash
telnet $target 555
```

## Description

Attempts a basic TCP connection to port 555 on the target to verify if the JMX service is responsive and lacks immediate auth barriers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$target` | Domain or IP (e.g., jabber.basecamp.com) | Yes |
| `555` | Port number for JMX | Yes |

## Examples

### Basic Usage

```bash
telnet jabber.37signals.com 555
```

### Advanced Usage

```bash
telnet -c jabber.37signals.com 555
```

## Expected Output

Trying 192.0.2.1...
Connected to jabber.37signals.com.
Escape character is '^]'.
JMXMP [protocol version 1.0]

## Related

- [[Related Procedure: Probe-Exposed-JMX-Server]]
