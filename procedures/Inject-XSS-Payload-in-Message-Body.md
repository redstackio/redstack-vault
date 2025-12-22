---
tags:
  - xss
  - payload-injection
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c9f5b8db-2a07-4c97-a0e9-7e62d37d0e79
created_at: '2025-12-14T03:46:38.226Z'
updated_at: '2025-12-14T03:46:38.226Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Message-Body

## Summary

This procedure injects a malicious JavaScript payload into the msgBody parameter of a private message reply in Concrete CMS, exploiting insufficient sanitization for stored XSS.

## Description

In Concrete CMS 8.5.2, the private messaging feature fails to validate or escape user input in the message body, allowing HTML and JS injection. This procedure uses the reply form to store the payload, which embeds into HTML responses viewed by admins. Prerequisites include an open reply form in a low-priv session. Expected outcome is successful submission and storage, leading to execution on admin hover.

## Requirements

1. Open reply form in private messaging
2. Knowledge of XSS payloads (e.g., onmouseover events)
3. No client-side validation bypass needed, as server-side is weak

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization using libraries like DOMPurify
- Escape HTML entities in all user-generated content
- Scan for script tags and event handlers in message logs

## Objectives

1. Bypass input validation to store malicious script
2. Ensure payload triggers on admin interaction (e.g., hover)
3. Achieve arbitrary JS execution in victim context

## Instructions

### Step 1: Craft and Enter Payload

**Context**: Prepare an event-based payload to evade basic filters.

In the msgBody field, type: `<input><img src=a onmouseover=window.location.href='https://www.test.com'>` or `<img src=x onmouseover=alert('XSS-Stored')>Bar`.

> These payloads use onmouseover to trigger on hover, common in messaging UIs.

### Step 2: Submit the Message

**Context**: Send the reply to store the payload.

Click the submit or send button on the form.

> The message saves without errors, appearing in the conversation as injected HTML.

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
- [[payload-injection]]
