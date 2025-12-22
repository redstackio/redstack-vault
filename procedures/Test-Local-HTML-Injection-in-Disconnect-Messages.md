---
tags:
  - xss
  - injection
  - csgo
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/disconnect-with-html-payload]]'
platforms:
  - Windows
  - 'CS:GO'
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 475c9191-23d1-4ff5-82f7-6012c5bada57
created_at: '2025-12-14T00:11:25.222Z'
updated_at: '2025-12-14T00:11:25.222Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Local HTML Injection in Disconnect Messages

## Summary

This procedure tests local disconnect messages in CS:GO to confirm that raw HTML is parsed, using simple payloads like images to verify XSS vulnerability.

## Description

Executing a disconnect command with an embedded img tag loads external content, confirming unsanitized HTML in popups. Run twice to handle caching.

## Requirements

1. CS:GO client installed
2. Access to console
3. Internet for loading external images

## Defense

Defensive measures and detection strategies:

- Sanitize disconnect messages
- Disable HTML parsing in UI labels

## Objectives

1. Confirm local XSS
2. Validate payload parsing
3. Escalate to JS testing

## Instructions

### Step 1: Execute Disconnect Command

**Context**: Test HTML injection with image payload.

Execute [[commands/disconnect-with-html-payload]]:

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

> Run twice; image should appear in popup after caching.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/disconnect-with-html-payload]]

## Tools Used



## Tags

- [[xss]]
- [[injection]]
- [[csgo]]
