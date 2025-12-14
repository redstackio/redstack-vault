---
data: >-
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days
  1 -nodes -subj
  "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
tags:
  - certificate
  - openssl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.027Z'
id: c9fc0410-d862-485f-bac3-45358d009d5e
verified: false
validated: true
submitted: true
---
# openssl-generate-cert

## Command

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 1 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
```

## Description

Generates self-signed cert and key for HTTPS server in curl vuln repro.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -x509 | Self-signed | Yes |
| -newkey rsa:4096 | RSA key size | Yes |
| -keyout key.pem | Key output | Yes |
| -out cert.pem | Cert output | Yes |
| -sha256 | Hash algo | Yes |
| -days 1 | Validity | Yes |
| -nodes | No passphrase | Yes |
| -subj | DN string | Yes |

## Examples

### Basic Usage

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 1 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
```

## Expected Output

Generating key... writing cert and key files.

## Related

- [[procedures/Generate-Self-Signed-Certificate-for-HTTPS-Server]]
- [[commands/python3-server-py]]
