---
type: command
executor: bash
data: openssl x509 -in $_CERT_FILE -noout -fingerprint -sha1
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - fingerprint
  - tls
verified: true
validated: true
---

# openssl-x509-fingerprint

## Command

```bash
openssl x509 -in $_CERT_FILE -noout -fingerprint -sha1
```

## Description

Computes the SHA1 fingerprint of a provided X.509 certificate file to uniquely identify the registry's TLS cert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CERT_FILE | Path to the certificate file (e.g., cert.pem) | Yes |
| -noout | Suppresses output of the encoded version of the certificate | No |
| -fingerprint | Outputs the certificate fingerprint | No |
| -sha1 | Uses SHA1 algorithm (default) | No |

## Examples

### Basic Usage

```bash
openssl x509 -in cert.pem -noout -fingerprint -sha1
```

## Expected Output

```
SHA1 Fingerprint=12:34:56:78:9A:BC:DE:F0:12:34:56:78:9A:BC:DE:F0:12:34:56:78
```

A 40-character hex string. Mismatches indicate tampering or wrong cert.

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
- [[commands/openssl-sclient-connect-registry]]
