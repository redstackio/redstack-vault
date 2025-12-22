---
tags:
  - phishing
  - social-engineering
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
id: 4bbe2299-a205-4575-9045-65c834653133
created_at: '2025-12-14T17:27:57.223Z'
updated_at: '2025-12-14T17:27:57.223Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trick-Victim-into-Visiting-Malicious-Page

## Summary

This procedure uses social engineering to lure the victim to a malicious HTML page, triggering the hidden Login CSRF actions without their awareness.

## Description

The malicious page is designed to be non-intrusive, with hidden elements performing logout and redirect. By disguising the link as legitimate (e.g., via email phishing), the attacker ensures the victim loads it, forcing SAML authentication and granting session access for data theft.

## Requirements

1. Hosted malicious HTML from prior procedure
2. Communication channel to victim (email, chat)
3. Victim's interaction without suspicion

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Browser warnings for cross-site requests
- Logging of unexpected logouts or SAML initiations

## Objectives

1. Induce victim to execute CSRF payload
2. Achieve stealthy authentication takeover
3. Minimize detection through invisibility

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a convincing pretext to get the victim to click the link.

Example email: "Check this urgent update: http://evil.com/csrf.html" (disguised as hackerone.com).

> Use URL shortener if needed to obfuscate.

### Step 2: Monitor and Confirm Trigger

**Context**: Track victim visit and SAML flow completion.

If hosting on own server, log access. Test in controlled env to confirm redirect to IdP.

> Expected: Victim logs in via SAML; attacker gains access post-auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
