---
id: proc-twitter-dm-trigger-nav-001
tags:
  - xss
  - trigger
  - twitter
  - dm
  - navigation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.316Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Recent Conversations Selection

## Summary

This procedure executes the stored XSS in a Twitter DM group name by navigating to new messages and selecting the group from recent conversations, rendering the unsanitized name.

## Description

Accessing the 'New message' dialog displays recent DM groups, including their names, without proper HTML escaping. Selecting the vulnerable group triggers the script execution in the browser's JavaScript environment. This is a passive trigger, exploitable during routine navigation. Affects web users in the group. Prerequisites: Vulnerable group exists. Outcome: JS execution enabling data exfiltration or UI manipulation.

## Requirements

1. Vulnerable DM group with members
2. Victim's Twitter session
3. Web browser

## Defense

Defensive measures and detection strategies:

- Escape HTML in recent conversations lists and selection UIs
- Implement strict CSP to prevent script execution from user content
- Monitor DOM manipulations in DM interfaces

## Objectives

1. Trigger via UI navigation
2. Execute JS without content sharing
3. Highlight broad attack surface

## Instructions

### Step 1: Open New Message Dialog

**Context**: Initiate the navigation flow.

Click the Messages icon, then 'New message' to open the DM composer.

> Recent conversations list loads, including group names.

### Step 2: View and Select Recent Group

**Context**: Render the malicious name.

Scroll to recent conversations; the vulnerable group name renders, executing the payload. Click to select it.

> Script runs on render; e.g., alert appears.

### Step 3: Confirm Trigger

**Context**: Verify in browser tools.

Open dev console; look for payload effects like network requests or logs.

> Success: Execution in DM context without further action.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[twitter]]
- [[dm]]
- [[navigation]]
