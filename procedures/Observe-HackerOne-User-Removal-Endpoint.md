---
tags:
  - recon
  - web
  - hackerone
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
updated_at: '2025-12-14T17:25:23.564Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3ce6a606-dcf5-4bdb-a205-240a6a14f778
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-HackerOne-User-Removal-Endpoint

## Summary

This procedure involves monitoring network traffic to identify the DELETE endpoint for removing external users from HackerOne bug reports, revealing the request structure for subsequent exploitation.

## Description

In the context of testing HackerOne's bug report management, use developer tools or a proxy to capture the legitimate removal request. This endpoint is vulnerable to IDOR, allowing parameter manipulation. Prerequisites include an authenticated session with access to a report containing external users.

## Requirements

1. Authenticated HackerOne session as a report participant
2. Access to browser developer tools or a web proxy (e.g., Burp Suite)
3. A bug report ID with at least one external user

## Defense

Defensive measures and detection strategies:

- Implement request logging for DELETE operations on user management endpoints
- Use web application firewalls (WAF) to monitor for parameter tampering in authenticated requests

## Objectives

1. Capture the exact request format for user removal
2. Identify required headers like CSRF token and authentication cookies
3. Prepare for IDOR testing by understanding the endpoint

## Instructions

### Step 1: Initiate Legitimate Removal

**Context**: Perform a standard removal of an invited external user to trigger the request.

No specific command; use the HackerOne UI to remove a participant and monitor the network tab in browser dev tools.

> Observe the DELETE request to /reports/<report_id>/external_users/<user_id> with headers including X-CSRF-Token, Cookie, Referer, and X-Requested-With: XMLHttpRequest.

### Step 2: Document Request Structure

**Context**: Note all parameters and headers for replication.

No command; manually record the Host (hackerone.com), method (DELETE), and any Accept headers.

> Expected: Full request details ready for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
