---
id: aec19f9e-2f13-40f0-b2ec-71cc71654f2f
name: driverquery-custom-enumerate-non-msft-drivers
type: command
executor: cmd
data: DriverQuery.exe --no-msft
output: null
created_at: '2023-04-06T03:56:29.800552+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - drivers
  - signatures
verified: true
validated: true
---

# driverquery-custom-enumerate-non-msft-drivers

## Command

```cmd
DriverQuery.exe --no-msft
```

## Description

This command runs the custom DriverQuery.exe tool (from OffensiveCSharp) to enumerate Windows driver services, check file signatures, and exclude Microsoft drivers. It provides detailed info for identifying vulnerable third-party drivers during privilege escalation assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --no-msft | Excludes Microsoft-signed drivers from output | Yes |

## Examples

### Basic Usage

```cmd
DriverQuery.exe --no-msft
```

### With Output Redirection

```cmd
DriverQuery.exe --no-msft > non_msft_drivers.txt
```

## Expected Output

```
[+] Enumerating driver services...
[+] Checking file signatures...
Citrix USB Filter Driver
    Service Name: ctxusbm
    Path: C:\Windows\system32\DRIVERS\ctxusbm.sys
    Version: 14.11.0.138
    Creation Time (UTC): 17/05/2018 01:20:50
    Cert Issuer: CN=Symantec Class 3 SHA256 Code Signing CA, OU=Symantec Trust Network, O=Symantec Corporation, C=US
    Signer: CN="Citrix Systems, Inc.", OU=XenApp(ClientSHA256), O="Citrix Systems, Inc.", L=Fort Lauderdale, S=Florida, C=US
<SNIP>
```

Detailed per-driver info; unsigned or outdated entries signal potential vulns.

## Related

- [[procedures/windows-privilege-escalation-evaluating-vulnerable-drivers]]
- [[tools/OffensiveCSharp-DriverQuery]]
