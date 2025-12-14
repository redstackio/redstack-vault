---
id: proc-bmc-traversal-lfi-2024
tags:
  - path-traversal
  - lfi
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:58.719Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Attempt Path Traversal LFI

## Summary

This procedure exploits insufficient input sanitization in the x-urlpath parameter to attempt Local File Inclusion (LFI) via directory traversal, targeting sensitive files like /passwd, though the read fails but sets up the auth bypass.

## Description

Applied to BMC Remedy AR System's login endpoint, this involves injecting ../ sequences into x-urlpath to traverse to root directories and read system files. While direct file disclosure doesn't occur due to protections, the malformed parameter disrupts auth logic. Prerequisites include access from Step 1; outcomes confirm traversal acceptance, leading to error states exploitable in follow-on steps.

## Requirements

1. Active session from login page navigation.
2. Browser developer tools for URL inspection/modification.
3. Understanding of Unix-like path structures for traversal depth.

## Defense

Defensive measures and detection strategies:

- Sanitize and normalize URL parameters to block ../ sequences using libraries like OWASP ESAPI.
- Log and alert on traversal patterns in web access logs (e.g., via SIEM rules for multiple ../ in queries).

## Objectives

1. Probe for LFI to map file system access.
2. Induce error state for auth bypass facilitation.
3. Validate parameter vulnerability without direct data leak.

## Instructions

### Step 1: Inject Traversal Payload

**Context**: Modify x-urlpath to traverse multiple directories aiming for /passwd.

**Action** (URL Manipulation):

Change the URL to: https://[redacted]?x-app=itsm&x-urlpath=../../../../../../../../passwd

> Use enough ../ to reach root (typically 10+ for web roots); load the URL to trigger the request.

### Step 2: Observe Failure

**Context**: Confirm LFI attempt fails but parameter is processed.

**Action** (Error Check):

Note the response (e.g., 404 or blank page).

> Expected: No file contents shown, but no 403/500 blocking the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- lfi
