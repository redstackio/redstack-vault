---
id: proc-inject-xss-oberlo
tags:
  - xss-injection
  - payload-delivery
  - stored-xss
  - oberlo
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.236Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Profile-Name

## Summary

This procedure exploits the lack of input sanitization in Oberlo's profile name field by injecting a JavaScript payload, storing it for later execution when profiles are viewed.

## Description

The name field in Oberlo's profile settings accepts arbitrary input without proper escaping, allowing stored XSS. The payload `"><img src=x onerror=alert(document.domain)>` breaks out of HTML attributes and triggers JavaScript on error. This is submitted via the web form and persists in the backend. Prerequisites include profile access; outcomes enable client-side attacks like alert execution or more malicious scripts for data theft.

## Requirements

1. Access to profile settings page
2. Web browser
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs on storage and output
- Use Content Security Policy (CSP) to restrict inline scripts
- Validate input length and content for profile fields

## Objectives

1. Store malicious JavaScript in the profile name
2. Ensure payload survives form submission
3. Enable execution for profile viewers

## Instructions

### Step 1: Locate Name Field

**Context**: Identify the vulnerable input on the profile page.

On https://app.oberlo.com/settings/account/profile, find the "Name" text input field.

> The field appears as a standard HTML input without restrictions.

### Step 2: Enter Payload

**Context**: Craft and input the XSS payload to inject script.

Type or paste `"><img src=x onerror=alert(document.domain)>` into the Name field.

> This payload closes any surrounding HTML tags and executes JS on image load failure.

### Step 3: Submit Form

**Context**: Save the profile to store the payload backend.

Click the "Save" or "Update Profile" button to submit.

> If successful, the page reloads without errors, confirming storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-delivery]]
- [[stored-xss]]
- [[oberlo]]
