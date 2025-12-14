---
tags:
  - xss-trigger
  - execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.679Z'
sub_techniques: []
id: dc1a93f8-55ff-4960-aa1f-e803e7a7546c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Page-Edit

## Summary

This procedure describes inducing a victim to edit the compromised wiki page, causing the stored XSS payload to execute in their browser for potential data exfiltration or hijacking.

## Description

The vulnerability triggers during the edit load phase, where the page content is rendered unsafely. In the attack scenario, social engineering or access luring gets another authenticated user to open the edit URL, executing the JavaScript. This enables collection of session data; prerequisites include the saved payload and victim access.

## Requirements

1. Compromised page with stored payload
2. Victim with edit access to the page
3. Victim's browser loading the edit endpoint

## Defense

Defensive measures and detection strategies:

- Escape all stored content during editor rendering
- Browser-based CSP to prevent script execution
- User education on suspicious edit requests

## Objectives

1. Execute the injected JavaScript in victim context
2. Demonstrate impact like domain alerts or cookie access
3. Enable follow-on attacks such as session theft

## Instructions

### Step 1: Lure Victim to Edit

**Context**: Direct the victim to the edit URL to load the content.

No specific command; share the URL https://apps.topcoder.com/wiki/pages/editpage.action?pageId=165871793.

> Victim accesses as signed-in user.

### Step 2: Observe Execution

**Context**: Monitor for payload activation upon editor load.

No specific command; execution is automatic.

> Expected output: Alert with document.domain; console logs or network requests for exfil.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[Collection]]
