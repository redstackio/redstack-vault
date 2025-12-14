---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - privilege-escalation
  - social-engineering
  - phishing
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:27:36.122Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Lure Admin and Execute Privilege Escalation

## Summary

This procedure covers luring the router's admin (root) user to visit the malicious CSRF page, triggering the configuration replacement and achieving privilege escalation from operator to admin in Ubiquiti EdgeOS.

## Description

With the CSRF page ready, the attacker uses social engineering to direct the admin to the page while they are authenticated to the router UI. The auto-submitting form exploits the backup feature's CSRF flaw, replacing the config to elevate privileges. This step integrates phishing and relies on the admin's session being active. Target: EdgeOS web interface.

## Requirements

1. Hosted CSRF page and malicious config file
2. Contact method for the admin (e.g., email, chat)
3. Operator access already established

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition and verify links before clicking
- Implement email filters for suspicious links and monitor external visits
- Enable logging of config changes and alert on unauthorized backups

## Objectives

1. Deliver the lure to the admin user
2. Ensure the admin visits while authenticated as root
3. Confirm privilege escalation post-execution

## Instructions

### Step 1: Craft the Lure Message

**Context**: Create a convincing pretext to get the admin to visit the page.

Compose a phishing email or message, e.g., "Urgent: Check this router status update at http://attacker.com/csrf.html". Make it seem legitimate, perhaps mimicking Ubiquiti support.

### Step 2: Deliver the Lure

**Context**: Send the message to the admin.

Use email, internal chat, or other channels to send the link. Time it when the admin is likely managing the router.

### Step 3: Execute and Verify

**Context**: Monitor for visit and check escalation.

Once the admin clicks (while logged in as root), the form submits, replacing the config. Return to operator login and test admin features like config editing.

**Expected Output**: Successful config replacement; operator account now has admin rights.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- privilege-escalation
- social-engineering
- phishing
