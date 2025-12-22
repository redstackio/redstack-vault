---
id: ac-uuid-001
tags:
  - smb
  - access-control
  - cctv
  - privacy
  - thailand
type: attack_chain
tools:
  - '[[tools/nmap]]'
  - '[[tools/smbclient]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Network
  - SMB
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Exposed-SMB-Servers]]'
  - '[[procedures/Access-SMB-Shares-Without-Authentication]]'
step_count: 2
techniques:
  - '[[Active Scanning]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:52.670Z'
description: >-
  Attack chain exploiting improper access controls on SMB servers in Thailand to
  gain unauthorized access to sensitive CCTV footage and images from Starbucks
  locations.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[External Remote Services]]'
---
# Unauthorized Access to Starbucks CCTV Footage via Exposed SMB Shares

Multi-stage attack chain demonstrating a complete attack workflow exploiting misconfigured SMB servers to access sensitive CCTV data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Exposed SMB] --> B[Initial Access: Connect to Shares]
    B --> C[Objective: Retrieve CCTV Footage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/nmap]]
- [[tools/smbclient]]

### Target Environment

- Network-accessible SMB servers (ports 445/TCP open)
- No authentication required on shares
- Windows or Linux hosts with SMB protocol enabled

### Initial Access Requirements

- Network connectivity to target IP range (e.g., Thai IP addresses)
- No credentials needed due to misconfiguration
- Basic reconnaissance tools

## Detailed Attack Procedures

### Step 1: Discover Exposed SMB Servers
procedure: [[procedures/Discover-Exposed-SMB-Servers]]

**Objective**: Identify SMB servers hosting CCTV footage that are exposed without authentication.

**Instructions**: Scan a target IP range for open SMB ports using [[commands/nmap-scan-smb]] to detect vulnerable servers:

```bash
nmap -p 445 --script smb-security-mode 192.168.1.0/24
```

Follow up by checking for anonymous access with [[commands/smbclient-enum-shares]] on detected hosts:

```bash
smbclient -L //target-ip -N
```

**Expected Output**: List of hosts with SMB open and shares visible without credentials.

**Success Indicators**:
- SMB port 445 detected on multiple hosts
- Anonymous share enumeration succeeds

### Step 2: Access SMB Shares Without Authentication
procedure: [[procedures/Access-SMB-Shares-Without-Authentication]]

**Objective**: Connect to exposed SMB shares and retrieve sensitive CCTV footage and images.

**Instructions**: Connect to the identified share using [[commands/smbclient-connect-anon]]:

```bash
smbclient //target-ip/CCTV-Backup -N
```

Once connected, list and download files with commands like `ls` and `get` inside smbclient:

```bash
get footage.mp4
exit
```

**Expected Output**: Successful connection and file downloads, revealing CCTV videos and images.

**Success Indicators**:
- Anonymous login accepted
- Files downloaded without errors

## Attack Chain Summary

### Key Achievements

1. Identified multiple exposed SMB servers in Thailand via port scanning.
2. Accessed CCTV backup shares anonymously, retrieving privacy-sensitive footage from Starbucks.
3. Demonstrated impact of improper access controls on sensitive data exposure.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
