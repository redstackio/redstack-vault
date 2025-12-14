---
id: proc-content-manipulation-exfil
tags:
  - data-manipulation
  - exfiltration
  - csrf-impact
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:27:15.323Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Data from Local System]]'
---
# Demonstrate-Content-Manipulation-and-Exfiltration

## Summary

This procedure exploits the hijacked session to manipulate content (e.g., add charts or posts) in the attacker's account via the unaware victim, allowing the attacker to later view and exfiltrate the data for theft or further compromise.

## Description

Post-silent login, the victim believes they are in their account but operates in the attacker's. Interactions like adding to the library (e.g., Facebook posts, charts) create assets visible only to the attacker. The attacker refreshes their session to access these, enabling data theft (e.g., sensitive project details) or escalation to full takeover. This highlights CSRF's impact on state-changing actions without proper protections.

## Requirements

1. Hijacked victim session active
2. Attacker's parallel session for monitoring
3. Access to Infogram features like library

## Defense

Defensive measures and detection strategies:

- Session isolation and logout on suspicious logins
- Audit logs for content changes tied to mismatched sessions
- Content access controls beyond simple authentication

## Objectives

1. Induce victim to create exfiltrable content
2. Access manipulated data from attacker side
3. Demonstrate potential for data theft or takeover

## Instructions

### Step 1: Lure Victim Interaction

**Context**: Guide the victim to perform actions assuming their own account.

Direct the victim to the library feature and have them add an item, e.g., a sample chart or Facebook post integration.

**Expected Output**: Content created without errors.

### Step 2: Refresh Attacker Session

**Context**: Pull in the changes made by the victim.

In the attacker's browser, log in (if needed) and refresh the library page.

**Expected Output**: New content appears in attacker's library.

### Step 3: Exfiltrate Data

**Context**: Extract the victim's unintended contributions.

View, download, or share the added projects (e.g., export chart data).

**Expected Output**: Data copied or transferred out of the platform.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-manipulation]]
- [[Exfiltration]]
- [[csrf-impact]]
