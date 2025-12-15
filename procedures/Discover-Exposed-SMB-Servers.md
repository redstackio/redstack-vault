---
id: proc-uuid-001
tags:
  - smb
  - reconnaissance
  - scanning
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-scan-smb]]'
  - '[[commands/smbclient-enum-shares]]'
verified: false
platforms:
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:52.667Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Exposed-SMB-Servers

## Summary

This procedure involves scanning networks to identify SMB servers that are exposed and potentially accessible without authentication, focusing on shares hosting sensitive data like CCTV footage.

## Description

In scenarios like the Starbucks Thailand incident, reconnaissance reveals SMB servers misconfigured with open shares. The procedure uses port scanning to find SMB services (port 445) and enumerates shares anonymously to confirm exposure. Prerequisites include network access to the target range, such as Thai IP blocks, and tools like nmap for scanning.

## Requirements

1. Network connectivity to target IP range (e.g., public IPs in Thailand)
2. Nmap installed for port and service scanning
3. No credentials required for initial detection

## Defense

Defensive measures and detection strategies:

- Implement firewall rules to restrict SMB (port 445) to trusted networks only
- Enable SMB signing and require authentication on all shares
- Monitor for anomalous port scans using IDS like Snort

## Objectives

1. Identify hosts running SMB services
2. Enumerate shares accessible without authentication
3. Confirm presence of sensitive data shares (e.g., CCTV backups)

## Instructions

### Step 1: Scan for SMB Ports

**Context**: Use nmap to detect open SMB ports on the target network.

**Command** ([[commands/nmap-scan-smb]]):
```bash
nmap -p 445 --script smb-security-mode 192.168.1.0/24
```

> This command scans the specified IP range for port 445 and checks SMB security mode. Expected output includes hosts with SMB enabled and whether guest access is allowed.

### Step 2: Enumerate Shares Anonymously

**Context**: Probe detected SMB hosts for anonymous share access.

**Command** ([[commands/smbclient-enum-shares]]):
```bash
smbclient -L //target-ip -N
```

> This lists available shares without a password (-N for null session). Expected output shows shares like 'CCTV-Backup' if exposed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/nmap-scan-smb]]
- [[commands/smbclient-enum-shares]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[smb]]
- [[Reconnaissance]]
