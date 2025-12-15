---
tags:
  - arp-spoofing
  - mitm
  - network
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:30:58.467Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[ARP Cache Poisoning]]'
id: 7ba58801-5004-49e2-8aab-02b21e2f58aa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Perform ARP Spoofing for MiTM on WebSocket Connection

## Summary

This procedure uses ARP spoofing to intercept WebSocket traffic on the local WiFi network, positioning the attacker between the PoS server and customer view app for message alteration.

## Description

By poisoning ARP caches, the attacker redirects port 5000 traffic through their relay. This exploits the server's all-interfaces binding, allowing injection of modified messages, including new public keys, without detection in the crypto protocol's receiveMessageFromServer() method when cryptoType != 1.

## Requirements

1. Attacker on the same WiFi subnet as PoS device and client
2. ARP spoofing tool (e.g., arpspoof from dsniff or Bettercap)
3. Root/admin privileges on attacker machine
4. Knowledge of target IPs (PoS server and client)

## Defense

Defensive measures and detection strategies:

- Enable ARP inspection or static ARP entries on network switches
- Monitor for duplicate IP/MAC bindings or traffic volume spikes
- Use WPA3 or wired connections for PoS to avoid WiFi MiTM

## Objectives

1. Redirect WebSocket traffic to attacker relay
2. Maintain connection stability during spoofing
3. Enable message modification for key injection

## Instructions

### Step 1: Identify Target IPs

**Context**: Use tools like arp-scan to find PoS device and client IPs on the network.

**Command** (example with arp-scan):
```bash
arp-scan --localnet
```

> Lists devices; identify PoS by port 5000 scan or app behavior.

### Step 2: Execute ARP Spoofing

**Context**: Spoof ARP to make devices route through attacker; integrate with relay for WebSocket handling.

**Command** (using arpspoof):
```bash
arpspoof -i wlan0 -t <client-ip> <pos-ip>
arpspoof -i wlan0 -t <pos-ip> <client-ip>
```

> In another terminal, run relay; expect traffic reroute confirmed by tcpdump or relay logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

- [[ARP Cache Poisoning]] ARP Cache Poisoning

## Commands Used


## Tools Used


## Tags

- arp-spoofing
- mitm
- network
