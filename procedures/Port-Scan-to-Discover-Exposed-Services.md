---
tags:
  - scanning
  - port-scan
  - service-discovery
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-port-scan-with-service-detection]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Vulnerability Scanning]]'
id: 7e74e4e3-3494-4306-a839-e1a5ecd3b21d
created_at: '2025-12-14T03:16:37.268Z'
updated_at: '2025-12-14T03:16:37.268Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Port-Scan-to-Discover-Exposed-Services

## Summary

This procedure uses nmap to perform a full port scan on a target IP, identifying open ports like 4567 to bypass .htaccess protection on port 80 and expose services such as an unprotected NodeBB forum.

## Description

Port scanning is a key discovery technique to map the attack surface. Here, after identifying the target IP 104.131.159.88 from SSL details, an aggressive nmap scan detects all open ports with service versioning, revealing port 4567 running NodeBB without authentication. This bypasses the .htaccess on port 80. Prerequisites include sudo access for raw scanning and a quiet network to avoid detection. Outcomes include a list of exploitable services.

## Requirements

1. nmap installed with sudo privileges
2. Target IP resolved (e.g., 104.131.159.88)
3. Network connectivity without firewalls blocking scans

## Defense

Defensive measures and detection strategies:

- Implement firewall rules to restrict port exposure
- Use IDS like Snort to detect nmap signatures
- Rate-limit incoming scans and log anomalous traffic

## Objectives

1. Identify all open ports on the target
2. Detect service versions for vulnerability assessment
3. Uncover misconfigurations like unprotected ports

## Instructions

### Step 1: Execute Full Port Scan

**Context**: Launch nmap to scan all 65535 ports with service detection.

**Command** ([[commands/nmap-port-scan-with-service-detection]]):
```bash
sudo nmap -sSV -p- 104.131.159.88 -oA stage_ph -T4
```

> This command uses -sSV for service/version detection, -p- for all ports, -oA for multiple output formats, and -T4 for aggressive timing. Expected output includes open ports like 4567/tcp open tram? | http://nodebb... indicating NodeBB.

### Step 2: Analyze Results

**Context**: Review scan output for unprotected services.

Parse the nmap XML/Grepable output to confirm port 4567 hosts NodeBB without .htaccess.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- [[commands/nmap-port-scan-with-service-detection]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[scanning]]
- [[port-scan]]
- [[service-discovery]]
