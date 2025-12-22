---
id: proc-relay-cookies-auth-bypass
tags:
  - authentication-bypass
  - csrf-bypass
  - session-hijacking
type: procedure
tools:
  - '[[tools/Intercepting-Proxy-Tool]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T04:39:01.849Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Pass the Hash]]'
---
# Relay Captured Cookies To Bypass Authentication

## Summary

This procedure uses an intercepting proxy to inject stolen SSO cookies into the attacker's session, relaying the CSRF state to complete authentication and impersonate the victim.

## Description

With captured data, the attacker starts a new browser session, sends the auth URL with state cookie via proxy to auth.uber.com, intercepts the response, swaps _csid with victim's, and forwards Set-Cookie headers. This bypasses CSRF without IP checks, granting access to riders.uber.com/trips as the victim.

## Requirements

1. Captured cookies/tokens from prior step
2. Intercepting proxy like Burp Suite
3. Separate browser for attacker session

## Defense

Defensive measures and detection strategies:

- Implement IP validation for session resumption
- Use short-lived CSRF tokens not relayable
- Log and alert on cookie modifications or anomalous auth flows

## Objectives

1. Bypass SSO using relayed credentials
2. Achieve account takeover
3. Access protected Uber services

## Instructions

### Step 1: Initiate Relay Request

**Context**: Send captured URL and state cookie to auth endpoint.

**Instructions**: Configure proxy to target auth.uber.com, paste captured Cookie header, and submit request.

> Intercept at response. Expected: Auth response with Set-Cookie for new session.

### Step 2: Inject Victim's Cookie and Forward

**Context**: Modify response to steal session.

**Instructions**: Replace _csid in Set-Cookie with victim's value, drop other attacker cookies, and forward to browser.

> Browser completes redirect to riders.uber.com as victim. Success: Authenticated access confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Intercepting-Proxy-Tool]]

## Tags

- authentication-bypass
- csrf-bypass
- session-hijacking
