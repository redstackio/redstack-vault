---
id: proc-complete-oauth-with-stolen-token
tags:
  - app-authorization
  - privilege-escalation
  - token-abuse
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:29:56.761Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
---
# Complete-OAuth-Authorization-with-Stolen-Token

## Summary

This procedure uses the stolen OAuth token to authorize the attacker's application on the victim's Vimeo account, granting full privileges without consent.

## Description

The token, extracted via Flash, is submitted to Vimeo's OAuth flow for the attacker's app (e.g., 'OAuthBypass'). This bypasses user approval due to the CSRF vulnerability. Victim can check https://vimeo.com/settings/apps for confirmation. Outcome: Attacker controls the account via app scopes.

## Requirements

1. Valid stolen OAuth token
2. Attacker-registered Vimeo app
3. API access to Vimeo endpoints
4. Knowledge of app client ID/secret

## Defense

Defensive measures and detection strategies:

- Require explicit user consent for app authorizations
- Monitor for unauthorized app grants in audit logs
- Revoke tokens on suspicious activity
- Limit app scopes and implement token binding

## Objectives

1. Authorize malicious app using stolen token
2. Gain persistent access to victim's account
3. Escalate privileges via app permissions

## Instructions

### Step 1: Prepare App Authorization Request

**Context**: Use token in OAuth completion flow.

Construct request to Vimeo's token endpoint with the stolen code/token.

```http
POST /oauth/access_token
Content-Type: application/x-www-form-urlencoded

client_id=ATTACKER_CLIENT_ID&client_secret=SECRET&code=STOLEN_TOKEN&grant_type=authorization_code
```

> Replace with actual values; this exchanges for access token.

### Step 2: Submit and Receive Access

**Context**: Complete the flow to bind app.

Send via curl or API client.

> Expected: JSON response with access_token and scopes.

### Step 3: Verify Authorization

**Context**: Check victim's app settings.

Direct victim or monitor: Visit https://vimeo.com/settings/apps.

> Success if 'OAuthBypass' app appears with full privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- app-authorization
- privilege-escalation
- token-abuse
