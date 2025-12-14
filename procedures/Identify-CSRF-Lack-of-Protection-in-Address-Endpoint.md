---
id: proc-csrf-identify-001
tags:
  - csrf
  - web
  - vulnerability-identification
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:23.615Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF Lack of Protection in Address Endpoint

## Summary

This procedure involves inspecting a web application's address management endpoint to detect the absence of CSRF protection, confirming that cross-origin requests can modify user data using only session cookies.

## Description

In the context of Bumble's shop, the POST endpoint at https://shop.bumble.com/account/addresses lacks CSRF token validation, allowing attackers to forge requests from external sites. This is identified by analyzing network requests during legitimate address addition and testing for token absence. Prerequisites include access to a browser and the target site while authenticated.

## Requirements

1. Authenticated session to the target application (e.g., Bumble shop)
2. Browser with developer tools enabled
3. Basic knowledge of HTTP requests and CSRF mechanics

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing endpoints
- Enforce same-origin policy and validate referer/origin headers
- Monitor for anomalous address additions in user accounts

## Objectives

1. Confirm lack of CSRF protection on the target endpoint
2. Document request structure for exploit crafting
3. Assess potential for cross-site data modification

## Instructions

### Step 1: Inspect Legitimate Request

**Context**: Perform a normal address addition to capture the request details and check for CSRF tokens.

Open the Bumble shop, navigate to account addresses, and add a test address. Use browser dev tools (Network tab) to inspect the POST request to https://shop.bumble.com/account/addresses.

> Look for parameters like _token or csrf_token in form data or headers. If absent, note the reliance on session cookies alone.

### Step 2: Test Cross-Origin Submission

**Context**: Simulate a forged request from a different origin to verify vulnerability.

Create a simple HTML form on a local file or external host targeting the endpoint with sample data. Load it in a browser while authenticated to Bumble and submit.

> If the request succeeds without errors (e.g., 200 OK and address added), CSRF protection is missing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[Reconnaissance]]
