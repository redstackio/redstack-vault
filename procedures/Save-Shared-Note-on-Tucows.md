---
tags:
  - web
  - post-request
  - notes
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
updated_at: '2025-12-14T17:30:07.445Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d37bbff-1d3f-4801-91aa-4bf5d1eb4578
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Save-Shared-Note-on-Tucows

## Summary

This procedure saves arbitrary text to the Shared Notes field on Tucows via a POST request, generating the vulnerable endpoint interaction needed for CSRF PoC creation.

## Description

The attacker inputs text into the notes area and submits it, triggering a POST to the notes-saving endpoint with parameters like ajax=save_note, client_id, note, and area=client. This step is crucial for capturing the exact request format lacking CSRF protection. In a web environment, it simulates normal user behavior before exploitation.

## Requirements

1. Active session after login
2. Access to Shared Notes interface
3. Knowledge of parameter structure (inferred from platform)

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all state-changing POST endpoints
- Log and alert on unusual note modifications

## Objectives

1. Trigger capturable POST request
2. Confirm endpoint behavior
3. Set up for interception

## Instructions

### Step 1: Input Note Text

**Context**: Enter content to prepare the save action.

Use the web form to type arbitrary text in the notes field.

> Example: "Test note for capture."

### Step 2: Submit Save Request

**Context**: Send POST to endpoint.

Click save; browser sends POST with params: ajax=save_note, client_id=your_id, note=text, area=client.

> Expected: Success response, notes updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- post-request
