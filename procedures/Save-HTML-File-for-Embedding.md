---
tags:
  - clickjacking
  - html-file
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.158Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 21f40f2c-be34-4bbd-8ddf-15e77dab6d27
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Save-HTML-File-for-Embedding

## Summary

This procedure saves the created HTML iframe code as a local file with .html extension, preparing it for browser execution to test site embedding.

## Description

Saving the HTML ensures the iframe code is persisted and can be easily loaded in a browser. This step is crucial for offline testing of clickjacking feasibility without needing a web server, directly exploiting the target's lack of frame protection on AWS S3-hosted pages.

## Requirements

1. Text editor with save functionality.
2. Write permissions on local filesystem.
3. The HTML code from the creation procedure.

## Defense

Defensive measures and detection strategies:

- Educate developers on header implementation to avoid such simple tests.
- Use browser developer tools to inspect for local file-based attacks during testing.
- Employ web application firewalls (WAF) to detect anomalous embedding attempts.

## Objectives

1. Create a portable .html file for the clickjacking demo.
2. Enable quick iteration and sharing of the test artifact.
3. Confirm file readiness for browser validation.

## Instructions

### Step 1: Save Content as HTML File

**Context**: Use the text editor's save dialog to store the iframe HTML with appropriate extension, ensuring browser compatibility.

No command execution required; manually select File > Save As, name it e.g., "cj.html", and choose .html type.

> Upon success, the file icon should indicate an HTML document, ready for opening.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[file-saving]]
- [[local-testing]]
