---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Explore-Lark-AutoReply-Feature
tags:
  - recon
  - lark
  - autoreply
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-config]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:28.501Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Account Discovery]]'
---
# Explore-Lark-AutoReply-Feature

## Summary

This reconnaissance procedure involves exploring Lark's AutoReply feature to identify how files are referenced using alphanumeric IDs, setting the stage for IDOR exploitation by mapping out vulnerable endpoints and payload structures.

## Description

Lark's AutoReply allows automated messaging with file attachments, where files are referenced directly via IDs in API requests. By inspecting these interactions, attackers can uncover the lack of authorization on ID references. This occurs in the web platform, requiring an authenticated session, and helps in understanding the attack surface for subsequent manipulation. Outcomes include documented API behaviors and potential file ID patterns for targeting.

## Requirements

1. Valid Lark account credentials for authentication
2. Browser or API client (e.g., curl) to interact with the web interface
3. Access to developer tools for inspecting network requests
4. Basic knowledge of JSON payloads and HTTP methods

## Defense

Defensive measures and detection strategies:

- Log all AutoReply configuration accesses and review for unusual patterns
- Obfuscate internal API documentation and limit feature exploration via rate limits
- Implement client-side obfuscation of file IDs to hinder reconnaissance
- Use anomaly detection on session behaviors during feature usage

## Objectives

1. Map out AutoReply endpoints and file referencing mechanisms
2. Identify alphanumeric ID usage without auth checks
3. Gather prerequisites for IDOR exploitation

## Instructions

### Step 1: Authenticate and Access AutoReply

**Context**: Log in and navigate to the AutoReply section to trigger relevant API calls.

**Command** ([[commands/curl-fetch-config]]):
```bash
curl -X GET 'https://lark.example.com/api/v1/autoreply/config' -H 'Authorization: Bearer YOUR_TOKEN'
```

> Retrieves the current AutoReply setup. Expected output: JSON response showing file attachments and ID references, e.g., {"attachments": [{"id": "abc123"}]}. Use this to note the ID format.

### Step 2: Inspect File Attachment Requests

**Context**: Attempt to add a sample file to AutoReply and capture the request to analyze ID handling.

**Command** ([[commands/curl-fetch-config]]):
```bash
curl -X POST 'https://lark.example.com/api/v1/autoreply/test' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"test_response": "With file ID: SAMPLE_ID"}'
```

> Simulates a test response with a file ID. Expected output: Server echo or error revealing direct ID processing without validation. Document the endpoint for later manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-config]]

## Tools Used


## Tags

- recon
- lark
- autoreply
- discovery
