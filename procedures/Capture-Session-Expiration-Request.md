---
tags:
  - request-capture
  - proxy
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:29.811Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: a315cbd2-03d0-4d75-89fc-c897724f29ce
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Capture-Session-Expiration-Request

## Summary

This procedure intercepts the HTTP POST request sent when expiring the attacker's own sessions, providing a template for modification in the IDOR exploit.

## Description

To exploit the IDOR, the attacker first triggers the session expiration on their own account while proxying traffic. This captures the exact request format, including headers, parameters, and authenticity token, which can then be repurposed for the victim.

## Requirements

1. Proxy tool configured (e.g., [[tools/Burp-Suite]] intercepting browser traffic)
2. Active session in Shopify admin
3. Access to account settings page

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic patterns or repeated self-session expirations
- Enforce CSRF tokens validation strictly on session endpoints
- Use web application firewalls (WAF) to detect proxy signatures

## Objectives

1. Trigger and intercept the baseline expiration request
2. Extract request details for tampering
3. Ensure token validity for reuse

## Instructions

### Step 1: Configure Proxy

**Context**: Set up traffic interception before interacting with the page.

In [[tools/Burp-Suite]], configure the browser proxy to 127.0.0.1:8080 and enable intercept.

> Expected output: All HTTP traffic routed through Burp.

### Step 2: Trigger Expiration

**Context**: Initiate the action to generate the request.

Click 'Expire all sessions' on the account settings page.

> Burp captures the POST to /admin/settings/account/expire_specific_users_sessions/{attacker_id} with params utf8=%E2%9C%93&_method=patch&authenticity_token={token}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-capture]]
- [[proxy]]
- [[shopify]]
