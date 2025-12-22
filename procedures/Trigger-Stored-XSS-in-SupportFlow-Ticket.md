---
id: proc-trigger-xss-supportflow
tags:
  - xss
  - execution
  - wordpress
  - admin-exploit
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
updated_at: '2025-12-14T03:16:08.105Z'
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
# Trigger-Stored-XSS-in-SupportFlow-Ticket

## Summary

This procedure triggers the stored XSS by having an admin user view the malicious ticket, causing the unescaped subject payload to execute JavaScript in the browser context of the dashboard.

## Description

Once the payload is stored, accessing the ticket via the admin interface (SupportFlow -> All Tickets -> [ID]) renders the subject in an <input value="..."> without esc_attr(), allowing attribute breakout and script execution. This occurs in the plugin's admin class at line 905, affecting any viewing admin and potentially leading to session theft or further escalation within the WordPress context. The attack relies on social engineering or shared access to lure an admin view.

## Requirements

1. Admin privileges to access the SupportFlow admin dashboard.
2. Malicious ticket already created with valid payload.
3. Target browser without XSS protections (e.g., no strict CSP).

## Defense

Defensive measures and detection strategies:

- Escape outputs with esc_attr() in admin templates.
- Implement Content Security Policy (CSP) to block inline scripts.
- Audit plugin code for escaping issues and apply updates/patches.

## Objectives

1. Execute the stored JavaScript in an admin's browser session.
2. Demonstrate impact like alerts or data exfiltration.
3. Highlight the vulnerability for reporting or patching.

## Instructions

### Step 1: Access Admin Ticket List

**Context**: Log in as an admin and navigate to the SupportFlow section to locate the injected ticket.

**Command** (Manual navigation, no CLI command):

> Go to WordPress Admin -> SupportFlow -> All Tickets. The malicious subject may appear in the list.

### Step 2: View the Specific Ticket

**Context**: Click on the ticket ID to load the details page, where the subject is re-rendered in the form input, triggering the payload.

**Command** (Manual click):

> Select the ticket with the payload subject and open it. The <input value="1"><script>alert('hi');</script>"> executes immediately.

> Expected output: JavaScript alert pops up; inspect element to confirm the broken attribute and script tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- wordpress
- admin-exploit
