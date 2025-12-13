---
tags:
  - injection
  - bypass
type: procedure
tools:
  - '[[tools/Proxy-Tool]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 656f4de0-d08e-4555-923a-822f53fd9213
created_at: '2025-12-13T09:01:26.301Z'
updated_at: '2025-12-13T09:01:26.301Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Inject Modified Response and Bypass Authentication

## Summary

This procedure replaces the SAMLResponse in the intercepted request with the modified version and forwards it to complete the bypass.

## Description

By injecting the tampered response, the application validates the signature on the original but processes assertions from the malicious one, granting access as the specified user.

## Requirements

1. Intercepted request in proxy
2. Modified SAMLResponse from POC
3. Network access to server

## Defense

Defensive measures and detection strategies:

- Ensure signature covers the entire response
- Validate Response elements strictly

## Objectives

1. Replace SAMLResponse parameter
2. Forward the tampered request
3. Achieve unauthorized login

## Instructions

### Step 1: Edit the Intercepted Request

**Context**: Paste the modified SAMLResponse into the request.

In [[tools/Proxy-Tool]], edit the SAMLResponse parameter with the new value.

> Ensure it's URL-encoded if necessary.

### Step 2: Forward the Request

**Context**: Send the modified request to the server.

Release the request from the proxy to the Rocket.Chat server.

> Login should succeed as the targeted user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Proxy-Tool]]

## Tags

- injection
- bypass
