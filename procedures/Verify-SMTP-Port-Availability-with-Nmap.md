---
tags:
  - port-scan
  - recon
  - smtp
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-scan-port587]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:31:11.058Z'
sub_techniques: []
id: 83b15778-898d-4f4b-a433-c5669d91203f
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Verify-SMTP-Port-Availability-with-Nmap

## Summary

This procedure uses Nmap to scan specific SMTP ports on a target IP, confirming if the submission service is open and responsive for vulnerability testing.

## Description

During triage for apps.owncloud.com (IP 50.30.33.235), this verified port 587 status, essential before cipher testing. It detects open/closed states without deeper intrusion. Requires Nmap and target IP.

## Requirements

1. Nmap installed
2. Network access to target IP
3. Target port known (e.g., 587)

## Defense

Defensive measures and detection strategies:

- Firewall rules to limit port scans (e.g., rate-limit SYN packets)
- IDS rules for Nmap signatures (e.g., Snort rules for port scans)
- Use non-standard ports if possible

## Objectives

1. Confirm SMTP port openness
2. Ensure service availability for follow-on tests
3. Identify potential attack vectors

## Instructions

### Step 1: Scan Specific Port

**Context**: Target the SMTP submission port to check state.

**Command** ([[commands/nmap-scan-port587]]):
```bash
nmap 50.30.33.235 -p 587
```

> Scans port 587; output shows "open submission" if vulnerable and responsive.

### Step 2: Interpret Results

**Context**: Validate for open state.

**Command** (No execution; review):

> Success if port open; proceed to cipher tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/nmap-scan-port587]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[port-scan]]
- [[recon]]
- [[smtp]]
