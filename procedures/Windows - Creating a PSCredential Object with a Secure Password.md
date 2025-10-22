---
id: 0342282d-a959-4d9d-a521-a6c2f747eb85
name: Windows - Creating a PSCredential Object with a Secure Password
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.116096+00:00'
updated_at: '2023-04-10T20:38:05.416903+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[Powershell Credentials]]'
- '[[Powershell Remoting Protocol]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Create new PSCredential object]]'
---

# Windows - Creating a PSCredential Object with a Secure Password

## Summary

This procedure involves creating a new PSCredential object with a secure password for use in Powershell Remoting Protocol. This can be useful for maintaining security when using remote commands in Powershell. The PSCredential object can be used to authenticate with remote systems and run commands w

## Description

# Description

This procedure involves creating a new PSCredential object with a secure password for use in Powershell Remoting Protocol. This can be useful for maintaining security when using remote commands in Powershell. The PSCredential object can be used to authenticate with remote systems and run commands without having to enter a password each time. From an offensive perspective, this can be used to maintain persistence and execute commands on remote systems without being detected.

To create a new PSCredential object, the 'New-Object' cmdlet is used with the 'System.Management.Automation.PSCredential' class. The 'Get-Credential' cmdlet is used to prompt the user for a username and password, which is then securely stored in the PSCredential object. This object can then be used with the 'Invoke-Command' cmdlet to remotely execute commands on a target system.

The business value of this procedure is that it allows for secure remote management of systems without the need for manual authentication each time. This can save time and increase efficiency for IT administrators.

## Requirements

1. Access to Powershell Remoting Protocol

1. Ability to create and store a secure password

1. Permission to remotely execute commands on target systems

## Defense

1. Use strong and unique passwords for all accounts

1. Encrypt stored credentials using Windows Credential Manager or a similar tool

1. Monitor for suspicious activity and unauthorized access to remote systems

## Objectives

1. Create a new PSCredential object with a secure password

1. Authenticate with remote systems using the PSCredential object

1. Remotely execute commands on target systems using the PSCredential object

# Instructions

1. To create a new PSCredential object with a secure password, follow the steps below:
1. Use the ConvertTo-SecureString cmdlet to convert the password to a secure string. Example: $pass = ConvertTo-SecureString 'supersecurepassword' -AsPlainText -Force
2. Use the New-Object cmdlet to create a new PSCredential object. Example: $cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\Username', $pass)

**Code**: [[PS> $pass = ConvertTo-SecureString 'supersecurepas]]

> The ConvertTo-SecureString cmdlet converts a plain text password to a secure string. The -AsPlainText parameter specifies that the input is a plain text password. The -Force parameter forces the conversion even if the input string is not considered secure. The resulting secure string can be used to create a secure PSCredential object.
The New-Object cmdlet creates a new instance of a .NET object. In this case, it creates a new PSCredential object with the specified username and secure password.

**Command** ([[Create new PSCredential object]]):

```bash
$pass = ConvertTo-SecureString 'supersecurepassword' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\Username', $pass)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials in Files|T1081 - Credentials in Files]]

## Commands Used

- [[Create new PSCredential object]]

## Tags

- [[Powershell Credentials]]
- [[Powershell Remoting Protocol]]
- [[Windows - Using credentials]]
