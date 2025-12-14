---
id: proc-capture-cookie
tags:
  - credential-access
  - cookie-theft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T04:38:39.639Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Unsecured Credentials]]'
---
# Capture Leaked Session Cookie

## Summary

This procedure intercepts and logs the SSO session cookie from victim requests to the malicious subdomain, then validates it against the authentication API.

## Description

The imagefetch.php script in the attack logged the UBIC_AUTH cookie in HTML comments and used it to query sso.ubnt.com/api/sso/v1/user/self, confirming the session's value for hijacking.

## Requirements

1. Malicious server receiving victim traffic
2. Intercepting proxy for traffic analysis
3. Valid endpoint for cookie testing (e.g., SSO API)

## Defense

Defensive measures and detection strategies:

- Log and alert on cookie access from unexpected subdomains
- Use short-lived session tokens and monitor for anomalous API calls with stolen creds

## Objectives

1. Extract the session cookie from request headers
2. Store it securely for reuse
3. Prove validity by fetching user data

## Instructions

### Step 1: Log Incoming Requests

**Context**: Modify the script to capture cookies passively.

**Instructions**: In imagefetch.php, use print_r($_COOKIE) in <!-- --> comments; serve a benign image to avoid suspicion.

### Step 2: Intercept with Proxy

**Context**: Monitor traffic for detailed analysis.

**Instructions**: Configure browser or server to route through [[tools/Burp-Suite]]; inspect headers for UBIC_AUTH on requests to ping.ubnt.com.

### Step 3: Validate Cookie

**Context**: Test the cookie's usability.

**Instructions**: Use curl or the script to send a request to https://sso.ubnt.com/api/sso/v1/user/self with Cookie: UBIC_AUTH=leaked_value. Check for 200 OK with user JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[credential-access]]
- [[cookie-theft]]
