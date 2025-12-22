---
tags:
  - discovery
  - grep
type: procedure
tools:
  - '[[tools/grep]]'
  - '[[tools/SourceMod]]'
  - '[[tools/Metamod]]'
  - '[[tools/CS:GO-Dedicated-Server]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/disconnect-html-test]]'
  - '[[commands/kickid-test]]'
  - '[[commands/sm-kick-test]]'
  - '[[commands/sm-testkick-rce]]'
platforms:
  - Windows
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 62b77e5d-ec62-44e9-bfce-f326917e7807
created_at: '2025-12-11T06:10:15.661Z'
updated_at: '2025-12-11T06:10:15.661Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1590]]'
---
# Search for Vulnerable HTML Tags

## Summary

This procedure uses grep to search extracted Panorama files for tags that allow raw HTML parsing, identifying potential XSS vectors.

## Description

Grepping for 'html="true"' reveals labels in XML files that parse raw HTML without sanitization, such as in popup_generic.xml used for disconnect messages.

## Requirements

1. Extracted Panorama files
2. grep tool installed
3. Basic command-line knowledge

## Defense

Defensive measures and detection strategies:

- Secure game file integrity
- Patch known vulnerabilities

## Objectives

1. Locate unsanitized HTML attributes
2. Identify files like chat.xml and popup_generic.xml
3. Confirm vulnerability locations

## Instructions

### Step 1: Run Grep Search

**Context**: Search all layout files.

Execute grep:

```bash
grep -r 'html="true"' panorama/layout/
```

> Lists files with matching tags.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Network Information]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/grep]]

## Tags

- discovery
- grep
