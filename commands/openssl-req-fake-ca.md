---
data: >-
  openssl req -x509 -new -nodes -key fake_ca.key -sha256 -days 365 -out
  fake_ca.crt -subj "/CN=Fake CA"
tags:
  - openssl
  - certgen
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.069Z'
id: 1c5ebc40-f3b4-4c1b-a73b-7febfcc150db
verified: false
validated: true
submitted: true
---
# openssl-req-fake-ca

## Command

```bash
openssl req -x509 -new -nodes -key fake_ca.key -sha256 -days 365 -out fake_ca.crt -subj "/CN=Fake CA"
```

## Description

Creates a self-signed CA certificate for the fake authority.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-x509` | Output self-signed cert | Yes |
| `-new` | New certificate request | Yes |
| `-nodes` | No DES encryption | Yes |
| `-key fake_ca.key` | Input private key | Yes |
| `-sha256` | Signature hash | Yes |
| `-days 365` | Validity period | Yes |
| `-out fake_ca.crt` | Output cert file | Yes |
| `-subj "/CN=Fake CA"` | Subject name | Yes |

## Examples

### Basic Usage

```bash
openssl req -x509 -new -nodes -key fake_ca.key -sha256 -days 365 -out fake_ca.crt -subj "/CN=Fake CA"
```

### Advanced Usage

```bash
openssl req -x509 -new -nodes -key fake_ca.key -sha256 -days 365 -out fake_ca.crt -subj "/CN=Fake CA/O=FakeOrg"
```

## Expected Output

CA certificate file created.

## Related

- [[commands/openssl-genrsa-fake-ca]]
