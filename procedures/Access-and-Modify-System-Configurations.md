---
tags:
  - configuration-modification
  - access-bypass
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.690Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f640bdab-88ce-43b4-a19b-ef9419319f6d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-and-Modify-System-Configurations

## Summary

This procedure demonstrates accessing and editing system configurations and catalogs through dashboard widgets, bypassing role restrictions to potentially alter operational settings in the DoD application.

## Description

By interacting with widget elements, standard users can view and modify configurations without checks, targeting items like catalogs with 22+ entries. This occurs in the primary dashboard; outcomes include unauthorized changes that could lead to system misconfiguration or denial of service.

## Requirements

1. Widgets already added exposing configurations
2. Active dashboard session
3. Basic understanding of the UI

## Defense

Defensive measures and detection strategies:

- Add granular permissions for configuration endpoints.
- Audit all modification attempts, flagging non-admin access.
- Use immutable configurations for critical catalogs.

## Objectives

1. View restricted configuration items.
2. Perform unauthorized edits.
3. Highlight privilege escalation risks.

## Instructions

### Step 1: Interact with Configuration Widget

**Context**: Expand a widget to reveal configuration details.

In the third added widget, click on text like 'All(22)' to load the full list.

> A detailed view of configuration items appears, including editable fields.

### Step 2: View Configuration Details

**Context**: Inspect the exposed data.

Browse the list of items, noting sensitive operational details.

> 22+ items load without access denial.

### Step 3: Modify Configurations

**Context**: Attempt edits to test controls.

Select an item and edit fields (e.g., update values), then save.

> Changes apply successfully, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[configuration-modification]]
- [[access-bypass]]
