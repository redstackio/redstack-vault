---
data: openssl x509 -in node.crt -text -noout
tags:
  - openssl
  - certificate
type: command
executor: bash
platforms:
  - Linux
id: 1c06c576-fb62-4318-9c9e-039035d17ef8
created_at: '2025-12-13T09:00:27.276Z'
updated_at: '2025-12-13T09:00:27.276Z'
verified: false
validated: true
submitted: true
---
# openssl-x509

## Command

```bash
openssl x509 -in node.crt -text -noout
```

## Description

Extracts and displays textual information from a certificate file, used to analyze leaked certificates in security exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `x509` | Certificate display utility | Yes |
| `-in node.crt` | Input certificate file | Yes |
| `-text` | Print certificate in text form | Yes |
| `-noout` | Do not output encoded certificate | Yes |

## Examples

### Basic Usage

```bash
openssl x509 -in node.crt -text -noout
```

## Expected Output

Certificate details including issuer, validity, subject, public key, and extensions.

## Related

- [[procedures/Analyze-Leaked-Certificates]]
