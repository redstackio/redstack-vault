---
tags:
  - xss
  - injection
  - twitter
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
impact_level: low
detection_risk: low
sub_techniques: []
id: 51b879ce-4280-401b-9a51-9404475ed2d6
created_at: '2025-12-14T03:16:14.482Z'
updated_at: '2025-12-14T03:16:14.482Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Poll-Option

## Summary

This procedure involves entering a malicious HTML/JavaScript payload into the poll option input field during Twitter poll creation to test for insufficient input sanitization, enabling potential reflected XSS.

## Description

In the context of Twitter's poll feature, user inputs for poll options are not adequately sanitized on the client side, allowing HTML tags and JavaScript to be injected. This step focuses on crafting and submitting a simple payload like an onerror-based image tag, which can lead to code execution upon rendering. The attack is limited to the attacker's session but highlights a flaw exploitable in older browsers. Prerequisites include a logged-in Twitter account and access to the compose tweet interface with poll options.

## Requirements

1. Active Twitter session with poll creation permissions
2. Web browser capable of handling HTML input
3. Internet access to twitter.com

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization using libraries like DOMPurify on client and server sides
- Enforce robust Content Security Policy (CSP) to block inline script execution
- Monitor for anomalous JavaScript alerts or DOM manipulations in browser logs

## Objectives

1. Validate lack of client-side sanitization in poll inputs
2. Prepare payload for reflection in preview
3. Confirm payload acceptance without immediate rejection

## Instructions

### Step 1: Access Poll Creation

**Context**: Log in to Twitter and start creating a new poll to access the option input fields.

Navigate to twitter.com, compose a new tweet, and select the poll option to add input fields for poll choices.

### Step 2: Enter Malicious Payload

**Context**: Input the XSS payload into an option field to test reflection.

Enter the following payload into one of the poll option text fields:

```html
<img src=x onerror=alert(1)>
```

> This payload creates an invalid image that triggers an onerror event, executing alert(1) when rendered. The input should be accepted without escaping.

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
- [[injection]]
