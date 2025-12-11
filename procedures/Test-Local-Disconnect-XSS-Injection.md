---
tags:
  - xss
  - testing
type: procedure
tools:
  - '[[tools/grep]]'
  - '[[tools/SourceMod]]'
  - '[[tools/Metamod]]'
  - '[[tools/CS:GO-Dedicated-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/disconnect-html-test]]'
  - '[[commands/kickid-test]]'
  - '[[commands/sm-kick-test]]'
  - '[[commands/sm-testkick-rce]]'
platforms:
  - Windows
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 08347e02-83ac-4ae8-ac3c-4d323b946725
created_at: '2025-12-11T06:10:15.658Z'
updated_at: '2025-12-11T06:10:15.658Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Test Local Disconnect XSS Injection

## Summary

This procedure tests if disconnect popups in CS:GO parse raw HTML by injecting an image tag locally.

## Description

Using the disconnect command with an img src payload confirms that the Panorama UI parses external content, laying groundwork for remote exploitation.

## Requirements

1. Running CS:GO client
2. Console access
3. Internet connection for image loading

## Defense

Defensive measures and detection strategies:

- Sanitize UI inputs
- Disable HTML parsing in labels

## Objectives

1. Confirm HTML injection
2. Test caching behavior
3. Validate local XSS

## Instructions

### Step 1: Execute Disconnect Command

**Context**: Inject img tag in disconnect message.

Execute [[commands/disconnect-html-test]]:

```bash
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

> Displays image after second run due to caching.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/disconnect-html-test]]

## Tools Used



## Tags

- xss
- testing
