---
id: p-attempt-xss-payload-length-limit
tags:
  - xss
  - payload-testing
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.975Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Attempt XSS Payload with Length Limitation

## Summary

This procedure tests an initial XSS payload in the URL path, revealing a character length restriction that prevents full execution.

## Description

A URL-encoded payload like '%22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3e' (decoding to "<img src=x onerror=><svg onload=alert(1)>) is inserted into the /Job/ path. The web platform truncates longer inputs, blocking execution. This step confirms the vulnerability but highlights the need for bypass.

## Requirements

1. Identified reflection point
2. URL encoding knowledge
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Enforce strict URL path length limits with validation
- Log and alert on encoded payloads in paths

## Objectives

1. Verify XSS potential
2. Document length restriction
3. Prepare for bypass

## Instructions

### Step 1: Encode and Insert Payload

**Context**: URL-encode the payload and append to the path before the existing search term.

Construct URL:

```url
https://www.glassdoor.co.in/Job/%22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3epratt-whitney-jobs-SRCH_KE0,13.htm?
```

> Load the page. Expected output: Payload partially reflected but truncated; no alert due to length limit.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[xss]]
- [[payload-testing]]
