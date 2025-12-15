---
tags:
  - csrf
  - web
  - recon
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
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
updated_at: '2025-12-14T17:27:36.056Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 85b08dc5-9a76-4bc4-b889-4b4445797843
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-Vulnerable-Signup-Endpoint

## Summary

This procedure involves analyzing a web endpoint, such as Yelp's signup API, to detect the absence of CSRF protections, allowing subsequent exploitation for unauthorized actions.

## Description

In a typical attack scenario, the target is a public-facing web application like https://auto-api.yelp.com/account/create_secure. By observing request handling, confirm that POST requests succeed without validating cookies, CSRF tokens, or user-agent headers. This vulnerability enables attackers to forge requests from a victim's authenticated session. Prerequisites include basic web knowledge and access to network inspection tools. Expected outcomes: Identification of exploitable endpoints, including similar issues on login (/account/login_secure) and password reset (/account/send_password_email_secure).

## Requirements

1. Network access to the target endpoint (https://auto-api.yelp.com)
2. Web proxy tool like Charles for request inspection
3. No authentication needed for initial analysis

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Validate Origin/Referer headers and user-agent strings
- Monitor for anomalous account creation from unusual IPs or patterns

## Objectives

1. Confirm lack of CSRF protections on signup endpoint
2. Identify similar vulnerabilities on related endpoints
3. Establish foundation for crafting exploits

## Instructions

### Step 1: Inspect Endpoint Behavior

**Context**: Use a proxy to monitor legitimate requests and test for protection bypass.

No specific command; observe via proxy that requests process without token checks.

> Expected: Requests succeed without security headers, confirming vulnerability.

### Step 2: Test Basic POST Without Tokens

**Context**: Send a minimal POST to verify no validation.

Use browser dev tools or proxy to simulate; no command executed in extraction.

> Expected: Successful processing without errors related to missing tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- [[csrf]]
- [[web]]
- [[recon]]
