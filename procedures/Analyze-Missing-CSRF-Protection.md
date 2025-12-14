---
id: proc-uuid-2
tags:
  - csrf
  - analysis
  - web-vuln
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
updated_at: '2025-12-14T17:27:35.767Z'
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
# Analyze Missing CSRF Protection

## Summary

This procedure examines the VK.com view counting endpoint for CSRF vulnerabilities by checking for required anti-CSRF tokens, confirming the absence of protection against unauthorized requests.

## Description

Targeted at the VK.com web platform, this involves replaying captured requests without security parameters. The attack scenario exploits session-based auth without token validation, allowing cross-origin requests. Prerequisites: Captured endpoint from prior recon. Outcomes include proof of vulnerability via successful unauthorized requests.

## Requirements

1. Browser developer tools or proxy like Burp Suite
2. Logged-in VK.com session
3. Knowledge of CSRF mechanics

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Log and alert on requests missing tokens

## Objectives

1. Identify absence of 'hash' parameter validation
2. Test request integrity without protection
3. Document vulnerability for exploitation planning

## Instructions

### Step 1: Inspect Request Parameters

**Context**: Review captured requests for CSRF indicators.

**Instructions**: In network logs, check for 'hash' or similar tokens in POST/GET params. Note if present in legitimate requests.

> Legitimate requests may include 'hash', but test shows it's not enforced.

### Step 2: Replay Without Token

**Context**: Simulate a request omitting the 'hash' to test validation.

**Instructions**: Use browser console or proxy to send a request to https://vk.com/al_page.php?act=seen&al=1&data=[sample_data] without 'hash'.

> If views increment, CSRF protection is missing, confirming the vuln.

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
- [[analysis]]
