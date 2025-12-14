---
id: proc-uuid-003
tags:
  - file-download
  - credential-harvest
  - info-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-download-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:56.875Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Download-and-Inspect-Exposed-Sensitive-File

## Summary

This procedure covers downloading an exposed JSON file from a web server and inspecting it for sensitive information like API credentials and passwords.

## Description

Once a directory is accessed, files like json.json can be downloaded to reveal unredacted data such as customer_key, customer_secret, and jira_password. This targets misconfigured dev servers and can lead to unauthorized access to services like Twitter API or Jira. Inspect using text editors or jq for JSON parsing; assumes prior directory access.

## Requirements

1. Direct URL to the exposed file (e.g., https://cards-dev.twitter.com/keys/json.json)
2. Download tool (curl or wget)
3. JSON parser (cat, jq) for inspection

## Defense

Defensive measures and detection strategies:

- Rotate credentials immediately upon exposure detection
- Sanitize and remove exposed endpoints from production/dev servers
- Implement file access logging and anomaly detection with SIEM tools

## Objectives

1. Retrieve the sensitive file securely
2. Extract and validate credentials
3. Assess potential impact on linked services

## Instructions

### Step 1: Download the File

**Context**: Use curl to fetch the JSON file to local storage.

**Command** ([[commands/curl-download-file]]):
```bash
curl -k -O https://cards-dev.twitter.com/keys/json.json
```

> The -O flag saves the file locally. Expected output: File saved as json.json.

### Step 2: Inspect File Contents

**Context**: Open and review the file for sensitive data.

**Command** ([[commands/curl-download-file]]):
```bash
cat json.json | jq '.'
```

> Use jq for formatted JSON view; look for keys like "customer_key". Expected output: Parsed JSON showing credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-download-file]]

## Tools Used


## Tags

- credential-harvest
- file-download
