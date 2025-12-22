---
type: command
executor: bash
data: >-
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
  -nodes
output: null
platforms:
  - Linux
tags:
  - openssl
  - certificate
verified: true
validated: true
---

# openssl-generate-self-signed-cert

## Command

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

## Description

Generates a self-signed X.509 certificate and private key for use in SSL/TLS servers, ideal for quick setups in testing or reverse shell listeners without public CA involvement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -x509 | Output a self-signed certificate instead of CSR | Yes |
| -newkey rsa:4096 | Generate a new 4096-bit RSA private key | Yes |
| -keyout key.pem | Output file for the private key | Yes |
| -out cert.pem | Output file for the certificate | Yes |
| -days 365 | Certificate validity in days | No (default 30) |
| -nodes | Do not encrypt the private key | No |

## Examples

### Basic Usage

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

Prompts for subject details (e.g., country, organization).

### Advanced Usage

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=attacker.local"
```

Non-interactive with subject specified.

## Expected Output

Interactive prompts for certificate details, followed by:

```
writing new private key to 'key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
(... prompts ...)
writing RSA key
Signature ok
certificate request completed
-----BEGIN CERTIFICATE-----
(... base64 cert ...)
-----END CERTIFICATE-----
```

Files key.pem and cert.pem are created.

## Related

- [[commands/openssl-start-server-with-cert]]
- [[procedures/openssl-reverse-shell]]
