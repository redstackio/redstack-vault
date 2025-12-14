---
tags:
  - xss-trigger
  - execution
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.373Z'
sub_techniques: []
id: 33c4d5eb-df33-4f66-9bb0-16d8055a9ae6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-No-Pages-View

## Summary

This procedure demonstrates triggering the stored XSS by accessing a view that renders the malicious message, executing the JavaScript payload.

## Description

When a user (authenticated or not) views a sitemap or page section with no listed pages, Concrete CMS outputs the stored message directly into the HTML without escaping, executing the injected script in the victim's browser context for attacks like cookie theft or defacement.

## Requirements

1. Payload saved in configuration from prior steps
2. Access to the frontend of the CMS (no admin needed)
3. A page or section intentionally or naturally lacking listed pages

## Defense

Defensive measures and detection strategies:

- Output encoding in all template renders (e.g., htmlspecialchars in PHP)
- Content Security Policy (CSP) to block inline scripts
- Client-side monitoring for unexpected alerts or network requests

## Objectives

1. Execute the stored payload
2. Validate impact on victim browsers
3. Demonstrate potential for escalation

## Instructions

### Step 1: Navigate to Vulnerable View

**Context**: Load a page that displays the no-pages message.

Go to a sitemap URL or create/test a section with no child pages, e.g., /sitemap or an empty category view.

> The page renders, and the message appears, triggering the script.

### Step 2: Observe Execution

**Context**: Confirm the payload runs as expected.

Look for the alert popup or check network tab for exfiltration requests.

> JavaScript executes, showing alert(1) or sending data to attacker server.

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
- [[Execution]]
