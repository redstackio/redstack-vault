---
id: proc-direct-admin-access
tags:
  - unauthorized-access
  - data-exfiltration
  - path-traversal
  - saba-lms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.480Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Direct Access to Admin Directories via URL Manipulation

## Summary

This procedure uses an authenticated non-admin session to directly traverse to admin directories in Saba LMS via crafted URLs, allowing manipulation and exfiltration of sensitive administrative resources without proper checks.

## Description

With a standard session, URL paths like /Saba/Web_wdk/[context]/platform/system/admin/systemMain.rdf can be accessed due to lacking input validation, enabling directory traversal. This targets web apps with poor path handling, resulting in exposure of IPs, passwords, emails, and configs, plus risks of defacement, DoS, RCE, and deletion.

## Requirements

1. Authenticated session (from standard login)
2. Base URL and context knowledge (e.g., https://target.com/Saba/Web_wdk/[custom])
3. Browser or proxy for URL construction

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all URL parameters for traversal sequences
- Apply least-privilege principles to session tokens
- Audit access logs for unauthorized admin path requests

## Objectives

1. Gain direct access to admin RDF files and directories
2. Exfiltrate sensitive data
3. Manipulate resources for further compromise

## Instructions

### Step 1: Construct Admin URL

**Context**: Build a traversal URL targeting admin endpoints.

No command; enter https://target.com/Saba/Web_wdk/[context]/platform/system/admin/systemMain.rdf in the browser.

> The page loads admin content, such as system configurations, without prompting for admin creds.

### Step 2: Access Additional Admin Paths and Exfiltrate

**Context**: Repeat for other directories to gather data.

Navigate to https://target.com/Saba/Web_wdk/[context]/Platform/system/admin/usersStatistics.rdf.

> Extract visible data like usernames, emails, and passwords; screenshot or download for exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauthorized-access]]
- [[data-exfiltration]]
