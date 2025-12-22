---
id: cmd-telnet-smtp-banner
data: telnet target.example.com 25
tags:
  - recon
  - smtp
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.351Z'
verified: false
validated: true
submitted: true
---
# telnet-smtp-banner

## Command

```bash
telnet target.example.com 25
```

## Description

Connects to SMTP port 25 to retrieve the server's welcome banner, revealing Exim version for vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.example.com` | Target hostname | Yes |
| `25` | SMTP port | Yes |

## Examples

### Basic Usage

```bash
telnet mail.example.com 25
```

### Advanced Usage

```bash
telnet -e /dev/null target.example.com 25
```

## Expected Output

Trying 192.168.1.1...
Connected to target.example.com.
Escape character is '^]'.
220 target.example.com ESMTP Exim 4.91

## Related

- [[Related Procedure: Detect-Exim-Vulnerability]]
