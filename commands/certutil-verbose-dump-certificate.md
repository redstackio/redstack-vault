---
id: 9c79ed72-b2fb-4149-8b95-d4ab6fa9a005
name: certutil-verbose-dump-certificate
type: command
executor: cmd
data: certutil -v -dump $_CERT_FILE
output: null
created_at: '2023-04-06T03:56:06.176406+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - certificate
  - dump
verified: true
validated: true
---

# certutil-verbose-dump-certificate

## Command

```cmd
certutil -v -dump $_CERT_FILE
```

## Description

Dumps verbose details of a certificate file (PFX or CER) including subject, issuer, serial number, validity dates, and extensions. Used to verify certificate usability for PKINIT attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Verbose output mode | Yes |
| -dump | Dump certificate properties | Yes |
| $_CERT_FILE | Path to the certificate file (e.g., admin.pfx) | Yes |

## Examples

### Basic Usage

```cmd
certutil -v -dump admin.pfx
```

### With Prompt for Password

If PFX is protected, it will prompt; output includes decoded content.

## Expected Output

CertUtil: -dump command completed successfully.

  Certificate:
    Subject: CN=Domain Admin, DC=domain, DC=local
    Issuer: CN=Domain CA, DC=domain, DC=local
    NotBefore: 1/1/2023
    NotAfter: 1/1/2024
    Serial Number: 1234567890abcdef
    ... (full extensions and key info)

## Related

- [[procedures/Pass-The-Certificate-Attack]]
