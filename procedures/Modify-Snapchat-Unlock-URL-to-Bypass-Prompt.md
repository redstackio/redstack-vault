---
id: p-snapchat-modify-bypass-url
tags:
  - csrf
  - snapchat
  - bypass
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.596Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Modify Snapchat Unlock URL to Bypass Prompt

## Summary

This procedure modifies the Snapchat lens unlock URL by changing the 'type' parameter to bypass the user confirmation prompt, enabling silent lens installation via CSRF.

## Description

Snapchat's unlock endpoint lacks proper CSRF protection, allowing the 'type' parameter to be altered from 'SNAPCODE' (prompt-enabled) to 'SNAPCODE_NO_PROMPT' (no prompt). This forces the lens to install without interaction when the link is opened, applicable on web and app integrations. The attack relies on social engineering to get victims to click the link.

## Requirements

1. Valid lens UUID and metadata
2. Text editor for URL modification
3. Snapchat app on target platform for testing

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to unlock endpoints
- Validate 'type' parameter server-side
- Log and alert on NO_PROMPT usage without auth

## Objectives

1. Create a prompt-bypassing URL
2. Test silent installation
3. Confirm unauthorized lens add

## Instructions

### Step 1: Edit Type Parameter

**Context**: The vulnerability stems from unchecked parameter allowing bypass.

**Instructions**: Take the normal URL https://www.snapchat.com/unlock/?type=SNAPCODE&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01 and replace 'type=SNAPCODE' with 'type=SNAPCODE_NO_PROMPT'.

### Step 2: Test Modified URL

**Context**: Verify the bypass works without prompt.

**Instructions**: Open the modified URL https://www.snapchat.com/unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01 in a browser on a device with Snapchat. The lens should install automatically.

> Expected: Lens appears in the user's collection without any dialog.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[snapchat]]
