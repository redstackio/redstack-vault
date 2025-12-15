---
tags:
  - content-addition
  - data-exposure
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.686Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b91e4462-1b86-429a-81fe-7003fc3b3310
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Content-in-Alternative-Interface

## Summary

This procedure uses the 'Add Content' feature in the alternative dashboard to incorporate widgets similar to the primary interface, facilitating further sensitive data access.

## Description

The alternative view at `███/home` mirrors widget functionality but with more options; adding content exploits the same access flaws. Requires prior navigation; outcomes include replicated exposure in an enhanced environment.

## Requirements

1. Access to `███/home`
2. Active user session
3. UI familiarity

## Defense

Defensive measures and detection strategies:

- Mirror access controls across all interfaces.
- Track content additions in logs for review.
- Limit widget availability in non-primary views.

## Objectives

1. Replicate widget exposure in alternative UI.
2. Access additional data sources.
3. Test consistency of vulnerability.

## Instructions

### Step 1: Access Add Content Feature

**Context**: Locate the content addition tool.

In the top-left corner of `███/home`, click 'Add Content'.

> Dialog or menu for widgets opens.

### Step 2: Add Widgets

**Context**: Select and place content similar to primary dashboard.

Choose widgets (e.g., user-related) and add them to the layout.

> Widgets load, displaying data without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[content-addition]]
- [[data-exposure]]
