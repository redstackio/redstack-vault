---
id: proc-save-request-file
tags:
  - request-export
  - automation-prep
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
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:46:26.005Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Save-Modified-Request-for-Automation

## Summary

Export the intercepted and payload-modified HTTP request from Burp Suite to a file for use in automated tools like sqlmap.

## Description

Saving the request preserves the full HTTP structure, including headers, cookies, and the injectable selMajcom parameter, allowing seamless transition to automated exploitation without manual repetition.

## Requirements

1. Modified request in Burp Repeater or Intruder
2. File system access for export
3. sqlmap installed for subsequent use

## Defense

Defensive measures and detection strategies:

- Monitor for exported request artifacts in logs if proxy is internal
- Use request signing or nonces to invalidate replayed requests

## Objectives

1. Create a reusable request file for sqlmap
2. Maintain session integrity in the export
3. Enable scalable testing

## Instructions

### Step 1: Prepare Request

**Context**: Ensure the request includes the SQLi payload.

In Burp Repeater, verify the selMajcom parameter has a test payload.

> Request is ready with authentication headers.

### Step 2: Export to File

**Context**: Save the raw request.

Right-click the request in Repeater and select "Copy to file" or use the save option, naming it dod.txt.

> Expected output: dod.txt file containing the full HTTP request text, e.g., GET /path?selMajcom=MAT';... HTTP/1.1\nHost: ...\nCookie: ... 

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-export]]
- [[automation-prep]]
