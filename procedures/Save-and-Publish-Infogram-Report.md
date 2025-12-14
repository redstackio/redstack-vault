---
id: proc-infogram-publish-001
tags:
  - publish
  - report
  - storage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.895Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-and-Publish-Infogram-Report

## Summary

This procedure saves the modified report with the injected payload and publishes it publicly, making the stored XSS accessible to victims via a shareable URL.

## Description

After injection, saving persists the payload in Infogram's backend. Publishing generates a public view URL where the Overview Table renders the malicious HTML/JS without further sanitization. This step transitions the attack from preparation to deployment, with impact realized upon victim interaction. Requires editor access from previous steps.

## Requirements

1. Injected payload in editor
2. Save permissions (standard user)
3. Public publishing enabled on account

## Defense

Defensive measures and detection strategies:

- Scan saved content for executable scripts before publishing
- Rate-limit report publications to detect abuse

## Objectives

1. Persist the payload server-side
2. Generate public access URL
3. Confirm payload in published preview

## Instructions

### Step 1: Save the Report

**Context**: Commit changes to store the payload.

Click the 'Save' button in the editor toolbar.

> Confirmation message appears; no errors if payload accepted.

### Step 2: Publish the Report

**Context**: Make the report viewable externally.

Select 'Publish' and choose public visibility, generating URL like https://infogram.com/report-classic-1g57pr0g3xdvp01.

> Public link ready for sharing; payload visible in published view.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[publish]]
- [[report]]
- [[storage]]
