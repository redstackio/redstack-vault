---
tags:
  - oauth
  - redirect
  - bypass
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-oauth-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.138Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6dc7e220-4aaa-4937-a45b-64e3918f5431
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-OAuth-Redirect-Bypass

## Summary

This procedure tests the OAuth redirect validation in Respondly's Twitter integration by sending a request with a full URL in the requestTokenAndRedirect parameter, aiming to observe normal behavior and identify potential flaws for further exploitation.

## Description

In the context of Respondly's web application built on Meteor, the Twitter OAuth endpoint (/ _oauth/twitter/) handles redirect URIs during authorization. By attempting a bypass with a external domain like hackerone.com, this step reveals if validation is strict or allows inspiration for malformed inputs. No crash occurs, but it sets up for error-prone testing. Expected outcome is a standard OAuth initiation without disruption.

## Requirements

1. Access to a web browser or curl tool
2. Public internet connectivity to reach https://app.respond.ly
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement strict URI validation to reject external or malformed redirects
- Log all OAuth parameter inputs for anomaly detection
- Rate-limit authorization attempts to prevent repetition

## Objectives

1. Probe OAuth endpoint for redirect handling weaknesses
2. Confirm parameter acceptance without errors
3. Gather baseline for escalating to malformed URI tests

## Instructions

### Step 1: Access OAuth Endpoint with Standard Redirect

**Context**: Simulate a legitimate but external redirect attempt to test validation boundaries.

**Command** ([[commands/curl-access-oauth-endpoint]]):
```bash
curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com"
```

> This command sends a GET request to the OAuth endpoint with a full HTTPS redirect URI. Expected output includes a redirect or authorization prompt, confirming the parameter is processed without immediate failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-oauth-endpoint]]

## Tools Used


## Tags

- [[oauth]]
- [[redirect]]
- [[bypass]]
