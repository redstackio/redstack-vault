---
id: proc-idor-manipulate-001
tags:
  - idor
  - parameter-tampering
  - credentials-exposure
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.402Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Manipulate-ID-Parameter-for-Unauthorized-FTP-Access

## Summary

This procedure exploits an IDOR vulnerability by directly manipulating the ID parameter in the DoD FTP push server URL, allowing viewing, updating, or deleting of another user's FTP/sFTP credentials without ownership validation.

## Description

In the DoD web application, the FTP server management endpoint uses a path-based ID (e.g., /filepush/ftp/<ID>/) without server-side checks for user ownership. An authenticated attacker can alter this ID to access any server's details, revealing sensitive information like hostname, username, password, and path. This enables immediate credential theft and potential server compromise, with broader implications for data exfiltration.

## Requirements

1. Active authenticated session from DoD website login
2. Web browser with URL editing capability (e.g., address bar or developer console)
3. Knowledge of a target ID (start with low numbers like 1 if unknown)

## Defense

Defensive measures and detection strategies:

- Implement proper access controls validating user ownership of objects before serving data
- Log and monitor URL parameter changes for anomalies in authenticated sessions
- Use indirect references (e.g., hashed IDs) instead of sequential numeric identifiers

## Objectives

1. Access unauthorized FTP server configurations
2. Extract credentials for external FTP/sFTP connections
3. Demonstrate potential for configuration updates or deletions

## Instructions

### Step 1: Identify Baseline URL

**Context**: Locate the ID parameter in your own FTP management page.

After login, navigate to your FTP server page, noting the URL structure (e.g., https://████████/█████/filepush/ftp/303/).

> The ID (303) is the direct object reference; this is the manipulation point.

### Step 2: Tamper with ID Parameter

**Context**: Replace the ID to target another user's server.

Edit the URL by changing the ID to a different value (e.g., https://████████/█████/filepush/ftp/1/) and press Enter to load.

> If valid, the page displays the target server's details: hostname, username, password, and path in editable fields. No error or redirect occurs due to missing validation.

### Step 3: Interact with Exposed Data

**Context**: Verify and exploit the access.

View the credentials; optionally, test update/delete functions or copy details for external use.

> Success: Full configuration visible and modifiable, confirming IDOR exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- ftp-credentials
- dod
- unauthorized-access
