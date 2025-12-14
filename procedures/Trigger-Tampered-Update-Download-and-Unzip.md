---
id: proc-concrete-update-trigger-001
tags:
  - update-trigger
  - zip-unzip
  - concrete-cms
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:24.100Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Python]]'
---
# Trigger-Tampered-Update-Download-and-Unzip

## Summary

This procedure initiates the update check in Concrete CMS, allowing the proxy to tamper the JSON response, download the malicious ZIP from the attacker server, and unzip it into the writable updates directory using a timestamp-based name.

## Description

With proxy rules active, the admin dashboard's update check fetches the tampered JSON over HTTP, believes an update (e.g., to 8.6) is available, downloads the ZIP, and unzips it to /updates/<php_time()>/, placing poc.php there. This exploits the writable directory and HTTP MITM. Prerequisites: prior steps completed; expected outcome: malicious files deployed for RCE access.

## Requirements

1. Admin access with proxy configured
2. Tampered JSON rules in Burp Suite
3. Malicious ZIP hosted and accessible
4. Writable /concrete/updates/ directory

## Defense

Defensive measures and detection strategies:

- Make updates directory read-only or non-web-accessible
- Verify update integrity with hashes/signatures
- Audit file creations in updates folder

## Objectives

1. Download and unzip malicious ZIP
2. Deploy payload in predictable location
3. Enable direct access for RCE

## Instructions

### Step 1: Initiate Update Check

**Context**: Trigger the JSON fetch to activate tampering.

In Dashboard > Extend > Dashboard > Updates, click 'Check for Updates'.

> Expected output: Proxy intercepts, modifies JSON; dashboard shows new version available.

### Step 2: Download and Install

**Context**: Proceed with the fake update to unzip payload.

Click 'Download' then 'Install'.

> Expected output: ZIP fetched from attacker server, unzipped to /updates/<timestamp>/ (timestamp from PHP time()). Verify directory creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Python]] PHP

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- update-trigger
- zip-unzip
- concrete-cms
