---
id: 0f61ee07-0e8d-4687-aff2-372c6f774de7
name: Trigger Wiki Page Rendering for RCE
type: procedure
verified: false
submitted: true
created_at: '2025-12-09T00:20:45.088Z'
updated_at: '2025-12-09T00:20:45.088Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - rce
  - rendering-trigger
commands: []
platforms:
  - Web
tools: []
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Trigger Wiki Page Rendering for RCE

## Summary

This procedure loads the malicious Wiki page to trigger Kramdown rendering and execute the embedded Ruby code.

## Description

Accessing the page causes the server to render the .rmd file, activating the unsafe inline options and leading to RCE.

## Requirements

1. Malicious page pushed to Wiki
2. Browser access to GitLab Wiki
3. Payload uploaded previously

## Defense

Defensive measures and detection strategies:

- Update Kramdown to safe versions
- Log and alert on rendering errors

## Objectives

1. Execute payload on server
2. Achieve RCE
3. Confirm via logs

## Instructions

### Step 1: Load Page

**Context**: Refresh and access the page.

Refresh the Wiki and load the page1 page, triggering rendering.

> This executes the code via Kramdown.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #rce
- #rendering-trigger
