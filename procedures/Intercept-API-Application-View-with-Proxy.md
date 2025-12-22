---
id: proc-pressable-intercept-view
tags:
  - proxy
  - intercept
  - pressable
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.401Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept API Application Details View with Proxy

## Summary

This procedure sets up a proxy to monitor and intercept HTTP traffic when viewing an API application details page in Pressable, capturing session tokens and request structures for modification.

## Description

To exploit the IDOR, intercept the GET request for the application details view using a proxy tool. This occurs on the web platform and requires configuring the browser to route traffic through the proxy. The expected outcome is visibility into the application's update flow, including authenticity_token.

## Requirements

1. Proxy tool (e.g., Burp Suite) installed and running
2. Browser configured for proxy interception (e.g., FoxyProxy extension)
3. Valid Pressable session

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to complicate proxy interception
- Log and alert on proxy-like traffic patterns from user IPs

## Objectives

1. Capture application view request
2. Extract authenticity_token
3. Prepare for update request interception

## Instructions

### Step 1: Configure Proxy and View Application

**Context**: Enable proxy and access the application details to trigger the GET request.

No specific command; perform via tool interface:

- Start Burp Suite and configure proxy listener on 127.0.0.1:8080
- Set browser proxy to match
- Navigate to the created application's details page in Pressable

> Proxy intercepts the GET request. Inspect for session cookies and tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[proxy]]
- [[intercept]]
- [[pressable]]
