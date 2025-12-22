---
id: proc-save-request-001
tags:
  - web
  - recon
  - file-prep
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:05.343Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Save HTTP Request for SQLMap

## Summary

This preparatory procedure saves the raw intercepted HTTP request to a file format compatible with SQLMap for automated exploitation.

## Description

SQLMap requires a raw HTTP request file (-r flag) to replay and test injections accurately. Saving the GET request from the proxy ensures all headers, including cookies and User-Agent, are preserved for the Acronis API endpoint.

## Requirements

1. Proxy tool with request history (e.g., Burp Suite)
2. Local file system access for saving
3. Text editor to verify file integrity

## Defense

Defensive measures and detection strategies:

- Log and alert on unusual request patterns or tools like SQLMap signatures
- Use request signing or tokens to prevent replay attacks
- Monitor for file-based request submissions in logs

## Objectives

1. Create a reusable request artifact
2. Enable automated testing without manual proxy use
3. Maintain session authenticity

## Instructions

### Step 1: Export from Proxy

**Context**: Copy the full raw request from the interception tool.

In Burp, right-click the request and select "Copy to file" or manually paste into a .txt file.

> File contains lines like GET /api/admin/pages... HTTP/1.1 followed by headers.

### Step 2: Verify File Content

**Context**: Ensure the file is correctly formatted.

Open the .txt file and confirm it starts with the method, URL, and includes the search parameter.

> No parsing errors when loaded into tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- recon
