---
id: proc-gist-malicious-create-001
tags:
  - xss
  - github
  - gist
  - payload-creation
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
updated_at: '2025-12-13T23:56:19.760Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-GitHub-Gist

## Summary

This procedure creates a GitHub Gist with a filename designed to exploit XSS vulnerabilities in integrations like Slack by embedding an SVG onload JavaScript payload.

## Description

In the context of testing Slack's Gist integration, a malicious filename such as "><svg onload=alert(1)>" is used. When Slack renders the Gist filename in an HTML context without proper escaping, the SVG tag triggers JavaScript execution. This step requires a GitHub account and focuses on payload crafting for client-side attacks. Expected outcome is a shareable Gist URL that delivers the payload indirectly.

## Requirements

1. Active GitHub account with permission to create public Gists
2. Basic knowledge of HTML/SVG and JavaScript payloads
3. Internet access to GitHub

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs like filenames in integrations
- Use Content Security Policy (CSP) to block inline scripts and SVG execution
- Monitor for anomalous Gist shares in collaboration tools like Slack

## Objectives

1. Generate a Gist that embeds an XSS payload in the filename
2. Ensure the payload survives GitHub's processing
3. Prepare for delivery in vulnerable integrations

## Instructions

### Step 1: Log in to GitHub and Create New Gist

**Context**: Access GitHub's Gist creation interface to set up the malicious file.

Navigate to https://gist.github.com and sign in. Click 'New Gist'.

### Step 2: Set Malicious Filename and Content

**Context**: Craft the filename to include the XSS payload while adding innocuous content to the file body.

Enter the filename as "><svg onload=alert(1)>" (or a more stealthy variant). Add any text to the file content, e.g., 'Test file'. Select 'Create public gist'.

**Expected Output**: Gist URL generated, e.g., https://gist.github.com/username/abc123.

### Step 3: Verify Payload Integrity

**Context**: Confirm the filename renders the payload correctly.

View the raw Gist URL (e.g., https://gist.githubusercontent.com/username/abc123/raw/) and inspect the source to ensure the filename is preserved.

**Expected Output**: Filename appears as "><svg onload=alert(1)> in the HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[github]]
- [[gist]]
