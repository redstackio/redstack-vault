---
id: proc-prepare-attacker-profile
tags:
  - idor
  - request-prep
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:48.118Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Attacker-Profile-for-Interception

## Summary

This procedure logs in as the attacker and initiates a blog addition on IntenseDebate to generate a save request that can be intercepted and modified for IDOR exploitation.

## Description

Switching to the attacker's session prepares the environment for proxy interception. The goal is to mimic a legitimate save action while setting up for parameter tampering. Burp Suite must be running as a proxy. Expected outcome: An interceptable POST request to the profile endpoint.

## Requirements

1. Attacker account credentials
2. Burp Suite configured as browser proxy (e.g., 127.0.0.1:8080)
3. Victim's hidBlogID from previous step

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and monitor for proxy-intercepted traffic
- Rate-limit profile save requests per user
- Alert on unusual request patterns from authenticated sessions

## Objectives

1. Authenticate attacker session
2. Load profile editor for blog addition
3. Position for request interception

## Instructions

### Step 1: Log In as Attacker

**Context**: Switch sessions to the attacker.

**Instructions**: Log out of victim if needed, then log in to attacker's account at https://intensedebate.com.

> Confirm access to dashboard.

### Step 2: Access Profile and Start Addition

**Context**: Initiate the form to trigger the save request.

**Instructions**: Go to https://www.intensedebate.com/edit-user-profile, click 'Add Blog / Website', fill basic form details (do not save yet).

> Ensure browser traffic routes through Burp Suite proxy.

### Step 3: Prepare for Intercept

**Context**: Set up to capture the save action.

**Instructions**: With form filled, position cursor on 'Save Settings' button, ready to click while monitoring Burp's Intercept tab.

> Burp should be in intercept mode.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[request-prep]]
