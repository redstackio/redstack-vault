---
tags:
  - social-engineering
  - browser
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[User Execution]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 75192a75-f242-4286-a4f6-b8f4230f455e
created_at: '2025-12-13T09:01:26.504Z'
updated_at: '2025-12-13T09:01:26.504Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Force Victim to Visit Malicious Page

## Summary

This procedure tricks the victim into visiting a malicious HTML page in a browser with cleared cookies to trigger the Login CSRF.

## Description

The victim loads the page, which includes an iframe and JavaScript redirect, initiating the SSO-SAML flow automatically.

## Requirements

1. Hosted malicious page
2. Social engineering to lure victim
3. Victim's browser with clear cookies

## Defense

Defensive measures and detection strategies:

- Educate users on phishing risks
- Use browser extensions to block suspicious iframes

## Objectives

1. Achieve initial victim interaction
2. Load exploit payload
3. Proceed to forced login

## Instructions

### Step 1: Host and Lure

**Context**: Host the page and send link to victim.

> No specific command; use social engineering techniques.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser]]

## Tags

- [[social-engineering]]
