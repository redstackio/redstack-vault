---
tags:
  - xss
  - github
  - server-setup
type: procedure
tools:
  - '[[tools/Dummy-GitHub-Server]]'
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
updated_at: '2025-12-13T23:55:20.975Z'
sub_techniques: []
id: 88dcea35-f008-4f8d-bb3b-e5418d6cab2b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-Malicious-GitHub-Server

## Summary

This procedure sets up a dummy GitHub server hosting a repository with a scoped label containing an XSS payload in the color field, allowing injection during GitLab imports.

## Description

The vulnerability stems from insufficient validation of label colors in scoped labels (format 'group::label') during GitHub imports into GitLab. By hosting a fake GitHub API server, the attacker crafts a label like 'yvvdwf::label-name' with a color value that closes HTML tags and injects a form with a script, bypassing CSP. This payload persists in the imported project and executes on label/issue views.

## Requirements

1. Server hosting capability (e.g., VPS at IP 51.75.74.52)
2. Port 11211 open and accessible
3. Knowledge of GitHub API structure to mimic responses
4. Fake GitHub token for import simulation

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all imported label data, especially colors for scoped labels
- Implement strict CSP with no unsafe-inline/eval
- Log and review import activities for anomalous hostnames

## Objectives

1. Create a malicious scoped label with XSS payload
2. Expose it via a fake GitHub API endpoint
3. Ensure compatibility with GitLab's import process

## Instructions

### Step 1: Deploy Dummy Server

**Context**: Host a server mimicking GitHub's repository and label APIs.

Use [[tools/Dummy-GitHub-Server]] configured at http://51.75.74.52:11211. Implement endpoints like /repos/{owner}/{repo}/labels to return the malicious label.

> Expected output: Server logs showing requests; curl to /api/v3/repos/test/labels should return JSON with the label.

### Step 2: Create Malicious Label

**Context**: Define the label with XSS in color.

In the server config, set label: { "name": "yvvdwf::label-name", "color": ">yvvdwf-label<form class='hidden gl-show-field-errors'><input title='<script>alert(document.domain)</script>'>' }.

> Expected output: Label JSON verifiable; payload includes tag closure and script injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Dummy-GitHub-Server]]

## Tags

- [[xss]]
- [[github]]
- [[server-setup]]
