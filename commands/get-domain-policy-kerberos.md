---
id: 0adbc0e3-b159-4250-8f1f-918fdb06c9b7
type: command
executor: powershell
data: (Get-DomainPolicy).\"kerberos policy\"
output: null
created_at: '2023-04-06T03:56:02.228593+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Kerberos Policy Configuration

## Command

```powershell
(Get-DomainPolicy)."kerberos policy"
```

## Description

Retrieves Kerberos policy settings from the domain policy to identify potential weaknesses in ticket lifetimes or pre-auth requirements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses output from Get-DomainPolicy | No |

## Examples

### Basic Usage

```powershell
(Get-DomainPolicy)."kerberos policy"
```

## Expected Output

Hashtable including 'MaxTicketAge', 'MaxRenewAge', etc.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
