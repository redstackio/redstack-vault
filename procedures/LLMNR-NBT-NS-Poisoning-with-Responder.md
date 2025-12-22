---
id: 89e279ef-50f3-4702-bbd6-adb6da444995
name: LLMNR-NBT-NS-Poisoning-with-Responder
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.278115+00:00'
updated_at: '2023-04-10T20:25:10.716121+00:00'
tactics:
  - '[[Collection]]'
  - '[[Credential Access]]'
techniques:
  - '[[Adversary-in-the-Middle]]'
sub_techniques: []
tags:
  - network-discovery
  - responder
  - llmnr
  - nbt-ns
  - credential-access
commands:
  - '[[commands/responder-analyze-incoming-requests]]'
  - '[[commands/responder-enable-poisoning-and-wpad]]'
platforms:
  - Linux
  - Network
tools:
  - '[[tools/Responder]]'
validated: true
---

# LLMNR-NBT-NS-Poisoning-with-Responder

## Summary

The LLMNR-NBT-NS Poisoning with Responder procedure uses the Responder tool to listen for and respond to Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) requests on a local network. These protocols are fallback name resolution mechanisms in Windows environments that can be exploited through poisoning attacks to capture NTLM hashes or credentials when targets attempt to resolve non-existent hostnames. This enables adversary-in-the-middle (AitM) scenarios for credential theft and potential relay attacks to access network shares or escalate privileges.

## Description

LLMNR and NBT-NS are enabled by default on Windows systems for local name resolution when DNS fails. Attackers position themselves on the same network segment and use Responder to poison these requests by responding with a spoofed IP (their own machine). When a victim queries for a hostname (e.g., via mistyped UNC path like \\nonexistent), Responder intercepts the request and serves fake responses, prompting the victim to authenticate to the attacker's system via SMB, HTTP, or other protocols. Captured NTLMv1/v2 hashes can be relayed in real-time or cracked offline. This technique is effective in internal networks with weak segmentation and is often used during red team engagements for initial foothold expansion or lateral movement preparation. It requires layer 2 access but no elevated privileges on the attacker machine.

## Requirements

1. Layer 2 network access to the target segment (same broadcast domain as victims).
2. Responder tool installed on a Linux-based attacker machine (e.g., Kali).
3. No firewall blocking multicast traffic (ports 5355/UDP for LLMNR, 137/UDP for NBT-NS).
4. Optional: Wordlist for offline hash cracking if not relaying live.

## Defense

- Disable LLMNR and NBT-NS via Group Policy or registry (e.g., HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient: EnableMulticast=0).
- Enforce SMB signing and disable NTLMv1; prefer LDAP over NetBIOS.
- Implement network segmentation with VLANs to limit broadcast domains.
- Monitor for anomalous multicast traffic or unexpected SMB/HTTP connections to unknown IPs using tools like Zeek or Windows Event Logs (Event ID 4624 for failed logons).
- Deploy endpoint detection for Responder signatures (e.g., Python processes listening on multiple ports).

## Objectives

1. Identify active devices sending LLMNR/NBT-NS queries on the network.
2. Capture NTLM authentication attempts (hashes or plaintext if misconfigured).
3. Relay captured credentials to access remote shares or services for privilege escalation.
4. Map network resources visible to compromised accounts.

## Instructions

### Step 1: Analyze Incoming Requests Without Responding

**Context**: Begin by running Responder in analysis mode to passively monitor LLMNR, NBT-NS, and BROWSER requests. This step helps identify active protocols and query patterns without alerting potential IDS/IPS, allowing you to assess network activity before enabling active poisoning.

**Command** ([[commands/responder-analyze-incoming-requests]]):
```bash
responder -I $_INTERFACE -A
```

> This command listens on the specified network interface without sending any spoofed responses. It logs incoming queries to the console, showing source IPs, queried hostnames, and protocol types. Run this for 5-10 minutes to baseline traffic. Expected output includes lines like "[LLMNR] Poisoner is up" but no responses sent; look for frequent queries indicating misconfigurations.

### Step 2: Enable Poisoning and WPAD Rogue Server

**Context**: Switch to active mode to poison LLMNR/NBT-NS requests and enable a rogue WPAD proxy for potential HTTP credential capture. The -r flag activates the poisoner, -w starts the WPAD server to intercept browser proxy settings, and -f forces SMBv1 for compatibility with legacy systems. This step tricks victims into authenticating to your machine, capturing hashes in real-time.

**Command** ([[commands/responder-enable-poisoning-and-wpad]]):
```bash
responder.py -I $_INTERFACE -wrf
```

> Execute this on the attacker machine positioned to receive broadcasts. Responder will respond to queries with its IP, prompting victims to connect via SMB/HTTP. Monitor the output for captured hashes (e.g., "[SMB] NTLMv2 Hash captured: username::domain:challenge:hash"). Save logs for later analysis or relay with tools like ntlmrelayx. Stop with Ctrl+C after sufficient captures; success is indicated by hash logs or connection attempts.
