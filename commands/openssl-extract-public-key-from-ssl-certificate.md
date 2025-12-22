---
type: command
executor: bash
data: 'openssl s_client -connect $_TARGET_HOST:443 | openssl x509 -pubkey -noout'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - openssl
  - tls
  - certificate
  - recon
verified: true
validated: true
---

# openssl-extract-public-key-from-ssl-certificate

## Command

```bash
openssl s_client -connect $_TARGET_HOST:443 | openssl x509 -pubkey -noout
```

## Description

Connects to the target's HTTPS port, retrieves the TLS certificate, and extracts the RSA public key in PEM format for use in JWT key confusion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_HOST` | Domain or IP of the target server | Yes |
| `:443` | Standard HTTPS port | Yes |

## Examples

### Basic Usage

```bash
openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout
```

### Save to File

```bash
openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout > public.pem
```

## Expected Output

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
-----END PUBLIC KEY-----

## Related

- [[procedures/JWT-Key-Confusion-Attack-RS256-to-HS256]]
