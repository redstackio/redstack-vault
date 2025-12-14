---
id: proc-intercept-extraction
tags:
  - intercept
  - extraction
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:08.691Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Intercept-and-Trigger-RAR-Extraction

## Summary

This procedure triggers the RAR extraction in Nextcloud while intercepting the HTTP request to prepare for payload injection into the vulnerable parameters.

## Description

The 'Extract Here' action sends a POST to extractRar.php, where $file and $dir are unsanitized. Intercept with a proxy to modify. Expected outcome: Captured request ready for tampering.

## Requirements

1. Uploaded RAR file
2. Burp Suite configured as proxy
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Input validation on file parameters
- WAF rules for command injection patterns
- Proxy logging for request modifications

## Objectives

1. Initiate the vulnerable extraction
2. Capture the injectable request
3. Position for command injection

## Instructions

### Step 1: Trigger Extraction

**Context**: Start the extraction to generate the request.

No command required.

> Right-click sample.rar > Extract Here. Expected output: Request intercepted in Burp.

### Step 2: Inspect Request

**Context**: Verify parameters for injection points.

Use Burp Suite interface.

> Examine POST body for nameOfFile. Expected output: Unsanitized parameters visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- extraction
