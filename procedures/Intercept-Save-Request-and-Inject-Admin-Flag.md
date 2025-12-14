---
tags:
  - privilege-escalation
  - payload-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:59.128Z'
skill_level: advanced
impact_level: high
sub_techniques: []
id: bcd737bb-f07b-407e-8dec-927ce412f869
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Intercept-Save-Request-and-Inject-Admin-Flag

## Summary

This procedure uses a proxy to intercept the POS User edit form submission in Stocky app and injects an 'admin=1' parameter to elevate privileges.

## Description

Submit the modified form while proxying the POST request to the save endpoint, appending 'user[admin]=1' to the form data. This bypasses frontend restrictions in the Shopify Stocky app due to backend validation gaps. Prerequisites: Configured proxy and edited form. Outcome: POS User becomes admin, creating backdoor.

## Requirements

1. Running HTTP proxy like Burp Suite
2. Browser traffic routed through proxy
3. Modified form ready for submission

## Defense

Defensive measures and detection strategies:

- Validate all incoming parameters against allowed fields
- Reject unauthorized flags like 'admin' in user updates
- Monitor for proxy-intercepted requests via WAF logs

## Objectives

1. Inject admin privilege flag
2. Complete user update
3. Verify escalation

## Instructions

### Step 1: Configure Proxy

**Context**: Route traffic for interception.

Set browser proxy to Burp Suite (e.g., 127.0.0.1:8080) and enable intercept.

> Confirm traffic capture.

### Step 2: Submit and Modify

**Context**: Alter payload during transit.

Submit form; in proxy, add user[admin]=1 to POST data, then forward.

> Expected: 200 OK response, user updated.

### Step 3: Verify Escalation

**Context**: Test new admin access.

Logout and login with updated credentials to check admin features.

> Success: Full admin dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[privilege-escalation]]
- [[payload-injection]]
