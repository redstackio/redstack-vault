---
id: proc-extract-timestamp
tags:
  - recon
  - timestamp
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/grep-timestamp]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T05:32:13.408Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Extract-Upload-Timestamp

## Summary

This procedure parses the server's 500 error response to extract the upload timestamp, which is used to construct the predictable file path for the webshell.

## Description

The Monero forum's error message includes the save timestamp; grepping or inspecting the response yields this value, often in Unix format, enabling URL prediction without direct file listing access.

## Requirements

1. Server response from upload (via browser console or curl)
2. Basic text parsing tools (grep, etc.)
3. Knowledge of response format

## Defense

Defensive measures and detection strategies:

- Avoid leaking file paths or timestamps in error messages
- Use opaque error responses without sensitive details
- Log access to error endpoints

## Objectives

1. Identify the exact save time from response
2. Convert if needed for URL construction
3. Facilitate shell access

## Instructions

### Step 1: Capture and Parse Response

**Context**: Extract timestamp from the 500 error body.

**Command** ([[commands/grep-timestamp]]):
```bash
grep -o '[0-9]\{10\}' error_response.txt
```

> Assumes response saved to file; extracts 10-digit Unix timestamp. Expected output: e.g., 1527341299.

**Success Indicators**:
- Timestamp matches upload time
- Usable in URL

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/grep-timestamp]]

## Tools Used


## Tags

- error-parsing
- path-prediction
