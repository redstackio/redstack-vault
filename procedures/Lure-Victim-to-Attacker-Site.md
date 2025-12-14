---
id: proc-uuid-1
tags:
  - phishing
  - social-engineering
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:12.582Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
---

# Lure Victim to Attacker Site

## Summary

This procedure uses social engineering to direct a victim to an attacker-controlled website, setting up the stored XSS injection without requiring direct access to the target DoD site.

## Description

In the context of exploiting a stored XSS vulnerability on the DoD alerts system, the attacker first lures the victim (a logged-in DoD user) to attacker.com via phishing links or deceptive messages. Once there, automated scripts handle the payload injection and redirection. This step relies on the victim's trust and browser execution, leading to potential session compromise when the XSS triggers.

## Requirements

1. Control over a domain/website (e.g., attacker.com) with JavaScript enabled
2. Knowledge of victim's email or communication channels for phishing
3. Victim must have an active session on the DoD site

## Defense

Defensive measures and detection strategies:

- User training on phishing recognition and link verification
- Email filters to block suspicious links
- Browser extensions for link scanning (e.g., uBlock Origin)

## Objectives

1. Gain victim's browser access to the attacker's domain
2. Position for automated exploitation of the target site
3. Minimize direct interaction to avoid suspicion

## Instructions

### Step 1: Craft Phishing Lure

**Context**: Create a deceptive message or email to entice the victim to click a link to attacker.com.

No command required; use email tools or social media to send: "Click here for urgent DoD update: http://attacker.com/dod-alert"

> Expected: Victim clicks and loads attacker.com.

### Step 2: Confirm Access

**Context**: Log the visit to verify the lure worked.

Use server logs or JavaScript analytics on attacker.com to track IP/user-agent.

> Expected: Log entry showing victim's access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]

