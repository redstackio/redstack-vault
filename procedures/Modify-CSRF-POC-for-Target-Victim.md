---
tags:
  - csrf-modify
  - victim-targeting
  - html-edit
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:07.440Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b25e9ead-ca7f-4eb9-bf6b-ef6b40adeb19
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Modify-CSRF-POC-for-Target-Victim

## Summary

This procedure customizes the generated CSRF PoC HTML to target a specific victim's client_id, enabling unauthorized note changes.

## Description

Editing the HTML form replaces the client_id value with the target's ID, allowing the auto-submit to forge a request on behalf of the victim. This heightens impact in organizations where client_ids are known. The scenario assumes the victim is logged in; outcomes include data loss or malicious injection.

## Requirements

1. Generated CSRF PoC HTML file
2. Knowledge of victim's client_id
3. Text editor (e.g., VS Code)

## Defense

Defensive measures and detection strategies:

- Validate client_id against session user
- Implement referrer checks or same-origin policy enforcement

## Objectives

1. Target specific victim
2. Enable unauthorized actions like deletion
3. Maintain PoC functionality

## Instructions

### Step 1: Open HTML File

**Context**: Prepare for editing.

Open the PoC in a text editor.

> Locate the <form> section.

### Step 2: Edit client_id Parameter

**Context**: Swap to victim's ID.

Change <input type="hidden" name="client_id" value="original"> to <input type="hidden" name="client_id" value="victim_id">. Optionally, set note="" for deletion.

> Save file; test locally if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-modify
- victim-targeting
