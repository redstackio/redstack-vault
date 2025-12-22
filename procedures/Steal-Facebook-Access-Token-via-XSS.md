---
tags:
  - xss
  - token-theft
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1cef89bd-2c48-4da3-a624-b138164bc1bc
created_at: '2025-12-14T03:16:14.454Z'
updated_at: '2025-12-14T03:16:14.454Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Steal-Facebook-Access-Token-via-XSS

## Summary

This procedure leverages an injected stored XSS payload in a DigitalSellz public profile to execute JavaScript in a victim's browser, extracting and exfiltrating their Facebook access token for unauthorized account access.

## Description

Once the XSS payload is stored in the public profile, any authenticated user viewing it will execute the script in their session context. DigitalSellz's Facebook integration stores access tokens client-side (e.g., in localStorage via the Facebook SDK). The payload retrieves this token and sends it to an attacker-controlled endpoint. This enables full compromise of the victim's Facebook account, including data access and actions on their behalf. The attack relies on social engineering to drive views or organic discovery. Outcomes include token receipt on the attacker's server, verifiable via Facebook API tests.

## Requirements

1. Injected XSS payload already stored in a public profile
2. Attacker-controlled server to receive exfiltrated data (e.g., simple HTTP listener)
3. Victim authenticated with Facebook on DigitalSellz

## Defense

Defensive measures and detection strategies:

- Enforce strict same-origin policy and token storage in HttpOnly cookies
- Implement token binding to sessions and monitor for anomalous API usage
- Use browser security features like sandboxing and detect cross-origin requests

## Objectives

1. Execute script in victim's browser context
2. Extract Facebook access token from client-side storage
3. Exfiltrate token to attacker for reuse

## Instructions

### Step 1: Prepare Exfiltration Endpoint

**Context**: Set up a server to capture the stolen token, ensuring it's accessible via HTTP.

Deploy a simple listener (e.g., using Python's http.server or ngrok for tunneling) at http://attacker.com/steal.

### Step 2: Trigger Payload Execution

**Context**: Direct the victim to view the public profile containing the payload.

Share the profile URL (e.g., https://digitalsellz.com/profile/attacker) via phishing email or link in a forum. When loaded, the payload executes automatically.

### Step 3: Retrieve and Validate Token

**Context**: Monitor the endpoint for incoming requests containing the token.

Check server logs for the GET parameter with the token. Test validity by making a Facebook Graph API call:

Use a tool like curl: `curl -H "Authorization: Bearer <token>" https://graph.facebook.com/me` to fetch user info.

> Success shows victim details; failure indicates invalid/expired token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[Exfiltration]]
