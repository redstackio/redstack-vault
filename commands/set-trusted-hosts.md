---
id: 00000000-0000-0000-0000-000000000002
name: set-trusted-hosts
type: command
executor: powershell
data: 'Set-Item WSMan:\localhost\Client\TrustedHosts -Value $_TRUSTED_HOSTS -Force'
output: null
created_at: '2023-04-06T03:56:31.140924+00:00'
updated_at: '2023-04-10T20:37:59.190248+00:00'
platforms:
  - Windows
tags:
  - winrm
  - config
verified: true
validated: true
---

# set-trusted-hosts

## Command

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value $_TRUSTED_HOSTS -Force
```

## Description

Configures the attacker's machine to trust specified remote hosts for WinRM connections without Kerberos authentication. Use '*' for all or specific IPs/hosts; run on attacker side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TRUSTED_HOSTS | Comma-separated list of hosts/IPs (e.g., '10.10.10.10' or '*') | Yes |
| -Force | Overwrites without confirmation | Yes |

## Examples

### Basic Usage

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value '10.10.10.10' -Force
```

### All Hosts

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value '*' -Force
```

## Expected Output

WSMan:\localhost\Client\TrustedHosts

$_TRUSTED_HOSTS

## Related

- [[procedures/windows-powershell-remoting-with-pssession]]
- [[commands/enable-powershell-remoting]]
