---
id: proc-unauthorized-access-001
tags:
  - idor-exploit
  - unauthorized-modify
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
updated_at: '2025-12-14T17:25:23.595Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access and Modify Scorecard Unauthorized

## Summary

This core exploitation procedure uses the IDOR flaw to directly access a victim's scorecard URL from an attacker account, enabling viewing, editing, permission changes, and downloading without ownership verification.

## Description

IDOR vulnerabilities arise when applications expose internal object references in URLs without backend checks. Here, the scorecard name in https://demo.sftool.gov/TwsHome/ScorecardManage/{name} allows any authenticated user to manipulate objects by crafting or reusing URLs. The attacker loads the URL, interacts with the interface to edit fields, assign permissions (read-only/edit to arbitrary users), and export data. Impacts include data tampering and exposure; prerequisites are the target URL and attacker session.

## Requirements

1. Known scorecard URL from victim creation
2. Active attacker login session
3. Browser capable of form interactions and downloads

## Defense

Defensive measures and detection strategies:

- Validate object ownership on every access endpoint
- Obfuscate identifiers with hashes or tokens
- Monitor for direct URL hits and anomalous permission changes

## Objectives

1. Gain read access to unauthorized object
2. Perform write operations and permission escalation
3. Exfiltrate data via download

## Instructions

### Step 1: Load Direct URL

**Context**: Bypass dashboard to force access.

No specific command; enter https://demo.sftool.gov/TwsHome/ScorecardManage/testdsfdfsf in the browser address bar while logged in as attacker.

> Page loads with full scorecard view.

### Step 2: View and Edit Content

**Context**: Interact with the exposed object.

No specific command; inspect fields, modify information (e.g., update descriptions or data), and save changes.

> Edits apply without error, confirming write access.

### Step 3: Assign Permissions and Download

**Context**: Escalate by altering controls and extracting data.

No specific command; navigate to permissions section, add read-only or edit access for other users, then select download option.

> Permissions update; file downloads successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-bypass]]
- [[data-modification]]
- [[web-exploit]]
