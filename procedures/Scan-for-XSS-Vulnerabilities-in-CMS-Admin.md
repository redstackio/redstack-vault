---
id: proc-scan-xss-cms-001
tags:
  - xss
  - scanning
  - cms
  - concrete5
type: procedure
tools:
  - '[[tools/Netsparker]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:15:31.954Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Scan-for-XSS-Vulnerabilities-in-CMS-Admin

## Summary

This procedure uses automated web vulnerability scanners to identify reflected XSS entry points in Concrete5 CMS administrative endpoints by testing unsanitized parameters in dashboard features, tools, and dialogs.

## Description

In Concrete5 5.7.3.1, multiple admin areas lack proper input validation, allowing reflected XSS via parameters like banned_word[], channel, and accessType. Scanning reveals these flaws, enabling targeted exploitation. Prerequisites include network access to the CMS and basic web app knowledge; outcomes include a list of injectable points for further attacks.

## Requirements

1. Access to Netsparker or similar DAST tool
2. Valid URL to the Concrete5 instance
3. Authenticated session if scanning requires login

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts
- Use web application firewalls (WAF) to detect payload patterns like <script>alert
- Regularly scan with tools like OWASP ZAP for early detection

## Objectives

1. Map vulnerable parameters across admin interfaces
2. Confirm reflection without encoding
3. Prepare for payload delivery

## Instructions

### Step 1: Configure Scanner Scope

**Context**: Define the scan targets to focus on admin paths in Concrete5.

Launch Netsparker and set the start URL to the dashboard, including paths like /dashboard/system/, /tools/required/, and /ccm/system/dialogs/.

**Command** (Netsparker GUI or CLI equivalent):

No direct bash command; use tool interface to initiate scan with XSS module enabled.

> Expected: Scan report generates in ~5-10 minutes, highlighting parameters.

### Step 2: Review and Validate Findings

**Context**: Analyze scan results for confirmed XSS vectors.

Examine output for alerts like "Reflected XSS in parameter 'channel' via GET" and manually verify by accessing the URL with a benign payload.

**Command** (Manual verification with curl):

Use [[commands/curl-test-xss]] to probe:

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/dashboard/reports/logs/view?channel=<script>alert(1)</script>'
```

> Expected: Payload appears unescaped in response HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Netsparker]]

## Tags

- xss
- scanning
- cms
