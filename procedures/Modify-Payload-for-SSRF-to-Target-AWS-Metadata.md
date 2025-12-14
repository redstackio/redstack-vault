---
id: proc-infogram-ssrf-payload-001
tags:
  - ssrf-payload
  - aws-metadata
type: procedure
tools:
  - '[[tools/Infogram-Java-API-Library]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Set-Content-SSRF-Payload]]'
verified: false
platforms:
  - Web
  - AWS
  - Java
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[T1210.001]]'
updated_at: '2025-12-14T17:32:10.706Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1210.001]]'
---
# Modify-Payload-for-SSRF-to-Target-AWS-Metadata

## Summary

This procedure updates the 'content' payload to include an iframe sourcing the AWS instance metadata endpoint, chaining XSS to SSRF during preview rendering on the backend.

## Description

Building on XSS, the iframe src points to internal 169.254.169.254, exploited when the AWS-hosted Infogram server generates previews. This leaks metadata like instance IDs or credentials in images. Prerequisites: Base XSS success. Target: API creation with new payload. Outcomes: Stored SSRF for data exfil.

## Requirements

1. Existing parameters map from XSS step
2. Knowledge of AWS metadata service URL
3. API client ready

## Defense

Defensive measures and detection strategies:

- Validate and block internal/private IPs in URL attributes during rendering
- Disable or sandbox iframe rendering in preview generation
- Monitor backend logs for requests to link-local addresses like 169.254.169.254

## Objectives

1. Inject SSRF via iframe in stored content
2. Target internal AWS services
3. Prepare for metadata disclosure in previews

## Instructions

### Step 1: Update Content Parameter

**Context**: Replace XSS with SSRF payload.

Execute [[commands/Set-Content-SSRF-Payload]]:

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<iframe src=http://169.254.169.254/latest/meta-data/></iframe>\"}"]");
```

> Escaped JSON with iframe to metadata. Expected: Parameter updated.

### Step 2: Reuse Creation Process

**Context**: Submit as before.

Repeat API POST using updated parameters (from prior creation procedure).

> Expected: 201 response for new infographic.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1210.001]] Exploitation of Remote Services

### Sub-Techniques

-

## Commands Used

- [[commands/Set-Content-SSRF-Payload]]

## Tools Used

- [[tools/Infogram-Java-API-Library]]

## Tags

- ssrf
- iframe-injection
