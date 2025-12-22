---
tags:
  - xss-trigger
  - js-execution
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
updated_at: '2025-12-14T03:16:31.083Z'
sub_techniques: []
id: a799aca0-ccb3-4a1e-916f-451db3311202
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS

## Summary

This procedure visits the public profile to render the stored payload and interacts with the malicious link to execute arbitrary JavaScript in the browser context.

## Description

The final exploitation step involves loading the profile where Markdown is rendered into HTML links. Clicking the javascript: URI executes code like alerting cookies or setting onerror handlers for theft. Impact includes client-side attacks on any visitor, as profiles are public.

## Requirements

1. Saved malicious statement on a public profile
2. Victim browser (can be attacker's for testing)
3. No CSP blocking inline JS (not present here)

## Defense

Defensive measures and detection strategies:

- Block javascript: and other unsafe protocols in link rendering
- Implement strict CSP to prevent JS execution
- Monitor for JS errors and alerts in client logs

## Objectives

1. Render and click malicious link
2. Execute JS payload
3. Demonstrate impact like cookie exfiltration

## Instructions

### Step 1: Load Public Profile

**Context**: Access the page where payload renders.

Navigate to https://gratipay.com/~username/ in a browser (use incognito for victim simulation).

### Step 2: Locate Malicious Link

**Context**: Identify the rendered statement.

Scroll to the profile statement section; look for the clickable link from the payload (e.g., 'notmalicious').

### Step 3: Interact to Trigger

**Context**: Execute the JS.

Click the link; observe alert with document.cookie or console for onerror output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[web]]
