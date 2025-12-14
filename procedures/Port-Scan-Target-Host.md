---
id: uuid-port-scan
tags:
  - port-scan
  - solr
type: procedure
tools:
  - '[[tools/Nmap-Port-Scanner]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-port-scan]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:23:37.353Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Port Scan Target Host

## Summary

Scan the target IP to identify open ports, specifically discovering an exposed Apache Solr instance on a non-standard port without authentication.

## Description

This procedure uses port scanning to map the target's attack surface. In the attack, a full port scan revealed an open port (e.g., 8984) hosting Solr, allowing unauthenticated access. This step is crucial for identifying vulnerable services in public-facing applications.

## Requirements

1. Target IP address from reconnaissance
2. Installed Nmap tool
3. Network connectivity to target

## Defense

Defensive measures and detection strategies:

- Deploy firewalls to block unnecessary ports
- Use intrusion detection systems (IDS) to alert on port scanning patterns like SYN floods

## Objectives

1. Discover open ports on target
2. Identify Solr service exposure
3. Confirm lack of authentication

## Instructions

### Step 1: Execute Port Scan

**Context**: Run a comprehensive scan to find open services.

**Command** ([[commands/nmap-port-scan]]):
```bash
nmap -p- -T4 target-ip
```

> This aggressive scan (-T4) checks all ports (-p-) and identifies the Solr port as open, with banner grabbing showing Apache Solr.

### Step 2: Verify Service

**Context**: Access the port to confirm Solr.

Use browser or curl to http://target-ip:port/ and check for Solr admin interface.

> Expected: Solr dashboard or API endpoints without login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/nmap-port-scan]]

## Tools Used

- [[tools/Nmap-Port-Scanner]]

## Tags

- [[port-scan]]
- [[solr]]
