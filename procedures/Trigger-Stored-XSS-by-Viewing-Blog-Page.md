---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - xss-trigger
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.305Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Blog-Page

## Summary

This procedure demonstrates loading the affected blog page to execute the stored JavaScript payload, confirming the success of the stored XSS attack in Concrete CMS.

## Description

When the blog page renders, the CMS outputs the stored Custom Title Text without escaping, causing the browser to parse and execute the injected script. This affects all users viewing the page, leading to arbitrary JS execution in their session context within the web platform.

## Requirements

1. Payload successfully saved in the blog tile.
2. Access to view the public blog page (no auth needed for trigger).
3. Victim's browser without XSS protections like NoScript.

## Defense

Defensive measures and detection strategies:

- Output-encode all dynamic content (e.g., using htmlspecialchars in PHP) before rendering.
- Deploy browser-based protections like XSS auditors and monitor for unexpected JS alerts or network requests.

## Objectives

1. Load the page to trigger payload execution.
2. Observe JS effects like alerts or data exfiltration.
3. Validate impact on victim browsers.

## Instructions

### Step 1: Navigate to Blog Page

**Context**: Visit the page containing the malicious tile to initiate rendering.

In a web browser, go to the URL of the blog page (e.g., `/blog`).

> The page loads, and the title renders the payload, triggering the script.

### Step 2: Observe Execution

**Context**: Confirm the payload runs by checking for expected behaviors.

Look for the alert(1) popup or inspect the browser console for errors/script output.

> Alert box appears, proving JS execution in the page context.

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
- [[javascript-execution]]
