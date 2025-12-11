---
id: 098695ed-f8fb-4ecc-9f73-eec861cb2c2f
name: Trigger SSRF by Submitting Malicious URL
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.612Z'
updated_at: '2025-12-11T06:10:15.612Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - api-exploit
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
platforms:
  - Web
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Trigger SSRF by Submitting Malicious URL

## Summary

This procedure submits a malicious URL to the Snapchat API to trigger server-side fetching of the rebinding payload.

## Description

By providing the URL to the /api/v1/media/import endpoint, the server fetches and processes the malicious HTML, enabling the JS to run in the server's context.

## Requirements

1. Access to the import interface
2. Malicious HTML hosted
3. Valid session in Snapchat business

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL parameters
- Implement SSRF protections like URL blacklisting

## Objectives

1. Force server to fetch arbitrary URL
2. Load malicious JS payload
3. Initiate rebinding sequence

## Instructions

### Step 1: Submit URL to Endpoint

**Context**: Hit the API with the malicious URL parameter.

Submit to /api/v1/media/import on ads.snapchat.com with URL set to http://demon.███████/ssrf.html.

> This triggers the SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[ssrf]]
- [[api-exploit]]
