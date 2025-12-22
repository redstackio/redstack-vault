---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - recon
  - interception
  - csrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:42.775Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Vulnerable-Delete-Endpoint

## Summary

This procedure involves intercepting the album deletion request to identify the vulnerable GET endpoint lacking CSRF protections in the DoD media gallery.

## Description

To exploit the CSRF vulnerability, the attacker must first understand the delete mechanism. By performing a legitimate deletion from their account and capturing the traffic, the endpoint /mediagallery/delete/id/{album_id} is revealed as using GET without token validation. This is done in a web environment with proxy tools. Prerequisites: Authenticated session and interception tool. Outcome: Confirmed vulnerability details for PoC crafting.

## Requirements

1. Authenticated attacker account with an album
2. Proxy tool like Burp Suite configured
3. Browser traffic routed through proxy

## Defense

Defensive measures and detection strategies:

- Enforce POST for state-changing operations
- Implement CSRF tokens on all endpoints
- Monitor for proxy-intercepted traffic anomalies

## Objectives

1. Capture the delete request format
2. Verify absence of CSRF protections
3. Document endpoint for exploitation

## Instructions

### Step 1: Perform Deletion Action

**Context**: Trigger the delete to generate the request.

From the gallery, select the test album and choose delete option.

> Confirm deletion in UI; do not complete if not intercepting.

### Step 2: Intercept and Analyze

**Context**: Use proxy to capture and inspect the request.

Configure [[tools/Burp-Suite]] as proxy. Perform deletion and view in Proxy/HTTP history the GET to /mediagallery/delete/id/{album_id}.

> Note: Request lacks CSRF token; uses GET method, vulnerable to forgery.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[interception]]
