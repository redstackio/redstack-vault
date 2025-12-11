---
tags:
  - request-hijacking
  - open-redirect
type: procedure
tools:
  - '[[tools/Smuggler]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator-Client]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/smuggler-discover-vuln]]'
  - '[[commands/http-smuggling-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 52a25c3f-923b-420a-8406-d4f92b7b9ffb
created_at: '2025-12-11T06:10:33.358Z'
updated_at: '2025-12-11T06:10:33.358Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Hijack Victim Requests and Trigger Open Redirect

## Summary

This procedure involves monitoring the effects of a poisoned socket, where hijacked victim requests are forced into a GET that triggers a 301 open redirect on the backend, including sensitive cookies.

## Description

After poisoning, incoming requests are desynced, interpreted as a GET to the attacker's URL, leading to redirects that leak cookies like 'd'. This is passive but requires prior exploitation. Targets backend servers vulnerable to open redirects on absolute URLs.

## Requirements

1. Successfully poisoned socket from prior step.
2. Active victim traffic to the target.
3. Monitoring setup for redirects.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect URLs to prevent open redirects.
- Monitor for unexpected 301 responses with external URLs.

## Objectives

1. Hijack victim requests.
2. Trigger backend open redirect.
3. Facilitate cookie leakage.

## Instructions

### Step 1: Monitor for Hijacked Requests

**Context**: Wait for victim requests to hit the poisoned socket; no command needed, but observe backend behavior.

> The backend will interpret the hijacked request as GET https://<URL> HTTP/1.1, resulting in a 301 redirect including cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[request-hijacking]]
- [[open-redirect]]
