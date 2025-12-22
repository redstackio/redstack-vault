---
tags:
  - privilege-escalation
  - shopify
  - role-inspection
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.036Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4966936a-e02c-4bb9-9644-6d94f0942d98
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Open Full Permissions Role and Click on Assigned Staff

## Summary

This procedure opens the full-permissions role in the POS roles page and interacts with the assigned staff section by clicking on a staff member, scrolling to reveal hidden elements.

## Description

The roles page in POS contains nested sections that, when scrolled and clicked, can load additional context without permission re-checks. This step deepens the UI exploit path toward admin bridging.

## Requirements

1. Roles listing page loaded in POS
2. Full-permissions role with assigned staff
3. Browser capable of scrolling interactions

## Defense

Defensive measures and detection strategies:

- Hide or disable nested links in limited views
- Enforce permission checks on scroll-revealed elements
- Log interactions with role assignments

## Objectives

1. Load details of elevated role
2. Access assigned staff panel
3. Prepare for further navigation

## Instructions

### Step 1: Select Role

**Context**: Target the high-privilege role.

On the roles page, click to open the full-permissions role from setup.

> Role details expand.

### Step 2: Scroll and Click Staff

**Context**: Reveal and interact with assignments.

Scroll down to 'Assigned Staff' section. Click on a listed staff member.

> Staff details load in the context.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[role-inspection]]
