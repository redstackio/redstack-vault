---
id: proc-uuid-2
tags:
  - csrf
  - token-revocation
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:39.305Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Submit-Form-to-Revoke-API-Token

## Summary

This procedure delivers and executes the malicious HTML form in the victim's browser, forcing a CSRF request to the Enjin GraphQL interface that revokes their API token using the active session.

## Description

Once the form is crafted, the attacker lures the victim to load the page (e.g., via email or malicious site). The browser, if authenticated to Enjin, will submit the form using the session token, bypassing XSRF checks and revoking the token. This disrupts API access, potentially locking the victim out of services. Expected outcome: Token invalidation without user consent.

## Requirements

1. Crafted HTML form from prior procedure
2. Delivery method (e.g., phishing link to hosted HTML)
3. Victim's active Enjin session

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) to prevent cross-site submissions
- Log and alert on token revocations from unexpected sources
- Educate users on phishing and suspicious links

## Objectives

1. Execute the CSRF attack to revoke the token
2. Confirm disruption of victim's platform access
3. Validate the bypass of XSRF protection

## Instructions

### Step 1: Host the Malicious HTML

**Context**: Serve the form on an attacker-controlled domain to avoid origin restrictions.

Use a simple web server:

```bash
python3 -m http.server 8000
```

Place the HTML file in the directory and note the URL (e.g., http://attacker.com/csrf.html).

### Step 2: Deliver to Victim

**Context**: Trick the victim into visiting the URL while logged into Enjin.

Send a phishing email or link: "Click here to claim your Enjin reward: http://attacker.com/csrf.html".

### Step 3: Verify Revocation

**Context**: Monitor or check if the token is revoked post-submission.

After victim visits, attempt API calls with the token; expect 401 Unauthorized.

> Successful execution: GraphQL returns { success: true }, token revoked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[api-revocation]]
- [[session-exploit]]
