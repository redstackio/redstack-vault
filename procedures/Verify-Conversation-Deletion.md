---
tags:
  - verification
  - ui-check
  - deletion-impact
type: procedure
tools:
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/reveal-copilot-gui]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:48.176Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5801c622-2ae9-49c6-8624-5bd7a6992a1c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-Conversation-Deletion

## Summary

This procedure confirms the success of the IDOR exploitation by refreshing the victim account's page, revealing the GUI, and observing the absence of the deleted conversation.

## Description

After deletion, switch to the victim account to validate impact. Re-run the reveal script and check for missing elements. This step ensures the mutation had the intended destructive effect without server-side errors.

## Requirements

1. Victim account access
2. Knowledge of the targeted conversation's appearance
3. Browser console access

## Defense

Defensive measures and detection strategies:

- Implement soft deletes with audit trails for recovery
- Notify users of deletions and log for forensics
- Monitor for repeated verification patterns indicating testing

## Objectives

1. Confirm conversation removal
2. Assess real-world impact
3. Document exploitation success

## Instructions

### Step 1: Switch and Refresh

**Context**: Log in as victim and reload the opportunities page.

Navigate to https://hackerone.com/opportunities/all.

> Clears any cached state.

### Step 2: Reveal and Inspect

**Context**: Re-expose the UI and check for the conversation.

**Command** ([[commands/reveal-copilot-gui]]):
```javascript
document.querySelectorAll('div').forEach(e=>{ e.classList.remove('hidden'); e.classList.remove('dark:text-white'); });
```

> Run in console. Expected output: GUI visible, but targeted conversation gone (no ID match in DOM).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/reveal-copilot-gui]]

## Tools Used

- [[tools/Browser-Console]]

## Tags

- verification
- ui-check
