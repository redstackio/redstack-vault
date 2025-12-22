---
id: 0e6f716f-40a3-49ca-8935-dd395fc54b2a
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:44:52.509187+00:00'
updated_at: '2023-05-26T00:42:42.415825+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - nmap
  - service-enumeration
  - os-detection
platforms:
  - Linux
commands:
  - '[[commands/nmap-aggressive-scan-with-version-detection]]'
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Perform-Aggressive-Port-Scan-with-Nmap

## Summary

This procedure runs Nmap in aggressive mode (-A) to detect open ports, identify service versions, perform OS fingerprinting, and execute default NSE scripts for vulnerability hints on target hosts.

## Description

Nmap's -A enables version detection (-sV), OS detection (-O), script scanning (-sC), and traceroute. Ideal for follow-up to Masscan, providing depth on fewer targets. Outputs verbose details like banners and CPEs; use on live IPs from recon to prioritize exploits.

## Requirements

- Target IP or host
- Nmap installed (standard on Kali)
- Network access to target

## Defense

- Nmap signature detection in IDS (e.g., unusual probe patterns)
- Honeypots to mislead scanners
- Service version obfuscation

## Objectives

- Enumerate services and versions
- Fingerprint OS
- Run basic vuln scripts

## Instructions

### Step 1: Run Aggressive Scan

**Context**: Comprehensive scan combining multiple Nmap features.

**Command** ([[commands/nmap-aggressive-scan-with-version-detection]]):

```bash
nmap -A $_TARGET_IP -oN $_OUTPUT_FILE
```

Scans top 1000 ports by default; add -p- for all.
