---
data: >-
  curl -s -X POST https://hackerone.com/[program-handle]/saml/metadata -d
  'query=enumerate' --header 'Content-Type: application/xml'
tags:
  - web
  - request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6ad911cb-afbb-49aa-a626-8ca529c86905
created_at: '2025-12-13T09:01:26.533Z'
updated_at: '2025-12-13T09:01:26.533Z'
verified: false
validated: true
submitted: true
---
# Curl SAML Request

## Command

```bash
curl -s -X POST https://hackerone.com/[program-handle]/saml/metadata -d 'query=enumerate' --header 'Content-Type: application/xml'
```

## Description

This command sends a POST request to a SAML metadata endpoint to probe for enumeration vulnerabilities, useful in reconnaissance against web services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | No |
| `-X POST` | Specify POST method | Yes |
| `-d 'query=enumerate'` | Data payload for enumeration | Yes |
| `--header 'Content-Type: application/xml'` | Set XML content type | Yes |

## Examples

### Basic Usage

```bash
curl -s https://hackerone.com/example/saml/metadata -I
```

### Advanced Usage

```bash
curl -s -X POST https://hackerone.com/example/saml/metadata -d 'query=enumerate' --header 'Content-Type: application/xml' -o response.xml
```

## Expected Output

XML or text response containing potential leaked SAML entity information.

## Related

- [[procedures/Exploit-SAML-Enumeration-Vulnerability]]
- [[procedures/Identify-Target-HackerOne-Programs]]
