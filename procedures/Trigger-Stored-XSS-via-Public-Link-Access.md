---
tags:
  - xss
  - execution
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 86a1b4fe-7ebb-4067-a48c-943c8d1612d4
created_at: '2025-12-14T03:16:31.133Z'
updated_at: '2025-12-14T03:16:31.133Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Public-Link-Access

## Summary

This procedure involves sharing and accessing the public link to execute the stored JavaScript payload in the browser.

## Description

When the public link is opened, Slack renders the file post's title and body as HTML without proper escaping, causing the injected script to execute. In this case, it triggers an alert, but could be extended for more severe actions like keylogging or redirects. The sandbox domain limits impact by lacking cookies, preventing session hijacking.

## Requirements

1. Valid public link from the malicious post
2. Target browser (victim's or test)
3. No authentication needed for access

## Defense

Defensive measures and detection strategies:

- Apply HTML entity encoding to all rendered user content on public pages
- Implement browser-based sandboxing or no-script modes for public views
- Monitor access logs for public links and alert on suspicious patterns (e.g., high access from single IPs)

## Objectives

1. Execute arbitrary JavaScript in the victim's context
2. Validate the stored XSS vulnerability
3. Highlight risks of public content rendering

## Instructions

### Step 1: Share the Link

**Context**: Distribute the URL to potential victims.

Send the public link via email, social media, or other channels to the target.

### Step 2: Access the Link

**Context**: Load the page to trigger rendering.

Open the URL (e.g., `https://slack-files.com/T025LLJ2X-F025N8W7W-3a5691`) in a browser.

### Step 3: Observe Execution

**Context**: Confirm the payload activates.

Look for the alert box displaying '10', indicating successful JavaScript execution.

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
- [[Execution]]
- [[slack]]
