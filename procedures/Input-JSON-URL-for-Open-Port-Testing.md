---
id: proc-infogram-open-port-test-001
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
updated_at: '2025-12-14T04:39:18.596Z'
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
# Input-JSON-URL-for-Open-Port-Testing

## Summary

This procedure involves entering a JSON URL targeting an open port to exploit SSRF, resulting in a connection attempt that reveals port status via error messages.

## Description

By inputting a URL like http://targethost:openport/data.json, the Infogram server fetches it, succeeding if open, and returns "Download failed". This differentiates open ports for scanning internal/external hosts.

## Requirements

1. JSON input field open
2. Known target host and open port (e.g., port 80)
3. Valid JSON endpoint on target

## Defense

Defensive measures and detection strategies:

- Whitelist allowed URLs and ports in SSRF filters
- Monitor server logs for outbound connections to non-standard ports
- Block requests to internal IPs

## Objectives

1. Trigger SSRF fetch to open port
2. Observe success indicator for port confirmation
3. Gather reconnaissance on host services

## Instructions

### Step 1: Construct URL

**Context**: Format the JSON URL with target host and open port.

```plaintext
http://example.com:80/data.json
```

> Ensure the endpoint returns valid JSON if fetched.

### Step 2: Submit and Observe

**Context**: Enter and submit the URL in the JSON field.

```plaintext
Paste URL into input > Submit
```

> Server attempts fetch; expect "Download failed" if open.

**Expected Output**: "Download failed" error confirms open port.

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
