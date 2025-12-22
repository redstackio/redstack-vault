---
id: proc-uuid-001
tags:
  - reconnaissance
  - ssh
  - banner-grabbing
  - version-detection
type: procedure
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/netcat-banner-grab]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:24:55.802Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Gather-SSH-Server-Version-via-Banner-Grabbing

## Summary

This procedure involves connecting to an SSH service on port 22 to capture the server banner, which reveals the OpenSSH version. It is used to assess potential vulnerabilities like CVE-2012-0814, an information disclosure issue in older versions where debug messages leak sensitive authorized_keys options to authenticated users.

## Description

In this reconnaissance technique, an attacker passively connects to the SSH port without authentication to read the initial banner string. The banner typically includes the protocol version and server software details, such as "SSH-2.0-OpenSSH_5.5p1". This information allows comparison against vulnerability databases. For CVE-2012-0814, versions before 5.7 are affected, but patches like Debian Squeeze's openssh_5.5p1-6+squeeze5 mitigate it. The procedure targets Linux-based SSH servers and requires no credentials, making it low-risk for detection. Expected outcomes include version identification and a decision on further exploitation feasibility.

## Requirements

1. Network access to target port 22 (TCP)
2. Tool like Netcat installed for connection
3. Basic knowledge of SSH protocol banners

## Defense

Defensive measures and detection strategies:

- Disable or customize SSH banners to hide version info (e.g., via sshd_config: Banner /dev/null)
- Monitor SSH port connections for anomalous probes using tools like fail2ban or IDS signatures for banner grabs
- Keep OpenSSH updated and apply patches promptly

## Objectives

1. Retrieve SSH server banner to identify OpenSSH version
2. Assess vulnerability to information disclosure (e.g., CVE-2012-0814)
3. Determine if further authenticated testing is warranted

## Instructions

### Step 1: Establish Connection and Capture Banner

**Context**: Initiate a TCP connection to the SSH port to trigger the server banner response without proceeding to authentication.

**Command** ([[commands/netcat-banner-grab]]):
```bash
nc blog.greenhouse.io 22
```

> This command uses Netcat to connect to the target host on port 22. The server immediately sends the banner (e.g., "SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze5"). Type 'exit' or Ctrl+C to disconnect. Parse the output for version details and cross-reference with CVE databases.

### Step 2: Analyze Banner for Vulnerabilities

**Context**: Manually or scripturally parse the banner to check against known CVEs.

**Command** ([[commands/grep-version-parse]]):
```bash
echo "SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze5" | grep -oP 'OpenSSH_\K[^ ]+'
```

> This extracts the version (e.g., "5.5p1"). Compare to CVE-2012-0814 requirements (pre-5.7 vulnerable, but check distro patches like Debian Squeeze).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/netcat-banner-grab]]
- [[commands/grep-version-parse]]

## Tools Used

- [[tools/Netcat]]

## Tags

- [[Reconnaissance]]
- [[SSH]]
- [[banner-grabbing]]
