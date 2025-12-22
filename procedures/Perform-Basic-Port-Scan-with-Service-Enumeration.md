---
id: 5758d331-ac13-44ca-afde-6476996867c4
name: Perform-Basic-Port-Scan-with-Service-Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:24:17.694083+00:00'
updated_at: '2023-06-24T04:49:52.579043+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - network
  - reconnaissance
commands:
  - '[[commands/nmap-port-scan-with-service-version-detection]]'
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Perform-Basic-Port-Scan-with-Service-Enumeration

## Summary

This procedure uses Nmap to scan target hosts for open ports in the common range (1-1024) and enumerate service versions and banners, identifying potential attack vectors like SMB services.

## Description

Port scanning with service enumeration reveals the attack surface by detecting listening services and their versions. This is crucial in Windows environments to confirm SMB (port 445) availability for share enumeration. The scan targets well-known ports and uses NSE scripts for deeper insights without aggressive probing.

## Requirements

- Network access to target IP
- Nmap installed ([[tools/Nmap]])
- No credentials required for basic scan

## Defense

- Implement firewall rules to limit port exposure
- Use intrusion detection systems (IDS) to alert on scan patterns
- Enable logging for anomalous network traffic

## Objectives

1. Identify open ports on the target
2. Enumerate service versions for vulnerability assessment
3. Confirm SMB service presence for subsequent steps

## Instructions

### Step 1: Execute Port Scan with Version Detection

**Context**: This step scans the target and probes open ports for service details, helping prioritize SMB if available.

**Command** ([[commands/nmap-port-scan-with-service-version-detection]]):
```bash
nmap -sV $_TARGET_IP
```

> This command performs a TCP SYN scan (-sS implied) with version detection (-sV). Expected output includes port states and service versions; look for 445/tcp open for SMB.

### Step 2: Review and Validate Results

**Context**: Analyze output to confirm SMB and note any other services for chaining attacks.

Save results to file for reference: nmap -sV $_TARGET_IP -oN scan_results.txt.

> Success if SMB is detected; proceed to share enumeration.
