---
tags:
  - direct-exploitation
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:30:47.137Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e7d1c809-f1ce-453d-9c2e-b49abf76a0f7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Steal Web Session Cookie]]'
---
# Directly-Access-Specific-ELMAH-Log

## Summary

This procedure directly requests a specific ELMAH log detail using its ID, bypassing UI to extract sensitive information like cookies and secrets.

## Description

Using the detail endpoint with a known log ID (e.g., from list), attackers retrieve full log contents including user sessions, AUTH_PASSWORD, and IP addresses. This scripted approach allows automation for multiple logs, facilitating ATO via session hijacking.

## Requirements

1. Log ID obtained from list
2. Curl or similar for direct GET
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Authenticate detail endpoints
- Validate log ID access with object-level controls
- Audit direct API calls to ELMAH

## Objectives

1. Retrieve specific log details
2. Extract hijackable sessions
3. Collect PII for further attacks

## Instructions

### Step 1: Direct Detail Request

**Context**: Construct URL with log ID and fetch details.

**Command** ([[commands/curl-access-url]]):
```bash
curl https://proze.yelp.com/tmwebapi/elmah.axd/detail?id=5A4E7ED8-28E8-4E39-9017-F55E2C9F5371
```

> Expected output: Full log XML/HTML with sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[direct-exploitation]]
- [[credential-theft]]
