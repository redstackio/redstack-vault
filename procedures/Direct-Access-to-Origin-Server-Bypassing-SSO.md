---
id: proc-004
tags:
  - authorization-bypass
  - sso-bypass
  - origin-ip
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
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:57.322Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Direct-Access-to-Origin-Server-Bypassing-SSO

## Summary

This procedure accesses the DoD application directly via the origin IP, circumventing Akamai's SSO enforcement to gain authenticated access without credentials.

## Description

The root cause is that SSO is managed by the Akamai load balancer, but the internal origin server does not re-enforce authentication. By connecting directly to https://█████, an unauthenticated attacker impersonates an authenticated user. This grants access to protected features. Prerequisites: Verified origin IP from prior steps, web browser.

## Requirements

1. Verified origin IP
2. Web browser with HTTPS support
3. Direct network path to the IP (may require no firewall blocks)

## Defense

Defensive measures and detection strategies:

- Ensure origin servers validate sessions independently
- Block direct IP access via firewalls or IP whitelisting
- Log and alert on traffic bypassing CDN

## Objectives

1. Bypass Akamai and SSO
2. Achieve authenticated access
3. Access protected application areas

## Instructions

### Step 1: Navigate to Origin IP

**Context**: This step replaces the domain with the IP in the browser to hit the internal server directly.

**Command** (Browser Navigation):

No command-line; visit https://█████ in a web browser.

> The application should load without redirecting to SSO, indicating successful bypass.

**Expected Output**: Authenticated application interface loads, allowing navigation without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[authorization-bypass]]
- [[sso-bypass]]
- [[origin-ip]]
