---
tags:
  - intercept
  - proxy
type: procedure
tools:
  - '[[tools/Proxy-Tool]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 586b56f0-90e7-4b2a-b8ca-c2d2c9a15409
created_at: '2025-12-13T09:01:26.311Z'
updated_at: '2025-12-13T09:01:26.311Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept SAML Login Request

## Summary

This procedure involves using a proxy to capture the SAML login POST request and extract the SAMLResponse for modification.

## Description

During the SAML authentication process, a POST request is sent with the SAMLResponse. Intercepting this allows extraction of the encoded response, which is then fed into the POC script for tampering.

## Requirements

1. Proxy tool configured to intercept traffic
2. Access to the Rocket.Chat login page
3. Network position to MITM the request

## Defense

Defensive measures and detection strategies:

- Use HTTPS with HSTS to prevent interception
- Monitor for proxy usage indicators in logs

## Objectives

1. Capture the SAML POST request
2. Extract URL-encoded SAMLResponse
3. Prepare for response modification

## Instructions

### Step 1: Set Up Proxy

**Context**: Configure the proxy to intercept requests to the Rocket.Chat server.

Launch [[tools/Proxy-Tool]] and set it as the system proxy.

> Ensure traffic to the login endpoint is routed through the proxy.

### Step 2: Perform Login Attempt and Intercept

**Context**: Initiate SAML login and capture the POST.

Attempt to log in via SAML and pause the request in the proxy when the POST with SAMLResponse is sent.

> Copy the URL-encoded SAMLResponse parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Proxy-Tool]]

## Tags

- intercept
- proxy
