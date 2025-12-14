---
id: proc-create-poc-html-iframe
tags:
  - clickjacking
  - poc-creation
  - iframe-test
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.837Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Proof-of-Concept-HTML-for-Iframe-Embedding

## Summary

This procedure creates a simple HTML file that embeds the target site (e.g., yelp.com) in an iframe to test for clickjacking susceptibility, confirming if the site can be framed without restrictions.

## Description

Clickjacking exploits rely on embedding victim sites in iframes on attacker-controlled pages. This PoC simulates a malicious page by using basic HTML to load the target in a fixed-size iframe. It requires a text editor and local file saving. Outcomes include a testable file that, when loaded, demonstrates embedding success, aiding in vulnerability validation.

## Requirements

1. Text editor (e.g., Notepad, VS Code)
2. Local file system access
3. Target URL (e.g., http://yelp.com)

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header to block embedding
- Scan for iframe usage in client-side code
- Educate users on phishing indicators

## Objectives

1. Generate embeddable PoC for testing
2. Simulate attacker-controlled framing
3. Prepare for browser verification

## Instructions

### Step 1: Write HTML Code

**Context**: Construct the basic iframe structure.

Create a new file and add: <html><body><iframe src="http://yelp.com" width="500" height="500"></iframe></body></html>

> This sets up the iframe with Yelp as source and visible dimensions.

### Step 2: Save File

**Context**: Store the PoC for local execution.

Save the file as "yelp-iframe-poc.html" on your local machine.

> File saves successfully; ready for browser loading. Expected output: HTML file icon in file explorer.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[clickjacking]]
- [[poc-creation]]
