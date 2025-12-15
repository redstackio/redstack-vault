---
id: proc-uuid-004
tags:
  - xss-execution
  - phishing
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.490Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Victim-Profile-View

## Summary

This procedure relies on the victim accessing their modified profile, triggering the stored XSS to execute JavaScript like prompts or redirects to phishing sites.

## Description

Once injected, the payload renders in the victim's browser during normal profile view, executing arbitrary code. This can prompt for input, steal session data, or redirect to attacker-controlled phishing pages mimicking government sites to harvest credentials. The chain completes the attack from takeover to exploitation.

## Requirements

1. Injected XSS payload in profile
2. Victim must log in legitimately
3. Attacker-controlled phishing domain ready

## Defense

Defensive measures and detection strategies:

- Escape output in dynamic content rendering
- Monitor for XSS alerts in browser consoles
- Educate users on phishing indicators

## Objectives

1. Execute JS in victim context for data theft
2. Redirect to phishing for credential capture
3. Achieve session hijacking or further compromise

## Instructions

### Step 1: Logout and Wait for Victim

**Context**: Ensure the legitimate user logs in post-injection.

Log out of the compromised session to avoid interference.

**Expected Output**: Session ends cleanly.

### Step 2: Victim Views Profile

**Context**: Payload activates on profile load.

When victim navigates to their profile, the XSS triggers (e.g., `prompt(1)` or redirect to https://evil.com/).

**Expected Output**: JS execution: alert box, redirect, or phishing form load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[Phishing]]
- [[credential-theft]]
