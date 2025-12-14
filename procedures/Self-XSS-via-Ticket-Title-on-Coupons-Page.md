---
id: proc-camptix-self-xss-001
tags:
  - xss
  - self-xss
  - wordpress
  - camptix
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.792Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Self-XSS-via-Ticket-Title-on-Coupons-Page

## Summary

This procedure exploits a self-XSS vulnerability in the Camptix plugin by injecting JavaScript into the Ticket Title field, which executes solely in the attacker's browser when viewing the coupons page, limited to session-specific impacts but useful in chained attacks.

## Description

Due to improper output escaping, the Ticket Title is rendered without sanitization on the coupons page. An attacker injects a payload while editing a ticket, and upon navigating to the coupons page in their own session, the script executes. While self-limiting (no direct victim impact), it can steal the attacker's own cookies or be leveraged in phishing scenarios. Discovered via plugin testing on WordPress.

## Requirements

1. Authenticated session in WordPress with Camptix access for ticket editing.
2. Vulnerable Camptix plugin version.
3. Browser session to trigger self-execution.

## Defense

Defensive measures and detection strategies:

- Enforce input validation and output escaping (e.g., esc_html in WordPress) for all fields.
- Enable strict CSP to block inline scripts.
- Log and alert on suspicious payload patterns in admin inputs.

## Objectives

1. Execute JavaScript in the attacker's session via unsanitized output.
2. Highlight self-XSS risks for awareness or chaining.
3. Confirm insufficient escaping on coupons page.

## Instructions

### Step 1: Edit Ticket Title with Payload

**Context**: Prepare the injection in the ticket management area.

Log in to WordPress admin, go to Events > Tickets, edit a ticket, and set Title to: `<script>alert('Self-XSS on Coupons Page: ' + document.cookie);</script>`. Save.

### Step 2: Navigate to Coupons Page

**Context**: Trigger the self-XSS by loading the affected page.

Go to Events > Coupons in the admin panel, where the ticket is referenced. The payload should execute immediately.

> Expected: Alert shows cookies from your session, confirming self-execution.

### Step 3: Assess Impact

**Context**: Evaluate the limited scope and potential chaining.

Inspect console for data exfiltration; note it only affects your session. For demos, use payloads that log to an external server.

> In chained attacks, combine with social engineering to trick users into self-injecting.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[self-xss]]
- [[wordpress]]
- [[camptix]]
