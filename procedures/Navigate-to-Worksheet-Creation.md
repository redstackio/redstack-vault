---
id: proc-navigate-worksheet-creation
tags:
  - web
  - navigation
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
updated_at: '2025-12-14T17:33:06.209Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Worksheet-Creation

## Summary

Procedure to locate and access the worksheet creation page within the DoD legal request application, positioning the attacker to interact with vulnerable form elements.

## Description

From the main page, specific UI elements lead to the creation interface. This manual navigation exploits the application's structure to reach text fields. Outcomes include access to form inputs; requires no tools beyond a browser.

## Requirements

1. Successful main page load
2. Basic UI interaction capability
3. Awareness of labeled buttons/menus

## Defense

Defensive measures and detection strategies:

- Add session-based access controls post-navigation
- Log UI interactions for anomaly detection

## Objectives

1. Reach worksheet creation section
2. Identify entry to form areas
3. Avoid detection during navigation

## Instructions

### Step 1: Select Creation Option

**Context**: Click the designated link to enter worksheet mode.

No command; browser interaction:

```plaintext
Click `█████████`
```

> Redirects to creation page. Expected: Options for new worksheets.

### Step 2: Choose Sub-Option

**Context**: Refine to legal request type.

```plaintext
Click `███ and ████████` ██████████
```

> Loads targeted interface. Expected: Worksheet start prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[navigation]]
