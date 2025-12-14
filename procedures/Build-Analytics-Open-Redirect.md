---
tags:
  - open-redirect
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
updated_at: '2025-12-14T17:24:31.627Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 250adce5-6c69-4681-8e08-9a9f3bda7554
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Build-Analytics-Open-Redirect

## Summary

This procedure exploits the open redirect vulnerability on analytics.twitter.com by embedding a target URL in the 'rd' parameter of the daa_optout_actions endpoint, allowing arbitrary external redirects without validation.

## Description

The endpoint https://analytics.twitter.com/daa/0/daa_optout_actions?action_id=4&rd= accepts any URL in 'rd' and redirects to it, bypassing Twitter's link checks. Combined with encoding, it chains to forbidden domains. Requires the encoded URL from prior steps and a browser for testing.

## Requirements

1. Encoded target URL from Unicode procedure
2. Web browser to construct and test
3. Understanding of URL parameters

## Defense

Defensive measures and detection strategies:

- Validate 'rd' parameter to restrict to trusted domains only
- Implement redirect rate limiting and logging for analytics.twitter.com
- Use Content-Security-Policy to block untrusted redirects

## Objectives

1. Construct a redirect to the disguised forbidden URL
2. Double-encode for chaining compatibility
3. Verify redirect functions without errors

## Instructions

### Step 1: Append to Endpoint

**Context**: Add the single-encoded URL to the 'rd' parameter and include %3F.

Manually build: https://analytics.twitter.com/daa/0/daa_optout_actions?action_id=4&rd=https%3A%2F%2Fddosecrets%25E3%2580%2582com%3F

> Expected: Parameterized URL ready.

### Step 2: Double Encode Full URL

**Context**: Encode the entire analytics URL to evade parsing in the next chain.

Use URL encoder: Results in https%3A%2F%2Fanalytics.twitter.com%2Fdaa%2F0%2Fdaa_optout_actions%3Faction_id%3D4%26rd%3Dhttps%253A%252F%252Fddosecrets%2525E3%252580%252582com%253F

> This prevents premature decoding; test in browser to confirm redirect.

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
