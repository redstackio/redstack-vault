---
data: >-
  openssl req -x509 -new -nodes -key legit_ca.key -sha256 -days 365 -out
  legit_ca.crt -subj "/CN=Legit CA"
tags:
  - openssl
  - certgen
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.092Z'
id: 336c2b50-f68e-4154-b4e2-461187b2c604
verified: false
validated: true
submitted: true
---
# openssl-req-legit-ca

## Command

```bash
openssl req -x509 -new -nodes -key legit_ca.key -sha256 -days 365 -out legit_ca.crt -subj "/CN=Legit CA"
```

## Description

Creates a self-signed CA certificate for the legitimate authority using the provided key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-x509` | Output self-signed cert | Yes |
| `-new` | New certificate request | Yes |
| `-nodes` | No DES encryption | Yes |
| `-key legit_ca.key` | Input private key | Yes |
| `-sha256` | Signature hash | Yes |
| `-days 365` | Validity period | Yes |
| `-out legit_ca.crt` | Output cert file | Yes |
| `-subj "/CN=Legit CA"` | Subject name | Yes |

## Examples

### Basic Usage

```bash
openssl req -x509 -new -nodes -key legit_ca.key -sha256 -days 365 -out legit_ca.crt -subj "/CN=Legit CA"
```

### Advanced Usage

```bash
openssl req -x509 -new -nodes -key legit_ca.key -sha256 -days 730 -out legit_ca.crt -subj "/CN=Legit CA/O=Org"
```

## Expected Output

CA certificate file created; X.509 PEM format.

## Related

- [[commands/openssl-genrsa-legit-ca]]
