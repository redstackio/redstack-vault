---
tags:
  - xss-execution
  - javascript
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
updated_at: '2025-12-13T23:52:20.829Z'
sub_techniques: []
id: 006d09c3-b917-4978-9037-d80c4f214715
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Public-Profile

## Summary

This procedure simulates a victim viewing the attacker's public profile and interacting with the malicious link to execute the stored JavaScript payload.

## Description

The final exploitation step loads the public profile, where the unsanitized description renders the HTML. Clicking the link triggers the data URI, executing JS in the viewer's context. Prerequisites: Saved payload. Outcomes: Arbitrary code runs, enabling attacks like phishing or theft.

## Requirements

1. Public profile URL with stored recommendation
2. Victim browser (incognito for simulation)
3. No attacker privileges needed for trigger

## Defense

Defensive measures and detection strategies:

- Escape HTML on output/rendering (e.g., use DOMPurify)
- Block data URIs and base64 in CSP headers
- Monitor for XSS alerts or unusual JS execution in client logs

## Objectives

1. Load the profile to render the payload
2. Execute JS via user interaction
3. Demonstrate impact like alert or data exfil

## Instructions

### Step 1: Access Public Profile

**Context**: Simulate victim view.

Navigate to the profile URL in a new browser session.

> Profile loads with recommendations visible.

### Step 2: Interact with Payload

**Context**: Trigger execution.

Locate and click the "Click Here" link in the description.

> Alert "XSS" appears; replace with malicious code for real attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[JavaScript]]
