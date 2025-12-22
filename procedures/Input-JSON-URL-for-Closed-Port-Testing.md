---
id: proc-infogram-closed-port-test-001
tags:
  - ssrf
  - port-scanning
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:18.593Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Input-JSON-URL-for-Closed-Port-Testing

## Summary

This procedure tests a closed port by inputting a JSON URL, leveraging SSRF to observe failure responses that confirm port closure.

## Description

Inputting a URL like http://targethost:closedport/data.json causes a connection timeout or refusal, yielding "Invalid data source". Combined with open port tests, this enables full port scanning.

## Requirements

1. JSON input field open
2. Known target host and closed port (e.g., port 9999)
3. Valid JSON endpoint setup

## Defense

Defensive measures and detection strategies:

- Implement URL sanitization to block non-standard ports
- Alert on repeated failed fetches in application logs
- Use firewalls to restrict outbound traffic

## Objectives

1. Trigger SSRF failure on closed port
2. Differentiate via error message
3. Complete port status mapping

## Instructions

### Step 1: Construct URL

**Context**: Format the JSON URL with target host and closed port.

```plaintext
http://example.com:9999/data.json
```

> The port should have no listening service.

### Step 2: Submit and Observe

**Context**: Enter and submit the URL.

```plaintext
Paste URL into input > Submit
```

> Server fails to connect; expect "Invalid data source".

**Expected Output**: "Invalid data source" confirms closed port.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[port-scanning]]
