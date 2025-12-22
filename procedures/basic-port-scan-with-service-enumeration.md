---
id: 5758d331-ac13-44ca-afde-6476996867c4
name: Basic-Port-Scan-with-Service-Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:24:17.694083+00:00'
updated_at: '2023-06-24T04:49:52.579043+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - enumeration
  - network
commands:
  - '[[commands/nmap-port-scan-with-banner-enumeration]]'
platforms:
  - Linux
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Basic-Port-Scan-with-Service-Enumeration

## Summary

This procedure uses Nmap to perform a basic port scan on a target IP, focusing on ports 1-1024 and popular services, while enumerating service versions and banners to identify potential entry points like RPC and SMB in an AD environment.

## Description

Port scanning with service enumeration helps attackers map the attack surface by identifying open ports and running services. In AD compromise scenarios, confirming RPC (135), SMB (445), and WinRM (5985) availability is crucial for subsequent enumeration and access steps. The scan is non-intrusive but can be detected by network monitoring.

## Requirements

- Network access to the target IP
- Nmap installed on attacker machine
- No credentials required for basic scan

## Defense

- Implement network segmentation and firewalls to limit scan visibility
- Use intrusion detection systems (IDS) to alert on port scans
- Enable logging on endpoints for service probes

## Objectives

1. Discover open ports on the target
2. Enumerate service versions for vulnerability assessment
3. Confirm AD-related services like RPC and SMB

## Instructions

### Step 1: Execute Nmap Scan with Version Detection

**Context**: This step scans the target for open ports in the default range (1-1024) plus common AD ports, detecting service details to guide further actions.

**Command** ([[commands/nmap-port-scan-with-banner-enumeration]]):
```bash
nmap -sV $_TARGET_IP
```

> The -sV flag probes open ports for version info. Expected output includes port states and service banners, e.g., '445/tcp open microsoft-ds Windows 10 Microsoft-DS'.

### Step 2: Review and Save Results

**Context**: Parse the output to identify relevant services and save for documentation.

No command; manually note open ports like 135/rpc, 445/smb.

**Expected Output**: Saved scan results in text or XML for reference.

## Expected Output

Nmap report listing open ports, e.g.:

PORT    STATE SERVICE  VERSION
135/tcp open  msrpc    Microsoft Windows RPC
445/tcp open  microsoft-ds Windows 10 Enterprise 15063 microsoft-ds
