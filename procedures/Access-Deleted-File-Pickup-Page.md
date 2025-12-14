---
id: proc-496326-step1
tags:
  - recon
  - web
  - dod
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.905Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Deleted-File-Pickup-Page

## Summary

This procedure involves navigating to the file pickup page in the DoD sharing system using a known deleted file ID to confirm accessibility and gather details for exploitation.

## Description

In the attack scenario, attackers with knowledge of a file ID (e.g., from prior emails or uploads) access the pickupfiles.aspx endpoint. Even for deleted files, the page loads without CAC, revealing the file's status. This step sets up the environment for cookie forgery by confirming the ID and observing the deletion state. Prerequisites include network access to the system and the file ID; no authentication is needed initially.

## Requirements

1. Network access to the DoD file sharing domain (e.g., https://███████/██████/)
2. Known file ID (e.g., 15849581 from upload history or leak)
3. Web browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Enforce CAC for all pickup page access
- Log and monitor accesses to deleted file IDs
- Implement rate limiting on ID-based requests

## Objectives

1. Confirm file ID and deletion status
2. Gather endpoint details for later requests
3. Validate public accessibility without auth

## Instructions

### Step 1: Navigate to Pickup Page

**Context**: Use a browser or client to load the page with the deleted file ID, observing the interface.

No specific command; use browser URL: https://███████/██████/pickupfiles.aspx?id=15849581

> The page should load, showing file details but indicating unavailability due to deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[dod]]
