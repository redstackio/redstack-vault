---
type: command
executor: bash
data: 'openssl s_client -connect $_REGISTRY_HOST:$_REGISTRY_PORT -showcerts'
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

# openssl-sclient-connect-registry

## Command

```bash
openssl s_client -connect $_REGISTRY_HOST:$_REGISTRY_PORT -showcerts
```

## Description

Establishes a TLS connection to the Docker registry and displays the certificate chain for fingerprinting and verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGISTRY_HOST | Hostname or IP of the registry | Yes |
| $_REGISTRY_PORT | Port (e.g., 443 for HTTPS, 5000 for HTTP) | Yes |
| -showcerts | Displays full certificate chain | No |

## Examples

### Basic Usage

```bash
openssl s_client -connect registry.example.com:443 -showcerts
```

### With Specific Host

```bash
openssl s_client -connect 192.168.1.100:5000 -showcerts
```

## Expected Output

Outputs connection details, including:

```
Certificate chain
 0 s:/CN=registry.example.com
   i:/CN=registry.example.com
-----BEGIN CERTIFICATE-----
MIID... (base64 cert data)
-----END CERTIFICATE-----
```

Copy the cert for further analysis. Errors if connection refused or no TLS.

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
- [[commands/openssl-x509-fingerprint]]
