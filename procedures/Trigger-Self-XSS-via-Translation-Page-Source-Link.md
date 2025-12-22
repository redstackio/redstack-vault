---
tags:
  - xss
  - self-xss
  - trigger
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.280Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: fc9a7015-b773-4fdd-a3b8-a69c01c1aeed
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-via-Translation-Page-Source-Link

## Summary

This procedure triggers the stored self-XSS payload in Weblate by navigating to a translation page and clicking a source file link, causing the malicious Editor link to execute JavaScript in the user's browser.

## Description

After configuring the Editor link with a JavaScript payload, accessing a translation page (e.g., for a project like 'hello') and interacting with source information links invokes the custom Editor link. This executes the payload, such as alerting document cookies, in the attacker's session only. The vulnerability stems from unsanitized storage and client-side handling of the link, enabling self-XSS without server involvement in execution.

## Requirements

1. Previously configured malicious Editor link in profile
2. Access to translation projects in Weblate
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Sanitize or validate Editor link outputs to prevent JavaScript URIs
- Client-side escaping of user-stored links before use
- Log and alert on unexpected JavaScript execution in web apps

## Objectives

1. Invoke the stored payload via normal UI flow
2. Execute JavaScript to access session data
3. Confirm self-XSS limited to user context

## Instructions

### Step 1: Navigate to Translation Page

**Context**: Set up the environment to access triggerable links.

Go to https://demo.weblate.org/translate/hello/master/en_GB/?type=all.

> The translation interface loads, including the Source Information section with file links.

### Step 2: Click Source File Link

**Context**: Trigger the Editor link by interacting with a source file.

Click on the 'main.c' link under Source Information.

> This opens the file using the configured Editor link, executing the JavaScript URI and displaying an alert with cookies followed by a confirm dialog.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- self-xss
- weblate
