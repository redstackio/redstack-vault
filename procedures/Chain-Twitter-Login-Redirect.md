---
tags:
  - open-redirect
  - chaining
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:31.623Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8e03b054-9f41-471b-831d-032ea0e51888
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Chain-Twitter-Login-Redirect

## Summary

This procedure chains the double-encoded analytics redirect into Twitter's login redirect_after_login parameter, creating a full path that evades link shortening and warnings while redirecting to external sites post-login.

## Description

The twitter.com/login endpoint accepts arbitrary URLs in redirect_after_login, intended for Twitter subdomains but exploitable via chaining. This completes the bypass, allowing seamless redirection after authentication. Requires the double-encoded analytics URL.

## Requirements

1. Double-encoded analytics URL
2. Twitter login access
3. Browser for URL construction

## Defense

Defensive measures and detection strategies:

- Restrict redirect_after_login to whitelisted Twitter domains only
- Decode and validate chained parameters recursively
- Log and alert on external redirects from login flows

## Objectives

1. Embed analytics redirect in login parameter
2. Ensure chain executes post-login
3. Bypass t.co shortening and interstitials

## Instructions

### Step 1: Append to Login Parameter

**Context**: Add the double-encoded URL to the login endpoint.

Manually construct: https://twitter.com/login?redirect_after_login=https%3A%2F%2Fanalytics.twitter.com%2Fdaa%2F0%2Fdaa_optout_actions%3Faction_id%3D4%26rd%3Dhttps%253A%252F%252Fddosecrets%2525E3%252580%252582com%253F

> Expected: Final chained URL; test by pasting in browser address bar.

### Step 2: Verify Chain

**Context**: Access the URL to confirm redirect sequence.

Load in browser; it should prompt login if needed, then redirect via analytics to target.

> Success if no blocks occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[chaining]]
