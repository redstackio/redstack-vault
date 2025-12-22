---
id: proc-imgur-drag-trick
tags:
  - ui-manipulation
  - drag-drop
  - social-engineering
type: procedure
tools:
  - '[[tools/firefox-browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ondragend-handle-ui-update]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:47:13.049Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Trick User into Dragging Image via UI Manipulation

## Summary

This procedure handles the dragend event on the upload area to detect user interaction and updates the UI to prompt copying the malicious payload, advancing the social engineering chain.

## Description

After detecting the upload page, the attacker overlays a drag zone. When the victim drags an image (tricked by clickjacking), the ondragend event fires, clearing and updating buttons to guide pasting. This exploits user trust in the UI. Expected outcome: Victim proceeds to clipboard step.

## Requirements

1. Upload page detected from prior monitoring
2. Overlaid drag elements in place
3. Victim interaction via mouse/touch

## Defense

Defensive measures and detection strategies:

- Validate drag sources and destinations server-side
- Disable or sandbox drag events in embeds
- Warn users of unexpected UI prompts
- Log anomalous drag interactions

## Objectives

1. Confirm user engagement with upload
2. Prompt next payload delivery step
3. Maintain deception flow

## Instructions

### Step 1: Attach Dragend Handler

**Context**: Listen for drag completion and sequence UI changes.

**Command** ([[commands/ondragend-handle-ui-update]]):
```javascript
ondragend = function() {
  btn1.innerHTML = '';
  setTimeout(function() {
    btn1.innerHTML = '';
    btn2.innerHTML = 'copy the red text and paste here after that, press enter!';
  }, 1100);
};
```

> Updates UI post-drag. Expected output: Buttons clear and new prompt after 1.1s.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Steal Web Session Cookie]] Drive-By Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/ondragend-handle-ui-update]]

## Tools Used

- [[tools/firefox-browser]]

## Tags

- drag-event
- ui-trickery
