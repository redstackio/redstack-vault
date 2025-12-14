---
tags:
  - xss
  - trigger
  - slack
  - facebook
type: procedure
tools:
  - '[[tools/jQuery-Facebook-Photo-Selector]]'
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:16:08.057Z'
sub_techniques: []
id: 4d376234-a25c-4e5c-8e08-47dc468eb7a5
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Trigger-XSS-via-Facebook-Photo-Import-in-Slack

## Summary

This procedure triggers the stored XSS by selecting the malicious Facebook album in Slack's photo import selector, causing the unsanitized album name to execute JavaScript in the browser context.

## Description

Upon selecting the Facebook option in Slack's profile photo settings, the jQuery-Facebook-Photo-Selector library fetches album data. The album name, containing the XSS payload, is inserted into the DOM without HTML escaping, leading to JavaScript execution such as alerting cookies for theft.

## Requirements

1. Malicious Facebook album already created
2. Access to Slack photo settings
3. Facebook-Slack integration authorized

## Defense

Defensive measures and detection strategies:

- Escape HTML in all reflected third-party data
- Audit third-party libraries like jQuery-Facebook-Photo-Selector for sanitization issues
- Implement browser-based protections like XSS auditors

## Objectives

1. Fetch and reflect the malicious album name
2. Execute arbitrary JavaScript in Slack session
3. Steal session cookies for potential hijacking

## Instructions

### Step 1: Select Facebook Import

**Context**: Initiate the integration to open the photo selector.

In Slack's photo change interface, click "Change using Facebook" and authorize if needed.

### Step 2: Choose Malicious Album

**Context**: Select the album to trigger payload reflection.

Browse albums and select the one with the malicious name. The name will be displayed unsanitized.

### Step 3: Observe Execution

**Context**: Confirm XSS trigger.

The payload executes, e.g., alerting document.cookie. For real attacks, replace alert with exfiltration to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Credential Access]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/jQuery-Facebook-Photo-Selector]]

## Tags

- xss
- trigger
- slack
- facebook
