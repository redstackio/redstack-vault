---
id: a8fa27bb-c9c1-4802-a4b6-7bb82ea7d9dd
name: sstimap-interactive-auth-scan
type: command
executor: bash
data: >-
  python3 ./sstimap.py -i -A -m POST -l 5 -H 'Authorization: Basic
  bG9naW46c2VjcmV0X3Bhc3N3b3Jk'
output: null
created_at: '2023-04-06T03:56:38.834603+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssti
  - auth
verified: true
validated: true
---

# sstimap-interactive-auth-scan

## Command

```bash
python3 ./sstimap.py -i -A -m POST -l 5 -H 'Authorization: Basic bG9naW46c2VjcmV0X3Bhc3N3b3Jk'
```

## Description

Conducts an interactive SSTI scan with all plugins enabled, using POST method and authentication headers for protected endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Enable interactive mode for manual payload selection | Yes |
| -A | Activate all plugins | Yes |
| -m POST | Use POST HTTP method | Yes |
| -l 5 | Scan level 5 | Yes |
| -H | Custom headers (e.g., Authorization) | Yes |

## Examples

### Basic Usage

```bash
python3 ./sstimap.py -i -A -m POST -l 5 -H 'Authorization: Basic bG9naW46c2VjcmV0X3Bhc3N3b3Jk'
```

## Expected Output

Interactive prompts and results like:
```
[i] Select payload: 1
[+] Vulnerability confirmed in POST body.
```

## Related

- [[procedures/Exploit-Server-Side-Template-Injection-with-tplmap-and-sstimap]]
- [[tools/sstimap]]
