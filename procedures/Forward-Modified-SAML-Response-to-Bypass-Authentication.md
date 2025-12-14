---
tags:
  - saml
  - bypass
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
id: a949232b-deef-490b-ab8c-dc9f2f7e2635
created_at: '2025-12-14T17:31:19.331Z'
updated_at: '2025-12-14T17:31:19.331Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Forward Modified SAML Response to Bypass Authentication

## Summary

This procedure submits the altered SAMLResponse via proxy to exploit the validation flaw, resulting in unauthorized login to Rocket.Chat.

## Description

With the modified response, the server verifies the signature on the original but uses malicious assertions from the prepended Response, bypassing auth. This grants access as specified user. Targets the /auth/saml POST endpoint in Rocket.Chat.

## Requirements

1. Intercepted request in Burp Repeater or Proxy
2. Modified SAMLResponse from POC script
3. Valid session context from initial interception

## Defense

Defensive measures and detection strategies:

- Implement Response-Signature association checks
- Rate-limit SAML POSTs and validate XML schema
- Monitor for login successes with mismatched attributes

## Objectives

1. Complete the login with bypassed credentials
2. Verify access to targeted user account
3. Confirm admin privileges if applicable

## Instructions

### Step 1: Replace Parameter

**Context**: Update the request body in the proxy tool.

In Burp, edit the SAMLResponse value to the script output, keeping other params (e.g., RelayState) intact.

> Ensure URL-encoding is preserved.

### Step 2: Forward Request

**Context**: Send to server and observe response.

Click Forward in Burp Proxy or Send in Repeater.

> Expect 302 redirect to dashboard; check user profile for altered attributes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[saml]]
- [[bypass]]
