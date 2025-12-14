---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - recon
  - confluence
  - version-fingerprinting
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-version-check]]'
  - '[[commands/nmap-vuln-scan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:13.114Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Vulnerable Atlassian Confluence Instance

## Summary

This procedure identifies an internet-facing Atlassian Confluence instance running an outdated version susceptible to SSRF vulnerabilities like CVE-2017-9506, enabling initial reconnaissance for exploitation.

## Description

In a DoD-hosted environment, attackers scan for public Confluence deployments and fingerprint the version to confirm lack of patches. This step reveals exposure to SSRF, allowing subsequent internal pivoting without authentication. Expected outcomes include version confirmation and vulnerability validation, setting up firewall bypass.

## Requirements

1. Internet access to the target Confluence URL.
2. Basic tools like curl and nmap installed.
3. Knowledge of CVE-2017-9506 (affects Confluence < 6.1.0).

## Defense

Defensive measures and detection strategies:

- Regularly patch Confluence to latest versions.
- Implement web application firewalls (WAF) to block version disclosure probes.
- Monitor access logs for unusual GET/POST requests to /plugins/servlet/ endpoints.

## Objectives

1. Confirm presence of vulnerable Confluence instance.
2. Gather version details for exploit planning.
3. Identify potential SSRF entry points.

## Instructions

### Step 1: Probe for Confluence Presence and Version

**Context**: Send a basic request to detect Confluence and extract version information from responses or headers.

**Command** ([[commands/curl-version-check]]):
```bash
curl -s "https://target-confluence.dod.mil/" | grep -i "confluence\|version"
```

> This command fetches the homepage and greps for version strings. Expected output: Lines like "Atlassian Confluence 5.x" indicating vulnerability.

### Step 2: Vulnerability Scanning

**Context**: Use Nmap to perform service version detection and check for known vulns.

**Command** ([[commands/nmap-vuln-scan]]):
```bash
nmap -sV --script vuln target-confluence.dod.mil
```

> Scans for open ports and runs vuln scripts. Expected output: Service version and potential CVE matches, confirming SSRF exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-version-check]]
- [[commands/nmap-vuln-scan]]

## Tools Used

- None

## Tags

- [[recon]]
- [[Confluence]]
