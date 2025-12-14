---
tags:
  - reconnaissance
  - gitlab
  - version-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4ab6629a-0abf-4a73-99b7-25740dad5b7b
created_at: '2025-12-14T17:23:50.205Z'
updated_at: '2025-12-14T17:23:50.205Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Outdated-GitLab-Server

## Summary

This procedure involves reconnaissance to identify an outdated GitLab server vulnerable to RCE via ExifTool command injection, focusing on version enumeration without authentication.

## Description

In this attack scenario, the target is a publicly accessible GitLab instance at https://169.38.86.185/ (edst.ibm.com). The procedure uses passive and active scanning to confirm the platform and version, revealing susceptibility to known ExifTool flaws (e.g., CVE-2021-22205 or similar). Expected outcomes include version details confirming exploitability, enabling subsequent RCE without alerting defenses.

## Requirements

1. Internet access to the target URL.
2. Web browser or HTTP client for probing.
3. Knowledge of GitLab version history for vulnerability mapping.

## Defense

Defensive measures and detection strategies:

- Regularly update GitLab to the latest version and monitor for outdated instances using tools like Nessus.
- Implement web application firewalls (WAF) to block reconnaissance probes on admin endpoints.
- Log and alert on unusual access to version-disclosing pages (e.g., /help or API).

## Objectives

1. Confirm GitLab presence and extract version information.
2. Validate vulnerability to ExifTool command injection.
3. Prepare for exploitation without triggering alerts.

## Instructions

### Step 1: Access and Identify GitLab Instance

**Context**: Visit the target to visually and technically confirm it's a GitLab server.

Navigate to https://169.38.86.185/ using a web browser. Look for GitLab-specific elements like the login page, dashboard, or branding.

> Inspect the page source (Ctrl+U) for meta tags or comments indicating the version, such as "GitLab 13.x".

### Step 2: Enumerate Version Details

**Context**: Probe for explicit version disclosure to confirm outdated status.

Use browser developer tools (F12) to check network requests or JavaScript files for version strings. Alternatively, access common GitLab endpoints like /help or /api/v4/version (if unauthenticated access allowed) to retrieve JSON with version info.

> Expected output: Version string like "14.0.0" confirming pre-patch status for ExifTool vuln.

### Step 3: Validate Vulnerability

**Context**: Cross-reference version with known CVEs.

Search public databases (e.g., NIST NVD) for the identified version and ExifTool integration flaws. Confirm if the version is affected by command injection in metadata processing.

> Success: Version matches known vulnerable releases (e.g., <14.1.2).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- Web browser (e.g., Chrome DevTools)

## Tags

- [[Reconnaissance]]
- [[version-enumeration]]
