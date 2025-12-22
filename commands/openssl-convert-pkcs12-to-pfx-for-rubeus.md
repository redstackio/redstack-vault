---
id: 3176843c-b3b9-4468-b0e0-90fd5608c427
name: openssl-convert-pkcs12-to-pfx-for-rubeus
type: command
executor: bash
data: >-
  openssl pkcs12 -in $_INPUT_PEM -keyex -CSP "$_CSP_NAME" -export -out
  $_OUTPUT_PFX
output: null
created_at: '2023-04-06T03:56:28.361239+00:00'
updated_at: '2023-04-10T20:37:28.980808+00:00'
platforms:
  - Linux
  - Windows
tags:
  - certificate-conversion
  - pkcs12
verified: true
validated: true
---

# openssl-convert-pkcs12-to-pfx-for-rubeus

## Command

```bash
openssl pkcs12 -in $_INPUT_PEM -keyex -CSP "$_CSP_NAME" -export -out $_OUTPUT_PFX
```

## Description

This command converts a PEM-formatted certificate and key into a password-protected PFX file using OpenSSL, specifying a Windows-compatible Cryptographic Service Provider (CSP). It is essential for preparing certificates obtained via tools like Certify for use in Windows Kerberos tools like Rubeus.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_PEM | Input PEM file containing certificate and key (e.g., cert.pem) | Yes |
| -keyex | Export key exchangeable | Built-in |
| $_CSP_NAME | CSP for Windows compatibility (e.g., "Microsoft Enhanced Cryptographic Provider v1.0") | Yes |
| -export | Flag to export as PFX | Built-in |
| $_OUTPUT_PFX | Output PFX file path (e.g., cert.pfx) | Yes |

## Examples

### Basic Usage

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```

### Advanced Usage

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx -passout pass:Passw0rd123!
```

## Expected Output

Prompts for export password, then:

```
Enter Export Password:
Verifying - Enter Export Password:
MAC verified OK
```

The PFX file is created without errors.

## Related

- [[procedures/Request-User-Certificate-and-TGT-for-Domain-Persistence]]
- [[commands/certify-request-user-certificate]]
