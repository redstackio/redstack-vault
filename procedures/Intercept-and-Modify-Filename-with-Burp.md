---
id: proc-713407-intercept-modify
tags:
  - intercept
  - burp
  - modify
  - filename
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
  - '[[Web Protocols]]'
updated_at: '2025-12-14T17:26:56.301Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Intercept-and-Modify-Filename-with-Burp

## Summary

This procedure uses Burp Suite to intercept the profile picture upload request and inject special characters into the filename, setting up the ActiveStorage exception for DoS.

## Description

During the upload to https://hackerone.com, intercept the multipart/form-data POST request and alter the filename parameter to include disruptive characters like '+', '%20', or '%0d%0a'. This exploits poor sanitization in ActiveStorage, leading to processing failures. Prerequisites include Burp proxy setup and ongoing upload attempt.

## Requirements

1. Burp Suite running as proxy (e.g., 127.0.0.1:8080)
2. Browser configured to route traffic through Burp
3. Captured upload request from standard upload

## Defense

Defensive measures and detection strategies:

- Sanitize filenames on server-side before ActiveStorage processing
- Detect anomalous request modifications via WAF

## Objectives

1. Intercept the upload request payload
2. Modify filename to trigger exceptions
3. Prepare malicious request for submission

## Instructions

### Step 1: Configure Interception

**Context**: Set up Burp to catch the specific request.

No command required; in Burp Proxy > Intercept, enable interception for the upload endpoint.

> Traffic halts at the upload POST request.

### Step 2: Edit Filename Parameter

**Context**: Inject special characters into the filename.

No command required; in the intercepted request, locate the filename in the Content-Disposition header (e.g., filename="image.jpg") and change to filename="image%20+.jpg" or similar.

> Updated request shows modified parameter; drop or forward as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Web Protocols]] Application Layer Protocol

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- burp
- modify
- filename
