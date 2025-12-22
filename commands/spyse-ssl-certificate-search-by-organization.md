---
type: command
executor: bash
data: 'spyse -target "org: $_ORGANIZATION" --ssl-certificates'
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

# spyse-ssl-certificate-search-by-organization

## Command

```bash
spyse -target "org: $_ORGANIZATION" --ssl-certificates
```

## Description

This command queries Spyse for all SSL/TLS certificates linked to a specific organization, providing a broad view of corporate infrastructure. Ideal for discovering assets across multiple domains owned by the organization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ORGANIZATION | Target organization name (e.g., Microsoft) | Yes |
| -target | Specifies the search target with 'org:' prefix | Built-in |
| --ssl-certificates | Limits results to certificate information | Yes |

## Examples

### Basic Usage

```bash
spyse -target "org: Microsoft" --ssl-certificates
```

### Paginated Search

```bash
spyse -target "org: Microsoft" --ssl-certificates --page 2
```

## Expected Output

JSON array of organization certificates:

```json
{
  "success": true,
  "data": [
    {
      "id": "cert-456",
      "name": "microsoft.com",
      "issuer": "Sectigo",
      "validity_not_after": "2025-06-15",
      "subjects": ["*.microsoft.com", "azure.com"]
    }
  ],
  "total": 1500
}
```

Look for high 'total' counts indicating extensive infrastructure. Handle large outputs by piping to tools like jq.

## Related

- [[procedures/SSL-Certificate-Discovery-using-Spyse]]
- [[commands/spyse-ssl-certificate-search-by-domain]]
