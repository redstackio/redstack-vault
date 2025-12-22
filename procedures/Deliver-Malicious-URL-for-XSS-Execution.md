---
tags:
  - xss-execution
  - victim-delivery
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:15.853Z'
sub_techniques: []
id: 67955fa2-745f-436d-afff-71189fc85b55
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174004
name: Deliver-Malicious-URL-for-XSS-Execution
type: procedure
verified: false
submitted: false
created_at: 2024-10-01T00:00:00Z
updated_at: 2024-10-01T00:00:00Z
tactics: [[Collection]]
techniques: [[JavaScript]], [[Drive-by Compromise]]
sub_techniques: []
tags: xss-execution, victim-delivery, social-engineering
commands: []
platforms: Web
tools: []
---

# Deliver-Malicious-URL-for-XSS-Execution

## Summary

This procedure involves delivering the crafted malicious URL to a victim, resulting in the execution of the injected JavaScript payload when they access the TopCoder wiki endpoint.

## Description

Once the payload is in place, social engineering or phishing delivers the URL. Upon access, the reflected XSS executes in the victim's browser context, potentially stealing cookies or performing actions on their behalf. Impact includes session hijacking; targets are web users with access to the wiki.

## Requirements

1. Crafted malicious URL from previous step
2. Method to deliver URL (email, chat, etc.)
3. Victim with browser access to the site

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Monitor for anomalous JS execution via browser logs
- Implement XSS auditors or CSP headers

## Objectives

1. Ensure victim interaction with the URL
2. Confirm payload execution
3. Achieve data collection or further compromise

## Instructions

### Step 1: Prepare Delivery

**Context**: Select a method to share the URL without arousing suspicion.

Embed in a message like "Check this wiki attachment error: [URL]"

> Victim receives and clicks the link.

### Step 2: Verify Execution

**Context**: Observe or log the outcome when victim accesses the URL.

The page loads, triggering the onerror event and alert(document.domain).

> Success: JS executes, e.g., alert shows domain; potential for exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[victim-delivery]]
- [[social-engineering]]
