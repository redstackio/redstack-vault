---
id: proc-uuid-003
tags:
  - stored-xss
  - cookies
  - headers
  - survey-pages
type: procedure
tools: []
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
updated_at: '2025-12-14T17:26:55.832Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Stored-XSS-in-Cookies-and-Headers-on-Survey-Pages

## Summary

This procedure uncovers stored XSS in cookie and header combinations on survey input pages, where payloads persist and execute for users accessing the affected content.

## Description

Endpoints like /mz-survey/interview/collectQuestions_input.htm/ on Glassdoor fail to encode inputs from cookies and custom headers, allowing stored XSS when combined with cache poisoning. This turns transient inputs into persistent threats.

## Requirements

1. Access to survey endpoints
2. Capability to set custom headers and cookies
3. Testing environment for persistence

## Defense

Defensive measures and detection strategies:

- Encode all outputs from headers and cookies
- Avoid storing untrusted data in sessions or caches
- Log and monitor anomalous header values

## Objectives

1. Inject persistent XSS via cookie-header
2. Verify storage and execution across sessions
3. Integrate with cache mechanisms for broader impact

## Instructions

### Step 1: Inject via Header and Cookie

**Context**: Combine header and cookie for storage trigger.

Send request with custom header:

```bash
curl -v -b "surveycookie=<script>alert(document.domain)</script>" -H "X-Survey-Header: <script>alert(1)</script>" "https://target.com/mz-survey/interview/collectQuestions_input.htm/"
```

> Inspect response for stored reflection.

### Step 2: Check Persistence

**Context**: Reload or access from new session to confirm storage.

Repeat request without injection; payload should remain if stored.

**Expected Output**: Script executes on subsequent loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None specific

## Tags

- stored-xss
- mz-survey
- headers
