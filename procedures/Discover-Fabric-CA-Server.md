---
id: proc-uuid-1
tags:
  - discovery
  - port-scan
  - fabric-ca
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:30:27.231Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Discover Fabric-CA Server

## Summary

This procedure identifies the Fabric-CA server by scanning for its default listening port (7054) and confirming external accessibility due to binding on 0.0.0.0, enabling subsequent exploitation.

## Description

In Hyperledger Fabric networks, the Fabric-CA server handles certificate authority tasks and is often misconfigured to listen on all interfaces without restrictions. This procedure uses network scanning to locate the server, verifying its exposure which allows external attackers to target authentication endpoints. Prerequisites include network access to the target's IP range.

## Requirements

1. Network access to scan the target IP
2. Port scanning capabilities (e.g., nmap installed)
3. Knowledge of default Fabric-CA port 7054

## Defense

Defensive measures and detection strategies:

- Bind Fabric-CA to localhost or specific internal interfaces only
- Implement firewall rules to block port 7054 from external access
- Monitor for unusual port scans on port 7054 using IDS like Snort

## Objectives

1. Locate the Fabric-CA server on the network
2. Confirm external reachability and default configuration
3. Prepare for authentication exploitation

## Instructions

### Step 1: Scan for Open Port 7054

**Context**: Perform a targeted port scan to detect the Fabric-CA service listening on the default port.

**Command** (nmap-port-scan):
```bash
nmap -p 7054 --open target-ip-range
```

> This command scans the specified IP range for port 7054 and reports if it's open. Expected output includes service details confirming Fabric-CA if version detection is enabled (add -sV flag).

### Step 2: Verify Service Accessibility

**Context**: Test connectivity to the endpoint to ensure it's reachable externally and responds to Fabric-CA requests.

**Command** (curl-connectivity-test):
```bash
curl -k https://target-ip:7054/cainfo
```

> This sends a request to the CA info endpoint. Successful output returns JSON with CA configuration details, indicating exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- discovery
- port-scan
- fabric-ca
