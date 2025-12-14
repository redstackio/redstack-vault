---
tags:
  - oauth
  - auth-bypass
  - token-impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0703fc2b-af07-47bf-9be9-2ad4b7855fa3
created_at: '2025-12-14T17:31:52.697Z'
updated_at: '2025-12-14T17:31:52.697Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# OAuth-Token-Impersonation

## Summary

This procedure exploits a lack of OAuth token validation in PicsArt's authentication flow with Facebook or Google providers, allowing a malicious app to impersonate a user and access their PicsArt account using a token obtained from the same provider.

## Description

In the OAuth flow, users authorize apps to access their data via providers like Facebook or Google. PicsArt did not verify if the submitted access token was issued for its own client ID by querying the provider's API (e.g., Facebook's debug_token endpoint or Google's tokeninfo). This allows any app with a token from the same user and provider to impersonate them on PicsArt, leading to unauthorized account access and potential data compromise. The attack requires the user to have authorized both the legitimate and malicious apps.

## Requirements

1. Access to a malicious app registered with Facebook or Google OAuth
2. Target user who has authorized PicsArt with the same provider
3. Network access to PicsArt's OAuth endpoints and the provider's validation APIs (though not used by PicsArt)
4. Ability to capture and replay OAuth access tokens

## Defense

Defensive measures and detection strategies:

- Implement server-side validation of access tokens using provider APIs (e.g., verify audience/client ID)
- Use short-lived tokens and require re-authentication for sensitive actions
- Monitor for anomalous access patterns, such as logins from unfamiliar apps or IPs
- Educate users on app permissions and revoke access to suspicious third-party apps

## Objectives

1. Obtain a valid access token from the target user via a malicious app
2. Impersonate the user on PicsArt to access account data
3. Achieve unauthorized read/write access to the victim's PicsArt resources

## Instructions

### Step 1: Register Malicious App and Obtain Token

**Context**: Set up a third-party app to trick the user into authorizing it, capturing the OAuth token.

Direct the user to your malicious app's authorization URL (e.g., for Facebook: https://www.facebook.com/v18.0/dialog/oauth?client_id=YOUR_APP_ID&redirect_uri=YOUR_REDIRECT&scope=public_profile,email). Upon approval, exchange the authorization code for an access token via the provider's token endpoint.

> For Facebook, use a POST to https://graph.facebook.com/v18.0/oauth/access_token with client_id, client_secret, code, and redirect_uri. The response includes the access_token.

### Step 2: Replay Token on PicsArt

**Context**: Submit the token to PicsArt's OAuth callback or API endpoints without validation checks.

Send the access token in the Authorization header (Bearer token) or as a parameter to PicsArt's login/verify endpoint (e.g., POST to https://picsart.com/oauth/facebook with access_token). Since PicsArt skips client ID validation, it grants access to the associated user account.

> Example request: curl -X POST https://picsart.com/api/auth/facebook -H "Authorization: Bearer YOUR_ACCESS_TOKEN". Successful response includes user session or profile data.

### Step 3: Access and Exfiltrate Data

**Context**: Once authenticated, interact with the account to retrieve or modify data.

Use the established session to call PicsArt APIs for user images, profile, or other features. For example, GET /api/user/profile to fetch details.

> Monitor responses for sensitive information; potential for further escalation if editing capabilities are available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[auth-bypass]]
- [[token-impersonation]]
