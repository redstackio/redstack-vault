---
id: proc-configure-hackerone-webhook
tags:
  - webhook
  - hackerone
  - configuration
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
updated_at: '2025-12-14T17:28:36.479Z'
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
# Configure-HackerOne-Webhook

## Summary

This procedure details logging into HackerOne with an organizational account, navigating to program settings, and creating a webhook that points to the malicious public PHP redirect URL, setting the stage for SSRF exploitation.

## Description

HackerOne's webhook feature allows organizations to configure endpoints for notifications. By using a URL controlled by the attacker, this step prepares the SSRF payload. The target environment is the HackerOne web platform. No commands are executed; it's UI-based. Success is confirmed when the webhook is saved without validation errors.

## Requirements

1. Valid HackerOne account with organization management permissions
2. Access to the previously hosted PHP URL
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Enforce webhook URL whitelisting to trusted domains only
- Audit webhook configurations for suspicious URLs
- Log all webhook setup attempts and review for anomalies

## Objectives

1. Integrate the SSRF payload into the target's webhook system
2. Avoid triggering any immediate validation blocks
3. Enable subsequent test requests for exploitation

## Instructions

### Step 1: Log In and Navigate

**Context**: Access the HackerOne dashboard and reach the relevant settings.

**Instructions**: Log in at hackerone.com, select the organization, go to 'Settings' > 'Programs' > select the program > 'Webhooks'.

> Expected: Webhooks configuration page loads.

### Step 2: Create Webhook

**Context**: Add a new webhook using the public PHP URL.

**Instructions**: Click 'Add Webhook', enter the PHP URL (e.g., https://your-site.000webhostapp.com/h1.php) as the target, configure any necessary events, and save.

> Expected: Webhook created successfully, listed in the interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- webhook
- configuration
