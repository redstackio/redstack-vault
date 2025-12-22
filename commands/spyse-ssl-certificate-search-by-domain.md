---
type: command
executor: bash
data: spyse -target $_DOMAIN --ssl-certificates
output: null
created_at: '2023-04-06T03:56:22Z'
updated_at: '2023-04-10T20:25:08Z'
platforms:
  - Linux
  - macOS
tags:
  - osint
  - recon
  - ssl
verified: true
validated: true
---

# spyse-ssl-certificate-search-by-domain

## Command

```bash
spyse -target $_DOMAIN --ssl-certificates
```

## Description

This command uses the Spyse CLI to search for SSL/TLS certificates associated with a specific domain, retrieving details from certificate transparency logs and OSINT sources. Useful for initial reconnaissance to map a target's web infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., example.com) | Yes |
| -target | Specifies the search target | Built-in |
| --ssl-certificates | Filters results to SSL certificate data | Yes |

## Examples

### Basic Usage

```bash
spyse -target hotmail.com --ssl-certificates
```

### With Output Redirection

```bash
spyse -target example.com --ssl-certificates > domain_certs.json
```

## Expected Output

A JSON response with certificate details:

```json
{
  "success": true,
  "data": [
    {
      "id": "cert-123",
      "name": "hotmail.com",
      "issuer": "DigiCert Inc",
      "validity_not_after": "2024-01-01",
      "subjects": ["hotmail.com", "www.hotmail.com"]
    }
  ]
}
```

Success is indicated by "success": true and populated data array. Errors may occur if API quota is exceeded.

## Related

- [[procedures/SSL-Certificate-Discovery-using-Spyse]]
- [[commands/spyse-ssl-certificate-search-by-organization]]
