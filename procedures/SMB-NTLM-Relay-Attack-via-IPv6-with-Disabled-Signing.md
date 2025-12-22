---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.475202+00:00'
updated_at: '2023-04-10T20:25:58.216889+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Use-Alternate-Authentication-Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques: []
tags:
  - '[[tags/Active-Directory-Attacks]]'
  - '[[tags/Man-in-the-Middle-attacks-relaying]]'
  - '[[tags/SMB-Signing-Disabled-and-IPv6]]'
commands:
  - '[[commands/crackmapexec-generate-smb-relay-list]]'
  - '[[commands/mitm6-ipv6-dns-takeover]]'
  - '[[commands/impacket-ntlmrelayx-spoof-wpad-relay-to-loot]]'
  - '[[commands/impacket-ntlmrelayx-create-socks-proxy]]'
  - '[[commands/impacket-ntlmrelayx-relay-to-specific-target]]'
platforms:
  - Windows
  - Network
  - Active Directory
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Mitm6]]'
  - '[[tools/Impacket]]'
validated: true
---

# SMB-NTLM-Relay-Attack-via-IPv6-with-Disabled-Signing

## Summary

This procedure performs an SMB and NTLM relay attack targeting environments where SMB signing is disabled and IPv6 is enabled. It intercepts NTLM authentication attempts over SMB, spoofs WPAD for credential capture, and relays them to other services like LDAP, enabling lateral movement and unauthorized access to sensitive domain resources.

## Description

In networks with SMB signing disabled, attackers can intercept and relay NTLM hashes without detection. This procedure leverages IPv6 for DNS manipulation to poison the network, forcing clients to authenticate to the attacker's controlled WPAD server. Once NTLM credentials are captured, they are relayed to target services such as LDAP on domain controllers, allowing privilege escalation or data access. This technique is effective in Active Directory environments and requires the attacker to be on the same network segment. Success depends on IPv6 being active and no protections like SMB signing or extended NTLM protection in place.

## Requirements

1. Network access to the target domain (same L2 segment for ARP/DHCP poisoning).
2. SMB signing disabled on target systems (verify via enumeration).
3. IPv6 enabled on target network and systems.
4. Administrative privileges on the attacker's machine for running relay tools.
5. Tools installed: CrackMapExec, Mitm6, and Impacket suite.

## Defense

- Enable SMB signing on all systems to prevent relay attacks.
- Disable IPv6 if not required, or implement IPv6-specific filtering.
- Deploy Extended Protection for Authentication (EPA) for LDAP and other services.
- Monitor for anomalous WPAD requests and unexpected IPv6 DHCP traffic.
- Use network segmentation and tools like Microsoft ATA for anomaly detection.

## Objectives

1. Capture NTLM hashes from SMB authentication attempts.
2. Relay captured credentials to high-value targets like domain controllers.
3. Achieve lateral movement and access to sensitive AD resources.
4. Establish persistent access via SOCKS proxy if needed.

## Instructions

### Step 1: Generate SMB Relay Target List

**Context**: Identify potential SMB targets that do not enforce signing, creating a list for selective relaying to avoid detection on signed hosts.

**Command** ([[commands/crackmapexec-generate-smb-relay-list]]):
```bash
crackmapexec smb $_HOSTS --gen-relay-list $_OUTPUT_FILE
```

This command scans the specified hosts for SMB services and generates a relay.txt file listing vulnerable targets without signing enforced. Run it from the attacker's machine with network access to the targets. If the scan completes without errors, the file will contain IPs suitable for relaying.

### Step 2: Perform IPv6 DNS Takeover

**Context**: Use Mitm6 to poison IPv6 DNS resolution and DHCPv6, redirecting clients to the attacker's controlled services for WPAD spoofing.

**Command** ([[commands/mitm6-ipv6-dns-takeover]]):
```bash
mitm6 -i $_INTERFACE -d $_DOMAIN
```

Execute this on the interface facing the target network. It listens for IPv6 router advertisements and sends forged DHCPv6 responses filtered to the specified domain. This step prepares the network for credential interception by manipulating DNS for WPAD. Monitor the output for successful poisoning events.

### Step 3: Spoof WPAD and Relay NTLM Credentials to Loot

**Context**: Start the NTLM relay server with IPv6 support, spoofing WPAD to capture hashes and store them in a loot directory for offline cracking or immediate use.

**Command** ([[commands/impacket-ntlmrelayx-spoof-wpad-relay-to-loot]]):
```bash
impacket-ntlmrelayx -6 -wh $_WPAD_HOST -of $_LOOT_DIR -tf $_TARGET_FILE
```

This invokes the relay server in IPv6 mode, serving a fake WPAD file from the specified host IP. It uses the relay list from Step 1 to target vulnerable hosts. Captured hashes are saved to the loot directory. If clients authenticate via SMB, hashes will appear in the output and loot files.

### Step 4: Create SOCKS Proxy from Relayed Connections

**Context**: Extend the relay to create a SOCKS proxy for further lateral movement, allowing traffic forwarding through relayed sessions with debug logging for troubleshooting.

**Command** ([[commands/impacket-ntlmrelayx-create-socks-proxy]]):
```bash
impacket-ntlmrelayx -6 -wh $_WPAD_HOST -l $_LISTEN_DIR -socks -debug
```

Run this concurrently or after Step 3 to listen for relayed connections and expose them as a SOCKS proxy. The debug flag provides verbose output on authentication attempts. Successful relays will show proxy connections ready for use in tools like Proxychains.

### Step 5: Relay to Specific High-Value Target

**Context**: Direct relayed NTLM credentials to a specific service like LDAPS on a domain controller for authentication and access.

**Command** ([[commands/impacket-ntlmrelayx-relay-to-specific-target]]):
```bash
impacket-ntlmrelayx -ip $_INTERFACE_IP -wh $_WPAD_HOST -t $_TARGET_URL
```

Specify the interface IP, WPAD host, and target (e.g., ldaps://dc.example.com). This relays captured SMB auth to the target service. If the relay succeeds, you'll gain access to the target using the victim's credentials, potentially dumping AD data or executing commands.
