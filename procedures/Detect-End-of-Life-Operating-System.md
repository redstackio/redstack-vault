---
tags:
  - os-detection
  - reconnaissance
  - eol-os
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/nmap-os-detect]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:28:36.529Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2c6b93d6-772c-4a63-8ed1-5257320039a9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Detect-End-of-Life-Operating-System

## Summary

This procedure involves querying a remote host to retrieve its self-reported operating system version, identifying if it is end-of-life (EOL) like Ubuntu 12.04, which lacks security patches and exposes the system to known exploits.

## Description

In this scenario, the target is the stun.nextcloud.com server hosting a STUN service. By checking the Unix OS version through service banners or direct queries, attackers can determine the OS is Ubuntu 12.04, unsupported since 2017. This discovery enables further targeting of unpatched vulnerabilities, such as privilege escalation exploits. Prerequisites include network access to the target and basic reconnaissance tools. Expected outcomes include confirmation of EOL status, paving the way for exploitation without performing actual attacks.

## Requirements

1. Network access to the target host (e.g., stun.nextcloud.com)
2. Scanning tools like nmap for banner grabbing
3. Knowledge of OS support lifecycles (e.g., Ubuntu EOL dates)

## Defense

Defensive measures and detection strategies:

- Regularly update OS to supported versions and apply patches
- Disable unnecessary service banners to avoid OS fingerprinting (e.g., configure SSH/HTTP to not reveal version info)
- Monitor for port scans using tools like fail2ban or IDS like Snort

## Objectives

1. Accurately identify the target's OS version
2. Confirm EOL status to assess patch availability
3. Enable targeted exploit research

## Instructions

### Step 1: Scan Target for Service and OS Information

**Context**: Use network scanning to capture the self-reported OS version from exposed services like STUN on port 3478.

**Command** ([[commands/nmap-os-detect]]):
```bash
nmap -sV -O -p 3478 stun.nextcloud.com
```

> This command performs service version detection (-sV) and OS fingerprinting (-O) on the specified port. Expected output includes lines like "OS details: Linux 3.2 - 4.9 (Ubuntu 12.04)" confirming the EOL version.

### Step 2: Verify EOL Status

**Context**: Cross-reference the detected OS with vendor support information to confirm lack of patches.

No specific command; manually check Ubuntu's release schedule or use a browser to visit canonical.com for EOL dates.

> Expected output: Confirmation that Ubuntu 12.04 reached EOL in April 2017, with no security updates available.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/nmap-os-detect]]

## Tools Used


## Tags

- [[os-detection]]
- [[Reconnaissance]]
- [[eol-os]]
