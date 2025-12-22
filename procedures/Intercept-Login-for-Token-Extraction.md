---
tags:
  - token-extraction
  - intercept
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 58355f6d-f178-4825-8e9b-be1117789f6b
created_at: '2025-12-13T09:01:21.723Z'
updated_at: '2025-12-13T09:01:21.723Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Login for Token Extraction

## Summary

This procedure involves logging into the application and intercepting a POST request to extract authentication tokens and cookies for use in advanced smuggling attacks.

## Description

By visiting the edit page and saving changes, intercept the request to obtain identity_id, session_token, _launchpad_session, and authenticity_token for crafting authenticated smuggled requests.

## Requirements

1. Valid account on launchpad.37signals.com
2. Proxy tool for interception (e.g., browser dev tools)
3. Network access

## Defense

Defensive measures and detection strategies:

- Implement strong CSRF protections
- Monitor for unusual POST requests to identity endpoints

## Objectives

1. Extract necessary tokens
2. Prepare for cookie capture exploitation
3. Enable authenticated smuggling

## Instructions

### Step 1: Perform Login and Intercept

**Context**: Visit the edit page, save changes, and capture the request.

> No specific command; use a proxy to intercept the POST to /identity and extract values manually.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[token-extraction]]
- [[intercept]]
