---
tags:
  - csrf
  - initial-access
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
updated_at: '2025-12-14T17:33:06.158Z'
sub_techniques: []
id: 3c5574d1-0c66-4190-beed-e08a76ca1df8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Victim-Authentication-Setup

## Summary

This procedure ensures the victim is authenticated to the target web application, setting the stage for CSRF exploitation by maintaining an active session.

## Description

In a CSRF attack, the victim must be logged in for the forged request to succeed using their session cookies. This step involves luring the victim to authenticate via social engineering, such as sending a phishing link to the legitimate app. The target is a ColdFusion-based web app where the victim visits /registration/index.cfm after login. Expected outcome: Victim's browser holds valid auth tokens vulnerable to cross-site requests.

## Requirements

1. Knowledge of the target's login URL and username
2. Method to communicate with victim (email, messaging)
3. Victim's interaction with the app

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use SameSite cookies to restrict cross-site requests
- Monitor for unusual account updates from unknown IPs

## Objectives

1. Establish victim's authenticated session
2. Position victim for CSRF payload delivery
3. Enable forged requests using victim's credentials

## Instructions

### Step 1: Lure Victim to Login

**Context**: Direct the victim to the application's login page to ensure authentication.

No specific command; use social engineering to send a link like "Check your account at https://target.com/registration/index.cfm".

> Victim logs in manually, creating an active session.

### Step 2: Verify Session Readiness

**Context**: Confirm the victim remains logged in, perhaps by having them interact with a non-malicious page.

No command; observe if victim reports being logged in or proceed to next step.

> Expected: Victim navigates within the app post-login.

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
