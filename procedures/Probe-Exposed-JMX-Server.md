---
tags:
  - recon
  - jmx
  - port-scan
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-jmx-probe]]'
  - '[[commands/telnet-port-check]]'
verified: false
platforms:
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:41.541Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b75076e4-dbf1-4ea0-affb-aa18d84f93c8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Probe-Exposed-JMX-Server

## Summary

This procedure scans target domains for exposed Java JMX servers on port 555, identifying unauthenticated interfaces vulnerable to remote exploitation. It was used to discover lingering exposures from decommissioned services like Jabber in the Basecamp incident.

## Description

In scenarios where services are decommissioned but DNS records persist, old IPs may expose management interfaces like JMX without authentication. This procedure uses port scanning to detect open JMX ports and basic connection tests to confirm accessibility, revealing potential RCE vectors via deserialization. Prerequisites include network access to the target and tools like nmap installed.

## Requirements

1. Network connectivity to the target domain/IP on port 555
2. Installed nmap with JMX scripts
3. Basic knowledge of Java services and ports

## Defense

Defensive measures and detection strategies:

- Remove unused DNS records promptly after decommissioning services
- Implement firewall rules to block JMX ports (1099/5555 default, but custom like 555)
- Monitor for anomalous port scans on management ports using IDS like Snort

## Objectives

1. Identify open JMX interfaces on target hosts
2. Confirm lack of authentication on the service
3. Map the attack surface for further exploitation

## Instructions

### Step 1: Resolve Domain and Scan Port 555

**Context**: Resolve the target domain to its IP and probe port 555 for JMX service presence using nmap's dedicated script.

**Command** ([[commands/nmap-jmx-probe]]):
```bash
nmap -p 555 --script=jmx-info jabber.37signals.com
```

> This command scans port 555 and runs the jmx-info script to extract service details, such as Java version or MBean info. Expected output includes confirmation of JMX if vulnerable, e.g., "JMX port open, no auth required."

### Step 2: Verify Connectivity with Telnet

**Context**: Test direct connection to confirm the port responds without authentication prompts.

**Command** ([[commands/telnet-port-check]]):
```bash
telnet jabber.37signals.com 555
```

> Telnet attempts a raw connection; success shows a connected banner or JMX protocol response, indicating exposure. Exit with Ctrl+C if connected.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/nmap-jmx-probe]]
- [[commands/telnet-port-check]]

## Tools Used

- [[tools/nmap]]

## Tags

- recon
- jmx
- port-scan
