---
id: proc-120312-submit-request
tags:
  - web
  - http-request
  - exploit
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.342Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit Modified Venue Creation Request

## Summary

This procedure resubmits the tampered HTTP request to the Veris venue creation endpoint, exploiting IDOR to create a venue under an unauthorized parent and achieve privilege escalation.

## Description

With the 'parent' parameter modified, submitting the request tests the lack of authorization checks. The endpoint processes the request without validating permissions, resulting in the creation of a venue in a restricted hierarchy. This can lead to broader compromises like accessing sensitive areas.

## Requirements

1. Modified HTTP request with unauthorized 'parent'
2. Active authenticated session
3. Access to submission tool (proxy or HTTP client)

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and ownership checks on all parameters
- Rate-limit and monitor creation requests for anomalies

## Objectives

1. Execute the exploit to create unauthorized venue
2. Confirm server acceptance without errors
3. Escalate privileges through hierarchy access

## Instructions

### Step 1: Replay Request via Proxy

**Context**: Forward the modified request to the server.

In the proxy tool's repeater, paste and send the altered POST request to /api/venues.

**Expected Output**: HTTP 200 response with success message and new venue ID.

### Step 2: Handle Any Redirects or Follow-ups

**Context**: Follow any post-creation redirects if needed.

Monitor for additional requests triggered by creation and ensure they succeed.

**Expected Output**: No authorization denial in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[http-request]]
- [[exploit]]
